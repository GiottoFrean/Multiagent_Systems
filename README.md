# Multiagent Systems

My notes for the book Multiagent Systems by Yoav Shoham and Kevin Leyton-Brown.

This repository contains a collection of exploratory notebooks covering the foundations of multiagent systems. The material progresses from basic coordination problems through game theory, learning, and mechanism design.

Multiagent systems are everywhere: autonomous vehicles coordinating traffic, distributed sensors aggregating information, trading algorithms in financial markets, robots collaborating on tasks, and humans negotiating agreements. Understanding how independent agents can coordinate, compete, and coexist is fundamental to modern AI and distributed systems.

The notebooks are organized into 10 major topics, each building on previous concepts:

---

## [1. Distributed Constraint Satisfaction](1%20Distributed%20Constraint%20Satisfaction/)

How can independent agents coordinate to satisfy constraints without a central controller? Uses graph coloring as the running example (e.g., cell towers selecting frequencies). Covers domain-pruning algorithms, hyper-resolution, heuristic search, and the asynchronous backtracking algorithm.

---

## [2. Distributed Optimization](2%20Distributed%20Optimization/)

Extends constraint satisfaction to optimization - finding the *best* solution, not just any valid one. Covers dynamic programming for path-finding, MDPs for stochastic environments, linear programming, competitive equilibrium, and auctions.

---

## [3. Introduction to Noncooperative Game Theory - Games in Normal Form](3%20Introduction%20to%20Noncooperative%20Game%20Theory%20-%20Games%20in%20Normal%20Form/)

Introduces game theory foundations: utility theory, normal-form games, classic games (Prisoner's Dilemma, Battle of the Sexes), Pareto optimality, and Nash equilibrium. Shows that rational self-interested behavior can lead to suboptimal outcomes.

---

## [4. Computing Solution Concepts for Normal-Form Games](4%20Computing%20solution%20concepts%20for%20Normal-Form%20games/)

Unfortunately, computing Nash equilibria is computationally hard (PPAD-complete). Covers algorithms for specific game classes: linear programming for zero-sum games, support enumeration, Lemke-Howson algorithm, dominated strategy elimination, and correlated equilibria.

---

## [5. Games with Sequential Actions](5%20Games%20with%20Sequential%20Actions/)

Moves beyond simultaneous-move games to sequential decision-making. Covers perfect-information extensive-form games, backward induction, subgame-perfect equilibrium, imperfect information with information sets, and the sequence form for computational efficiency.

---

## [6. Richer Representations - Beyond the Normal and Extensive Forms](6%20Richer%20Representations%20-%20Beyond%20the%20Normal%20and%20Extensive%20Forms/)

Extends basic game models to capture more complex scenarios: repeated games and the folk theorem, finite automata strategies, stochastic games, Bayesian games with private information, congestion games, and compact representations (graphical games).

---

## [7. Learning and Teaching](7%20Learning%20and%20Teaching/)

Learning in multiagent systems is fundamentally different from single-agent learning because the environment changes as other agents adapt. Covers fictitious play, rational learning, reinforcement learning, no-regret learning, and evolutionary dynamics.

---

## [8. Communication](8%20Communication/)

When can agents benefit from communication? Covers cheap talk (costless but potentially uninformative), signaling games (costly signals that credibly reveal information), and speech-act theory (commitments and revelation).

---

## [9. Aggregating Preferences, Social Choice](9%20Aggregating%20preferences%2C%20social%20choice/)

How do we aggregate individual preferences into collective decisions? Covers voting systems, Arrow's impossibility theorem, Condorcet winners, and the fundamental tension between different desirable properties.

---

## [10. Protocols for Strategic Agents - Mechanism Design](10%20Protocols%20for%20Strategic%20Agents%20-%20Mechanism%20Design/)

Inverts game theory: instead of analyzing existing games, design new ones to achieve desired outcomes. Covers the revelation principle, Gibbard-Satterthwaite impossibility, Vickrey auctions, and VCG mechanisms.

---

## Images

All visualizations from the notebooks have been extracted to the [`images/`](images/) folder, organized by topic. The extraction script [`extract_notebook_images.py`](extract_notebook_images.py) can regenerate these if needed.

---

## Structure

Each numbered folder contains:
- A `README.md` with detailed descriptions of the notebooks
- Jupyter notebooks (`.ipynb` files) with implementations and examples
- Heavy use of NetworkX, matplotlib, and numpy for visualizations

The notebooks are designed to be self-contained and can be explored in any order, though the numbering suggests a logical progression.
