# Phase 011 — Repository bootstrap

**Status: COMPLETE / GREEN.**

The real engine project is `game/project.godot`. Open it with the standard Godot 4.7.2 editor. Its single status scene is deliberately empty of gameplay.

Entry: `0f614ae0f07cad2ac63a6b5126c80ed2b20d2145`. Immutable Phase 010 tag: `preproduction-v1` → `016c22d2d44be9168627e6045626ab0e097a35e5`.

All 38 prescribed leaf directories in [layout.json](layout.json) follow the controlling master-bible section 10, not the alternate older document layout. Blank directory markers are not implemented systems.

[Closure and clean-clone record](CLOSURE_EVIDENCE.md) · [Machine-readable executed evidence](VERIFICATION_RESULTS.json) · [Setup guide](../../CONTRIBUTING.md) · [Tool pins](../../toolchain.json)

Actual acceptance covers native Windows Server and Linux headless import/run, cache recovery, nine invalid cases per operating system, clean Git status, and Linux graphical editor/scene capture. It does not certify later gameplay, exports, Steam Deck, performance or Blender production assets.

The temporary acceptance workflow was removed after its successful run; exact historical source and logs are linked in the closure record. Developer verification scripts remain available in `tools/`.

Next safe gate: **Phase 012 — Build and continuous-integration skeleton**.
