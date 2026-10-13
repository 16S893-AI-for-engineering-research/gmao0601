---
id: TASK-1.4
title: Create US3D plugin skeleton and no-op regression
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-12 16:40'
labels: []
dependencies:
  - TASK-1.3
references:
  - planV1.0.md
parent_task_id: TASK-1
type: task
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A minimal, supported plugin integration is needed before introducing electromagnetic physics so build, configuration, and callback problems are distinguishable from model bugs.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The plugin builds/loads on the supported US3D version and reports invalid configuration clearly.
- [ ] #2 Plugin disabled or configured with no coupling reproduces the recorded baseline within documented numerical variation.
- [ ] #3 Configuration, output, restart, and MPI lifecycle paths have automated checks or documented executable integration tests.
<!-- AC:END -->
