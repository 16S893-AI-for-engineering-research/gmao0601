---
id: TASK-7
title: Initialize custom diffusion model without activating equations
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-6
references:
  - .pi/ref-library/US3D-Developer-Manual.pdf
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add model-specific state/setup to the verified skeleton while leaving existing diffusion and CFD behavior intact. Use user-supplied required variables, parameters, and initialization values/rules; missing definitions are questions, not permission to invent a model. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Excludes active equation contributions or modification of existing solver fields/transport coefficients. The next verification task establishes unchanged CFD outputs.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Each required variable is classified as new plugin-owned state or existing solver state, with approved new-state initialization values/rules and documented lifecycle location; unspecified definitions are resolved with the user before affected implementation.
- [ ] #2 Only approved new model state is initialized; existing solver values, diffusion calculations, and transport coefficients remain unchanged and custom equation contributions remain inactive.
- [ ] #3 Any required shared-state modification or registration that may alter solver behavior is raised for review before implementation rather than assumed harmless.
- [ ] #4 Applicable configuration validation and local initialization checks cover valid values and invalid inputs, without substituting for actual US3D integration evidence.
- [ ] #5 Build/run instructions and requested outputs allow the user to verify model initialization in the target environment; no unchanged-CFD claim is made before the next paired-run test.
<!-- AC:END -->
