---
id: TASK-1.2
title: Assess plasma regime and approve first-release MHD equations
status: To Do
assignee: []
created_date: '2026-10-12 16:40'
updated_date: '2026-10-12 16:40'
labels: []
dependencies:
  - TASK-1.1
references:
  - planV1.0.md
parent_task_id: TASK-1
type: spike
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Magnetic-window hypersonic plasmas may invalidate the proposed low-magnetic-Reynolds-number, scalar-conductivity, imposed-field model. Estimate target regimes using representative conditions and the chemistry/transport state available in US3D. A rejected candidate model changes downstream scope before implementation.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Representative operating cases have documented estimates for magnetic Reynolds number, Hall parameter, ionization fraction, collisional scales, and conductivity sensitivity, with inputs and assumptions.
- [ ] #2 The first-release equation set, energy-mode partition, applicability limits, and explicit exclusions (including RF propagation) are recorded with a decision to accept or revise the candidate model.
- [ ] #3 Conductivity/electron-density sourcing from available chemistry and the need for induction or anisotropic transport are explicitly resolved or flagged as blockers.
<!-- AC:END -->
