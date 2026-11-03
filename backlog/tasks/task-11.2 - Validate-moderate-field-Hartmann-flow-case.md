---
id: TASK-11.2
title: Validate moderate-field Hartmann-flow case
status: To Do
assignee: []
created_date: '2026-11-03 22:09'
labels: []
dependencies:
  - TASK-11.1
parent_task_id: TASK-11
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Second Hartmann case using the approved moderate-field parameters. Reuse the shared reference and the first case workflow rather than independently choosing analytical assumptions, criteria, or building another comparator. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Parent benchmark approval and successful completion of the first case are prerequisites.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The user-approved shared benchmark assumptions and case-specific Hartmann number/settings are used; any incompatibility or missing decision blocks affected execution.
- [ ] #2 Reproducible inputs, submission scripts, run instructions, and a result-return manifest identify plugin/build/input provenance and the approved compute configuration.
- [ ] #3 Actual returned US3D results meet the predefined convergence requirements, with failures or missing evidence reported rather than treated as a pass.
- [ ] #4 Velocity profiles and other approved quantities are compared with the shared analytical reference using preapproved metrics/thresholds; results give an explicit pass/fail.
- [ ] #5 Approved mesh-sensitivity checks establish adequate Hartmann-layer resolution or explicitly report a failed/unresolved resolution requirement.
- [ ] #6 A readable case report preserves quantitative errors, plots/comparisons, provenance, convergence evidence, discrepancies, and limitations; thresholds/equations are not silently changed to obtain agreement.
<!-- AC:END -->
