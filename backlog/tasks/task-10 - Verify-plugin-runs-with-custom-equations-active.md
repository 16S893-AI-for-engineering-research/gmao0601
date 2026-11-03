---
id: TASK-10
title: Verify plugin runs with custom equations active
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-9
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Confirm the plugin compiles, loads, initializes, and completes the agreed short case with its implemented equations active. Passing means ready for validation, not physically validated. Reuse the previous short case unless a change is explicitly approved. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. This is an execution/integration check, not a second scientific-validation task. Failures warrant bounded diagnosis, not speculative equation or solver-setting changes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The active-model package identifies exact configuration, short-run length/checkpoints, build/run instructions, and outputs the user must return.
- [ ] #2 Actual returned evidence confirms successful plugin compilation/loading and model initialization, including expected initial values.
- [ ] #3 Evidence confirms the intended equation contributions execute; a nonzero CFD change is not required when the case physics predicts zero contribution.
- [ ] #4 The agreed short run completes without reported solver failure or nonfinite solution values; differences from the inactive case are recorded, not treated alone as pass/fail.
- [ ] #5 The initialization-only configuration still passes the established unchanged-CFD-output regression check with actual external evidence.
- [ ] #6 The result report explicitly labels a pass as ready for validation and makes no scientific accuracy claim.
<!-- AC:END -->
