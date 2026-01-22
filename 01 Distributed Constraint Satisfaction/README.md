# Distributed Constraint Satisfaction

Distributed constraint satisfaction addresses how agents with independent constraints can collectively reach a solution that satisfies all requirements.

Imagine a network of cell towers, where each tower needs to use a different frequency to those nearby. This is basically a graph coloring problem, where the frequencies are the colors.

---

## A - Domain-Pruning Algorithms

This notebook introduces domain pruning, where each node eliminates values from its domain that can't possibly work. It goes something like this:

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img1.png" alt="Filtering steps 1" width="320"/>
</p>

X3 removes red...

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img3.png" alt="Filtering steps 2" width="320"/>
</p>

X2 removes red...

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img5.png" alt="Filtering steps 3" width="320"/>
</p>

X2 removes blue...

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img7.png" alt="Filtering steps 4" width="320"/>
</p>
<p align="center"><em>Filtering algorithm progressively reducing domains until a solution is found.</em></p>

This works eventually, but it can get stuck if there are multiple solutions and won't always identify if a problem has no solution.

This notebook also introduces the hyper-resolution algorithm, which uses a general rule from propositional logic. It works by having nodes generate new constraints at each step, called "nogoods", and communicate those to their neighbours.

---

## B - Introduction to Heuristic Search Algorithms

While simple domain pruning is also expensive, so heuristic alternatives are often used. 

One *centralised* strategy for solving a constraint problem is to do recursive search of values, backtracking when you find one that doesn't work. We can take that idea and try to make it work in a decentalised way by having each node simply choose a value that works with it's current neighbours.

While easy to explain, it unfortunately sometimes fails to find a solution even when there is one. e.g.,

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell15_img1.png" alt="Fails in this case" width="320"/>
</p>
<p align="center"><em>The algorithm fails in this case.</em></p>

---

## C - The Asynchronous Backtracking Algorithm

The asynchonous backtracking algorithm can be thought of as a greedy version of the hyper-resolution algorithm, meeting somewhere between the two previous ideas. Essentially, we want every node to be trying values, and then backtracking with a 'nogood' when it can't.

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img1.png" alt="ABT step 1" width="700"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img3.png" alt="ABT step 2" width="700"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img5.png" alt="ABT step 3" width="700"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img7.png" alt="ABT step 4" width="700"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img9.png" alt="ABT step 5" width="700"/>
</p>
<p align="center"><em>Asynchronous backtracking progressively finding a solution through message passing.</em></p>
