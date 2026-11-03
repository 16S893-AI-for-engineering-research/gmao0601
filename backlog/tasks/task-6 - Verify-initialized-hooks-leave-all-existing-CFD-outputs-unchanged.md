---
id: TASK-6
title: Verify initialized hooks leave all existing CFD outputs unchanged
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-3
  - TASK-4
  - TASK-5
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Establish that the generated plugin can load and initialize approved new variables without changing the simulation before custom diffusion initialization or equations are added. Compare the same case without the plugin against the initialization-only plugin at initialization and matching checkpoints over a few subsequent steps. Fields may evolve, but must evolve identically between runs. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Agree on step count and distinguish solver iterations from physical time steps where necessary. Excludes active physics and scientific model validation.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A paired test package specifies matching case inputs, executable/build provenance, physical/numerical settings, execution configuration, checkpoints, and all required returned artifacts; only plugin presence/setup differs.
- [ ] #2 User-returned build/run evidence confirms successful compilation/loading, hook initialization execution, and expected initial values for new plugin variables.
- [ ] #3 The comparison inventories all existing CFD solution fields/outputs produced by the agreed baseline test and compares their values at initialization and every selected subsequent checkpoint, aligning mesh locations and checkpoints rather than assuming storage ordering.
- [ ] #4 Existing CFD values are exactly equal by default; only identified nonphysical metadata (such as timestamps/timing) is excluded. Any baseline nondeterminism is investigated and any proposed numerical allowance requires explicit user approval, never silent relaxation.
- [ ] #5 New plugin variables are checked separately; missing fields/outputs, unmatched locations, failed runs, and missing or mismatched checkpoints prevent a pass.
- [ ] #6 The reusable offline comparator has independent fixtures that pass equal data, detect introduced changes, and reject incomplete/misaligned data; readable reports locate differences by field/checkpoint/location and give their magnitude.
- [ ] #7 A report based on actual returned US3D evidence records pass/fail, configuration provenance, comparison rules, and discrepancies; local fixtures alone cannot complete external verification.
<!-- AC:END -->
