---
id: TASK-1
title: US3D plasma and MHD plugin for magnetic-window studies
status: To Do
assignee: []
created_date: '2026-10-12 16:39'
updated_date: '2026-10-21 20:37'
labels:
  - coordination
dependencies: []
references:
  - planV1.0.md
  - V1.1.md
type: feature
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Coordination task for the V1.1.md workflow, not a single implementation assignment. The user supplies equations, assumptions and calculation/update order and assesses physical suitability offline. Work here covers knowledge-base setup, specification, hook evidence, operator-free initialization, external no-op regression, equation-by-equation implementation, canonical verification and a hypersonic comparison. Sensitivity and release tasks remain broad. US3D is not and will not be installed on this computer. Reuse TASK-3 manual references and TASK-2 specialist progress. Do not assume induction, Hall, RF propagation or any particular candidate equations are in scope.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Tracked work collectively provides an approved user-supplied equation/order specification, evidence-backed integration, no-op verification, per-equation calculation/integration evidence, canonical verification and a reproducible hypersonic comparison.
- [ ] #2 Knowledge-base deliverables and agreed sensitivity/release work are accounted for, with external runtime evidence distinguished from local preparation.
- [ ] #3 Applicability limits, exclusions and unresolved blockers are explicit; no RF/blackout benefit is claimed solely from flow/plasma changes.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Reconciled with the user-approved V1.1.md workflow. This is a planning update, not implementation or verification evidence. Historical planV1.0.md references are retained for provenance; V1.1.md governs the revised scope.
<!-- SECTION:NOTES:END -->
