# Distributed Constraint Satisfaction

Distributed constraint satisfaction is about how agents with independent limitations can come to a solution where nobody has their requirements violated.

Imagine a network of cell towers, where each tower needs to use a different frequency to those nearby in order. This is essentially a graph coloring problem, where the frequencies are the colors.

---

## A - Domain-Pruning Algorithms

This notebook introduces **filtering algorithms** based on domain pruning. Each node checks its neighbours and tries to eliminate values from its domain that can't possibly work. Something like this:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img1.png" alt="Filtering steps 1" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img3.png" alt="Filtering steps 2" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img5.png" alt="Filtering steps 3" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img7.png" alt="Filtering steps 4" width="320"/>
</p>
<p align="center"><em>Filtering algorithm progressively reducing domains until a solution is found.</em></p>

And can also sometimes identify when a problem has no solution, but not always. Also it can get stuck if there are multiple solutions. Imagine the above but where every node has all 3 options. 

Later this notebook introduces the **hyper-resolution algorithm**, which expands on the above using the more general unit-resolution rule from propositional logic. Nodes generate new constraints at each step called "nogoods" and communicate those to their neighbours. It's unfortunately expensive in the number of nodes.

---

## B - Introduction to Heuristic Search Algorithms

This notebook looks at some heuristic algorithms for doing the above. 

One *centralised* option is to do a recursive search of values, backtracking when you find one that can't work. We can take that idea and try to make it work in a decentalised way by having each node simply choose a value that works with it's neighbours, but this isn't guaranteed to correctly find when there is no solution to a problem.

---

## C - The Asynchronous Backtracking Algorithm

The asynchonous backtracking algorithm can be thought of as a greedy version of the hyper-resolution algorithm. Essentially, we want every node to be trying to find a value, and then backtracking by sending a 'nogood' when it can't. This uses an arbitrary ordering of the nodes. Each node stores an idea of what the state of other nodes is.

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img1.png" alt="ABT step 1" width="700/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img3.png" alt="ABT step 2" width="700"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img5.png" alt="ABT step 3" width="700"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img7.png" alt="ABT step 4" width="700"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img9.png" alt="ABT step 5" width="700"/>
</p>
<p align="center"><em>Asynchronous backtracking progressively finding a solution through message passing.</em></p>

The algorithm elegantly handles the distributed, asynchronous setting - agents don't need to wait for synchronization points and can make progress independently.
