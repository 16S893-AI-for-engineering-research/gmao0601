---
id: TASK-8
title: Verify custom diffusion initialization leaves CFD outputs unchanged
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-7
  - TASK-6
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Repeat the no-change gate after model-specific diffusion state is added, before equations are implemented. Compare no-plugin baseline against the plugin with diffusion initialization present but contributions inactive. Reuse the earlier comparator and baseline only when case/settings/executable/execution provenance still matches; otherwise rerun the baseline. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A paired run package and returned provenance establish that the cases match except for initialization-only plugin presence; baseline reuse is justified or a new baseline is captured.
- [ ] #2 Actual returned evidence confirms diffusion initialization executed and new variables have their approved initial values.
- [ ] #3 All existing CFD outputs produced by the agreed short test match at initialization and each matching later checkpoint using the prior exact-equality/default comparison contract.
- [ ] #4 No tolerance is added to hide differences; any nondeterminism allowance requires explicit approval, only identified nonphysical metadata is excluded, and missing/misaligned outputs or failed runs prevent a pass.
- [ ] #5 The comparison report records actual external evidence, per-checkpoint results, and discrepancies; new variables are checked separately from existing CFD outputs.
<!-- AC:END -->
