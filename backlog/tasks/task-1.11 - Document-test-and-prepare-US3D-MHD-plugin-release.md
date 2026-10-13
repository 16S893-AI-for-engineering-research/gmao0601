---
id: TASK-1.11
title: 'Document, test, and prepare US3D MHD plugin release'
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-12 16:40'
labels: []
dependencies:
  - TASK-1.9
  - TASK-1.10
references:
  - planV1.0.md
parent_task_id: TASK-1
type: docs
ordinal: 12000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Future users need a reproducible installation and an honest statement of supported US3D versions, tested regimes, performance, and excluded physics before relying on magnetic-window studies.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 User/developer documentation covers installation, build, supported versions, inputs/outputs and units, boundary conditions, examples, restarts, MPI, and troubleshooting.
- [ ] #2 Automated test commands and canonical/hypersonic example reproduction steps are documented and pass in the target environment.
- [ ] #3 MPI rank-count and restart consistency, solver failure reporting, and runtime/memory overhead are measured or explicitly documented as unresolved release blockers.
- [ ] #4 Model validity, limitations, and deferred induction, Hall, and RF work are clearly stated.
<!-- AC:END -->
