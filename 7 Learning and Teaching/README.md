# Learning and Teaching

Learning in game theory involves repeated or stochastic games where agents adapt over time. The key: it's not just learning in isolation - agents are learning about other agents who are also learning. It's key that players teach/learn from each other.

---

## A - Why the Subject of "Learning" is Complex

Learning in multiagent systems is fundamentally different from single-agent learning. **The environment isn't stationary** - when others change strategies, your optimal strategy changes. Should agents learn to reach Nash equilibrium? Or something else? Descriptive vs prescriptive?

---

## B - Fictitious Play

**Fictitious play**: each agent tracks the empirical frequency of opponents' past actions and best-responds to it. Converges for some games (two-player zero-sum, potential games) but can cycle forever for others. Rock-Paper-Scissors converges to uniform strategy, as expected.

---

## C - Rational Learning

**Rational learning** assumes agents have models of how others learn and optimize taking those models into account. With common knowledge of rationality, agents might reach equilibrium immediately. But I'm not sure I really *get* it.

---

## D - Reinforcement Learning

**Reinforcement learning (RL)** doesn't assume agents know the game structure - just observe states, actions, and rewards. Q-learning, policy gradient, actor-critic. When multiple agents learn simultaneously, the environment is non-stationary and standard convergence guarantees often don't apply.

---

## E - No-Regret Learning and Universal Consistency

**Regret** measures how much better you could have done in hindsight. **Multiplicative weights** is a no-regret algorithm. If all players use no-regret algorithms, play converges to the set of correlated equilibria.

---

## F - Evolutionary Learning and Large Population Models

When there are many agents, model at population level. **Replicator dynamics**: strategies that perform above average grow. **Evolutionarily stable strategies (ESS)** resist invasion. Useful for cultural evolution and emergence of conventions.