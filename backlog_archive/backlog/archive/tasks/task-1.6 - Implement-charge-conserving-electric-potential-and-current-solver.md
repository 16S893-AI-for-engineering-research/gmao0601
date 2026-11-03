---
id: TASK-1.6
title: Implement charge-conserving electric-potential and current solver
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:38'
labels: []
dependencies:
  - TASK-1.3
  - TASK-1.4
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: task
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The low-induction candidate model requires a spatial charge-conservation solve, not independent per-cell source terms. Use only the approved, supported solver integration path and consistent face currents.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Manufactured-solution tests show documented mesh-refinement behavior for potential/current, including variable conductivity.
- [ ] #2 Insulating/electrode and applicable symmetry/periodic boundaries plus all-Neumann gauge handling are verified.
- [ ] #3 Discrete charge-balance and solver-residual diagnostics meet documented tolerances, including MPI partitioned runs.
- [ ] #4 Near-zero conductivity and solver nonconvergence have documented and test-covered behavior.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Superseded by the user-approved V1.1 equation-by-equation structure under TASK-1.5. The user will supply equations and their order; do not assume this candidate-specific equation is required. Archived as superseded, not completed or verified.
<!-- SECTION:NOTES:END -->
