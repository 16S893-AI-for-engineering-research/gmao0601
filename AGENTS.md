
<!-- BACKLOG.MD GUIDELINES START -->
<!-- backlog.md-instructions-version: 1.53.0 -->
<CRITICAL_INSTRUCTION>

## Backlog.md Workflow

This project uses Backlog.md for task and project management.

**At the beginning of each conversation in this project, run `backlog instructions overview` before answering or taking action. Re-read it only if you have not read it yet in the current conversation.**

Use the overview to decide whether to search, read, create, or update Backlog tasks.

Before task lifecycle actions, read the matching detailed guide:
- `backlog instructions task-creation` before creating or splitting tasks
- `backlog instructions task-execution` before planning, changing status or assignee, adding a plan or implementation notes, or implementing task work
- `backlog instructions task-finalization` before checking acceptance criteria, writing final summaries, or moving tasks to terminal statuses

Use `backlog <command> --help` before running unfamiliar commands. Help shows options, fields, and examples.

Do not edit Backlog task, draft, document, decision, or milestone markdown files directly. Use the `backlog` CLI so metadata, relationships, and history stay consistent.

</CRITICAL_INSTRUCTION>
<!-- BACKLOG.MD GUIDELINES END -->

## US3D reference navigation

For US3D documentation or supplied example-case questions, start at [`.pi/ref-library/MAP.md`](.pi/ref-library/MAP.md). It links existing topic/chapter indexes, explains source authority, and records artifact availability and unresolved environment questions. Use it as reference navigation, not as a task plan.

## Active working scope

- `backlog/` is the only authoritative task plan for this workspace.
- `archived-plans/` and `retired-skills/` contain abandoned or historical material, not active requirements or instructions.
- Do not read, search within, execute, or use those directories unless the user explicitly asks to consult historical material. Exclude them from repository-wide searches.
- Do not recover superseded plans or retired skills from Git history unless the user explicitly asks.
- Do not carry requirements from old plans, prior sessions, or historical material into the active plan without the user's approval.
- Other planning documents are not authoritative unless the user explicitly designates them as part of the active plan. Ask if their status is unclear.
- If an active document links to abandoned material, ask before following the link.
- Use only currently enabled skills relevant to the active work. Do not load or run retired skills unless explicitly requested.
- These scope rules govern agent behavior; they are not filesystem access controls.
