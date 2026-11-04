---
name: equations-to-hooks
description: Map symbolic equations and variable definitions to documented US3D hooks, including supporting data and initialization requirements. Use when selecting integration points for user-supplied equations. Ask targeted clarification questions and present a documented mapping for user approval; do not generate plugins or claim runtime verification.
---

# Equations to US3D hooks

**Symbolic equations + variable definitions → targeted clarification → documented mapping → user approval.**

## Input

Accept symbolic equations (plain text or LaTeX) and variable definitions directly in chat or from a user-provided file. Do not require a paper, source location, structured form or separate model-specification document.

Example:

```text
J = -D ∇φ
J: diffusive flux vector [kg/(m² s)]
D: constant scalar diffusivity [m²/s]
φ: scalar concentration [kg/m³]
∇: spatial gradient [1/m]
```

Preserve the user's expressions and definitions. Do not derive missing physics, change equations or silently assume conventions.

## Workflow

### 1. Clarify only what is needed

Read the supplied equations and definitions first. Ask focused questions only where missing or ambiguous information affects the mapping. For the example above:

- Which governing equation receives this flux?
- Is φ an existing US3D field or a new unknown?
- Does this add to or replace existing diffusion?

Ask about units, scalar/vector/tensor types, sign conventions, initial/boundary conditions or coefficient dependence only when needed. Do not repeat questions already answered.

Confirm the target US3D version. If only a manual version is available, offer a documentation-only mapping against that version; do not assume the installed solver matches it.

### 2. Research the documented interfaces

Start at `.pi/ref-library/MAP.md` in the project. Use its topic/chapter summaries to locate relevant material, then verify interface claims against the original manual pages. If the reference library is unavailable, request it rather than inventing interfaces.

Verify hook names, full signatures, invocation timing and data availability. Cite the original manual filename, version, section and physical one-based PDF page. Summaries alone are not sufficient evidence for exact interfaces. Preserve source conflicts or unclear signatures as unresolved questions.

A search miss means unverified, not necessarily unsupported. A storage-registration mechanism or flux hook alone does not establish support for an arbitrary new governing equation.

### 3. Map equations and supporting operations

Assign stable equation and mapping IDs, such as `eq-001` and `map-001`. Retain them when revising the same items.

Include both equation terms and necessary supporting operations, such as parameter initialization, storage, gradients, boundary handling or restart requirements. Stay within the user's requested model; do not design additional physics.

For each mapping entry, record:

- Equation ID or supporting operation and its purpose.
- Documented hook name and signature.
- Invocation timing.
- Required data, its availability and read/write behavior.
- Whether the operation adds to, replaces or only reads existing behavior.
- Original-manual citations and the reasoning connecting the interface to the operation.
- Supported, unresolved or documented-unsupported status, with outstanding questions.

Leave unknown fields explicitly unresolved rather than guessing. Use “unsupported” only when documentation affirmatively contradicts the requested operation; explain the specific limitation.

### 4. Present the mapping for review

Produce a readable Markdown report and a corresponding JSON mapping with the same IDs, findings, citations and questions. No helper scripts or formal schema are required. Check their consistency before presenting them. Confirm the destination before saving files, and do not silently overwrite previous reports.

Separate supported findings, unconfirmed assumptions, unresolved questions and approval status. State the target documentation version and any unknown installation compatibility.

For the example input, if φ is a new scalar whose evolution/storage support has not been established, the result should include separate unresolved entries for the flux and supporting storage/initialization. Ask for the missing governing-equation context; do not assign a guessed hook.

### 5. Obtain explicit approval

Treat every new or changed mapping as unapproved. Present the current mapping and resolve blocking questions before requesting explicit user approval for downstream skeleton work. Approval of this skill is not approval of a generated mapping.

Record which mapping revision the user approved. Changes to its equations, interfaces or supporting requirements require renewed approval. Do not proceed to skeleton generation without approval of the relevant mapping.

## Boundaries

This skill selects and explains integration points. It does not generate plugins, build code, run US3D or verify CFD results. Documentation-backed conclusions and local report checks are not runtime verification.

## Usage

After adding or changing this skill, run `/reload` in Pi, then invoke:

```text
/skill:equations-to-hooks J = -D ∇φ; J is a diffusive flux vector, D is constant scalar diffusivity, and φ is scalar concentration.
```

Or provide equations and definitions in ordinary chat and ask to map them to US3D hooks.
