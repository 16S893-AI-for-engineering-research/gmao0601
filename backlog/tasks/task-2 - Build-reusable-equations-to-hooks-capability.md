---
id: TASK-2
title: Build reusable equations-to-hooks capability
status: To Do
assignee: []
created_date: '2026-11-03 22:08'
labels: []
dependencies:
  - TASK-1
references:
  - .pi/ref-library/US3D-Developer-Manual.pdf
  - .pi/ref-library/summaries/README.md
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Turn user-supplied equations into reviewable US3D integration mappings rather than guessed interfaces. Include supporting initialization and data requirements as well as equation terms. Missing equation definitions trigger targeted clarification within this workflow; do not add a separate model-specification task or derive/change the physics. This is one combined design-and-implementation task, not a separate design task. Skill, tool, or hybrid packaging remains undecided: present the interface and packaging proposal for user approval before implementation. Skeleton generation requires approval of the resulting mapping. Excludes plugin generation and runtime verification.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The approved interface specifies required/optional equation inputs, model conventions, target version, outputs, clarification behavior, and one representative input/output example; reusable usage instructions are provided.
- [ ] #2 The implemented capability emits a readable Markdown review report and a structured machine-readable mapping (such as JSON), with stable entry IDs and consistent content.
- [ ] #3 Each mapping entry identifies the equation/source or supporting operation, documented hook name/signature, invocation timing, required data and availability, read/write behavior, and whether it adds to or replaces existing behavior, with original-manual section/page citations.
- [ ] #4 Reports clearly separate supported conclusions, unresolved assumptions/questions, and review/approval status; unknown or unsupported interfaces are not invented or presented as approved.
- [ ] #5 Missing definitions elicit targeted questions; the capability requires mapping approval before downstream skeleton generation.
- [ ] #6 Local checks/examples cover supported mappings, incomplete inputs, unsupported operations, and consistency between the human-readable and structured outputs; no local result claims US3D runtime verification.
<!-- AC:END -->
