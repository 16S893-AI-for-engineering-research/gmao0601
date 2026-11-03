---
id: doc-1
title: US3D plugin project — agreed plan and decision log
type: guide
created_date: '2026-11-03 22:10'
updated_date: '2026-11-03 22:21'
---
# US3D plugin project: agreed plan and decision log

## Planning session

Pi session ID: `01a1a267-7143-73f3-af8c-3f8760c76d7a`

This is the session in which the plan was reviewed and the initial Backlog tasks were created.

## Purpose and authority

This document records the plan developed and approved with the user before implementation. It preserves the reasons behind the task boundaries and safeguards so future agents do not need the original conversation.

The tasks in `backlog/` are authoritative for current scope, dependencies, acceptance criteria, and status. This log is a record of the initial agreement, not an alternate implementation plan. Later approved task changes take precedence; update this log through the Backlog CLI when significant decisions change. Do not recover requirements from archived plans or retired skills.

At creation, TASK-1 through TASK-11 and the three validation subtasks were unassigned and To Do. Research was recorded as DRAFT-1. No implementation or US3D validation had been performed as part of planning.

## Overall objective

Create reusable capabilities that turn supplied equations into documented US3D hooks, hooks into a plugin skeleton, case paths/settings into input files, and cluster/case settings into Slurm scripts. Introduce custom diffusion incrementally: first initialize without changing CFD behavior, then implement equations, verify execution, validate against Hartmann flow, and finally undertake research cases.

## Sources and execution boundary

Primary references are under `.pi/ref-library/`:

- `US3D-User-Manual.pdf` and `US3D-Developer-Manual.pdf`; the library README identifies these as US3D 1.2.1 manuals. The installed target version still requires confirmation.
- Chapter PDFs, indexes, and secondary summaries. Exact API/signature/syntax claims must refer back to original manual sections/pages.
- `input.inp`, `example_submit.sh`, and `post.scr`.

Inventory the supplied example as-is. Record missing files and unresolved environment requirements; resolving them is not required to finish the inventory. Do not modify the originals. The Slurm example requests 384 tasks but launches four MPI processes; this is an open question, not a value to copy or silently fix.

**Agents cannot access the target US3D/Slurm environment.** Agents prepare artifacts, local checks, instructions, and analysis. The user compiles/runs US3D and returns logs and requested outputs. Local tests, mocks, and static checks cannot establish actual compilation or simulation success. External verification remains pending until real evidence is available.

## Approved task map

| ID | Agreed scope |
| --- | --- |
| TASK-1 | Inventory manuals, topic references, example artifacts, missing assets, and questions. |
| TASK-2 | Build reusable equations-to-hooks capability with human-readable and structured mapping outputs. |
| TASK-3 | Build reusable hooks-to-plugin-skeleton capability, including approved variable initialization without active physics. |
| TASK-4 | Generate new US3D inputs from the supplied template and explicit settings. |
| TASK-5 | Generate Slurm scripts from the example and confirmed cluster settings. |
| TASK-6 | Verify initialized hooks leave all existing CFD outputs unchanged. |
| TASK-7 | Initialize custom diffusion state without activating equations or changing existing diffusion. |
| TASK-8 | Repeat the unchanged-CFD-output verification after diffusion initialization. |
| TASK-9 | Implement supplied custom diffusion equations, splitting bounded contributions if necessary. |
| TASK-10 | Verify that the active plugin compiles, loads, initializes, and completes the agreed short run. |
| TASK-11 | Coordinate the shared Hartmann benchmark and synthesize overall validation. |
| TASK-11.1 | Validate the weak-field Hartmann case and establish the reusable case/comparison workflow. |
| TASK-11.2 | Validate the moderate-field case using the established workflow. |
| TASK-11.3 | Validate the stronger-field case, including adequate thin-layer resolution. |
| DRAFT-1 | Deferred research placeholder; not ready for agent assignment. |

## Dependency and approval structure

- TASK-1 precedes TASK-2, TASK-4, and TASK-5. TASK-2 precedes TASK-3.
- TASK-6 depends on TASK-3, TASK-4, and TASK-5.
- Then follow diffusion initialization, its no-change verification, equation implementation, and the active execution check: TASK-7 through TASK-10.
- TASK-11 and its weak-field case follow TASK-10. Case execution also requires approval of the shared benchmark and criteria recorded under the parent.
- Finish the weak-field case before starting moderate/stronger cases. They reuse the same reference and comparison machinery rather than independently selecting assumptions or thresholds.
- TASK-11 remains open for overall synthesis; it does not have to be completed before its children can run. This avoids a parent/child dependency deadlock.
- Research readiness requires all three cases to pass and the overall validation review to be complete.

## Decisions and rationale

### Reusable capabilities, not one-off artifacts

The user wants reusable skills or tools, but packaging remains undecided. Each of TASK-2 through TASK-5 includes an interface/packaging approval checkpoint followed by implementation and local tests. Skills, deterministic tools, or hybrids may differ by capability.

Separate design tasks and duplicate build tasks were explicitly rejected. Do not recreate that split without approval. A standalone model-specification task was also rejected: clarify missing equation information inside the relevant capability or model work instead.

### Reviewable equations-to-hooks output

TASK-2 must produce two consistent views of the same mapping:

1. A readable Markdown report for human review.
2. A structured machine-readable representation, such as JSON, with stable entry IDs for future agents.

Each entry identifies the equation/source or supporting operation, hook/signature, timing, required data and availability, read/write behavior, add-versus-replace semantics, and original-manual citations. Include initialization/data requirements, not only direct equation terms. Clearly distinguish unresolved assumptions from approved instructions. Mapping approval is required before skeleton generation.

### Behavior-preserving initialization

TASK-3 and TASK-7 initialize approved new state while leaving existing solver values and CFD behavior unchanged. New physical contributions remain inactive. Zero values and empty hook bodies are not automatically safe: a hook might replace an existing calculation rather than add to it.

Use documented behavior-preserving handling. Ask when this cannot be established. Distinguish plugin-owned variables from existing solver state; review shared-state changes or registrations that might alter behavior. Do not invent initialization values or silently overwrite existing transport coefficients.

### Template-based input and submission generation

TASK-4 generates a new file from `.pi/ref-library/input.inp`; it is not a universal US3D input generator. Apply supplied settings and retain only approved template settings. Preserve the original and report changes. Filepaths alone do not specify physical parameters or boundary conditions. Keep launch-command paths separate from input-file contents, and do not treat inaccessible remote paths as necessarily invalid.

TASK-5 uses confirmed cluster/resource settings and keeps allocation and launch counts consistent. Preprocessing, solver execution, and postprocessing are separately selectable. Generation does not submit or execute a job. Both generators need missing-input handling and overwrite protection.

### Unchanged CFD output is a strict gate

TASK-6 and TASK-8 compare a no-plugin baseline with the initialization-only plugin at initialization and matching checkpoints over a few subsequent steps. Specify the actual step count and distinguish physical time steps from solver iterations when applicable.

Compare all existing CFD solution outputs produced by the agreed test. The solution may evolve, but it must evolve equivalently between the two runs. Align mesh locations, fields, and checkpoints rather than comparing storage ordering or whole files blindly.

- Exact equality of existing CFD values is the default.
- Exclude only identified nonphysical metadata, such as timestamps and execution timing.
- Investigate baseline nondeterminism; any numerical allowance requires explicit user approval.
- Check new plugin variables separately against expected initialization values.
- Missing fields, outputs, locations, or checkpoints prevent a pass.
- Reports identify changed fields, checkpoints, locations, and difference magnitudes.
- Reuse baseline artifacts only when case, settings, executable, and execution provenance still match.

### Equation implementation must be bounded

TASK-9 remains one overall task until the supplied equations are inspected. Split independently testable contributions into concrete subtasks where needed; do not artificially separate genuinely coupled terms. Each assignment must identify the equation, conventions, mapping entry, and expected reference results.

Reference values must be independently established, not merely calculated by copying the implementation expression into a test. Missing definitions or uncertain numerical-interface interpretation require review. Preserve the inactive configuration for regression testing.

### Execution success is not scientific validation

The user clarified that TASK-10's goal is to verify the plugin runs. Successful compilation, loading, initialization, active contribution execution, and completion of the short run establish readiness for validation, not physical accuracy. Do not expand it into a duplicate validation task. A case with physically zero contribution need not show an artificial CFD change to prove execution.

### Three Hartmann cases with shared validation criteria

Use classical steady, parallel-plate Hartmann flow, provided its assumptions match the implemented model. The three cases represent weak, moderate, and stronger magnetic influence; actual Hartmann numbers are deliberately not selected yet.

Before execution/evaluation, approve the reference, geometry, properties, forcing, electrical/current-closure conditions, boundary/initial conditions, metrics, accuracy thresholds, convergence requirements, and mesh-sensitivity expectations. Independently check reference calculations, including the applicable zero-field limit.

The final decision split the cases into three child tasks under a coordination parent to keep agent assignments bounded. The first case establishes reusable machinery. Each case needs real solver evidence and a quantitative pass/fail report. Do not relax thresholds or change equations simply to achieve agreement. State which model terms the benchmark does and does not exercise.

### Research remains intentionally deferred

DRAFT-1 is a high-level placeholder. After validation, the user supplies the scientific questions, concrete cases/studies, requested analysis, and compute limits. Only then refine or split it into executable assignments. Do not invent research directions or launch unapproved sweeps. Research does not need to confirm a preferred outcome; it needs trustworthy execution and honest analysis.

## Agent suitability and handoff guidance

The plan is designed for bounded assignments suitable for Sonnet-class agents. No particular capability level was established for a model called Terra; assess an unfamiliar agent on a bounded task rather than assume equivalence.

Highest-judgment work is hook selection, equation integration, and validation design. Use source citations, explicit inputs/outputs, independent reference checks, and user approval gates. Human-readable artifacts plus stable structured references reduce the need for future agents to reconstruct context. This log does not authorize delegation or grant cluster access.

## Deferred decisions

- Skill/tool/hybrid packaging and exact artifact schemas/locations.
- Installed US3D version, complete case assets, and confirmed cluster launch settings.
- Equation sources, missing definitions, and approved model initialization values.
- Short-run length, output collection format, and any justified baseline nondeterminism allowance.
- Hartmann reference, actual parameter values, thresholds, and mesh requirements.
- Research questions, case definitions, analysis, and computational budget.

Resolve these within their associated tasks rather than inventing defaults or treating this log as proof that they have already been approved.
