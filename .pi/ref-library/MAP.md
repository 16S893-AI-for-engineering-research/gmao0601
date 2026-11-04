# US3D reference-library map

Start here to find documentation or understand the supplied example. This is a reference map, not a solver specification or work plan; `backlog/` remains the task plan of record.

## Quick start

- **Have a question?** Use the [topic guide](summaries/TOPICS.md), then read only the relevant chapter summary and cited original pages.
- **Have a chapter or page number?** Use the [chapter index](summaries/CHAPTERS.md).
- **Need to understand the example?** Start with [example artifacts](#example-artifacts) below. The files are supplied examples, not a verified runnable case.
- **Need exact syntax, signatures, or equations?** Verify the original PDF, not just a summary. Cite manual filename, version, section, and physical PDF page. If verification is unavailable or ambiguous, say so.

For a known symbol, a targeted search from the repository root can locate a starting point:

```sh
rg -n 'us3dh_init' .pi/ref-library/summaries/
```

Do not load every summary or both complete manuals for a narrow question. Expand to related sections or migration notes when needed. If a topic is not found, report it as unresolved—not unsupported by the solver.

## What lives here and which sources to trust

Paths below are relative to `.pi/ref-library/`. Only this map is intended for version control; the supplied library remains Git-ignored. A fresh checkout may therefore lack its linked materials. If a link is missing, report that limitation and request the library rather than inventing its contents.

| Material | Use and authority |
|---|---|
| [US3D-User-Manual.pdf](US3D-User-Manual.pdf) | Original User Manual, documented version **1.2.1**, 203 PDF pages. Primary source for documented user-facing behavior. |
| [US3D-Developer-Manual.pdf](US3D-Developer-Manual.pdf) | Original Developer Manual, documented version **1.2.1**, 196 PDF pages. Primary source for documented extension interfaces. |
| [summaries/README.md](summaries/README.md) | Reading conventions and entry point to 47 chapter/appendix summaries. Secondary navigation, not a tested API specification. |
| [summaries/TOPICS.md](summaries/TOPICS.md) / [CHAPTERS.md](summaries/CHAPTERS.md) | Existing question-to-chapter guide and full chapter/page index. Use these instead of building another catalogue. |
| [summaries/VALIDATION.md](summaries/VALIDATION.md) / [manifest.json](summaries/manifest.json) | Source fingerprints, extraction/review limitations, known ambiguities, and machine-readable page ranges. |
| [chapters/README.md](chapters/README.md) | Links to 47 separate chapter/appendix PDFs. Convenient viewing copies; extraction can alter searchable/copied characters. Use original manuals for exact copied syntax. |
| [input.inp](input.inp), [example_submit.sh](example_submit.sh), [post.scr](post.scr) | Original supplied case examples. Evidence of what the example contains, not proof of installation compatibility or successful execution. |

**Evidence boundaries:** the manuals document 1.2.1; the installed version is unconfirmed. Summary citations are leads until checked against original pages. Check installed headers/build options and runtime behavior separately before claiming compatibility. A documented hook or storage-registration mechanism does not establish support for an arbitrary new equation.

**Page numbers:** citations use physical, one-based pages in the original PDFs. In these editions' bodies, PDF page = printed page + 10; this does not apply to front matter or imply the same offset for another edition. Chapter-extract page numbers are not original PDF page numbers. See [provenance guidance](summaries/VALIDATION.md) before implementation or migration work; it also records source conflicts and text-only review limitations.

## Where to look by topic

This is a short routing table for the active work, not a replacement for the [full topic guide](summaries/TOPICS.md). Links go to secondary summaries; follow their page citations to the originals. These routes locate relevant material, not a recommendation of a particular implementation.

| Question | Start here | Expand only as needed |
|---|---|---|
| Hooks and lifecycle callbacks | [Developer 8 — Handlers](summaries/developer-ch08.md) | [Developer 6 — User subroutines](summaries/developer-ch06.md), [10 — Signals](summaries/developer-ch10.md) |
| Plugins and build/load procedures | [Developer 14 — Plugins](summaries/developer-ch14.md) | [Developer 6 — User-library builds](summaries/developer-ch06.md), [User 2 — Installation](summaries/user-ch02.md), [23 — Runtime configuration](summaries/user-ch23.md) |
| User variables and extra storage | [Developer 11 — User variables](summaries/developer-ch11.md) | [Developer 4 — Ordering/sizing](summaries/developer-ch04.md), [10 — Signals](summaries/developer-ch10.md) |
| Initialization | [Developer 8 — Startup/solution hooks](summaries/developer-ch08.md) | [Developer 6 — Startup routines](summaries/developer-ch06.md), [User 17 — Flow/BC initialization](summaries/user-ch17.md) |
| Diffusion/transport | [Developer 8 — Model/viscous-flux handlers](summaries/developer-ch08.md) | [Developer 6 — Transport routines](summaries/developer-ch06.md), [User 4 — Model controls](summaries/user-ch04.md), [22 — Solver options](summaries/user-ch22.md) |
| Input syntax | [User 4 — Solver input](summaries/user-ch04.md) | [User 15 — MANAGE](summaries/user-ch15.md), [17 — Boundary conditions](summaries/user-ch17.md), [22 — Options](summaries/user-ch22.md) |
| Output extraction | [User 5 — Postprocessing](summaries/user-ch05.md) | [User 7 — Output variables](summaries/user-ch07.md), [11 — Script syntax](summaries/user-ch11.md), [Developer 7 — Programmatic interface](summaries/developer-ch07.md) |
| Version-sensitive or conflicting APIs | [Topic guide's source cautions](summaries/TOPICS.md#version-and-source-cautions) | [Developer B](summaries/developer-appendix-b.md), [C](summaries/developer-appendix-c.md), [D](summaries/developer-appendix-d.md): migration context, not standalone current API catalogues |

All requested topic categories have navigation leads. Whether any interface satisfies a specific custom model remains unresolved until the model requirements and original contracts are examined.

## Example artifacts

The following records direct inspection of the supplied files, not an execution or endorsement of their settings.

| Available local file | Observed contents / role |
|---|---|
| [input.inp](input.inp) | Solver configuration containing `CFD_SOLVER`, `GAS_SPECIES`, `MANAGE`, and `CFD_BCS` blocks. Declares `Air` and six named boundary entries. Zone correspondence to the missing mesh is unverified. |
| [example_submit.sh](example_submit.sh) | Requests partition `xeon-p8`, 8 nodes and 384 tasks; sets a license endpoint, sources `/etc/profile`, and loads US3D/MPI modules. Contains preprocessing, solver, then postprocessing commands. Do not execute it as part of reference lookup. |
| [post.scr](post.scr) | Contains `pob_init`, `pob_write_fvs file=fvs.plt vars=uvw,p,t,m`, and `quit`. These are literal example tokens, not a verified syntax/variable interpretation. Consult User 5/7 above for their contracts. |

The script's file flow is: `grid.cas` → preprocessing → `grid.h5` + `conn.h5`; solver invocation also names `input.inp`, `air-perfect.dat`, and `data.h5`; postprocessing names those HDF5 files and `post.scr`, whose output filename is `fvs.plt`. This describes intended flow, not evidence that any output was generated.

### Availability snapshot

Inspected **2026-11-04**. All documentation and three example files linked above are locally present. The filename search below covered this workspace, excluding `.git/`, `archived-plans/`, and `retired-skills/`; it did not inspect the target cluster or external installation directories. Relative case paths depend on the execution working directory, which the script does not set.

| Referenced artifact | Role in supplied example | Local observation | Remote availability |
|---|---|---|---|
| `grid.cas` | Input to preprocessing | Not found in searched workspace | Unconfirmed |
| `air-perfect.dat` | Solver gas-data argument | Not found in searched workspace; installation/search-path resolution unconfirmed | Unconfirmed |
| `grid.h5`, `conn.h5` | Named preprocessing outputs, then solver/postprocessing inputs | Not found in searched workspace | Unconfirmed |
| `data.h5` | Named solver data file, then postprocessing input | Not found in searched workspace | Unconfirmed |
| `fvs.plt` | Named postprocessing output | Not found in searched workspace | Unconfirmed |

Not-found outputs are not automatically missing prerequisites: they may be generated by preceding steps. Not-found inputs may exist outside this workspace. No remote availability has been verified, including for the locally supplied examples.

### Questions needing user/environment confirmation

- **Installed version:** the module path is `/home/gridsan/gmao/modules/us3d/1.2-module`; what exact US3D version/build does it load? The name alone does not establish 1.2.1 compatibility.
- **Parallel allocation:** is requesting 384 Slurm tasks but launching `mpirun -np 4` intentional? Preserve both values until confirmed.
- **Inputs and working directory:** where is `grid.cas`, does it match the six configured boundary zones, and from which directory should the script run? Where does `air-perfect.dat` resolve?
- **Environment:** are partition `xeon-p8`, the US3D module path, `mpi/openmpi-4.1.8`, the configured license service, and executables `us3d-prepar`, `us3d`, and `us3d-postpar` available and compatible on the target system? `/etc/profile` is also an environment dependency, not a supplied case file.
- **Output support:** does the installed postprocessor support the requested `.plt` output and variables? Confirm using the User 5/7 references and installation evidence; the supplied command alone does not prove support.

No solver, Slurm job, plugin build, or example script was run for this inventory. Existing references and examples are preserved unchanged. Recheck availability when new files or environment evidence are supplied; do not silently repair examples or promote unknowns to facts.
