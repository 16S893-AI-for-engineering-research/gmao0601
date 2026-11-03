---
id: TASK-1.9
title: Verify coupled plugin with canonical cases - one task per case
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:37'
labels:
  - verification
  - planning-placeholder
  - external-us3d
dependencies:
  - TASK-1.5
  - TASK-1.13
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: task
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Coordination task for testing equations together after individual integration. Select canonical cases whose known reference solutions match the approved model; Hartmann flow is a candidate, not mandatory. Create one bounded execution task per selected case. Inputs are the integrated plugin, case definition and sourced reference solution with agreed comparison criteria. Preparation/analysis can occur here, but simulation execution requires the external installation.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Each selected canonical case has its own bounded task, matching physical assumptions, boundary conditions and a sourced reference solution.
- [ ] #2 Reproducible inputs, target build/version/settings, run instructions, external logs and results are retained for each case.
- [ ] #3 Comparison plots/error measures, relevant refinement and conservation checks meet agreed criteria, with explicit pass/fail and discrepancy reporting.
- [ ] #4 All required cases pass before this coordination task completes; reports distinguish coupled-equation verification from validation of hypersonic chemistry or RF/blackout predictions.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Reconciled with the user-approved V1.1.md workflow. This is a planning update, not implementation or verification evidence. Historical planV1.0.md references are retained for provenance; V1.1.md governs the revised scope.
<!-- SECTION:NOTES:END -->
