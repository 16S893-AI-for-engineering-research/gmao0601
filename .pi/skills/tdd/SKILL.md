---
name: tdd
description: Use test-driven development for a feature or bug fix: define behavior with a failing test, make the smallest change that passes it, then refactor with the test suite green.
---

# Test-Driven Development

## When to use this
Use this skill when adding behavior, modifying existing behavior, or fixing a bug in code that has an automated test setup. The requested outcome should be expressible as an observable, repeatable test.

## Steps
1. **Understand the behavior and test setup.** Inspect the relevant implementation, nearby tests, and project documentation/configuration to identify the test framework and its commands. State the expected inputs, outputs, failures, and important boundary cases. Ask for clarification when the requirement is ambiguous.
2. **Red: write a focused failing test.** Add the smallest test that describes one missing behavior or reproduces the reported bug. Follow the repository's existing naming, fixture, and assertion conventions. Prefer testing public behavior over private implementation details. Run the narrowest relevant test command and confirm that it fails for the expected reason.
3. **Green: implement the minimum change.** Change production code only enough to make the new test pass. Avoid unrelated cleanup, new abstractions, or additional features. Re-run the focused test and confirm it passes.
4. **Refactor: improve safely.** Remove duplication and improve names or structure only if doing so makes the code clearer. Run the focused test after meaningful changes; do not alter behavior during refactoring.
5. **Verify and report.** Run the relevant test suite and the repository's usual lint, formatting, or type-check commands when available. Report the behavior covered, files changed, and commands run with their results. If a command cannot be run, explain why and give the command the user should run.

## Notes
A test should be deterministic, independent of unrelated tests, and easy to read. Use the project's normal arrange-act-assert style where applicable. For a bug fix, preserve the failing regression test: it should fail before the fix and pass afterward. Do not delete, weaken, skip, or change unrelated tests simply to obtain a passing suite. Keep each red-green-refactor cycle small so failures clearly identify what changed.
