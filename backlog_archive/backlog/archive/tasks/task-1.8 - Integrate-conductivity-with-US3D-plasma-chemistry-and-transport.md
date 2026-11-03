---
id: TASK-1.8
title: Integrate conductivity with US3D plasma chemistry and transport
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:38'
labels: []
dependencies:
  - TASK-1.2
  - TASK-1.4
  - TASK-1.5
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: task
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Prescribed conductivity is useful for verification but magnetic-window predictions need a property model connected to the available electron/species state and the approved first-release regime.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Conductivity and electron density are obtained from documented US3D state/transport inputs or a justified documented fallback, with units and validity envelope.
- [ ] #2 Tests cover representative and limiting states, including low ionization and out-of-range/nonphysical inputs.
- [ ] #3 Coupled outputs expose conductivity and model-validity diagnostics so sensitivity studies can be interpreted.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Superseded by the user-approved V1.1 equation-by-equation structure under TASK-1.5. The user will supply equations and their order; do not assume this candidate-specific equation is required. Archived as superseded, not completed or verified.
<!-- SECTION:NOTES:END -->
