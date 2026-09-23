# Contributing and local setup

## Open the correct project

Clone this repository and fetch its tags. Use the standard **Godot 4.7.2** editor, not .NET or a development snapshot. The exact pins and official download locations are in [toolchain.json](toolchain.json). Download tools outside the repository and verify their official checksums. Blender **4.5.14 LTS** is the authored-asset pin; it is not required to open Phase 011.

In Godot Project Manager choose **Import**, select `game/project.godot`, open the editor, then press **F6** on the boot scene or **F5** for the configured project. Expected result: one centered status message naming the empty foundation. Close the native window to exit. This is not a playable prototype.

Command-line alternatives from the repository root:

```sh
/path/to/godot --editor --path game
/path/to/godot --path game
python3 tools/verify_bootstrap.py --godot /path/to/godot --check-history --self-test
```

Windows PowerShell (replace the executable path with the standard editor you downloaded):

```powershell
$Godot = 'C:\Tools\Godot_v4.7.2-stable_win64.exe'
& $Godot --editor --path game
py -3 tools/verify_bootstrap.py --godot $Godot --check-history --self-test
if ($LASTEXITCODE -ne 0) { throw 'Bootstrap verification failed.' }
```

Python 3.10 or newer and Git are needed for the repository checks, not for running the game. No pip, Node, npm, .NET, editor plugin, API key or online account is needed. A source clone/download initially needs access to its host; the installed editor and game run offline.

## Reproduce the bootstrap gate

The verifier fails for missing files, invalid manifest, wrong engine version, unsupported runtime plugins/services, altered frozen-tag target or modified historical phase packages. `--static-only` is explicitly incomplete: it validates files without claiming engine execution. `--self-test` corrupts disposable copies and confirms rejection; it never edits your real project.

For a graphical check, add `--visual --capture /absolute/path/outside/game/boot.png`. The check opens the GUI editor briefly and captures the scene. It explicitly selects Compatibility rendering, disables VSync for the probe, and uses EGL/GLES (`opengl3_es`) on Linux or `opengl3` elsewhere. This changes test launch arguments, not the saved project renderer. The default test uses Godot's headless driver and is not evidence of GPU performance.

A GPU-less Linux runner additionally needs Xvfb and Mesa software drivers. The verification environment installs `mesa-vulkan-drivers`, `vulkan-tools`, `libegl1`, `libegl-mesa0` and `libgles2`, selects its installed `lvp` ICD via `VK_DRIVER_FILES` and `VK_ICD_FILENAMES`, and sets `LIBGL_ALWAYS_SOFTWARE=1` before `xvfb-run`. These are disposable runner settings; do not apply them to a normal desktop unless software rendering is intended. The exact executed workflow is linked from the closure evidence. No graphics warning is hidden or excluded from the checker.

Before a clean import, close Godot and remove only the generated `game/.godot/` directory. Rerun the verifier. For the strongest test, clone into a new directory with no caches and repeat. Do not remove source, `.uid`, `.import` metadata or the frozen tag. An incompatible version must be corrected by installing the pinned tool, not editing expected results.

## Boundaries and repository discipline

Follow the master bible phase order and [GDD change-request process](docs/phase-007/CHANGE_REQUEST_TEMPLATE.md). `game/src/sim` is reserved for deterministic model code; presentation and UI cannot own outcomes. Empty directories are reserved paths, not implemented features.

Keep `.godot/`, local exports, logs, secrets, signing credentials, Blender backups and render intermediates out of Git. Commit approved source and its reproducibility scripts, not duplicate output. Retain Godot resource `.uid` sidecars and per-asset `.import` settings when introduced. Inspect `git status --short` after any editor operation.

`.gitattributes` enforces LF for source on Windows and Linux without altering global Git settings; binary assets are explicitly non-text. Do not bulk-renormalize historical phase files as incidental cleanup. Use Git without an editor VCS plugin. LFS is deliberately not enabled.

Read [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No new project-wide open-source license is selected by this bootstrap. Register future external assets under Phase 002 policy before making them dependencies. Never commit personal financial records or credentials.

## Verification boundaries

No save files, profiles, account connections or networking exist. Full input remapping, content validation, deterministic gameplay, final Blender export calibration, development exports and ongoing CI belong to later phases. A static status screen does not prove any of those.

The Phase 012 handoff is build/CI/export infrastructure, not the 9×9 board or combat.
