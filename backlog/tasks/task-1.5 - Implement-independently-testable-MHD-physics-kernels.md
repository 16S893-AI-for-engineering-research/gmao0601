---
id: TASK-1.5
title: Implement independently testable MHD physics kernels
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
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sign, unit, and energy-accounting mistakes in Ohm’s law and Lorentz-force sources can silently corrupt coupled runs. Isolate the arithmetic with prescribed conductivity and a uniform magnetic field before connecting a spatial solve.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Automated analytic-value tests cover Ohm’s law, cross products, Lorentz-force direction, electrical work/heating identity, and limiting zero-field/zero-conductivity behavior.
- [ ] #2 Inputs and outputs have documented SI units and sign/reference-frame conventions.
- [ ] #3 Invalid/nonphysical properties produce documented, test-covered behavior rather than silently nonfinite source terms.
<!-- AC:END -->
