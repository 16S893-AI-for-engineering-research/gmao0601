# Hook capability mapping: electron number density (n_e)

- **Skill used:** `hook-capability-mapping` (`hook-report-review` was NOT run; the single variable was checked by hand)
- **Target version:** US3D 1.2.1 (supplied manuals)
- **Evidence level:** documentation only. Nothing was run on a US3D installation.
- **Assumptions:** intent = `read` (derived quantity), location = cell-centered, gas = 11-species ionized air file or a custom file, stage not yet decided.
- **Citation convention:** "Dev" = `US3D-Developer-Manual.pdf`, "User" = `US3D-User-Manual.pdf`. PDF page = printed page + 10 in the body.
- **Tooling note:** `pdftotext` on this machine is broken (Anaconda `libpoppler.76.dylib` missing). PDF text was extracted with macOS PDFKit (a small Swift script, compiled in `/tmp/pdfx`, not kept in the repo). Page numbers below come from that extraction.

## Result in one line

US3D 1.2.1 documents no direct `n_e` variable. Derive it per cell from the electron mass fraction and the mixture density:

```
n_e(i) = r(i) * cs(k_e, i) / m_e
```

`k_e` is the electron index (expected 11 for the 11-species file; see open questions). `m_e = 9.1093837e-31 kg` is a physical constant used instead of `smw` (see notes).

## Summary table

| variable | intent | exists as / register as | read/write path | hook(s) + timing | status | citation |
|---|---|---|---|---|---|---|
| Mixture density ρ | read | built-in `r(1:net)`, cells | `r` pointer into `bigu` | any cell-loop handler (below) | documented | Dev Ch.4 Table 4.3, PDF p.21 |
| Electron mass fraction `cs_e` | read | built-in `cs(1:ns,1:net)`; electron is one index of `1:ns` | `cs(k_e,i)` | any cell-loop handler (below) | partial: how to find `k_e` by name is not documented | Dev Ch.4 Table 4.5, PDF p.22 |
| Electron density ρ_e = ρ·cs_e | read (derived) | derived, not stored | `r(i)*cs(k_e,i)` | same as above | documented (derivation) | Dev Ch.4, PDF p.19 |
| Electron mass / molar mass | read | no documented accessor found | n/a | n/a | partial: only `smw(n)` appears, in reaction scaling | Dev PDF p.43, p.104 |
| `n_e` itself | create / save | new storage (optional) | `us3d_register_slots`, `stype='bigu'`; output via `'save_cells'`, `'save_bound'`, `'save_slice'` | signal `us3d_bigu_request`, then `us3dh_dataio_addvars` at write time | documented (mechanism); runtime not verified | Dev Ch.11 PDF pp.149-151; Ch.10 PDF pp.146-148 |

## Per-variable notes

### Species ordering and the electron
- Verbatim, Dev PDF p.19: "the mixture density ρ appears as the first variable, and species densities ρs can be calculated from the species mass fractions cs and the mixture density".
- Dev PDF p.22, Table 4.5: `cs  bigu_vind_cs : bigu_vind_cs - 1 + ns ... cs(1:ns,1:net) The vector of the species mass fractions.`
- Dev PDF p.24, Table 4.7: equation slots `1:ns` are `ρs` species densities.
- User PDF p.24 lists the 11-species air files (`air-11sp-park90.dat`, `air-11sp-park93.dat`): `N2,O2,NO,NO+,N2+,O2+,N,O,N+,O+,e`. If the file order is the `cs` order, the electron is index 11 (last).
- **Unverified:** that the file order equals the `cs` index order. No explicit statement found. No documented name-to-index lookup found.

### Conversion to number density
- The only documented molecular-weight symbol is `smw(n)`, in the reaction loop `ws(n) = smw(n)*ws(n)` (Dev PDF p.43; handler version p.104).
- Same page: `xs(ns)  Array of molar densities (ρs/Ms)`. So `smw` is presumably 1/M_s. This is an inference, not a documented statement.
- Where `smw` is declared and how a plugin accesses it was not found. Using the physical constant `m_e` avoids depending on it. Check units against the chemistry file.

### Hooks by stage

| Stage | Hook | Documented timing | PDF page |
|---|---|---|---|
| Per iteration, cells | `us3dh_calcrate_pregrad` | in `calcrate`, before inviscid gradients | Dev p.100 |
| | `us3dh_calcrate_postgrad` | after inviscid gradients | Dev p.100 |
| | `us3dh_calcrate_previsflux` | before viscous flux | Dev p.100 |
| | `us3dh_calcrate_post` | after `visflux` | Dev p.99 |
| | `us3dh_update_pre` / `_mid` / `_post` | around the time-integration `update`; `_mid` gives `i1,i2` cell range and `iop=1/2` (before/after loop) | Dev pp.129-130 |
| Startup / index lookup | `us3dh_init` | from `startup`, before `user_init` | Dev p.110 |
| | `us3dh_init_mid` | after solution read or `init_soln` | Dev p.110 |
| | `us3dh_gas_t_init_post` | after gas init; `current_gas_t_pointer` associated | Dev p.108 |
| Diffusion/viscosity models | `us3dh_model_idmod` / `ivmod` | `gas_t` is NOT passed; store the gas pointer during `init` | Dev p.116 |
| Monitoring | `us3dh_monitor_vars` | adds monitor variables, cell or boundary | Dev pp.119-120 |
| Postprocessing only | `us3dh_postpar_stdvar` | gets `sv(pob%nsv,np)` and `isp`, returns `var(np)` | Dev p.122 |
| Existing postproc names | `rhos*`, `cs*` (e.g. `rhosN2`, `csN2`) | the electron names `rhose`/`cse` were NOT checked | User p.61 |

### Parallel, boundary, restart
- `bigu` covers interior, ghost and shared cells (Dev p.19), so `r` and `cs` exist on ghost cells. Whether they are up to date at a given stage was not verified.
- A new `bigu` slot may need `stype='exchange2'` for ghost-cell consistency (Dev pp.150-151). The `exchange2` use was not verified.
- To save `n_e`: register `save_cells`, `save_bound` and `save_slice` (all three, per Dev p.151), via signal `us3d_save_cb_request`, and fill the values in `us3dh_dataio_addvars` (Dev p.106). For slices, face values are averages of the two neighbouring cells (Dev p.106).

### Caveats
- The Ch.10 chapter summary omits the signal `us3d_ne_request` (where storage for extra equations is requested). It appears in the solver signal table at Dev pp.146-147. It is not needed for a derived `n_e`.
- Registration or a hook name alone does not prove new physics is supported.
- With a perfect-gas or non-ionized mixture there is no electron species, so `cs_e` does not exist.
- Restart: changing the species count changes the equation count and needs a new solution file via `--restart` or `[RESTART_SPECIES_REMAP]` (User p.195).

## Stage recommendation (undecided; user unsure)

1. Start with `us3dh_postpar_stdvar`. It cannot change the solution. Confirm the electron index and magnitude.
2. When the calculation is known, move the same formula into the matching `us3dh_calcrate_*` handler.
3. Add `bigu` storage and `save_*` output only if `n_e` must be in the restart file.

## Search log
- **Summaries read** (`.pi/ref-library/summaries/`): `developer-ch04`, `ch07`, `ch08`, `ch10`, `ch11`, plus an `rg` over all summaries for `electron|species|smw|rhos|cs`.
- **PDF search terms:** `smw`, `molecular weight`, `molar`, `avogadro`, `number density`, `electron`, `gas_t`, `rhos`, `csN2`, `ne_request`, `GAS_SPECIES`.
- **PDF pages checked:** Dev 19-22, 24, 43, 61, 70, 99-100, 104, 106-108, 110, 116, 119-120, 122, 129-132, 146-148, 149-151. User 23-24, 61, 195.

## Open questions and runtime checks

1. **Electron index `k_e`.** Expected 11 for the 11-species file. For a custom file, share its species list. Is the file order the `cs` order? Is there a documented name lookup (e.g. through `gas_t`)? Not found.
2. **What calculation uses `n_e`?** The equation would let us run `equation-to-requirements`, then pick one hook for the stage.
3. **Stored/saved or only read?** Decides whether `bigu`/`save_*` registration is needed.
4. **`smw` / species molar masses:** where a plugin gets them (`gas_t` fields or exported module) was not found.
5. **Runtime check on an installation:** a small plugin printing `ns`, `r(i)`, `cs(:,i)`, and `r*cs_e/m_e` for a few cells. Confirm the index, positivity, and magnitude. Also check ghost-cell values at the chosen stage.
6. **Not run:** `hook-report-review`.
