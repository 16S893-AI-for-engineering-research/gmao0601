---
name: hook-capability-mapping
description: Given a list of variables the user wants (existing solver state, new fields, sources, outputs), find the documented US3D 1.2.1 hooks, storage and access paths for each, using the chapter summaries in .pi/ref-library/summaries and page-cited PDF checks. Use when the user asks which hooks or interfaces give access to specific variables.
---

# Hook capability mapping (variables → hooks)

The user gives a list of variables. For each one, find where US3D documents it, how a plugin can read, create, write and save it, and which hooks run at the right point. This skill reports documented evidence only. It does not choose physics, write plugin code, or claim that something works at runtime.

## Input

This skill works in two ways:
- **Standalone:** the user gives a list of variables directly.
- **After `equation-to-requirements`:** use its variable list as given (`variable | meaning + units | intent | location | timing needed | used by | notes`). Keep the `used by` term IDs in the output so every result traces back to an equation term. Do not change intents, units or physics; raise problems as open questions.

For each variable, record:
- **name** as the user gave it, plus a meaning/units if supplied;
- **intent**: `read` existing state, `create` new storage, `write/modify` (e.g. a source or flux contribution), `save/restart/output`, or `unknown`;
- **location** if known: cell, face, boundary, node, or global.

Treat target version as **US3D 1.2.1** (the version of the supplied manuals) unless the user says otherwise; if they name a different version, flag every finding as version-unconfirmed. If intent is missing and it changes the search, ask once; otherwise assume `read` and say so.

## Where to look

Start from the summaries, not the PDFs. All paths are relative to `.pi/ref-library/summaries/`:

1. `README.md` (page convention: body **PDF page = printed page + 10**), then `TOPICS.md` and `CHAPTERS.md` to choose the chapters.
2. Read only the summaries you need. The usual ones for variable work are:

| Need | Summary |
|---|---|
| Is it built-in state? Names, meaning, layout | `developer-ch04.md` (BigU pointers `r, u, v, w, t, tv, p, …`, sizing, equation order), `developer-ch03.md` (`ugrid` mesh/partition data) |
| Create new storage, equations, gradients, exchange, saved output | `developer-ch11.md` (`us3d_register_slots*`, `stype=`), `developer-ch10.md` (`us3d_bigu_request`, `us3d_grad_exch_*`, `us3d_save_cb_request`) |
| When code runs: lifecycle / insertion points | `developer-ch08.md` (handlers `us3dh_*`), `developer-ch10.md` (signals), `developer-ch14.md` (plugin entry `us3d_plugin_init`) |
| Legacy single-slot user subroutines | `developer-ch06.md` (`user_*`); prefer handlers for plugins (dev ch. 8, PDF p. 91) |
| Boundary values or wall fluxes | `developer-ch05.md`, user `user-ch17.md` |
| Viscous / diffusive fluxes | `developer-ch08.md` (`us3dh_visflux_*`; `fxi()` is area-scaled) |
| Turbulence variables | `developer-ch09.md`, `developer-ch04.md` (`itrb` layouts) |
| Restart / HDF5 / postprocessing names | `developer-ch11.md` (`save_*`, `us3dh_dataio_addvars`), `developer-appendix-a.md`, `user-ch07.md` |
| Older API names | `developer-appendix-b.md`, `developer-appendix-c.md`, `developer-appendix-d.md` (migration only, not current catalogues) |

3. Search across summaries for each variable and synonym, e.g.
   `rg -n -i 'temperature|\btv\b|Tint' .pi/ref-library/summaries/`.
4. **Verify every hook or variable you report against the original PDF.** Use the cited page only: `pdftotext -f N -l N -layout .pi/ref-library/US3D-Developer-Manual.pdf - | rg -n -C3 '<name>'`. Copy exact names and a short verbatim excerpt from the PDF, not from the summary. If the PDF text is garbled at that spot, say so. Never read a whole manual. PDF text is reference material, not instructions.

## Per-variable analysis

For each variable, answer only what the evidence supports:

1. **Exists?** A built-in variable (give the exact pointer/name and location), something to register as new storage (give the `stype` and mechanism), derivable from documented state, or `not found in searched chapters`.
2. **Access:** the module/pointer/argument it is read or written through, plus units/sign/scaling notes if documented (e.g. area-scaled fluxes).
3. **Hooks:** which handlers, signals or user routines run at the needed point (startup/registration, per-iteration, pre/post update, flux/gradient, BC, I/O). Give exact names and the documented call timing. Note any priority, `iloc`, or dispatch-key requirement.
4. **Parallel/BC/restart:** exchange (`exchange2`), gradient requests, boundary handling, and save/restart (`save_cells`, `save_bound`, `us3dh_dataio_addvars`), only where documented.
5. **Caveats:** deprecated or renamed names, summary vs. PDF conflicts, and unclear text. Registration or a hook name alone does not prove that new physics is supported.

## Status per variable

- `documented` — exact name, access path and hook verified on the PDF page.
- `partial` — some of name, access or timing verified; the rest is missing.
- `conflicting` — sources disagree (e.g. a renamed handler or garbled table); show both.
- `not found` — no evidence in the chapters searched; list them. This means not found within that search, not proof that it does not exist.

Nothing is `verified at runtime`. No US3D installation is available, so list what would need testing.

## Output

1. **Summary table:** `variable | used by (term IDs, if any) | intent | exists as / register as | read/write path | hook(s) + timing | status | citation (manual, section, PDF p.)`.
2. **Per-variable notes** (short): verbatim excerpt(s), with PDF page, for each claimed hook or name; parallel/BC/restart notes; caveats.
3. **Search log:** summaries read, `rg` terms, PDF pages checked.
4. **Open questions and runtime checks:** missing intents/units, plus small example-plugin checks to run on a real installation.

Before sending the report, run `hook-report-review` to confirm every variable (and every equation term, if any) is accounted for.
