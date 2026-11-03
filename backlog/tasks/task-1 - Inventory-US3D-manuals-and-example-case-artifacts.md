---
id: TASK-1
title: Inventory US3D manuals and example case artifacts
status: To Do
assignee: []
created_date: '2026-11-03 22:07'
labels: []
dependencies: []
references:
  - .pi/ref-library/README.md
  - .pi/ref-library/input.inp
  - .pi/ref-library/example_submit.sh
  - .pi/ref-library/post.scr
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Establish a reliable starting point for future agents using the supplied US3D reference library and example case. Inventory the supplied artifacts as-is; missing assets and unresolved environment questions do not have to be resolved to complete this task. Reuse existing indexes instead of duplicating manual summaries. Agents cannot access the target US3D/Slurm environment. Original references must remain unchanged. Excludes plugin implementation, case redesign, and consulting archived plans or retired skills.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A concise reference inventory records manual paths, documented versions, and source hierarchy; summaries are navigation aids and exact API/syntax claims cite original manual sections/pages.
- [ ] #2 A topic lookup covers hooks, plugins, user variables, initialization, diffusion/transport, input syntax, build/load procedures, and output extraction; topics not located are explicitly unresolved.
- [ ] #3 input.inp, example_submit.sh, and post.scr are inspected, with their roles and referenced case files recorded.
- [ ] #4 The artifact manifest distinguishes files available locally, files unavailable locally, and unconfirmed remote availability.
- [ ] #5 Questions requiring user confirmation are recorded, including installed US3D version and the example discrepancy between 384 requested Slurm tasks and four launched MPI processes; examples are not silently corrected.
- [ ] #6 Original reference files are unchanged.
<!-- AC:END -->
