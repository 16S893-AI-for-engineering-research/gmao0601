---
id: TASK-1.13
title: Create input-file-writing reference guide and skill
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
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents need reusable guidance to prepare US3D cases without guessing physical settings. Inputs are manuals, completed summaries (TASK-3), inventory, and user-supplied prepared cases. Deliver a guide plus skill, not production project inputs or a dedicated agent. Inspect one case per bounded assignment, then consolidate; missing files remain explicit blockers. No local US3D execution is available.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The guide explains required files/settings, optional settings, model-dependent choices, documented incompatible combinations, versions and common omissions, citing manuals or supplied case files.
- [ ] #2 Each inspected case has a purpose, relevant input-file map and missing-dependency record; the skill asks for necessary case details rather than silently choosing physical settings.
- [ ] #3 A worked-example check exercises the guidance and available static checks without claiming that US3D accepts or runs the inputs.
- [ ] #4 The guide and skill are linked from the shared knowledge-base starting page.
<!-- AC:END -->
