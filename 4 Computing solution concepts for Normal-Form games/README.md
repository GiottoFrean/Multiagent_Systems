# Computing Solution Concepts for Normal-Form Games

Unfortunately, computing Nash equilibria is computationally challenging - it belongs to a class called PPAD, which is believed to grow exponentially. This section covers algorithms for finding equilibria.

---

## A - Computing Nash Equilibria

For **two-player zero-sum games**, finding Nash equilibria reduces to solving a linear program. The notebook implements this:

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell6_img1.png" alt="Zero-sum game 1" width="400"/>
</p>

<p align="center">
  <img src="../images/4 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell10_img1.png" alt="Zero-sum game 3" width="400"/>
</p>
<p align="center"><em>Computing optimal mixed strategies for zero-sum games.</em></p>

There we go. Unsuprisingly, the utility is 0 and the best option is to be random. For **2x2 games**, there are closed-form solutions.

---

## B - Computing Nash Equilibria, Deeper Look

For general games the problem is harder. **Support enumeration** tries all possible supports. **Linear Complementarity Problems (LCP)** can formulate Nash equilibria. **Lemke-Howson algorithm** is a pivoting method guaranteed to find at least one equilibrium.

---

## C - Computing Nash Equilibria as an Optimisation Problem

Can we formulate equilibrium-finding as optimization? This notebook explores **gradient-based methods**, **best-response dynamics**, and **fictitious play**. These don't always converge.

---

## D - Identifying Dominated Strategies, Iterative Dominance

Strategies can be eliminated if they're dominated. **Strict dominance** means always better. **Iterated elimination** keeps removing dominated strategies until no more exist.

---

## E - Finding Correlated Equilibria

A **correlated equilibrium** is easier to compute than Nash - it's just a linear program! A trusted mediator recommends actions, and coordination devices (like traffic lights) can help agents reach better outcomes.