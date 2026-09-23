# Phase 010 — Blender to Godot feasibility report

**Decision:** FEASIBLE FOR FOUNDATION / EXECUTION PROOF DEFERRED  
**Date:** 2026-09-23

## Intended production boundary

- Blender owns authored visual source: geometry, layered paper assets, masks, sprite-render inputs, hero/marketing scene source.
- Godot owns gameplay composition, deterministic runtime, UI, shaders/VFX timing, audio integration, import settings, and platform exports.
- glTF 2.0 / GLB is the preferred interchange for 3D source where interchange is needed.
- Generated runtime assets must remain reproducible from committed source and scripts/settings.

## External technical evidence

Godot documentation:
- https://docs.godotengine.org/en/latest/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html
- states glTF 2.0 is recommended and that Godot supports .gltf/.glb;
- documents direct Blender import as a Blender-to-glTF-to-Godot path.

Blender 4.5 LTS manual:
- https://docs.blender.org/manual/en/4.5/addons/import_export/scene_gltf2.html
- documents the glTF 2.0 import/export pipeline.

This supports the architecture choice; it does not prove our future asset template/import settings.

## Local command probe

The Phase 010 execution environment was checked for:
- \`blender\`
- \`godot\`
- \`godot4\`

No executable was exposed in this environment.

Therefore:
- no local Blender export was performed;
- no local Godot import was performed;
- no screenshot/render/runtime claim is made.

## Why Phase 010 can still proceed

The bible's Phase 010 asks to verify the **approach** and permits a report/fixture/capture/command. The actual pipeline is explicitly owned later:

- Phase 011: bootable empty Godot project + version manifest.
- Phase 019: versioned Blender template/exporter/calibration renders.
- Phase 020: Godot calibration scene/import preset/render comparison and approved visual-pipeline gate.

A failed Phase 019/020 clean round trip would block production art and reopen this assumption.

## Required Phase 019/020 proof

The later pipeline cannot be considered green until a clean environment can:

1. open the pinned Blender source/template;
2. reproduce the calibration export with recorded settings;
3. import the output into the pinned Godot project;
4. preserve scale, pivot, silhouette, alpha, normals/material behavior, camera relationship, masks, and naming;
5. regenerate without undocumented manual repair;
6. detect missing source/export mismatches;
7. record tool versions and file hashes.

## Pipeline risk decision

No technical evidence discovered here requires abandoning Blender + Godot. The remaining risk is execution/reproducibility risk, not a known incompatibility. Keep it on the living risk register until Phase 020 proves it.
