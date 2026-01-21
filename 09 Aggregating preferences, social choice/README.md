# Aggregating Preferences, Social Choice

It is often difficult to measure true utilities, so one alternative is to ask for *ordinal* preferences instead (e.g., “do you prefer A or B?”). The downside is you lose a lot of information about intensity of preference, which makes trade-offs and efficiency trickier.

---

## A - Models and Voting, Social Functions, Ranking Systems

The notebook starts with a simple formal model of preference profiles and aggregation, then walks through voting rules, social functions, and ranking systems.

A social choice function maps individual preferences to a collective outcome. Condorcet winner: beats every other candidate in pairwise votes, but doesn't always exist (cycles can occur).

Common voting systems: Plurality (spoiler effects), Borda count (manipulable), instant runoff (non-monotonic), approval voting (loses ranking info), range/quadratic voting.

It also distinguishes social welfare functions (aggregate into a ranking) from social choice functions (pick a single outcome).

Arrow's impossibility theorem: No social choice function can simultaneously satisfy Pareto efficiency, independence of irrelevant alternatives, and non-dictatorship.

The notebook’s main takeaway for me is how many “reasonable-sounding” desiderata conflict, and how system choice depends on what failure modes you’re willing to accept.