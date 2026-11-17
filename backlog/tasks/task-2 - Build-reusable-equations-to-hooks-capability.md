---
id: TASK-2
title: Build reusable equations-to-hooks capability
status: In Progress
assignee:
  - '@pi'
created_date: '2026-11-03 22:08'
updated_date: '2026-11-05 18:44'
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

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Per user direction, keep the implementation to one self-contained .pi/skills/equations-to-hooks/SKILL.md for now. This replaces the earlier multi-file implementation plan.
2. Remove the added helper scripts, tests, fixtures, reference contract and generated Python caches.
3. Keep concise skill instructions for symbolic equations and variable definitions, targeted clarification, original-manual-backed mapping, and explicit user approval before downstream skeleton work. No mandatory input form or source-location requirement.
4. Describe readable and structured mapping outputs within the skill without adding a schema, renderer, validator or automated approval machinery.
5. Check that only SKILL.md remains and that it has no references to removed files. Keep TASK-2 open; broader acceptance verification is deferred.

6. Run the user-authorized Opus report-writing trial: save the provisional Lorentz-source mapping to reports/task-2/lorentz-force-mapping.md and reports/task-2/lorentz-force-mapping.json; correct evidence and physics-labeling errors, verify original-manual citations, and check matching IDs/content and JSON validity. These are generated trial reports, not additions to the single-file skill implementation. Keep the mapping unapproved and TASK-2 In Progress; no plugin code or acceptance sign-off.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
User selected skill packaging. Interface proposal and implementation plan are being prepared; implementation remains gated on interface approval.

Reviewed Pi skill documentation, an existing project skill layout, and the reference-library map. Manuals document 1.2.1; installed version remains unconfirmed. Interface proposal recorded in the plan for user approval. No skill implementation files created.

User simplified the proposed input to symbolic equations and variable definitions. Awaiting approval to implement the revised interface; no skill files created.

User approved the revised simple-input workflow: symbolic equations and variable definitions, targeted clarification, documented mapping, explicit mapping approval. Implementation authorized; packaging is a project skill with bundled Python standard-library report helpers and examples.

Simplified at user request to a single self-contained SKILL.md. Removed the added scripts, tests, JSON fixtures, examples README, reference contract and Python caches. Removed automated digest/gate machinery. Only SKILL.md remains; checked that it has no references to removed supporting files. Broader task acceptance verification remains deferred; task stays In Progress.

User-authorized Opus trial reports saved to reports/task-2/lorentz-force-mapping.md and reports/task-2/lorentz-force-mapping.json (revision restart-opus-002). Parent reviewed both, corrected unsupported EM-field absence wording and variable provenance, and explicitly marked missing handler/supporting-operation contracts unresolved. Local checks passed: JSON parsing, 19 unique entry IDs present in Markdown, revision/unapproved status, equation and blocker references, finding IDs, and git diff --check. This is a provisional Lorentz integration-point report, not complete acceptance verification: source scaling/access, field/current/conductivity models, storage and energy coupling remain unresolved. No plugin generation or runtime verification; mapping unapproved and TASK-2 remains In Progress.
<!-- SECTION:NOTES:END -->
