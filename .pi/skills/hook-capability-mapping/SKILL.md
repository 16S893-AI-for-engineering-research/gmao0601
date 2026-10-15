---
name: hook-capability-mapping
description: Map equation requirements to evidence-backed candidate US3D integration hooks and blockers. Use after bounded manual evidence search, not as a substitute for testing a solver installation.
---

# Hook capability mapping

Use the requirements table from `equation-to-requirements` and evidence packets from `manual-evidence-search`. A matching word in a manual does not by itself demonstrate that an interface supports the requested numerical operation.

## Evaluate each requirement ID

1. Identify *candidate documented* hook/interface names only where an evidence packet supports them. Preserve exact names, documented prerequisites and version scope; never synthesize an API name.
2. Compare needed operation to documented capabilities: lifecycle/call frequency and ordering, read/write access, cell/face/boundary location, source or flux insertion, field-solve feasibility, configuration, units, parallel exchange, restart and diagnostics. Mark each dimension `supported by citation`, `contradicted by citation`, or `not established`; absence of evidence is not proof of impossibility.
3. Trace data flow between terms and hooks. Note conversions and conservation requirements, and distinguish a plugin callback from arbitrary access to internal solver state. If a coupling needs a spatial solve, do not assume a local source hook can implement it; flag an architectural blocker or a *hypothesis* to investigate.
4. When sources conflict or target version is unknown, show alternatives and version uncertainty; do not combine capabilities across incompatible releases. Separate documented candidates from experimentally verified capabilities (only a working example on the target installation can establish the latter).
5. Produce explicit follow-up questions/tests for any missing dimension. Do not write plugin code or approve the physics in this skill.

## Output

Return a matrix: `requirement ID | candidate hook/interface | lifecycle | reads/writes + units/location | boundary/parallel/restart implications | evidence (filename, PDF page, excerpt) | status | open verification`. Use statuses `documented candidate`, `partially documented`, `conflicting evidence`, `not established`, or `documented blocker`. Use `not established` if no candidate is found within the recorded search scope. End with a minimal target-installation/example-plugin verification checklist to hand to the US3D capability audit (TASK-1.1).
