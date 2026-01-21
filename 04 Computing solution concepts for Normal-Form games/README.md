# Computing Solution Concepts for Normal-Form Games

Unfortunately, computing Nash equilibria is computationally challenging - it belongs to a class called PPAD, which is believed to grow exponentially. This section covers algorithms for finding equilibria.

---

## A - Computing Nash Equilibria

For two-player zero-sum games, finding Nash equilibria reduces to solving a linear program. But for general games the problem is harder - this notebook focuses on the Lemke-Howson algorithm. The key insight: at equilibrium, each player's strategy can be "labelled" with their zero-probability actions plus the other player's best responses. An equilibrium occurs where the union of these labels covers all actions. Unintuitive!

The notebook visualizes this labelling process:

<p align="center">
  <img src="../images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell6_img1.png" alt="Player 2 utility curves" width="400"/>
  <img src="../images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell8_img1.png" alt="Player 1 labelling" width="400"/>
</p>

<p align="center">
  <img src="../images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell10_img1.png" alt="Player 1 utility curves" width="400"/>
  <img src="../images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell12_img1.png" alt="Player 2 labelling" width="400"/>
</p>
<p align="center"><em>Lemke-Howson algorithm: utility curves show best responses, labelling diagrams identify equilibrium points where all actions are covered.</em></p>

The algorithm successfully finds all three equilibria in the example game (two pure strategy equilibria plus one mixed).

---

## B - Computing Nash Equilibria, Deeper Look

This does a deeper dive into the Lemke-Howson algorithm.

---

## C - Computing Nash Equilibria as an Optimisation Problem

Can we formulate equilibrium-finding as optimization? This notebook explores gradient-based methods.

---

## D - Identifying Dominated Strategies, Iterative Dominance

One way to make the computation easier is to iteratively remove dominated strategies until no more exist, this notebook looks at domination by pure and mixed strategies.

---

## E - Finding Correlated Equilibria

A correlated equilibrium involves a trusted third party that recommends joint action profiles to players. Unlike Nash equilibria where players independently randomize, here players can condition on correlated signals (like traffic lights). Computing these is just a linear program - the constraints ensure no player wants to deviate from the mediator's recommendations. However, the algorithm finds many different correlated equilibria, not necessarily the intuitive ones. While every Nash equilibrium is also a correlated equilibrium, the ease of computing correlated equilibria doesn't help find Nash equilibria since Nash requires independent probability calculations.