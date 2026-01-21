# Introduction to Noncooperative Game Theory - Games in Normal Form

When we talk about self-interested agents we are talking about individuals with a capability to engage in different actions which can effect the world, and who have preferences about what the world looks like.

This section introduces game theory - the mathematical study of strategic interaction between rational agents. Unlike the previous chapters where agents cooperate to satisfy constraints or optimize a shared objective, here agents have their own preferences and may have conflicting goals.

The focus is on **normal-form games** (also called strategic-form games), where players choose actions simultaneously and receive payoffs based on the combination of actions chosen.

An overview of each notebook is given below.

---

## A - Self-Interested Agents and Utility Theory Maths

Before we can talk about games, we need a foundation for representing preferences. This notebook establishes the mathematical framework of **utility theory**.

The key question: when can preferences be represented by a utility function? The notebook presents the **Von Neumann-Morgenstern utility theorem**, which shows that if preferences satisfy certain axioms (completeness, transitivity, substitutibility, decomposability, monotonicity, and continuity), then they can be represented by a utility function over lotteries.

The point of it all has been to show that utility is grounded in the maths of preferences. If you accept the axioms, you must accept that preferences can be represented numerically, and that expected utility is the right way to evaluate uncertain outcomes.

---

## B - Games in Normal Form

A **normal-form game** consists of:
- A set of players
- A set of actions (or strategies) for each player  
- A payoff function for each player that maps action profiles to utilities

Games are typically represented as matrices where each cell contains $(u_1, u_2, ...)$ - the utilities for each player.

The notebook introduces classic games:

**Prisoner's Dilemma**: If both players cooperate they get a benefit of 5 each. If one cooperates and one defects they get overall 8, with one person getting 0. And if both defect they get 2. The best option is obviously (C,C). However, due to the incentives the outcome that ends up happening is the worst, (D,D).

**Battle of the Sexes**: Two players want to coordinate (going to the opera or football together is better than being apart), but have conflicting preferences about which activity.

**Matching Pennies**: A zero-sum game where one player wins exactly what the other loses. No pure strategy equilibrium exists.

The notebook visualizes mixed strategies using heatmaps:

<p align="center">
  <img src="../images/3 Introduction to Noncooperative Game Theory - Games in Normal Form/B - Games in normal form_cell3_img2.png" alt="Mixed strategy heatmap" width="500"/>
</p>
<p align="center"><em>Heatmap showing utilities for different mixed strategy combinations.</em></p>

---

## C - Analyzing Games, Optimality and Equilibrium

How do we predict what will happen in a game? This notebook introduces solution concepts.

**Pareto optimality**: An outcome is Pareto optimal if you can't make anyone better off without making someone else worse off. In Prisoner's Dilemma, (C,C) is Pareto optimal but (D,D) is not.

**Nash equilibrium**: A strategy profile where no player can improve by unilaterally changing their strategy. Formally, $(s_1^*, ..., s_n^*)$ is a Nash equilibrium if for all players $i$ and all alternative strategies $s_i'$:

$$u_i(s_1^*, ..., s_i^*, ..., s_n^*) \geq u_i(s_1^*, ..., s_i', ..., s_n^*)$$

The notebook proves that every finite game has at least one Nash equilibrium (possibly in mixed strategies). 

For Prisoner's Dilemma, unsuprisingly, the gradient on both of these graphs points to defecting. (D,D) is the unique Nash equilibrium, even though it's not Pareto optimal.

---

## D - Further Solution Concepts for Normal-Form Games

Nash equilibrium has limitations. This notebook explores refinements and alternatives.

**Minimax strategies**: In zero-sum games, players can guarantee a certain payoff by playing their minimax strategy. The notebook shows how to compute these.

**Correlated equilibrium**: A weaker concept where a trusted third party can recommend actions to players. This can sometimes achieve better outcomes than Nash equilibrium.

**Rationalizability and iterated elimination of dominated strategies**: If an action is always worse than another regardless of what opponents do, rational players shouldn't use it. Eliminating dominated strategies can sometimes solve games entirely.

The notebook includes visualizations showing:

<p align="center">
  <img src="../images/3 Introduction to Noncooperative Game Theory - Games in Normal Form/D - Further solution concepts for normal-form games_cell3_img1.png" alt="Solution concept 1" width="400"/>
  <img src="../images/3 Introduction to Noncooperative Game Theory - Games in Normal Form/D - Further solution concepts for normal-form games_cell3_img2.png" alt="Solution concept 2" width="400"/>
</p>

<p align="center">
  <img src="../images/3 Introduction to Noncooperative Game Theory - Games in Normal Form/D - Further solution concepts for normal-form games_cell7_img1.png" alt="Solution concept 3" width="400"/>
</p>
<p align="center"><em>Comparing different solution concepts and their predictions.</em></p>

Together, these notebooks provide the foundation for understanding strategic behavior in multiagent systems. The next section covers computational methods for actually finding these equilibria.