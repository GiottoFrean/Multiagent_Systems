# Computing Solution Concepts for Normal-Form Games

Unfortunately, computing Nash equilibria is computationally challenging - it belongs to a class called PPAD, which is believed to grow exponentially. This section covers algorithms for finding equilibria.

---

## A - Computing Nash Equilibria

This notebook starts with the easy case: two-player, zero-sum games, where computing a Nash equilibrium reduces to solving a linear program.

It then moves to general two-player games, where equilibrium computation is harder. The notebook introduces an LCP (linear complementarity problem) formulation and the Lemke-Howson algorithm as a pivoting method for finding equilibria.

One of the key geometric ideas is the “labelling” view: at equilibrium, each mixed strategy is labelled by its zero-probability actions and the opponent’s best-response actions, and an equilibrium occurs where the combined labels cover all actions.

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