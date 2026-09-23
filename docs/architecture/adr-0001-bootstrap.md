# ADR 0001 — Minimal Godot repository foundation

Date: 2026-09-23. Status: accepted for Phase 011 implementation.

## Context and authority

Master bible section 10 supplies the `/game`, `/art/blender`, `/docs` and `/tools` layout. Phase 011 requires an empty bootable Godot project and clean-clone evidence. `preproduction-v1` remains immutable at `016c22d2d44be9168627e6045626ab0e097a35e5`.

## Decisions

The Godot root is `game/`, not the repository root. Keep authored Blender source outside the Godot importer; future render intermediates belong in `art/blender/renders/`, and approved engine-ready output belongs in `game/assets/generated/`. Match all bible leaf directories; empty `.gitkeep` files preserve them without speculative classes.

Use the already approved standard Godot 4.7.2 and Blender 4.5.14 LTS pins in `toolchain.json`. Blender is not needed to open this asset-free game. No `.blend` import, scene router, save/profile/settings service, content registry, plugin, autoload or generic GameManager is introduced.

Use Compatibility rendering for this empty fixed-2D foundation; this is a bootstrap renderer decision, not a final GPU-budget certification. Changing it requires a measured calibration decision in the owning later phase.

The boot scene contains only a script-free Control and static Label. The label explicitly identifies the technical foundation, rather than suggesting gameplay exists. Native window close exits. There are no gameplay decisions or controller paths yet; future input systems belong to Phase 017.

Store tool pins once in the root manifest. Verification checks the exact Godot version before opening the project. Do not silently upgrade, install tools at runtime or make the game call a network endpoint.

Retain original project rights rather than silently selecting an open-source license for a planned commercial game. Engine/tool licenses remain separate. Do not add LFS until source storage and clean-clone costs justify it.

## Verification and rollback

Keep executable/bootstrap probes outside the game root to avoid shipping developer code. They check missing files, wrong engine versions and illegal bootstrap dependencies. Clean import, actual main-scene boot and a rendered scene inspection are separate evidence from static file checks.

The temporary Phase 011 acceptance workflow is a verification instrument, not Phase 012's export/CI skeleton. Remove it after evidence is recorded; keep the local probes. No new runtime dependency is created by the runner.

Rollback by reverting Phase 011 commits, never moving the preproduction tag. Clearing generated `.godot/` cache and reimporting is a supported recovery test; deleting authored source is not.
