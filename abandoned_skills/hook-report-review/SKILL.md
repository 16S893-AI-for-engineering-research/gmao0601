---
name: hook-report-review
description: Check that a hook-capability-mapping report accounts for every requested variable (and every equation term, when equations were supplied). Use before sending a variable-to-hook report to the user.
---

# Hook report review (coverage check)

This is a completeness check only. It confirms that every variable has been accounted for. It does not re-search the manuals, judge the physics, or add new hooks.

## Inputs

- The **variable list**: either the user's own list, or the variable list from `equation-to-requirements`.
- The **requirements table** from `equation-to-requirements`, if equations were supplied.
- The **report** from `hook-capability-mapping`.

## Checks

1. **Every variable is present.** Each variable in the list appears in the report's summary table under the same name. Flag any that are missing, renamed without explanation, merged, or split.
2. **Every intent is covered.** If a variable needs more than one intent (e.g. `create` and `save`), the report addresses each one.
3. **Every variable has a status.** Allowed values are `documented`, `partial`, `conflicting` or `not found`. A blank or vague status counts as missing.
4. **Every non-`not found` row has a citation:** manual, section and PDF page. A `not found` row lists the chapters that were searched.
5. **Every equation term is covered** (only when equations were supplied). Each term ID in the requirements table appears in the `used by` column of at least one variable. Flag any term with no variables.
6. **No extra variables.** Flag variables in the report that are not in the input list, unless the report explains why they are needed.

## Output

Return:

- **Result:** `complete` or `incomplete`.
- **Coverage table:** `variable | intents requested | intents covered | status | citation present (y/n) | problem`.
- **Uncovered equation terms** (if equations were supplied).
- **Fixes needed:** a short list of what `hook-capability-mapping` must add or correct.

If the result is `incomplete`, send the fixes back to `hook-capability-mapping` before the report goes to the user.
