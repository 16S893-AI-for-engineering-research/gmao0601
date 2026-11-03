---
id: TASK-1.5
title: Implement user-supplied equations - one task per equation
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:37'
labels:
  - equations
  - planning-placeholder
  - external-us3d
dependencies:
  - TASK-1.2
  - TASK-1.15
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: feature
ordinal: 12000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Coordination placeholder, not one large coding assignment. Inputs are the approved user-supplied equation list/order and passing no-op regression (TASK-1.15). Once equations are supplied, create one child task per equation, each with two independently checkable parts: (1) calculate/test without new flow effects; (2) integrate into US3D and verify externally. Assign one equation and one part at a time; split a large spatial solve further if needed. Do not preselect potential/current, Lorentz or conductivity equations from planV1.0.md. The old TASK-1.6 through TASK-1.8 assumptions are superseded by this user-driven structure.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Each approved equation has a bounded task with explicit inputs/outputs, dependencies and the user-specified order; conflicts are raised rather than silently reordered.
- [ ] #2 For every equation, Part 1 has documented units/conventions and agreed numerical details, independent-reference tests and relevant limiting/invalid-input checks, without applying new effects to the flow.
- [ ] #3 For every equation, Part 2 reads real US3D state at the approved update point, stores/applies only specified results and has external integration/reference/regression evidence; local checks alone do not pass runtime verification.
- [ ] #4 All required equation parts pass before this coordination task completes; coupled canonical verification remains separate and no assumed physics is added without user approval.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Reconciled with the user-approved V1.1.md workflow. This is a planning update, not implementation or verification evidence. Historical planV1.0.md references are retained for provenance; V1.1.md governs the revised scope.
<!-- SECTION:NOTES:END -->
