---
id: TASK-1.2
title: Document the user-selected equations and calculation order
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-21 20:37'
labels:
  - definition
  - needs-user-input
dependencies:
  - TASK-1.14
references:
  - planV1.0.md
  - V1.1.md
parent_task_id: TASK-1
type: docs
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Inputs: the target-problem specification (TASK-1.14), the user-supplied ordered equation list, offline physical assessment decisions, assumptions/applicability limits and defining references. Output a specification usable by hook assessment and equation tasks. Physical-model assessment is the user responsibility, not an agent task. No agent-generated regime report is required. Do not silently choose or change equations, order or physical assumptions.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The specification records equations in the user-provided calculation/update order, with solved/prescribed quantities, variable definitions, units and sign conventions.
- [ ] #2 Required state/properties, initial/boundary conditions, force/energy accounting, applicability limits and exclusions are documented from user decisions and sources.
- [ ] #3 Missing definitions and inconsistencies are raised to the user; unresolved physical choices preventing hook assessment keep the specification in draft.
- [ ] #4 The user approves the specification; numerical implementation choices are not silently substituted for physical decisions.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Reconciled with the user-approved V1.1.md workflow. This is a planning update, not implementation or verification evidence. Historical planV1.0.md references are retained for provenance; V1.1.md governs the revised scope.
<!-- SECTION:NOTES:END -->
