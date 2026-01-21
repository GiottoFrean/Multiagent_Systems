# Aggregating Preferences, Social Choice

It is often difficult to measure the true utilities people place on different outcomes. One alternative is to ask about preferences instead (i.e., do you prefer A or B). The downside is you lose a huge amount of information. Nevertheless, a lot of work has been done in this area which will be covered here very very briefly. I am not so interested in this! Preferences are dumb...

Social choice theory studies how to aggregate individual preferences into collective decisions. This is the foundation of voting systems, but also has deep connections to mechanism design and multiagent coordination.

An overview of each notebook is given below.

---

## A - Models and Voting, Social Functions, Ranking Systems

A **social choice function** maps profiles of individual preferences to a collective outcome. For example, with three candidates {A, B, C} and preferences for each voter, we want to select a winner.

**Condorcet winner**: A candidate who would beat every other candidate in pairwise majority votes. The problem: Condorcet winners don't always exist! You can have cycles where A beats B, B beats C, and C beats A.

**Common voting systems**:
- **Plurality**: Each voter votes for one candidate, highest vote count wins. Can have spoiler effects.
- **Borda count**: Voters rank candidates, points awarded for positions. Can be manipulated.
- **Instant runoff**: Eliminate lowest-ranked candidates iteratively. Non-monotonic (getting more votes can make you lose).
- **Approval voting**: Vote for any subset of candidates. Simple but loses ranking information.
- **Range voting / quadratic voting**: Express intensity of preferences.

**Arrow's impossibility theorem**: No social choice function can simultaneously satisfy:
1. Pareto efficiency (if everyone prefers A to B, society should prefer A to B)
2. Independence of irrelevant alternatives (the choice between A and B shouldn't depend on C)
3. Non-dictatorship (no single voter always determines the outcome)

This seems to pour cold water on the idea of voting systems altogether.

**Smith sets and refinements**: When no Condorcet winner exists, we can look at the Smith set - the smallest set of candidates such that every member beats every non-member in pairwise comparison. Various methods attempt to select from this set.

The best is quadratic voting, and nothing much more needs to be said! Everything works in some cases not in others.

The notebook presents several examples showing how different voting systems can produce different outcomes from the same preferences, and how strategic voting can manipulate results.