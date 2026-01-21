# Learning and Teaching

Learning in game theory involves repeated or stochastic games where agents adapt over time. The key: it's not just learning in isolation - agents are learning about other agents who are also learning. It's key that players teach/learn from each other.

---

## A - Why the Subject of "Learning" is Complex

Learning in multiagent systems is fundamentally different from single-agent learning. The environment isn't stationary - when others change strategies, your optimal strategy changes. Additionally, intelligent agents aren't just learning but also teaching through their actions. Example: a player might play suboptimally in the short term to teach opponents they'll cooperate, enabling better long-term outcomes. The notebook distinguishes descriptive theories (how agents actually learn, e.g., converging to Nash equilibrium or empirical frequency equilibrium) from prescriptive theories (how agents should learn, with requirements like safety, rationality, and no-regret guarantees).

---

## B - Fictitious Play

Fictitious play: each agent tracks the empirical frequency of opponents' past actions and best-responds to it. Agents maintain a count of how many times opponents played each action, normalize to get probabilities, then play a best response. Key properties: (1) pure-strategy Nash equilibria are steady states of fictitious play, and vice versa; (2) if empirical distributions converge, they converge to Nash equilibrium. Guaranteed convergence for: zero-sum games, games solvable by iterated elimination of strictly-dominated strategies, potential games, and 2×n games with generic payoffs. Rock-Paper-Scissors demonstrates non-steady-state convergence: no fixed pure strategies, but empirical frequencies converge to uniform (1/3, 1/3, 1/3) as expected.

---

## C - Rational Learning

Rational learning extends fictitious play by allowing agents to model entire opponent strategies (like tit-for-tat or trigger strategies) rather than just action frequencies. Players maintain beliefs over a set of possible strategies, update via Bayesian inference after observing opponent actions, and choose best responses to their beliefs. Example: in repeated Prisoner's Dilemma, if an opponent cooperates for two rounds, a rational learner eliminates "always defect" and "trigger at t=0" from consideration, concentrating beliefs on longer-horizon strategies. The notebook includes a mistake probability to prevent beliefs from zeroing out (allowing for strategy changes). Converges to ε-equilibrium but requires careful tuning of belief updates and best-response functions.

---

## D - Reinforcement Learning

Reinforcement learning doesn't assume agents know transition probabilities or opponent payoffs. Q-learning updates action-values via Q(s,a) ← (1-α)Q(s,a) + α(r + γV(s')), with learning rate α declining as 1/t. The notebook demonstrates Q-learning on a simple 3-state MDP, showing convergence to optimal values without knowing transition matrices. For multiagent zero-sum games, extend Q to include opponent actions Q(s,a,o) and compute V via minimax: V(s) = max_a min_o Q(s,a,o). Example: a pursuit-evasion game on a 4-cell looping grid, where Q-learning with minimax finds mixed strategies for each position. The algorithm solves a linear program at each state to find minimax policies. Beyond zero-sum, Q-learning doesn't guarantee Nash convergence; belief-based variants model opponent behavior but lack theoretical guarantees.

---

## E - No-Regret Learning and Universal Consistency

Regret measures the difference between your average reward and the reward from always playing some fixed pure strategy. A no-regret algorithm guarantees non-positive regret for all pure strategies. Regret matching: at each timestep, choose actions with probability proportional to their regret (how much better that action would have been). Example: in stag hunt, regret matching quickly converges to mutual cooperation (C,C) despite occasional exploration. Smooth fictitious play uses softmax over expected payoffs rather than deterministic best response. Key result: if all players use no-regret learning, empirical action frequencies converge to correlated equilibria. Targeted learning relaxes the strict requirement of performing well against all opponents, instead optimizing for a target class while maintaining safety (maxmin) against others and achieving Pareto efficiency in self-play.

---

## F - Evolutionary Learning and Large Population Models

When modeling many agents, use population-level dynamics. Let θ(a) be the fraction playing action a. Replicator dynamics: the growth rate of strategy a is θ(a)(u(a) - ū), where u(a) is the payoff to a and ū is the population average. Strategies above average grow; those below shrink. Example: coordination game starting at 45% heads, 55% tails converges to 100% tails. Nash equilibria correspond to steady states. Evolutionarily stable strategies (ESS) resist invasion by mutants - even with a small fraction of invaders, the original strategy has higher payoff. Every ESS is a Nash equilibrium and asymptotically stable. Agent-based simulations can model individual interactions and strategy updates, showing how conventions emerge through repeated pairwise interactions. These models guarantee payoffs at least as high as maxmin.