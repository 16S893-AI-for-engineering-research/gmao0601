---
id: TASK-2
title: Build evidence-backed US3D hook-selection subagent
status: In Progress
assignee:
  - '@assistant'
created_date: '2026-10-15 04:13'
updated_date: '2026-10-21 20:37'
labels:
  - setup
dependencies: []
references:
  - >-
    https://16s893-ai-for-engineering-research.github.io/class-repo/sessions/pod-clinic-1/slides/#3
  - V1.1.md
type: feature
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Prepare a reusable equation-to-hook specialist, distinct from using it in TASK-1.3. Inputs are the existing four skills, manuals/searchable reference and small evaluation fixtures; future uses receive user-approved equations/order and a target version or explicit unknown. The skills already exist and their implementation notes are retained. Remaining agent integration, bounded evidence retrieval and fixture evaluation need focused assignments before execution. Reuse TASK-3 navigation rather than re-summarizing manuals. Do not scan PDFs merely to configure the agent. No local US3D installation is available, and documentation findings do not establish runtime support. The specialist does not choose physics or equation order; an equivalent manual audit may proceed without waiting for it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Given equations, required state/terms, and target US3D version (or an explicit unknown), the agent produces a hook-to-equation mapping with required input/output data, lifecycle, units, and parallel/BC considerations.
- [ ] #2 Each proposed hook has a manual/file/page citation and a short supporting excerpt; unsupported claims and conflicts are labeled unknown or blocked rather than invented.
- [ ] #3 The workflow searches and extracts bounded PDF page ranges, supports large or scanned documents with a declared fallback, and records provenance and extraction limitations.
- [ ] #4 A small fixture-based evaluation covers supported, missing, and conflicting hook candidates without requiring the full manuals for routine tests.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
Current requested slice: write four project skill SKILL.md files (equation-to-requirements, manual-evidence-search, hook-capability-mapping, hook-report-review), with clear inputs/outputs and evidence boundaries. Do not inspect the US3D PDFs or implement the agent, extension, or fixture evaluation in this slice. Validate frontmatter and internal references without touching manuals; leave the broader task open.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Wrote four project skills under .pi/skills/: equation-to-requirements, manual-evidence-search, hook-capability-mapping, and hook-report-review. Validated each SKILL.md frontmatter, nonempty body, and referenced skill paths with a local static check. Did not read either US3D PDF. Agent wiring, PDF helper/tool decisions, and fixture-based evaluation remain for future work.

V1.1 reconciliation: the recorded skills-only plan describes the completed requested slice, not the entire remaining feature. Preserve its evidence. Agent integration, bounded retrieval and fixture evaluation remain unfinished; research and record a bounded current plan when resuming. Project-specific hook assessment is now TASK-1.3.
<!-- SECTION:NOTES:END -->
