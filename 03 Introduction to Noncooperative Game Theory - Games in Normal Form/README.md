# Introduction to Noncooperative Game Theory - Games in Normal Form

Here self-interested agents who have their own preferences are introduced.

---

## A - Self-Interested Agents and Utility Theory Maths

This notebook establishes the mathematical framework of utility theory. The Von Neumann-Morgenstern utility theorem shows that if preferences satisfy certain axioms, they can be represented by a utility function over lotteries. The point is to show that utility is grounded in the maths of preferences.

---

## B - Games in Normal Form

A normal-form game consists of players, actions, and payoff functions. Games are represented as matrices with utilities for each player based on action profiles. Pure strategies are introduced as well as mixed strategies, where players randomize over actions.

The notebook introduces classic games like Prisoner's Dilemma: If both cooperate they get 5 each. If one cooperates and one defects, one gets 8 and the other gets 0. If both defect they get 2. The best option is (C,C) but the outcome is (D,D). Notice below that regardless of what player 2 does, player 1 is better off defecting (and vice versa).

<p align="center">
  <img src="../images/03 Introduction to Noncooperative Game Theory - Games in Normal Form/B - Games in normal form_cell3_img2.png" alt="Mixed strategy heatmap" width="700"/>
</p>
<p align="center"><em>Heatmap showing utilities for different mixed strategy combinations.</em></p>

---

## C - Analyzing Games, Optimality and Equilibrium

Talks about Nash equilibrium, which is where no player can improve by unilaterally changing their strategy. For Prisoner's Dilemma, (D,D) is the unique Nash equilibrium, even though it's not optimal.

---

## D - Further Solution Concepts for Normal-Form Games

This notebook explores refinements. Minimax strategies for zero-sum games, where each player minimizes the maximum possible loss. Correlated equilibrium, where a trusted third party recommends actions. Also discusses dominated strategies and iterated elimination of dominated strategies.