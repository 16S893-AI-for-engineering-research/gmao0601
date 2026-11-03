---
name: equation-to-requirements
description: Decompose user-specified solver equations into a checkable US3D integration-requirements checklist. Use before looking for plugin hooks or reading US3D manuals.
---

# Equation to requirements

Use this skill first when the user supplies equations or asks which solver hooks would be needed. This is requirements analysis, **not** a claim that US3D supports any particular hook. Do not open the PDFs in `.pi/ref-library` in this step.

## Input contract

Ask for or record: the exact equations (including definitions of symbols), the intended solver behavior, target US3D version/build if known, governing approximations, desired spatial/temporal discretization if prescribed, and whether the user wants an in-process plugin or will consider external coupling. Record missing information as `unknown`; never quietly choose physics, signs, units, or a coupling scheme. If a missing item changes the hook search materially, request clarification before searching.

## Decompose each equation

1. Give every equation and term a stable ID (`E1`, `E1.T1`, etc.); preserve the user's original form and distinguish specified terms from inferred implementation needs.
2. For each term list required state, material/transport properties, geometry or field data, derivatives, spatial location (cell/face/boundary), units and sign convention, and what must be read or written. Distinguish conserved variables from primitive variables and auxiliary fields.
3. Identify the numerical operation required: source update, flux, potential/field solve, boundary contribution, diagnostic, or other; mark unknown operations explicitly. Record when information must be available (initialization, per stage/iteration, boundary update, output/restart) without asserting that a corresponding US3D hook exists.
4. Note conservation and coupling constraints: e.g., consistency between momentum and energy terms if both are present, exchange across domain partitions, boundary conditions, restart state, and time-step/stability requirements. Include only constraints entailed by the supplied equations or clearly label them as questions.
5. Keep separate lists of **user-specified facts**, **derived needs with reasoning**, and **open questions/assumptions awaiting approval**.

## Handoff

Return two things:

1. **Requirements table:** `ID | equation/term | operation | reads (units/location) | writes (units/location) | timing | boundary/parallel/restart needs | unresolved questions`. Supply the target version or `unknown`.
2. **Variable list for `hook-capability-mapping`:** one row per distinct variable across all equations. Merge duplicates, and give each variable every intent it needs:

   `variable | meaning + units | intent (read / create / write / save, or unknown) | location (cell / face / boundary / node / global, or unknown) | timing needed | used by (term IDs) | notes`

   Include solver state that is read (e.g. density, velocity, temperature), new fields or properties that must be created (e.g. a conductivity, an electric potential, a magnetic field), contributions that are written (e.g. a momentum or energy source term, a face flux), and anything that must persist across restarts or appear in output. Use the user's symbol names. Do not guess US3D names or hooks; that is the mapping skill's job.

Pass the variable list to `hook-capability-mapping`, which also accepts a variable list given directly by the user. Keep the requirements table so `hook-report-review` can check that every term is covered. Do not propose named hooks here.
