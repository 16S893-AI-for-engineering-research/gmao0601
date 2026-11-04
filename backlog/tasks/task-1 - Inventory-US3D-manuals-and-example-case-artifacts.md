---
id: TASK-1
title: Map the US3D reference library for future agents
status: Done
assignee:
  - '@assistant'
created_date: '2026-11-03 22:07'
updated_date: '2026-11-04 18:57'
labels: []
dependencies: []
references:
  - .pi/ref-library/README.md
  - .pi/ref-library/input.inp
  - .pi/ref-library/example_submit.sh
  - .pi/ref-library/post.scr
  - .pi/ref-library/MAP.md
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Create a concise, discoverable map of .pi/ref-library so future agents can quickly understand what is available, where to start for a particular question, which sources are authoritative, and what remains unknown. Reuse and link existing topic/chapter indexes and provenance guidance rather than duplicating manual summaries. Include the supplied example-case artifacts and their dependencies as-is. Missing assets and unresolved environment questions do not have to be resolved to complete this task; agents cannot access the target US3D/Slurm environment.

The deliverable is a reference map, not a skill. Add a brief project-instructions pointer so future agents can discover it. Preserve existing reference files. Excludes skill creation, helper tooling, plugin implementation, case redesign, and consulting archived plans or retired skills. Backlog remains the authoritative task plan; the map is reference documentation, not a separate work plan.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A concise map at .pi/ref-library/MAP.md explains the library layout, manual paths, documented versions, and source hierarchy; it links existing indexes instead of duplicating manual summaries, and exact API/syntax claims cite original manual sections/pages.
- [x] #2 The map routes agents to hooks, plugins, user variables, initialization, diffusion/transport, input syntax, build/load procedures, and output extraction through existing guides or targeted chapter links; topics not located are explicitly unresolved.
- [x] #3 input.inp, example_submit.sh, and post.scr are inspected, with their roles and referenced case files recorded.
- [x] #4 The artifact inventory distinguishes files available locally, files not found within a stated local search scope, and unconfirmed remote availability; required inputs are distinguished from generated outputs.
- [x] #5 Questions requiring user confirmation are recorded, including installed US3D version and the discrepancy between 384 requested Slurm tasks and four launched MPI processes; examples are not silently corrected.
- [x] #6 All pre-existing reference-library files remain unchanged.
- [x] #7 A brief pointer in the project AGENTS.md directs future agents to the map for US3D reference questions; the map is usable without a custom skill.
- [x] #8 Local map links are checked and representative hook, input-syntax, and output-extraction navigation paths are exercised; checks distinguish navigation from technical source verification and runtime validation.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Reuse the completed read-only inspection and preservation baseline; inspect any remaining relevant index sections without consulting excluded historical material.
2. Write .pi/ref-library/MAP.md as a concise entry point: library layout/source hierarchy, question-to-reference routing, example-artifact inventory, and open questions. Link existing guides instead of reproducing them.
3. Add a brief US3D-reference pointer to the project AGENTS.md; do not modify existing reference-library files or create a skill.
4. Check local links and exercise representative hook, input-syntax, and output-extraction navigation paths. Verify exact claims against original sources if any are included.
5. Compare all pre-existing reference files against the captured fingerprint baseline, excluding the newly added map.
6. Present the map and checks for user review before finalization or closure.

Implementation detail: allow only MAP.md through .gitignore so the new entry point can be versioned while all supplied reference materials remain local/ignored.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Read-only inspection before skill drafting: reviewed library entry points, TOPICS.md, VALIDATION.md, chapter-PDF README, input.inp, example_submit.sh, and post.scr. Existing topic guide covers most required areas; targeted summary search locates diffusion/transport in Developer 6/8 and User 4/22. These are navigation leads, not newly verified original-page API claims. Chapter extracts have documented search/copy limitations; original manuals remain authoritative for exact syntax.

Example script requests 8 nodes/384 tasks but launches mpirun -np 4; module path names 1.2-module, which does not establish installed patch version. Script references grid.cas and air-perfect.dat and names generated grid.h5, conn.h5, data.h5; post.scr names fvs.plt. None of those six filenames was found in the searched workspace (excluded .git, archived-plans, retired-skills); absence of generated outputs is not by itself a missing prerequisite. Remote and installation-provided availability remain unconfirmed.

Preservation baseline: .pi/ref-library contains 120 regular files excluding .DS_Store. Aggregate SHA256 a7eeeaf70c7277b333d9fe7731e782d125e236bb973f5d8ad3e4efb184997647, computed from lexicographically path-sorted UTF-8 lines formatted SHA256(file bytes), two spaces, repository-relative POSIX path, newline. Both original PDF hashes match VALIDATION.md. Inventory/skill not written; awaiting outline approval.

User clarified the desired outcome: a map of the reference library that future agents can find and understand quickly, rather than a skill. This supersedes the earlier skill scope and outline; no skill or inventory file had been created. Task scope, acceptance criteria, and plan updated accordingly.

Implemented .pi/ref-library/MAP.md and the AGENTS.md discovery pointer. Map contains quick-start navigation, source hierarchy/version/page conventions, compact topic routing, direct example observations, scoped availability snapshot, and unresolved environment questions. Exact example tokens are explicitly observations, not API-contract claims. Added a narrow .gitignore exception for MAP.md; documented that a fresh checkout may lack the supplied local library.

Verification: 49 local links/anchors in MAP.md and AGENTS.md resolve. Manually exercised three routes through the relevant summaries to original PDF text using pdftotext: hook us3dh_init at Developer PDF p.110; input CFD_SOLVER at User PDF p.25; output pob_write_fvs at User PDF p.42. These check navigation destinations, not complete API contracts or installed compatibility. Repeated the scoped filename search: grid.cas, air-perfect.dat, grid.h5, conn.h5, data.h5, fvs.plt still not found. All 120 pre-existing library files match the recorded aggregate SHA256 baseline (excluding new MAP.md and .DS_Store). Git-ignore checks confirm only MAP.md is exposed; all 120 original files remain ignored. Whitespace checks passed. No example, solver, Slurm job, or plugin build executed.

Implementation ready for user review; leaving status In Progress per the agreed review-before-closure checkpoint.

User reviewed and approved the map and explicitly authorized completing Task 1.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Created .pi/ref-library/MAP.md with source hierarchy, topic navigation, example-artifact availability, and unresolved environment questions. Added the AGENTS.md discovery pointer and a narrow .gitignore exception for the map. Verified 49 local links/anchors, three navigation routes to original manual pages, scoped artifact availability, and unchanged fingerprints for all 120 pre-existing reference files. No US3D or Slurm execution was performed. All eight acceptance criteria satisfied; user review approved.
<!-- SECTION:FINAL_SUMMARY:END -->
