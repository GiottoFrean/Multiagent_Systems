# Computing Solution Concepts for Normal-Form Games

Unfortunately, computing Nash equilibria is a computationally challenging problem. It can be shown that it belongs to a class called PPAD, which it is believed grows exponentially.

This section covers various algorithms and computational approaches for finding Nash equilibria and other solution concepts in normal-form games. While the previous section established *what* equilibria are and why they matter, this section addresses *how* to actually compute them.

An overview of each notebook is given below.

---

## A - Computing Nash Equilibria

For **two-player zero-sum games**, finding Nash equilibria reduces to solving a linear program. If one player plays mixed strategy $p$ and the other plays $q$, we want:

$$\max_p \min_q p^T A q$$

This can be reformulated as an LP using the minimax theorem. The notebook implements this approach and visualizes the results:

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell6_img1.png" alt="Zero-sum game 1" width="400"/>
</p>

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell8_img1.png" alt="Zero-sum game 2" width="400"/>
</p>

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell10_img1.png" alt="Zero-sum game 3" width="400"/>
</p>

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell12_img1.png" alt="Zero-sum game 4" width="400"/>
</p>
<p align="center"><em>Computing optimal mixed strategies for different zero-sum games.</em></p>

There we go. Unsuprisingly, the utility is 0 and the best option is to be random.

For **2x2 games**, there are closed-form solutions. The notebook derives these formulas and shows when pure vs mixed equilibria exist.

---

## B - Computing Nash Equilibria, Deeper Look

For general games (non-zero-sum, more than 2x2), the problem is harder. This notebook covers:

**Support enumeration**: A Nash equilibrium in mixed strategies has a support (the set of actions played with positive probability). If we guess the support, we can solve a system of equations. The algorithm tries all possible supports.

**Linear Complementarity Problems (LCP)**: Nash equilibria can be formulated as an LCP: find $x$ such that $Mx + q \geq 0$, $x \geq 0$, and $x^T(Mx + q) = 0$. 

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/B - Computing Nash equilibria, deeper look_cell12_img1.png" alt="LCP visualization" width="500"/>
</p>
<p align="center"><em>Visualizing the linear complementarity formulation of equilibrium computation.</em></p>

**Lemke-Howson algorithm**: A pivoting method for solving the LCP formulation, similar to the simplex algorithm for linear programming. Guaranteed to find at least one equilibrium.

---

## C - Computing Nash Equilibria as an Optimisation Problem

Can we formulate equilibrium-finding as an optimization problem? This notebook explores several approaches:

**Gradient-based methods**: Trying to find equilibria by ascending the utility functions. This doesn't always work because equilibria aren't necessarily local optima.

**Best-response dynamics**: Iteratively have players choose best responses to current strategies. Can cycle and fail to converge.

**Fictitious play**: Players best-respond to the empirical distribution of opponent actions. Converges for some game classes but not all.

The notebook includes visualizations:

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/C - Computing Nash eqilibria as an optimisation problem_cell3_img1.png" alt="Optimization approach 1" width="450"/>
</p>

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/C - Computing Nash eqilibria as an optimisation problem_cell5_img1.png" alt="Optimization approach 2" width="450"/>
</p>
<p align="center"><em>Different optimization approaches to finding equilibria.</em></p>

---

## D - Identifying Dominated Strategies, Iterative Dominance

A simpler computational problem: which strategies can be eliminated without affecting equilibria?

**Strict dominance**: Strategy $s_i$ strictly dominates $s_i'$ if it's always better regardless of opponents' actions. Strictly dominated strategies are never played in any Nash equilibrium.

**Weak dominance**: Strategy $s_i$ weakly dominates $s_i'$ if it's never worse and sometimes better. Weakly dominated strategies might be played in some equilibria.

**Iterated elimination**: After removing dominated strategies, new dominations may emerge. Keep eliminating until no more exist.

The notebook implements algorithms to detect and eliminate dominated strategies. For some games, this process fully solves the game (reducing to a single outcome). For others, multiple outcomes remain.

---

## E - Finding Correlated Equilibria

A **correlated equilibrium** is easier to compute than Nash equilibrium. A trusted mediator recommends actions to players, and it's in each player's interest to follow the recommendation (assuming others do too).

Correlated equilibria can be found by solving a linear program - much easier than Nash equilibrium computation! The notebook demonstrates this and shows that correlated equilibria can sometimes achieve better social welfare than Nash equilibria.

The key insight: coordination devices (like traffic lights) can help agents reach better outcomes than pure decentralized decision-making.