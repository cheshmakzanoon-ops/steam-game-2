# Phase 011 — Repository bootstrap closure

**Status: COMPLETE / GREEN — empty technical foundation only.**

Project: Charterwake: The Last Relay (provisional). Date: 2026-09-23.
Entry commit: `0f614ae0f07cad2ac63a6b5126c80ed2b20d2145`.
Implementation commit: `fe837bec745e127f6fbb678aa7a383a691ea82e7`.
Final tested candidate: `777ae6b84562405d63203f0865d50c3e7f021487`.
Frozen tag remains `preproduction-v1` → `016c22d2d44be9168627e6045626ab0e097a35e5`.

## Deliverable and scope

The real Godot project is `game/project.godot`. Its main scene is a script-free Control with one centered status Label. It has no board, simulation, combat, content, save service, account, plugin or network dependency. Empty prescribed directories are not completed systems.

The root toolchain manifest pins the standard Godot 4.7.2 engine and Blender 4.5.14 LTS. Blender is an external authoring tool, not a dependency for opening the empty game. Source art and engine-ready assets are separated, and both initial asset/content manifests have zero entries.

## Bible work-package mapping

| Requirement | Implemented evidence |
| --- | --- |
| Initialize/standardize version control | Existing main history retained; immutable tag verified; no replacement repository or force push |
| Prescribed directory layout | All 38 leaf paths in `layout.json`, from master-bible section 10 |
| Pin actual tool versions | `toolchain.json` and executed publisher-checksum/version probes |
| Ignore and attributes | `.gitignore`, `.gitattributes`, tested exclusions and retained `.uid`/`.import` source types |
| README and contributor guide | Root README, `CONTRIBUTING.md`, architecture ADR |
| Line endings | UTF-8 without BOM and Git-local LF rules verified on Linux/Windows |
| License and third-party notices | Rights-preserving project notice; separate Godot/Blender notices; no unrequested open-source license grant |
| Clean clone opens | Fresh detached candidate checkouts, real engine import/run, graphical Linux probe and clean source-status checks |

## Executed acceptance evidence

[Final successful acceptance run](https://github.com/cheshmakzanoon-ops/steam-game-2/actions/runs/35859528934).

[Exact executed workflow](https://github.com/cheshmakzanoon-ops/steam-game-2/blob/777ae6b84562405d63203f0865d50c3e7f021487/.github/workflows/phase-011-bootstrap-check.yml).

Both jobs completed successfully:

- Ubuntu 24.04: job `107176029033`; headless and graphical checks PASS.
- Windows Server 2025: job `107176029415`; headless checks PASS. A graphical Windows check was not run.

Each performs a native fresh Git checkout, verifies the frozen tag, verifies the official Godot archive digest, runs all prior probes, executes headless editor import and the actual main scene, rejects nine invalid bootstrap cases, removes/rebuilds the import cache, and requires clean Git status. Linux additionally verifies Blender's numeric version and executes both the graphical editor and a rendered scene capture using Mesa/EGL software rendering. See `VERIFICATION_RESULTS.json` for exact versions, jobs, source hashes and evidence references.

The downloaded final artifacts were checked against their GitHub SHA-256 digests. Their reports identify the exact tested candidate. The Linux capture was visually reviewed at 1280×720: three centered readable status lines on a plain background, no clipped text, no gameplay or error overlay. Capture SHA-256: `28394c0afe85421df32fae316d041947bb563bf8c609da57d9826d19289fc367`.

Earlier runner attempts found a download HTTP refusal, a Blender version-banner suffix, missing graphics runtime libraries, and a GLX virtual-display warning. These were corrected without excluding warnings or skipping the graphical check. A successful GUI open also exposed Godot rewriting the project's header/property order; the committed project now uses the exact editor-produced serialization. No gameplay rule was changed to obtain a green result. Earlier failed attempts remain in GitHub history; acceptance is based on the final successful run, not those attempts.

## Verification boundary

Native GitHub-hosted environments executed the editor and scene. The assistant's local environment provided syntax/static checks and artifact inspection; it did not have Godot/Blender installed. Hosted verification is not a claim that the user's desktop has been tested.

The temporary acceptance workflow is removed in this closure commit. Its exact executed source remains available at the tested commit, and the local verification scripts remain in `tools/`. This is not Phase 012's continuing build/export CI skeleton. Run artifacts have 14-day retention; the source commands, results summary and hashes remain committed for reproduction.

The closure commit changes only documentation/evidence and removes the temporary workflow. The tested game, manifests, repository settings and verification scripts are retained unchanged.

## Normal, boundary and recovery cases

Normal: fresh clone → exact version check → import → configured main scene → scene assertions → clean source tree.

Boundary: verify every prescribed directory, precise tag target, no runtime plugin/service, no script attached to the bootstrap scene, stable project ID, UTF-8/LF, correct retained source identities, and no cache/secret leakage.

Failure: reject wrong patch version, prerelease, .NET edition, missing project, missing scene, malformed manifest, missing required directory, wrong main-scene configuration and online-service dependency. All mutations occur in disposable copies.

Recovery: remove only generated `game/.godot/`, reimport, rerun the main scene and probe, and confirm no tracked or untracked source changes. The historical Phase 001–010 directories remain unchanged.

## Prior regression counts actually returned

- Phase 004: 1,404 checks, 40 examples; eight deliberately invalid CLI cases rejected.
- Phase 005: 53 checks; invalid extra-doctrine case rejected.
- Phase 008: 388 checks; invalid reserve rejected.
- Phase 009: 145 checks; impossible threshold rejected.
- Phase 010: 23 checks; online dependency rejected.

These are the scripts' real returned counts, not a reassertion of historical count summaries. They validate their stated preproduction scope, not game runtime behavior.

## Scope limitations and next phase

A graphical boot is not a performance benchmark or final UI/accessibility acceptance. Windows Server runner tests are not a Windows 10/11 or Steam Deck certification. There are no saves, interactive controller paths, runtime content or production assets to claim tested. Actual Blender-to-Godot asset calibration remains Phase 019–020. Executable packaging and full build CI remain Phase 012.

The next gate is **Phase 012 — Build and continuous-integration skeleton**. Preserve the tag and historical documents, use the pinned project as the input, add reproducible development exports and build checks, and do not jump ahead to gameplay.
