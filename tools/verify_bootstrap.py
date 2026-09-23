#!/usr/bin/env python3
"""Phase 011 checks. Standard library only; never downloads tools or edits sources."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "016c22d2d44be9168627e6045626ab0e097a35e5"


class BootstrapError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BootstrapError(message)


def read_json(path: Path) -> dict[str, Any]:
    try:
        result = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise BootstrapError(f"Cannot read valid JSON: {path.name}: {error}") from error
    require(isinstance(result, dict), f"Expected JSON object: {path.name}")
    return result


def check_version(version: str, manifest: dict[str, Any]) -> None:
    expected = manifest["godot"]["version"] + "." + manifest["godot"]["channel"]
    require(bool(re.match(re.escape(expected) + r"(?:\.|$)", version.strip())),
            f"Godot version mismatch: expected {expected}, received {version.strip()!r}")
    require("mono" not in version.lower(), "Use the standard GDScript editor, not the .NET edition.")


def static_checks(root: Path) -> tuple[dict[str, Any], list[str]]:
    results: list[str] = []
    manifest = read_json(root / "toolchain.json")
    require(manifest.get("schema_version") == 1, "Unsupported toolchain schema.")
    require(manifest.get("project_id") == "steam-game-2", "Stable internal project ID changed.")
    require(manifest.get("preproduction_commit") == BASELINE, "Frozen baseline target changed.")
    require(manifest["godot"]["version"] == "4.7.2", "Unexpected Godot pin; use an ADR to revise it.")
    require(manifest["godot"]["channel"] == "stable", "Godot must be stable.")
    require(manifest["godot"]["edition"] == "standard", "Godot edition must be standard.")
    require(manifest["godot"]["renderer"] == "gl_compatibility", "Unexpected bootstrap renderer.")
    require(manifest["blender"]["version"] == "4.5.14", "Unexpected Blender pin.")
    require(manifest["blender"]["required_to_open_game"] is False, "Empty game must not require Blender.")
    require(manifest.get("runtime_plugins") == [], "Phase 011 must not add runtime plugins.")
    require(manifest.get("mandatory_online_services") == [], "No mandatory online service is allowed.")
    results.append("version, identity, offline and no-plugin contracts")
    layout = read_json(root / "docs/phase-011/layout.json")
    directories = layout.get("directories")
    require(isinstance(directories, list) and len(directories) == len(set(directories)),
            "Layout must contain unique directory entries.")
    for relative in directories:
        require(isinstance(relative, str) and not Path(relative).is_absolute()
                and ".." not in Path(relative).parts, "Unsafe layout path.")
        require((root / relative).is_dir(), f"Required directory missing: {relative}")
    results.append(f"all {len(directories)} bible-layout directories exist")
    required = ["game/project.godot", "game/scenes/boot/boot.tscn", "LICENSE",
                "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md", ".gitignore", ".gitattributes",
                ".editorconfig", "docs/architecture/adr-0001-bootstrap.md",
                "docs/production/content_manifest.json", "docs/art/generated_asset_manifest.json"]
    for relative in required:
        require((root / relative).is_file(), f"Required file missing: {relative}")
    project = (root / "game/project.godot").read_text(encoding="utf-8")
    require('run/main_scene="res://scenes/boot/boot.tscn"' in project, "Invalid or missing boot scene reference.")
    require('renderer/rendering_method="gl_compatibility"' in project, "Compatibility renderer not set.")
    require('[autoload]' not in project and '[editor_plugins]' not in project, "No services/plugins at bootstrap.")
    scene = (root / "game/scenes/boot/boot.tscn").read_text(encoding="utf-8")
    require('[node name="Boot" type="Control"]' in scene and 'No gameplay systems loaded.' in scene,
            "Empty foundation scene contract missing.")
    require("ext_resource" not in scene and "script =" not in scene, "Boot must have no runtime script dependency.")
    require(len(re.findall(r"^\[node ", scene, re.M)) == 2, "Expected Boot plus one status label.")
    for relative in ("docs/production/content_manifest.json", "docs/art/generated_asset_manifest.json"):
        require(read_json(root / relative).get("entries") == [], f"Unexpected production entries: {relative}")
    results.append("main scene, empty content and source/engine asset separation")
    attributes = (root / ".gitattributes").read_text(encoding="utf-8")
    require("* text=auto eol=lf" in attributes, "LF normalization is missing.")
    require("filter=lfs" not in attributes, "LFS has not been approved.")
    for folder in (root / "game", root / "tools"):
        for path in folder.rglob("*"):
            if path.is_file() and path.suffix in (".gd", ".py", ".godot", ".tscn", ".json"):
                raw = path.read_bytes()
                require(b"\r" not in raw and not raw.startswith(b"\xef\xbb\xbf"),
                        f"Expected UTF-8 without BOM and LF endings: {path.relative_to(root)}")
    results.append("source UTF-8/LF and explicit non-LFS policy")
    return manifest, results


def command(args: list[str], cwd: Path, timeout: int = 120, engine: bool = False) -> str:
    try:
        result = subprocess.run(args, cwd=cwd, text=True, encoding="utf-8", errors="replace",
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise BootstrapError(f"Command could not finish: {args[0]}: {error}") from error
    require(result.returncode == 0, f"Command failed ({result.returncode}): {args}\n{result.stdout}")
    if engine:
        require(not re.search(r"(?m)^\s*(?:SCRIPT ERROR|ERROR|WARNING):", result.stdout),
                f"Engine emitted an error/warning:\n{result.stdout}")
    return result.stdout


def history_checks(root: Path) -> list[str]:
    actual = command(["git", "rev-parse", "refs/tags/preproduction-v1^{commit}"], root).strip()
    require(actual == BASELINE, "preproduction-v1 is missing or points to the wrong commit.")
    paths = [f"docs/phase-{number:03d}" for number in range(1, 11)]
    changed = command(["git", "diff", "--name-only", BASELINE, "HEAD", "--", *paths], root).strip()
    require(not changed, f"Historical phase packages changed: {changed}")
    probes = ["game/.godot/cache.bin", "art/blender/source/sample.blend1", "art/blender/renders/frame.png",
              "exports/test.pck", ".env", "artifacts/test.log"]
    for path in probes:
        command(["git", "check-ignore", "--no-index", path], root)
    for path in ("game/src/sim/example.gd.uid", "game/assets/generated/example.png.import",
                 "art/blender/source/example.blend", "game/assets/generated/example.png"):
        result = subprocess.run(["git", "check-ignore", "--no-index", path], cwd=root,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        require(result.returncode == 1, f"Source/import identity wrongly ignored: {path}")
    attributes = command(["git", "check-attr", "eol", "--", "game/project.godot", "tools/verify_bootstrap.py"], root)
    require(attributes.count(": eol: lf") == 2, "Git did not apply LF attributes.")
    return ["frozen tag and Phase 001-010 preservation", "six cache/secret exclusions and four retained source types", "Git LF attributes"]


def negative_checks(root: Path, manifest: dict[str, Any]) -> list[str]:
    results: list[str] = []
    for label, version in (("wrong patch", "4.7.1.stable.official"),
                           ("release candidate", "4.7.2.rc1.official"),
                           ("wrong edition", "4.7.2.stable.mono.official")):
        try:
            check_version(version, manifest)
        except BootstrapError:
            results.append(label)
        else:
            raise BootstrapError(f"Negative check accepted {label}.")
    mutations = [
        ("missing project", lambda p: (p / "game/project.godot").unlink()),
        ("missing scene", lambda p: (p / "game/scenes/boot/boot.tscn").unlink()),
        ("malformed manifest", lambda p: (p / "toolchain.json").write_text("{", encoding="utf-8")),
        ("missing prescribed directory", lambda p: shutil.rmtree(p / "game/src/sim")),
        ("wrong main scene", lambda p: (p / "game/project.godot").write_text("config_version=5\n", encoding="utf-8")),
        ("online dependency", lambda p: (p / "toolchain.json").write_text(json.dumps({**manifest, "mandatory_online_services": ["backend"]}), encoding="utf-8")),
    ]
    for label, mutate in mutations:
        with tempfile.TemporaryDirectory(prefix="bootstrap-negative-") as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(root, copy, ignore=shutil.ignore_patterns(".git", ".godot", "__pycache__", "artifacts", ".local-tools"))
            mutate(copy)
            try:
                static_checks(copy)
            except (BootstrapError, KeyError):
                results.append(label)
            else:
                raise BootstrapError(f"Negative check accepted {label}.")
    # The real checkout is untouched by every failure/recovery test.
    static_checks(root)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--godot", default=os.environ.get("GODOT_BIN", "godot"))
    parser.add_argument("--static-only", action="store_true", help="Explicitly omit all engine execution.")
    parser.add_argument("--check-history", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--visual", action="store_true", help="Also open the GUI editor and capture the scene; needs a display.")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--capture", type=Path)
    args = parser.parse_args()
    try:
        require(not (args.visual and args.static_only), "--visual cannot be combined with --static-only.")
        manifest, checks = static_checks(ROOT)
        report: dict[str, Any] = {"schema_version": 1, "phase": 11, "static_checks": checks,
                                  "engine_executed": False, "visual_executed": False}
        if args.check_history:
            report["history_checks"] = history_checks(ROOT)
        if args.self_test:
            report["negative_checks_rejected"] = negative_checks(ROOT, manifest)
        if not args.static_only:
            binary = shutil.which(args.godot) or args.godot
            version = command([binary, "--version"], ROOT).strip()
            check_version(version, manifest)
            report["godot_version"] = version
            for name, flags in (("clean_import", ["--headless", "--editor", "--path", str(ROOT / "game"), "--import"]),
                                ("main_scene", ["--headless", "--path", str(ROOT / "game"), "--quit-after", "5"]),
                                ("scene_probe", ["--headless", "--path", str(ROOT / "game"), "--script", str(ROOT / "tools/bootstrap_probe.gd")])):
                output = command([binary, *flags], ROOT, engine=True)
                if name == "scene_probe":
                    require("BOOTSTRAP_SCENE_OK" in output, "Scene probe did not reach its success marker.")
                report[name] = output.strip()
            report["engine_executed"] = True
            if args.visual:
                require(args.capture is not None, "--visual requires --capture PATH outside game/.")
                capture = args.capture.resolve()
                require(not capture.is_relative_to(ROOT / "game"), "Do not write captures into engine source assets.")
                capture.parent.mkdir(parents=True, exist_ok=True)
                graphics_driver = "opengl3_es" if sys.platform.startswith("linux") else "opengl3"
                graphics_flags = ["--rendering-method", "gl_compatibility", "--rendering-driver", graphics_driver, "--disable-vsync"]
                report["visual_driver_flags"] = graphics_flags
                report["gui_editor"] = command([binary, *graphics_flags, "--editor", "--path", str(ROOT / "game"), "--audio-driver", "Dummy", "--quit-after", "60"], ROOT, engine=True).strip()
                report["visual_probe"] = command([binary, *graphics_flags, "--path", str(ROOT / "game"), "--audio-driver", "Dummy", "--script", str(ROOT / "tools/bootstrap_probe.gd"), "--", f"--capture={capture}"], ROOT, engine=True).strip()
                require(capture.is_file() and capture.stat().st_size > 0, "Scene capture is missing.")
                report["capture_sha256"] = hashlib.sha256(capture.read_bytes()).hexdigest()
                report["visual_executed"] = True
        report["status"] = "PASS"
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 0
    except (BootstrapError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"BOOTSTRAP_FAILED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
