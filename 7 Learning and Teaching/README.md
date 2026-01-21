# Learning and Teaching

Learning in game theory basically involves repeated or stochastic games. We need agents to adapt over time. An example of a simple rule might be 'tit-for-tat', but more complicated rules are possible.

The key insight: it's not just learning in isolation. Agents are learning about *other agents who are also learning*. When you change your strategy, it changes what others should learn. It's key that players teach / learn from each other what moves they will play and under what conditions.

This creates fascinating dynamics - sometimes leading to coordination, sometimes to cycles, sometimes to chaos. The "right" learning algorithm depends on what we want to achieve and what we assume about other agents.

An overview of each notebook is given below.

---

## A - Why the Subject of "Learning" is Complex

This notebook sets up the conceptual challenges. Learning in multiagent systems is fundamentally different from single-agent learning because:

**The environment isn't stationary**: When other agents change their strategies, your optimal strategy changes too. There's no fixed target to learn.

**Equilibrium vs learning**: Should agents learn to reach Nash equilibrium? Or some other outcome? Nash equilibrium assumes agents already know the game and can compute best responses - but if they're learning, they don't!

**Descriptive vs prescriptive**: Are we modeling how real agents learn (descriptive) or designing how they should learn (prescriptive)?

**Convergence questions**: 
- Does learning converge to anything?
- If so, is it a Nash equilibrium?
- How fast is convergence?
- What if agents use different learning algorithms?

The notebook discusses these tensions and sets up the frameworks explored in subsequent notebooks.

---

## B - Fictitious Play

**Fictitious play** is one of the oldest learning models. Each agent:
1. Tracks the empirical frequency of opponents' past actions
2. Best-responds to that empirical distribution

The idea: if you keep best-responding to what others have done historically, maybe you'll converge to equilibrium.

**Does it work?**: Surprisingly, yes for some games! For two-player zero-sum games and potential games, fictitious play converges to Nash equilibrium. But for general games, it can cycle forever.

The notebook implements fictitious play on several examples:
- Rock-Paper-Scissors: Over time this converges to a uniform strategy for both players, as you would expect.
- Coordination games: Can get stuck depending on initial conditions
- Games with no convergence guarantee

---

## C - Rational Learning

**Rational learning** assumes agents have models of how others learn, and optimize taking those models into account. This leads to a hierarchy:
- Level 0: Random or fixed strategy
- Level 1: Best-respond to level 0
- Level 2: Best-respond to level 1
- ...

With common knowledge of rationality, agents might reach equilibrium immediately. But in practice, agents have uncertainty about others' models.

The notebook covers:
- Bayesian learning with belief updates
- Consistency between beliefs and actions
- When learning reaches Nash equilibrium (and when it doesn't)

I think the method of choosing the best response needs to be more precise than the one I have above! Anyway, this has some nice properties, converges to an $\epsilon$-equilibrium, stuff like that! But I'm not sure I really *get* it.

---

## D - Reinforcement Learning

**Reinforcement learning (RL)** doesn't assume agents know the game structure. They just observe states, take actions, and receive rewards. Over time, they learn which actions work well.

Key algorithms covered:
- **Q-learning**: Learn action-value functions and gradually converge to optimal policies
- **Policy gradient**: Directly optimize policy parameters
- **Actor-critic**: Combine value functions with policy optimization

**Multiagent RL challenges**: When multiple agents learn simultaneously:
- The environment is non-stationary from each agent's perspective
- Agents might coordinate, compete, or both
- Standard convergence guarantees often don't apply

The notebook explores these issues with examples and discusses when different RL approaches work in multiagent settings.

---

## E - No-Regret Learning and Universal Consistency

**Regret** measures how much better you could have done in hindsight. A learning algorithm has "no regret" if the average regret vanishes over time.

**Multiplicative weights**: A classic no-regret algorithm that maintains weights on actions and increases weights for actions that performed well.

**Universal consistency**: An algorithm that eventually performs as well as any fixed strategy would have, regardless of what opponents do.

No-regret learning has nice properties:
- If all players use no-regret algorithms, play converges to the set of correlated equilibria
- This is weaker than Nash equilibrium but still a meaningful solution concept
- Provides a prescriptive answer: use no-regret learning even when you don't know what others are doing

---

## F - Evolutionary Learning and Large Population Models

When there are many agents, we can model learning at the population level rather than tracking individuals.

**Replicator dynamics**: Strategies that perform above average grow in population share, those below average shrink. This gives a differential equation describing population evolution.

**Evolutionarily stable strategies (ESS)**: A strategy that, if adopted by most of the population, cannot be invaded by any alternative strategy.

**Connection to Nash equilibrium**: ESS is related to Nash equilibrium but not identical. All ESS are Nash equilibria, but not all Nash equilibria are ESS.

The evolutionary perspective is useful for:
- Modeling cultural evolution
- Understanding emergence of conventions
- Analyzing systems with entry and exit of agents
- Biological game theory

Together, these notebooks show that learning in multiagent systems is complex and multifaceted. There's no single "correct" learning algorithm - the right choice depends on the domain, the agents, and what outcomes we want to achieve.