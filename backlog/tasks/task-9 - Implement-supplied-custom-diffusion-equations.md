---
id: TASK-9
title: Implement supplied custom diffusion equations
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-8
  - TASK-2
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Replace equation placeholders with the user-supplied contributions using the approved hook mapping and verified initialization state. Do not derive/change the physical model or add a separate model-specification task. After inspecting the equations, split multiple independently testable contributions into bounded implementation subtasks; keep genuinely coupled contributions together. Do not invent that breakdown in advance. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Excludes Hartmann validation and production research.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Equation scope is assessed before implementation; where several separable contributions exist, bounded subtasks identify the contribution, inputs/outputs, units/signs/coefficients, approved mapping ID, and add-versus-replace behavior.
- [ ] #2 Each implemented contribution is traceable to a supplied equation and approved mapping entry; missing definitions or uncertainty about the continuous-equation-to-US3D numerical interface is raised for review instead of guessed.
- [ ] #3 Implementation respects supplied conventions and documented integration behavior without unintended double-counting of existing terms.
- [ ] #4 Local mathematical tests compare each bounded contribution with independently established reference values and applicable limiting cases, not only a duplicate of the implementation expression.
- [ ] #5 Custom contributions can remain inactive so the initialization-only configuration and unchanged-output checks remain available.
- [ ] #6 Build/run instructions and unresolved external integration assumptions are recorded for the execution check; local mathematical tests do not claim successful US3D execution.
<!-- AC:END -->
