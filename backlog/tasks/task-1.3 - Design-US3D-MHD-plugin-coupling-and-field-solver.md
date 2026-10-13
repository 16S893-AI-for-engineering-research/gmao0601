---
id: TASK-1.3
title: Design US3D MHD plugin coupling and field solver
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-12 16:40'
labels: []
dependencies:
  - TASK-1.1
  - TASK-1.2
references:
  - planV1.0.md
parent_task_id: TASK-1
type: task
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A charge-conserving electromagnetic solve needs a discretization and coupling sequence compatible with supported US3D hooks and state definitions. Design it before integration code so boundary conditions, units, and conservation diagnostics are testable.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Reviewed design records equations, variable/units mapping, momentum and energy source accounting, update order, and explicit/iterative stability decision.
- [ ] #2 Face-current and potential discretization handles variable/near-zero conductivity, insulating/electrode and flow-domain boundaries, and gauge freedom.
- [ ] #3 Parallel, restart, configuration, diagnostics, uniform-field and field-map behavior are specified using supported integration mechanisms.
- [ ] #4 A viable path for the coupled field solve is demonstrated or a blocker and approved alternative architecture are documented.
<!-- AC:END -->
