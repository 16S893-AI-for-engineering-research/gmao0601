---
id: TASK-1.7
title: Couple Lorentz force and electromagnetic energy to US3D flow
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:38'
labels: []
dependencies:
  - TASK-1.4
  - TASK-1.5
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: task
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Potential/current results must alter flow through momentum and energy sources consistently with US3D total-energy and thermal-mode equations. Stable update ordering and clear failure reporting are essential for hypersonic cases.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Coupled simple cases confirm force direction, source magnitudes, and no double-counted energy deposition under the approved equations.
- [ ] #2 Zero-field and zero-conductivity runs introduce no spurious forces or heating compared with baseline.
- [ ] #3 Documented timestep or iterative convergence conditions and failure handling are exercised by integration tests.
- [ ] #4 Charge, momentum-source, and electromagnetic energy-budget diagnostics are available in output.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Superseded by the user-approved V1.1 equation-by-equation structure under TASK-1.5. The user will supply equations and their order; do not assume this candidate-specific equation is required. Archived as superseded, not completed or verified.
<!-- SECTION:NOTES:END -->
