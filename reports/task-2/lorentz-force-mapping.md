# Lorentz volumetric momentum source — provisional US3D mapping

**Mapping revision:** `restart-opus-002` (standalone Lorentz namespace; replaces earlier `restart-opus-001` findings-only output).
**Status:** unapproved; provisional seam identification only.
**Scope:** one externally supplied volumetric Lorentz momentum source. No physics closures (conductivity, Ohm's law, current source, magnetic-field source, energy term) are chosen.
**Target documentation:** US3D User Manual v1.2.1 and US3D Developer Manual v1.2.1 (local, Git-ignored under `.pi/ref-library/`). Installed-build compatibility: unconfirmed.
**ID namespace note:** `eq-001` here denotes the Lorentz body-force expression below. This is a distinct namespace from any earlier conductivity-model `eq-001`; the two expressions are not equated.

---

## Equation

### eq-001 — Lorentz volumetric momentum source
- Symbolic: `f_L(x,t) = J(x,t) × B(x,t)` [N/m³]
- Variables introduced for this provisional Lorentz-force mapping (not a user-approved current or field model):
  - `J(x,t)` — current density vector [A/m²]; provenance **unresolved** (candidates include prescribed field, Ohm's-law closure, or EM subsolve; none approved).
  - `B(x,t)` — magnetic flux density vector [T]; provenance **unresolved** (candidates include constant, prescribed time-varying, or coupled; none approved).
- Role: additive body-force per unit volume on the momentum equations.
- Energy consistency: **not** addressed in this mapping. See U3 below.
- Approved by user: no.

### eq-002 (optional, informational) — Scalar resistive Ohm's-law closure (candidate)
- Symbolic: `J = σ (E + u × B)` and, under this closure, resistive dissipation `J·(J/σ) = |J|²/σ`.
- Status: **candidate only**, not approved. Listed to anchor downstream discussion of U4/U3; nothing in this mapping depends on it.

---

## Mapping map-001 — supported integration-point identification

map-001 operates on eq-001 and comprises findings F1–F4 below. Each entry is a documented hook/seam identification, with directly verified original-manual citations. Supported here means the hook exists in the manual and its stated purpose covers "add source terms"; it does **not** verify the specific numerical convention used by that hook at run time (see U1).

### F1 — User-subroutine seam: `user_calcrate_post`
- Hook name: `user_calcrate_post`
- Signature (as printed):
  ```
  subroutine user_calcrate_post(iform)
  integer, intent(IN) :: iform
  end subroutine user_calcrate_post
  ```
- Module / procedure pointer: `us3d_user_module/user_calcrate_post`
- Called from: `us3d/calcrate`
- Invocation timing (manual wording): "Subroutine that is executed after calcrate. Here all gradients have been computed, and exchanges made. This would be a good place to add source terms."
- Argument `iform` (manual wording): "Whether to store the RHS. This is the variable iform that is passed into calcrate." No numeric values enumerated at this section.
- Citation: US3D Developer Manual v1.2.1, §6.4.10, PDF p. 41 (printed p. 31).

### F2 — Handler seam: `us3dh_calcrate_post`
- Hook name: `us3dh_calcrate_post` (string ID; instance `us3d_handler_class/us3dh_calcrate_post_ci`; class `us3d_handler_class/us3d_handler`; prioritized).
- Called from: `us3d/calcrate` before `user_calcrate_post`.
- Dispatch label as printed in the manual: "Called from calcrate with ILOC=US3D_ILOC_VISFLUX_POST after the call to visflux." Treat the ILOC label as manual wording, not a verified runtime constant (see C2).
- Argument `iform` IN, same manual wording as F1.
- Full type-bound procedure signature: **unresolved in this report**; the handler name and property table do not by themselves supply that signature.
- Citation: US3D Developer Manual v1.2.1, §8.2.6, PDF p. 99 (printed p. 89); argument table continues on PDF p. 100 (printed p. 90).
- Developer Manual states plugins should use handlers rather than single-slot user subroutines (§8.1, PDF p. 91 / printed p. 81), so handler form is the documented choice for a shipped plugin.

### F3 — Documented momentum equation slots in the residual array
- Table 4.7 "Equation order" lists:
  - `1 : ns` — species densities ρ_s
  - **`ns+1 : ns+3` — momentum equations ρu, ρv, ρw**
  - `ns+4` — mixture total energy ρe
  - `ns+4+1 : ns+4+ntint` — internal energy equations
  - `ns+4+ntint+1 : ns+4+ntint+nteq` — conserved turbulence variables
- Citation: US3D Developer Manual v1.2.1, Table 4.7 (within §4.4), PDF p. 24 (printed p. 14).
- A volumetric body force f_L therefore targets residual slots `ns+1`, `ns+2`, `ns+3`.

### F4 — Cell data available at the F1/F2 invocation site
- At entry to `user_calcrate_post`, the §6.4.10 wording states "all gradients have been computed, and exchanges made." Cell-based primitive and conserved variables are stored in the `BigU` structure (`r`, `u`, `v`, `w`, `t`, `tv`, …), allocated from `simvars`:
  ```
  use simvars, only : bigu
  use sizing, only : bu_size, net
  allocate(bigu(bu_size, net))
  ```
  (Developer Manual §4.1, PDF p. 19 / printed p. 9.) **Correction:** the prior Opus draft cited §4.1 at "PDF p. 29 / printed p. 19"; §4.1 actually begins on physical PDF p. 19 / printed p. 9.
- This provides read access to ρ, u, v, w, T, and any species mass fractions / internal energies that are allocated by the active model. It does **not** by itself establish that any EM-side quantity (`J`, `B`, `E`) is accessible.

---

## Supporting operations (status noted; nothing invented)

### sup-001 — Storage and initialization of `B(x,t)`, `J(x,t)`, and optional precomputed `f_L`
- Candidate mechanisms **not selected**; only the BigU registration overview is cited here. Full signatures, invocation timing, data availability, and read/write contracts for these supporting operations remain **unresolved**:
  - User-slot registration into `BigU`. Developer Manual §4.3 (PDF p. 24 / printed p. 14) states "Additional user-specified variables can be added to BigU by requesting space (slots) in the BigU array." It then prints an unresolved cross-reference "See ??", so the detailed procedure is not available in this chapter. Chapter 11 is referenced elsewhere in the manual for user variables and was not inspected in this pass.
  - Private module arrays allocated inside a `user_init` / `user_initialize` entry.
  - Restart-file persistence via `user_dataio_pre` / `user_dataio_post`.
- Status: **unresolved** (U6). No mechanism approved.

### sup-002 — Energy-equation consistency term
- A Lorentz body force in general does mechanical work `u · f_L = u · (J × B)`. Under a scalar resistive Ohm closure (eq-002, candidate only), the resistive heating would be `|J|² / σ` (dissipative), not `J · E` in general — labeling `J · E` as "Joule heating" is physically imprecise; it is the total electromagnetic power delivered to the fluid, of which the dissipative part is `|J|²/σ` and the mechanical-work part is `u · (J × B)` under this closure. Consistent accounting of both parts is required for a coupled run.
- No `ρe` modification is proposed here. The energy residual slot `ns+4` is identifiable from F3; the physics closure is not. The user's deferral of this topic is **not** an approval to leave the energy equation unchanged during a coupled run; it is only a deferral of research.
- Status: **unresolved** (U3). Must be resolved before any coupled implementation.

### sup-003 — Conductivity / collision-frequency model
- Explicitly deferred by the user. `.pi/ref-library/gupta.db` was not consulted this pass. No derivation here.
- Status: **unresolved** (U7).

---

## Unresolved items that block coupled implementation

| ID | Blocker |
|---|---|
| U1 | Exact in-cell convention (sign, volume factor, time-form) for accumulating a body-force source into the residual at the F1/F2 seam is **not written out** in §6.4.10 or §8.2.6. The only documented explicit accumulation pattern we have seen is the chemistry/reaction pattern `duex(:,i) = duex(:,i) - rform*vi*ws` with Jacobian `at(:,:,i) = at(:,:,i) - vi*aa` (Developer Manual §6.4.14 PDF p. 43 / printed p. 33, and §8.2.14 PDF p. 104 / printed p. 94). That chemistry analogy is **not proof** that the same sign, `rform` scaling, or `vi` scaling applies at `user_calcrate_post`; verification requires the installed `calcrate` source. |
| U2 | Jacobian obligation. If `J` depends on `bigu` (e.g., through eq-002 and `u`), implicit coupling may require `at(:,:,i)` entries for `∂f_L/∂(ρu_k)`. §8.2.6 shows no Jacobian slot in the handler argument list; user-subroutine seam only allows `at(:,:,i)` touches by convention. Blocked by U1 and the choice at U4. |
| U3 | Energy-equation consistency (sup-002). No closure approved. |
| U4 | Source of `J(x,t)`. No choice approved. |
| U5 | Source of `B(x,t)`. No choice approved. |
| U6 | Persistent storage for `J`, `B`, optional `f_L` across time steps and restart (sup-001). |
| U7 | Conductivity / collision-frequency model (sup-003). |

---

## Residual-array module/shape — unverified claims flagged

The chemistry patterns in §6.4.14 and §8.2.14 and the turbulence update in §9.1.2 use `duex(:,i)` and `duex(ns+4+nv+n,i)` as the explicit residual accumulator for in-cell sources. Appendix C §C.3.6 (PDF p. 182 / printed p. 172) states the related old-updates array `duexo` is "stored in `simvars/duexo`", which strongly implies `duex` is likewise a member of the `simvars` module but **does not state so explicitly** in the inspected pages. The usage pattern `duex(nq, cells)` is consistent with the printed indexing (`duex(:,i)` and `duex(ns+4+nv+n,i)`) but the explicit allocation / shape declaration of `duex` was **not** located in the inspected pages.

Therefore the following are supported integration-point identification only (F1–F4) and the following are not verified from the manual pages inspected this pass:

- `duex` module membership (strongly implied as `simvars` via §C.3.6, not explicitly stated for `duex` itself) — **unresolved**.
- `duex` declared shape and allocation site — **unresolved**.
- Sign / `rform` meaning / `vi` meaning at the `user_calcrate_post` seam — **unresolved** (U1).

These should not be presented as proven just because the chemistry section documents an analogous pattern.

---

## Caveats

- **C1** — Developer Manual PDF p. 41 §6.4.11 prints the "Module/Procedure Pointer" for `user_calcrate_pregrad` as `us3d_user_module/user_calcrate_post`. Section heading and "Procedure Interface" lines say `user_calcrate_pregrad`, so this is a manual typo. Not blocking for F1/F2.
- **C2** — The dispatch label `ILOC = US3D_ILOC_VISFLUX_POST` for `us3dh_calcrate_post` (§8.2.6, PDF p. 99 / printed p. 89) differs from the surrounding `US3D_ILOC_CALCRATE_POSTGRAD` / `US3D_ILOC_CALCRATE_PREGRAD` labels of §8.2.7 / §8.2.8 (same pages). The chapter-wide ILOC parameter list on PDF p. 94 / printed p. 84 contains `US3D_ILOC_CALCRATE_POSTGRAD`, `US3D_ILOC_CALCRATE_PREGRAD`, `US3D_ILOC_MAIN_POST`, and so on, but no `US3D_ILOC_CALCRATE_POST`. Treat the printed label as manual wording, not a verified runtime constant.
- **C3** — `us3dh_main_previsflux` was renamed to `us3dh_calcrate_previsflux` (Developer Manual §8.2.33, PDF p. 111 / printed p. 101). Do not inherit the old name from legacy examples.
- **C4** — Installed US3D build version is unconfirmed. All interface claims above are documentation-level only.
- **C5** — No earlier agent's page citations or BigU/duex claims were imported. All citations above were verified from the local PDFs this pass.
- **C6** — Correction to prior Opus findings-only draft: Developer Manual §4.1 begins on physical PDF p. 19 / printed p. 9, not physical p. 29 / printed p. 19 as previously cited (see F4).

---

## Minimum open questions

1. **Delivery form:** `libus3d_user.so` prototype using F1, or plugin/handler using F2?
2. **`J` and `B` provenance for this pass:** both prescribed; `B` prescribed and `J` scalar-Ohm with σ symbolic; or something else? Current status: nothing approved.
3. **Energy equation:** open U3 as a parallel work item now, or leave the mapping intentionally incomplete and defer the entire coupled run? (Deferral of research ≠ approval of leaving the energy equation untouched in a coupled run.)
4. **Storage decision (sup-001 / U6):** inspect Developer Manual Chapter 11 for BigU user slots before approving the seam, or defer until F1/F2 is approved?

---

## Approval

- **Mapping revision:** `restart-opus-002`.
- **Status:** unapproved. This is a provisional seam identification, not a complete mapping, not a verified interface against the installed build, and not permission to generate any skeleton, plugin, or user-subroutine code.
- **Not claimed:** CFD/runtime verification, installed-version compatibility, correctness of residual sign/volume/time convention at F1/F2, correctness of ILOC label C2, approval of any physics closure.
- **Allowed by this report:** nothing beyond continued discussion and the resolution of questions 1–4.
