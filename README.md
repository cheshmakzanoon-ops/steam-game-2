# Charterwake: The Last Relay

Compact one-board strategy roguelite for Steam. The public title remains provisional.

## Current state

**Phase 011 — Repository bootstrap: COMPLETE / GREEN.**

The repository now contains a real, verified empty Godot foundation, not a playable game. Open **`game/project.godot`** in the standard **Godot 4.7.2** editor and press **F5**. It displays the Phase 011 status message. No gameplay, save/profile data, account or network service is loaded.

[Setup and contribution guide](CONTRIBUTING.md) · [Exact tool pins](toolchain.json) · [Phase 011 closure](docs/phase-011/CLOSURE_EVIDENCE.md) · [Executed verification results](docs/phase-011/VERIFICATION_RESULTS.json)

```sh
python3 tools/verify_bootstrap.py --godot /path/to/godot --check-history --self-test
```

`game/` is the engine project, `art/blender/` contains the future authored-source pipeline, `docs/` keeps design and evidence, and `tools/` contains developer-only verification. Blender 4.5.14 LTS is pinned and its Linux binary version was verified; it is not needed to open this asset-free foundation. See the setup guide for Windows commands.

## Acceptance evidence

[Successful clean-checkout run](https://github.com/cheshmakzanoon-ops/steam-game-2/actions/runs/35859528934): native Windows Server 2025 and Ubuntu 24.04 headless editor/import/main-scene tests, nine rejected invalid cases per OS, cache recovery and clean source status. Linux additionally passed graphical editor launch and scene capture. The temporary acceptance workflow has been removed; its exact source and results remain linked in the closure record. This is not a claim of desktop compatibility, GPU performance, gameplay or exported-build certification.

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

The next gate is **Phase 012 — Build and continuous-integration skeleton**: reproducible development exports and ongoing build checks. No later phase is complete merely because its directory exists.
