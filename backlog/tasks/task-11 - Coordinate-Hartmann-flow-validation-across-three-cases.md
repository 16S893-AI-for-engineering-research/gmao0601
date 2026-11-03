---
id: TASK-11
title: Coordinate Hartmann-flow validation across three cases
status: To Do
assignee: []
created_date: '2026-11-03 22:09'
labels: []
dependencies:
  - TASK-10
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Validate implemented physics using classical steady parallel-plate Hartmann flow at weak, moderate, and stronger magnetic influence. This parent owns the shared benchmark definition and overall conclusion; three child tasks own case execution/evaluation. Select actual Hartmann numbers only after checking model applicability and mesh requirements. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Shared criteria must be approved before cases are evaluated. Complete the weak-field case first to establish reusable case/reference/comparison artifacts, then use them for the other cases. Do not change equations or relax thresholds merely to obtain agreement.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A traceable analytical reference and its assumptions are checked against the implemented model; incompatibilities are raised before simulation-based validation claims.
- [ ] #2 The user approves shared geometry, properties, forcing, electrical/current-closure conditions, boundary/initial conditions, and three Hartmann numbers before execution.
- [ ] #3 Comparison quantities, extraction conventions, quantitative error metrics/accuracy thresholds, convergence requirements, and mesh-sensitivity expectations are approved before judging results and shared across child cases.
- [ ] #4 Shared reference calculations have independent checks including the applicable zero-field limit; the first case establishes reusable generation/comparison artifacts before the other two begin.
- [ ] #5 All three child cases have evidence-backed pass/fail reports; the overall report summarizes errors, convergence, mesh sensitivity, and unresolved discrepancies without hiding failed cases.
- [ ] #6 The overall report explicitly states which implemented physics/terms are exercised and which are not; research readiness requires all three cases to pass and an overall validation review.
<!-- AC:END -->
