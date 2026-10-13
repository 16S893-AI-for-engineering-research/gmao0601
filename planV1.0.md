# US3D plasma and magnetohydrodynamics plugin — plan v1.0

**Status:** Approved as an initial plan; implementation has not begun. This document defines the proposed work and validation strategy, not verified US3D integration details. The US3D manuals and example plugins are not present in this repository; the first phase must inspect them before finalizing the plugin architecture.

## Objective and first-release boundary

Develop a US3D plugin for hypersonic, weakly ionized flow with magnetic-field/plasma coupling, aimed at studying magnetic-window concepts. The first *candidate* model is single-fluid, quasineutral, resistive MHD in the low magnetic-Reynolds-number limit with an imposed magnetic field. Verify that this approximation covers the intended operating regime before committing to it. RF signal propagation/attenuation, full magnetic induction, Hall/anisotropic transport, and other plasma physics are not automatically in scope; add them only after a documented regime assessment and scope review.

The first usable release should demonstrate quantitatively that the applied field changes the plasma and flow state, with conservation diagnostics and clear model limitations. It does not by itself establish improved communications performance.

## Phase 1 — US3D capability audit and reproducible baseline

**Required inputs:** US3D version and build environment, user/developer manuals, example plugins, a working hypersonic baseline case, and access to the target machine or cluster.

1. Inventory verified extension mechanisms: initialization, cell/face fields, source terms, boundary conditions, time-stepping callbacks, parallel exchange, restart, and output.
2. Build and run an unmodified example plugin and a baseline case. Retain inputs, outputs, build commands, results, and runtime as regression references.
3. Map US3D state, units, and conventions: species densities, momentum, total energy, other thermal modes, chemistry, and transport properties.
4. Check whether supported hooks allow persistent fields and a spatially coupled potential solve. If not, assess a supported external field-solver coupling before choosing an architecture; do not depend on undocumented internals.
5. Document version constraints, licensing/access requirements, MPI and restart behavior, and tests that can run without US3D.

**Gate:** an integration specification names verified hooks, data layout, units, lifecycle ordering, constraints, and unresolved blockers. The example and baseline build and run reproducibly.

## Phase 2 — Select the first-release physics

For the candidate low-magnetic-Reynolds-number model, solve charge conservation with

\[
\mathbf J=\sigma(-\nabla\phi+\mathbf u\times\mathbf B),\qquad \nabla\cdot\mathbf J=0.
\]

Feed Lorentz force \(\mathbf J\times\mathbf B\) into momentum. Couple consistent electromagnetic work and resistive heating into US3D energy equations without double-counting total and thermal-mode energy. Establish sign and reference-frame conventions explicitly.

Evaluate representative target conditions for magnetic Reynolds number, Hall parameter, ionization fraction, relevant collisional scales, and conductivity sensitivity. Decide and record:

- whether a prescribed field/low-induction model is adequate or an induction equation is needed;
- whether scalar conductivity is adequate or Hall/anisotropic effects matter;
- how electron density and conductivity are obtained from available chemistry/transport and whether the species mechanism suffices;
- how Joule heating is partitioned among US3D energy modes;
- whether the first release is steady/quasistatic, with RF propagation and attenuation handled separately.

**Gate:** approve the equations, validity envelope, explicit exclusions, and representative verification cases. If the candidate model does not cover magnetic-window conditions, revise scope and estimates before coding.

## Phase 3 — Numerical and plugin design

- **Potential/current discretization:** use the available US3D mesh representation; construct face currents consistently with the discrete charge-conservation operator. Specify treatment of spatially varying conductivity, near-zero conductivity, and gauge freedom for all-Neumann conditions.
- **Boundaries:** define insulating walls (\(\mathbf J\cdot\mathbf n=0\)), electrodes/prescribed potential when needed, and inflow, outflow, symmetry, and periodic behavior. Confirm each can be supported through verified hooks.
- **Applied magnetic field:** support a uniform field first, then a documented field-map interface with coordinates, units, interpolation, and out-of-domain behavior.
- **Flow coupling:** define when conductivity, potential, current, and flow sources update each step. Compare explicit/lagged and iterative coupling for stability and cost; document timestep or convergence requirements.
- **Operational behavior:** define MPI exchanges, restarts, solver failures, invalid input handling, zero-field and near-zero-conductivity limits, and conservation diagnostics.
- **Inputs/outputs:** validate configuration and expose \(\phi\), \(\mathbf E\), \(\mathbf B\), \(\mathbf J\), conductivity, force, heating, residual, and charge-balance error. Keep a clearly testable plugin-off path.

**Gate:** reviewed equations, units table, boundary-condition table, coupling sequence, parallel/restart design, and demonstrated route to a field solve through supported interfaces.

## Phase 4 — Implement in independently testable slices

1. Plugin skeleton: build/load, configuration, logging, restart and output plumbing; plugin-off baseline regression.
2. Independent physics kernel: prescribed conductivity and uniform field first; unit-test property and source calculations.
3. Electric-potential/current solver: face fluxes, boundary conditions, gauge treatment, residual and charge-balance diagnostics.
4. Flow coupling: momentum and energy sources, update ordering, stability controls, and failure reporting.
5. Plasma-property integration: chemistry/electron-state conductivity, validity checks, limits, and diagnostics.
6. Applied-field maps and production support: interpolation, MPI, restarts, example cases, and user documentation.

Keep physics calculations testable without a full US3D run where the plugin interface permits it. Require tests with each slice rather than deferring verification to final integration.

## Phase 5 — Verification, validation, and performance

Define tolerances using baseline numerical precision and mesh/time convergence studies, not an arbitrary single percentage.

| Level | Tests | Required evidence |
| --- | --- | --- |
| Unit | Ohm's law signs and units; cross product; Lorentz force; work/heating identity; conductivity limits; field interpolation; invalid inputs | Automated analytic-value tests with documented conventions |
| Discrete field solve | Manufactured potential/current solutions; insulating and electrode boundaries; variable conductivity; all-Neumann gauge | Expected refinement trend; face-current divergence and residual below documented tolerances |
| Plugin integration | Supported-version build/load; plugin-off baseline; zero conductivity and zero field | Reproducible runs; no spurious source terms; expected baseline numerical agreement |
| Coupled canonical cases | Hartmann channel flow with analytically consistent boundary conditions; complementary simple force/current cases | Velocity and relevant current/field profiles against analytic results over multiple meshes and Hartmann numbers |
| Hypersonic application | No-field reference then applied-field case; eventually a magnetic-window-relevant geometry | Flow/electron-density changes; force/heating budgets; field-strength, conductivity, mesh, and timestep sensitivity |
| Operational | MPI rank-count comparison; restart against uninterrupted run; scaling; field-solver failure injection | Consistent results within documented tolerances; measured memory/runtime overhead; actionable errors |

Report charge conservation, momentum-source totals, electrical/heating budgets, and model-validity indicators for coupled runs. Hartmann flow checks key MHD coupling but does **not** validate hypersonic nonequilibrium chemistry or RF blackout mitigation. Treat RF propagation/attenuation validation using exported plasma properties or a later coupled capability as a separate follow-on decision.

## Backlog breakdown

A parent feature tracks the initiative, with actionable child tasks and explicit prerequisites where required:

1. US3D capability audit and reproducible baseline.
2. Physics-regime assessment and first-release model decision.
3. Numerical/interface design.
4. Plugin skeleton and no-op regression.
5. Physics kernels and unit tests.
6. Electric-potential/current solver.
7. Flow/energy coupling.
8. Conductivity and chemistry integration.
9. Canonical MHD verification.
10. Magnetic-window demonstration and sensitivity study.
11. Documentation and release readiness.

Documentation and automated test infrastructure can proceed alongside implementation, but acceptance criteria for each task must be verified independently. Backlog tasks track intent, deliverables, prerequisites, and references; implementation plans should be added when each task is started, after re-checking the current US3D interface.

## Open questions and approval gates

1. What US3D version, manuals, example plugins, runnable baseline, and compute environment will be supplied?
2. Is field-induced change in the plasma sheath enough for version one, or must it include induction, Hall effects, or RF attenuation?
3. What are the target geometry and trajectory conditions? Do regime estimates support the proposed model?
4. Does the documented US3D extension API support the necessary field solve and conservation-consistent coupling, or is supported external coupling needed?
