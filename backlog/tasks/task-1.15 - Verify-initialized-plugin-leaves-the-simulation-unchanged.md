---
id: TASK-1.15
title: Verify initialized plugin leaves the simulation unchanged
status: To Do
assignee: []
created_date: '2026-10-21 20:37'
labels:
  - initialization
  - external-us3d
dependencies:
  - TASK-1.4
  - TASK-1.13
  - TASK-1.14
references:
  - V1.1.md
parent_task_id: TASK-1
type: task
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Separate runtime regression from local scaffold preparation so initialization defects are caught before physics is added. Inputs: the operator-free plugin, selected prepared case with all files, target version/build and execution access arranged through the user, and agreed justified comparison tolerances. US3D will not be installed locally. Outputs are external build/load and baseline/plugin-enabled run evidence plus a comparison report. A failed regression blocks physics integration.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 External evidence demonstrates that the plugin builds and loads, with commands, version/build details and logs.
- [ ] #2 Equivalent case inputs and execution settings are run without the plugin and with hooks/variables initialized; no new physics operators are active.
- [ ] #3 Agreed flow quantities and convergence behavior match within documented justified numerical variation; results and discrepancies are reported reproducibly.
- [ ] #4 The report records pass/fail with external run artifacts; locally prepared instructions or static checks alone cannot complete this task.
<!-- AC:END -->
