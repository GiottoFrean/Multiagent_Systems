# Distributed Constraint Satisfaction

Distributed constraint satisfaction addresses how agents with independent constraints can collectively reach a solution that satisfies all requirements.

Imagine a network of cell towers, where each tower needs to use a different frequency to those nearby. You can think of this as a graph coloring problem, where the frequencies are the colors.

---

## A - Domain-Pruning Algorithms

This notebook introduces domain pruning, where each node eliminates values from its domain that can't possibly work. It goes something like this:

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img1.png" alt="Filtering steps 1" width="320"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img3.png" alt="Filtering steps 2" width="320"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img5.png" alt="Filtering steps 3" width="320"/>
</p>

<p align="center">
  <img src="../images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img7.png" alt="Filtering steps 4" width="320"/>
</p>
<p align="center"><em>Filtering algorithm progressively reducing domains until a solution is found.</em></p>

This works and can also sometimes identify when a problem has no solution, but not always. Also it can get stuck if there are multiple solutions.

Later this notebook introduces the hyper-resolution algorithm, which expands on the idea using a more general unit-resolution rule from propositional logic. Nodes generate new constraints at each step called "nogoods" and communicate those to their neighbours.

---

## B - Introduction to Heuristic Search Algorithms

Domain pruning is expensive, so this notebook looks at some heuristic alternatives. 

One *centralised* option is to do a recursive search of values, backtracking when you find one that can't work. We can take that idea and try to make it work in a decentalised way by having each node simply choose a value that works with it's neighbours, but this isn't guaranteed to find when there isn't a solution.

---

## C - The Asynchronous Backtracking Algorithm

The asynchonous backtracking algorithm can be thought of as a greedy version of the hyper-resolution algorithm, meeting somewhere between the two previous ideas. Essentially, we want every node to be trying to find a value, and then backtracking by sending a 'nogood' when it can't.

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
