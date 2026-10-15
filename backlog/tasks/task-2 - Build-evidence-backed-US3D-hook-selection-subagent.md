---
id: TASK-2
title: Build evidence-backed US3D hook-selection subagent
status: In Progress
assignee:
  - '@assistant'
created_date: '2026-10-15 04:13'
updated_date: '2026-10-15 04:17'
labels: []
dependencies: []
references:
  - >-
    https://16s893-ai-for-engineering-research.github.io/class-repo/sessions/pod-clinic-1/slides/#3
type: feature
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The project needs a repeatable, equation-driven way to locate candidate integration hooks in large US3D manuals without filling the parent context or mistaking documentation claims for verified runtime capabilities. The manuals are present in .pi/ref-library, while .pi/agents/hook-selection.md is only a stub. This specialist should support the existing TASK-1.1 audit, not substitute for checking an installed version or a working example plugin. Do not scan the PDFs during agent setup; document analysis belongs to runs of the specialist on explicitly requested equations.
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
<!-- SECTION:NOTES:END -->
