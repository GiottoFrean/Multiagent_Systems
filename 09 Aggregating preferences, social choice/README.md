# Aggregating Preferences: Social Choice

Everything before has assumed clear utility functions. But in many cases you can't get utilities without them being gamed or misreported. Instead you can ask for preferences, i.e., choose A or B.

---

## A - Models and Voting, Social Functions, Ranking Systems

This notebook explores what properties we want from voting systems and why that's surprisingly difficult.

A sensible approach is to meet the Condorcet condition, where an option is selected if it beats every other in pairwise majority comparisons. But this doesn't always work, often there is no Condorcet winner. Plurality voting, Borda voting, pairwise elimination, and approval voting are explored.

Arrow's Impossibility Theorem is presented, where any social welfare function that produces a full ranking of outcomes must violate at least one of three basic fairness properties: Pareto efficiency (if everyone prefers A to B, rank A higher), independence of irrelevant alternatives (the ranking of A vs B shouldn't depend on C), or non-dictatorship (no single person determines everything). The proof shows that any decisive coalition, one that can force a ranking, can be split into smaller decisive coalitions recursively until you reach a single dictator.

There are some positive results if you restrict the problem. If outcomes are just the agents themselves and each agent has binary preferences (approve/disapprove), then approval voting satisfies analogous fairness conditions. For ranking systems in this setting, you can build iterative algorithms where votes propagate through the preference graph, achieving weaker but still meaningful fairness properties.