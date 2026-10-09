# Skills reorganize report: {{repo}}

Generated {{generated_at}} by SSS. This is a local working document in
`.sss/reports/`; it is not committed. Sections 3 to 7 answer one question each.

## 1. Summary

{{summary_text}}

{{question_table}}

## 2. What we looked at

{{inventory_table}}

## 3. Out of date

These skills are behind their source, or describe things that have since changed.

{{out_of_date}}

## 4. Duplicates

These skills cover the same ground: 0 or 1 star in the coverage matrix (see the
appendix). Keeping both wastes the agent's attention and lets them drift apart.

{{duplicates}}

## 5. Conflicts

These skills disagree. An agent that loads both will get two answers.

{{conflicts}}

## 6. Missing pieces

These skills point at files or other skills that are not here.

{{missing_pieces}}

## 7. Unuseful or out of place

These skills do not belong in this repo, or do not help an agent do anything.

{{out_of_place}}

## 8. Proposed changes

{{proposed_changes}}

## 9. What we left alone

{{left_alone}}

## 10. How to respond

Each item marked "needs decision" has an ID like `conf-81be44`. Reply with the
ID and your choice, either as a comment on the pull request or by adding a line
to `.sss/decisions.yaml`:

```yaml
dup-3f9a2c: accept
conf-81be44:
  choice: 3
  note: "Both are right in different regions."
```

The next run reads those answers and applies them. Items you have answered are
not asked again.

## Appendix: every skill we found

One entry per skill. "Goal" is what the skill is for, in one line. "Concerns"
lists every finding above that involves it.

{{appendix_skills}}

## Appendix: coverage matrix

Every skill was compared with every other skill and scored by how much they
cover the same ground.

{{appendix_matrix}}
