---
id: TASK-1.9
title: Verify coupled MHD with canonical analytic cases
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-12 16:40'
labels: []
dependencies:
  - TASK-1.7
  - TASK-1.8
references:
  - planV1.0.md
parent_task_id: TASK-1
type: task
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Passing arithmetic and field-solver tests alone does not establish that US3D and the plugin correctly solve coupled MHD. Hartmann flow and complementary cases provide controlled analytic comparisons before hypersonic application.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Hartmann channel boundary conditions and analytic assumptions are documented and match the simulated problem.
- [ ] #2 Velocity and relevant current/field profiles are compared with analytic results over multiple meshes and Hartmann numbers with stated error measures/refinement trends.
- [ ] #3 At least one complementary simple current/force case and coupled conservation budgets are reported.
- [ ] #4 Tests distinguish numerical MHD verification from validation of hypersonic chemistry or RF communications.
<!-- AC:END -->
