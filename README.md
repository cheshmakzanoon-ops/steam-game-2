# Charterwake: The Last Relay

Compact one-board strategy roguelite for Steam. The public title remains provisional.

## Current state

**Phase 011 — Repository bootstrap: implementation under verification.**

The repository now has an empty Godot foundation, not a playable game. Open **`game/project.godot`** in the standard **Godot 4.7.2** editor. Running it displays the Phase 011 status message. No gameplay, save/profile data or network service is loaded.

[Setup and contribution guide](CONTRIBUTING.md) · [Exact tool pins](toolchain.json) · [Phase 011 task record](docs/phase-011/README.md) · [Bootstrap ADR](docs/architecture/adr-0001-bootstrap.md)

```sh
python3 tools/verify_bootstrap.py --godot /path/to/godot --check-history --self-test
```

`game/` is the engine project, `art/blender/` contains the future authored-source pipeline, `docs/` keeps design and evidence, and `tools/` contains developer-only verification. Blender 4.5.14 LTS is pinned but not required to open this asset-free foundation. See the contributor guide for Windows commands.

## Frozen preproduction

The immutable `preproduction-v1` tag points to `016c22d2d44be9168627e6045626ab0e097a35e5`. Historical Phase 001–010 files are preserved. Start design work from the [GDD](docs/phase-007/GDD_V1.md), [core rules](docs/phase-004/CORE_RULES_V1.md), [scope](docs/phase-005/SCOPE_BUDGET.md), [roadmap](docs/phase-008/DEPENDENCY_GRAPH.md) and [risk criteria](docs/phase-009/KILL_CRITERIA.md).

## Existing preproduction checks

```sh
python3 docs/phase-004/verify_rules.py --self-test
python3 -S docs/phase-005/verify_scope.py --self-test
python3 -S docs/phase-008/verify_roadmap.py --self-test
python3 -S docs/phase-009/verify_risks.py --self-test
python3 -S docs/phase-010/verify_preproduction.py --self-test
```

These are preproduction probes, not gameplay runtime tests. [Project rights](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md) remain separate.

Phase 012 owns the development export and ongoing build/CI skeleton. No later phase is complete merely because its directory exists.
