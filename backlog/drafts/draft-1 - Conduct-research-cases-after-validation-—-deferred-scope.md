---
id: DRAFT-1
title: Conduct research cases after validation — deferred scope
status: Draft
assignee: []
created_date: '2026-11-03 22:09'
labels: []
dependencies:
  - TASK-11
  - TASK-11.1
  - TASK-11.2
  - TASK-11.3
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
User-approved high-level placeholder for actual research cases after preceding capabilities, implementation, and validation are complete. Intentionally remains vague and is not an executable agent assignment. Do not invent research questions, parameter sweeps, case settings, analysis requirements, or compute budgets now. Once validation is complete, obtain user direction and scope bounded case or closely related study tasks through the Backlog workflow. Agents cannot access the US3D/Slurm environment. The agent prepares artifacts, instructions, and analysis; the user compiles/runs US3D and returns logs and outputs. Local checks or mocks cannot establish successful US3D execution. External verification remains pending until actual evidence is returned. Production work requires all three Hartmann cases to pass and the overall validation review to be complete. No expectation that research must confirm a preferred scientific outcome.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Before activation, the user approves concrete scientific questions, case definitions, requested outputs/analysis, and compute limits; this placeholder is refined or split into bounded executable tasks.
- [ ] #2 Production readiness is supported by completed validation review and passing weak/moderate/stronger Hartmann cases; each research case passes its approved short-run check before production execution.
- [ ] #3 For the subsequently approved scope, actual returned production evidence meets agreed convergence/sampling requirements and preserves inputs, plugin/build/run configuration, and output provenance.
- [ ] #4 The agreed analysis distinguishes supported findings, numerical uncertainty, and unresolved issues; no new research direction or unapproved compute sweep is undertaken.
<!-- AC:END -->
