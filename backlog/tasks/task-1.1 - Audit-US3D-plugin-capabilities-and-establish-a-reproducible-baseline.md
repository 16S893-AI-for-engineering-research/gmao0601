---
id: TASK-1.1
title: Audit US3D plugin capabilities and establish a reproducible baseline
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
labels: []
dependencies: []
references:
  - planV1.0.md
parent_task_id: TASK-1
type: spike
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The US3D manuals and example plugins have not yet been supplied, and this repository contains no US3D solver code. Verify what is actually available before promising an in-process potential solver or a particular source-term API. Obtain the exact version, build environment, example plugin, and a working hypersonic baseline from the user.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A supplied example plugin builds and runs on the target US3D installation with reproducible commands and recorded version/environment.
- [ ] #2 A baseline case has archived inputs, outputs, and runtime for later no-op regression.
- [ ] #3 An integration specification documents verified lifecycle hooks, cell/face data, units, source terms, boundary conditions, parallel exchange, restart/output, and any API blockers.
- [ ] #4 The ability to host a spatial potential solve is established, or a supported external-solver coupling option and its constraints are documented.
<!-- AC:END -->
