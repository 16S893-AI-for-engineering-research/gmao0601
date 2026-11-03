---
id: TASK-5
title: Build reusable Slurm submission-script generator
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-1
references:
  - .pi/ref-library/example_submit.sh
  - .pi/ref-library/post.scr
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Generate repeatable submission scripts using .pi/ref-library/example_submit.sh and confirmed cluster settings. The supplied script is a reference, not a source of unquestioned defaults: it requests 384 tasks but launches four MPI processes. Inputs include case directory/paths, environment setup, executable/launch configuration, resources, selected execution stages, and output location. This is one combined design-and-implementation task, not a separate design task. Skill, tool, or hybrid packaging remains undecided: present the interface and packaging proposal for user approval before implementation. Confirmed settings may be reused. Excludes submission, monitoring, cluster access, performance tuning, and changes to case physics.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The user approves the interface/packaging and required cluster settings, including resolution of allocation-versus-launch ambiguity, before implementation; usage instructions and a representative example are supplied.
- [ ] #2 Generated scripts use supplied or explicitly approved reusable settings, with consistent resource allocation and process launch counts; missing cluster requirements are reported.
- [ ] #3 Preprocessing, solver execution, and postprocessing can be selected separately; working directory, logging, and failure behavior are explicit.
- [ ] #4 Source examples are unchanged, existing outputs are not silently overwritten, and generation never submits or executes the job.
- [ ] #5 A report identifies settings used, unresolved requirements, and local checks; shell syntax and representative generation/invalid-input tests pass without claiming target-cluster validation.
<!-- AC:END -->
