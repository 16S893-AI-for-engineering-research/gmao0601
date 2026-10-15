---
name: hook-report-review
description: Audit a proposed equation-to-US3D-hook report for traceable citations, unsupported claims, version conflicts, and missing verification. Use before sending hook recommendations to the user.
---

# Hook report review

Review the outputs of `equation-to-requirements`, `manual-evidence-search`, and `hook-capability-mapping`. This is a quality gate, not a second opportunity to guess missing API facts.

## Review checklist

- Every user equation/term and requirement ID appears in the mapping, or is explicitly listed as unaddressed. No new physical assumption is presented as user-specified.
- Every claimed interface, lifecycle, permitted access, and restriction has a **specific** document filename, PDF page index, and short supporting excerpt. Check that the excerpt actually supports the precise claim, not just a related topic. Cite printed page numbers separately if present.
- Each claim is marked documented, tested on the target installation, or unknown. Do not upgrade a manual citation to a runtime guarantee. Note manual revision versus target US3D version and whether that match is confirmed.
- Conflicting evidence, incomplete page coverage, unreadable/scanned pages, and unsuccessful searches remain visible. A scoped negative result must not be described as a global absence.
- Read/write locations, units/signs, update ordering, source/flux distinction, boundary behavior, parallel exchange, restart, and any coupled solve are accounted for or explicitly marked unverified.
- Proposed tests and blockers are actionable. Do not state that a hook can host a global solve solely because it can add a local source term.

If a claim fails review, remove it or downgrade it to a question with the exact missing evidence. Do not fabricate citations. If a required source cannot be checked, say so and return the unresolved item rather than presenting a definitive recommendation.

## Report format

Return these headings in order:

1. **Scope** — supplied equations, target version or `unknown`, manuals searched, ranges and extraction limitations.
2. **Requirements-to-hooks matrix** — IDs, candidate hooks, required access/timing, citations with excerpts, confidence/status, and blockers.
3. **Unresolved questions and conflicts** — including missing pages, version mismatches, and assumptions needing user approval.
4. **Verification on target US3D** — small, concrete example-plugin/build/runtime checks required before implementation decisions.

Keep the report compact enough for a parent agent to inspect; provide a location for any larger evidence log if one was explicitly requested. Do not inspect PDFs as part of skill authoring or invoke a document-analysis run without a user-provided equation request.
