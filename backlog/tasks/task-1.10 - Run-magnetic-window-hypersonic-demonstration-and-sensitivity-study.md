---
id: TASK-1.10
title: Compare no-field and applied-field hypersonic cases
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:37'
labels:
  - application
  - external-us3d
dependencies:
  - TASK-1.9
  - TASK-1.14
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: task
ordinal: 14000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
First bounded application demonstration, separate from the later sensitivity campaign. Inputs: canonically verified plugin, user-selected hypersonic case, agreed field conditions/quantities and model applicability limits. Prepare equivalent no-field/applied-field configurations, run externally and analyze the returned results. This task does not establish mesh/timestep independence or require a favorable magnetic-window effect.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 No-field and applied-field configurations are reproducible from versioned files/instructions and equivalent settings apart from the intended field change, with external execution evidence.
- [ ] #2 Both cases run successfully and agreed quantities such as electron density, flow changes and force/heating budgets are compared where supported by the selected model.
- [ ] #3 Relevant conservation/applicability checks and observed response are reported honestly, including limitations and unresolved issues.
- [ ] #4 The report does not infer validated RF attenuation/blackout mitigation or numerical independence from this single comparison.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Reconciled with the user-approved V1.1.md workflow. This is a planning update, not implementation or verification evidence. Historical planV1.0.md references are retained for provenance; V1.1.md governs the revised scope.
<!-- SECTION:NOTES:END -->
