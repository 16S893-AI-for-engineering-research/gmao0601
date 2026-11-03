---
id: TASK-3
title: Build reusable hooks-to-plugin-skeleton capability
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-2
references:
  - .pi/ref-library/US3D-Developer-Manual.pdf
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Generate repeatable plugin scaffolding from an approved hook mapping while preserving current CFD behavior. Inputs include the mapping, plugin name/output location, target US3D version, approved variable definitions/initialization rules, and known build configuration. This is one combined design-and-implementation task, not a separate design task. Skill, tool, or hybrid packaging remains undecided: present the interface and packaging proposal for user approval before implementation. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Includes documented registration/setup and approved variable initialization, but not active equations. Model-specific diffusion initialization is handled by a later task.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The user approves the interface and packaging proposal, including a representative input/output example, before implementation; reusable usage instructions are supplied.
- [ ] #2 Only approved mapping entries drive generated hooks and registration/setup; generated source and an artifact manifest trace back to stable mapping IDs and documented signatures.
- [ ] #3 New variables use explicitly approved initialization values/rules; existing solver values and calculations are preserved and new physical contributions remain inactive.
- [ ] #4 Each hook uses documented behavior-preserving handling; zero outputs or empty bodies are not presumed safe, and unresolved inactive behavior blocks affected generation pending clarification.
- [ ] #5 Missing definitions, unsupported interfaces, unknown build settings, and overwrite conflicts are reported rather than guessed or silently overwritten.
- [ ] #6 Outputs include source, identified equation placeholders, artifact manifest, build/run instructions, and a report separating local structural checks from unverified external compilation/runtime behavior.
- [ ] #7 Local generation tests cover representative approved mappings and rejection of unresolved inputs; actual behavior preservation is reserved for the paired-run verification task.
<!-- AC:END -->
