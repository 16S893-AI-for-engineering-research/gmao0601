---
id: TASK-1.12
title: Create plugin-writing reference guide and skill
status: To Do
assignee: []
created_date: '2026-10-21 20:37'
labels:
  - setup
dependencies:
  - TASK-1.1
  - TASK-3
references:
  - V1.1.md
parent_task_id: TASK-1
type: docs
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents need reusable, source-backed guidance for writing plugins without inventing interfaces. Inputs are the manuals, completed searchable summaries (TASK-3), inventory, and user-supplied example plugins. Deliver a guide plus skill, not the project plugin or a new dedicated agent. Inspect one example per bounded assignment, then consolidate; missing examples are blockers. No local US3D execution is available.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The guide explains plugin structure, callbacks, data access and demonstrated patterns, with primary manual citations or example file/code locations and known version constraints.
- [ ] #2 The skill directs bounded reference lookup, supported patterns, required clarification and stop conditions; it distinguishes static evidence from target-system verification.
- [ ] #3 A small worked-example check exercises the guide/skill; limitations and checks requiring US3D are recorded without claiming compilation or execution.
- [ ] #4 The guide and skill are linked from the shared knowledge-base starting page.
<!-- AC:END -->
