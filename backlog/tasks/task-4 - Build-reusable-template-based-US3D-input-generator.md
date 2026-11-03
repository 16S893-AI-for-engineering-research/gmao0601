---
id: TASK-4
title: Build reusable template-based US3D input generator
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-1
references:
  - .pi/ref-library/input.inp
  - .pi/ref-library/US3D-User-Manual.pdf
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Generate a new US3D input from .pi/ref-library/input.inp rather than construct arbitrary US3D configurations from scratch. Initial scope is the approved template and an explicit supported set of initial-case settings; later case needs may require approved extensions. Inputs are case paths, explicit physical/numerical settings, target version, and output location. Filepaths alone do not determine the physics. This is one combined design-and-implementation task, not a separate design task. Skill, tool, or hybrid packaging remains undecided: present the interface and packaging proposal for user approval before implementation. Paths used in launch commands are distinct from values inside input.inp. Excludes mesh generation, choosing physics, Slurm generation, and executing US3D.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The user approves the supported settings, input/output contract, packaging, and representative example before implementation; reusable usage instructions are supplied.
- [ ] #2 A new input file is generated from the supplied template without changing the original; existing output files are not silently overwritten.
- [ ] #3 Only supplied settings and explicitly approved retained template settings are used; missing physics, ambiguous boundary-zone mappings, or unsupported configurations trigger clarification rather than guessed values or syntax.
- [ ] #4 A readable change/settings report identifies user-provided values, approved retained values, changes from the template, and unresolved requirements.
- [ ] #5 A case-reference manifest separates input-file references from launch-command or other case dependencies; unavailable remote paths are marked unverified, not automatically invalid.
- [ ] #6 Local tests cover representative rendering, preservation of approved unchanged settings, missing/invalid input, unsupported settings, and overwrite protection; local validation is not described as solver acceptance.
<!-- AC:END -->
