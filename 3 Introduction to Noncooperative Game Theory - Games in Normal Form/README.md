# Introduction to Noncooperative Game Theory - Games in Normal Form

When we talk about self-interested agents we are talking about individuals with a capability to engage in different actions which can effect the world, and who have preferences about what the world looks like. Unlike the previous chapters where agents cooperate, here agents have their own preferences and may have conflicting goals.

---

## A - Self-Interested Agents and Utility Theory Maths

This notebook establishes the mathematical framework of **utility theory**. The **Von Neumann-Morgenstern utility theorem** shows that if preferences satisfy certain axioms, they can be represented by a utility function over lotteries. The point is to show that utility is grounded in the maths of preferences.

---

## B - Games in Normal Form

A **normal-form game** consists of players, actions, and payoff functions. Games are represented as matrices with utilities for each player.

The notebook introduces classic games like **Prisoner's Dilemma**: If both cooperate they get 5 each. If one cooperates and one defects, one gets 8 and the other gets 0. If both defect they get 2. The best option is (C,C) but the outcome is (D,D).

<p align="center">
  <img src="../images/3 Introduction to Noncooperative Game Theory - Games in Normal Form/B - Games in normal form_cell3_img2.png" alt="Mixed strategy heatmap" width="500"/>
</p>
<p align="center"><em>Heatmap showing utilities for different mixed strategy combinations.</em></p>

---

## C - Analyzing Games, Optimality and Equilibrium

**Nash equilibrium**: A strategy profile where no player can improve by unilaterally changing their strategy. The notebook proves every finite game has at least one Nash equilibrium (possibly in mixed strategies). For Prisoner's Dilemma, (D,D) is the unique Nash equilibrium, even though it's not Pareto optimal.

---

## D - Further Solution Concepts for Normal-Form Games

This notebook explores refinements: **minimax strategies** for zero-sum games, **correlated equilibrium** where a trusted third party recommends actions, and **iterated elimination of dominated strategies** where actions that are always worse can be removed.