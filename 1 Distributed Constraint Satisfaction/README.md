# Distributed Constraint Satisfaction

Distributed constraint satisfaction is about how independent agents can come up with a solution to a problem. We don't have to worry about individual preferences, but a central processor can't be used. 

It doesn't matter which solution we come up with, so long as the constraints are satisfied. In the next chapter we ask how independent agents can also optimise a global objective function.

A distributed constraint problem is defined by variables, domains for each variable, and constraints on what all the variables can be. The goal of the solver is to find a combination of values such that the contraints are satisfied, or else determine that no such combination exists. The constraints here are restricted to be binary (i.e., only between two variables), but more complicated constraints are possible.

**Example problem:** Consider a network of cell towers. Each tower needs to use a different frequency to those nearby in order to avoid interference. We want to choose those frequencies without using a central computer. This is essentially a graph coloring problem - each tower can be thought of as a node, with an edge between nodes if the towers are in close proximity, and where the frequencies are the colors.

An overview of each notebook is given below.

---

## A - Domain-Pruning Algorithms

This notebook introduces **filtering algorithms** based on domain pruning. Each node checks its neighbours and tries to eliminate values from its domain that can't possibly work. Nodes keep doing this repeatedly, and hope the domains become smaller and smaller, eventually finding a solution.

The notebook starts with a simple filtering algorithm where if a neighbour has been reduced to 1 option, we can eliminate that option from our own domain (we don't want to conflict). Here is a simple example:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell5_img1.png" alt="Example constraint graph" width="400"/>
</p>
<p align="center"><em>Example problem with X1 fixed to red, X2 can be red/blue/yellow, and X3 can be red/blue.</em></p>

The filtering algorithm successfully finds a solution on solvable problems:

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

And can identify when a problem has no solution:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell12_img1.png" alt="No solution example 1" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell12_img3.png" alt="No solution example 2" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell12_img5.png" alt="No solution example 3" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell12_img7.png" alt="No solution example 4" width="320"/>
</p>
<p align="center"><em>Detecting an unsolvable problem when a domain becomes empty.</em></p>

But not always! Sometimes even though a problem has no answer, this algorithm can't find that out:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell14_img1.png" alt="Filtering fails" width="400"/>
</p>
<p align="center"><em>A case where filtering can't make progress (2 colors, 3 connected nodes).</em></p>

The notebook then introduces the **hyper-resolution algorithm**. The filtering algorithm is based on the unit-resolution rule from propositional logic. Hyper-resolution extends this: when a variable can belong to a number of options, and each option has a possible problem, then all those problems cannot be true at the same time. Nodes generate new constraints at each step called "nogoods" and communicate those to their neighbours.

Unfortunately, while this method works it is very inefficient. The number of nogoods scales very quickly, and calculating a new nogood from the current ones is quite expensive. The notebook demonstrates this on several test cases:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell30_img1.png" alt="Hyper-resolution step 1" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell30_img3.png" alt="Hyper-resolution step 2" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell30_img5.png" alt="Hyper-resolution step 3" width="320"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell30_img7.png" alt="Hyper-resolution step 4" width="320"/>
</p>
<p align="center"><em>Hyper-resolution solving a problem with numerous nogood messages.</em></p>

In order to do better we might want to consider alternatives based on heuristics, which are covered in the next section.

---

## B - Introduction to Heuristic Search Algorithms

In the previous section we found an algorithm to solve a distributed constraint satisfaction problem, but it was very expensive. Hyper-resolution works, but it generates a huge number of "nogoods". Here we look at some alternatives based on heuristics.

One *slightly centralised* option is to do a recursive search of values, backtracking when you find one that can't work. The notebook demonstrates this on several examples:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell5_img1.png" alt="Recursive backtracking example 1" width="400"/>
</p>
<p align="center"><em>This should work - showing X1=red, X2=yellow and X3=blue.</em></p>

Not only does this work in simple cases, but is complete and identifies when there isn't a solution:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell8_img1.png" alt="No solution detected" width="400"/>
</p>
<p align="center"><em>Finding that no solution exists for the 3-node triangle with 2 colors.</em></p>

And finds an answer when there are multiple options:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell10_img1.png" alt="Multiple solutions" width="400"/>
</p>
<p align="center"><em>Successfully finding one solution among many possibilities.</em></p>

The notebook then introduces a simple distributed algorithm where nodes randomly choose values and inform neighbours, who then try to find consistent values. This works sometimes, but is not complete - in certain cases it will say there is no answer, even when there is one:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell13_img1.png" alt="Distributed algorithm succeeds" width="400"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell15_img1.png" alt="Distributed algorithm fails" width="400"/>
</p>
<p align="center"><em>The simple distributed algorithm works on some problems but not others.</em></p>

---

## C - The Asynchronous Backtracking Algorithm

The asynchonous backtracking algorithm can be thought of as a greedy version of the hyper-resolution algorithm. Essentially, we want every node to be trying to find a value, and then backtracking by sending a 'nogood' when it can't. This uses an arbitrary ordering of the nodes. Each node stores an idea of what the state of other nodes is, called an agent_view. Agents send an 'OK' message to inform other nodes of their value. The algorithm is defined by 3 main functions:

**On receive a nogood**
1. Add the new nogood to your list.
2. For each item in the nogood: add that node to your neighbours if you haven't already, and set the agent_view of that node to its nogood value
3. Check agent view


**On receive OK**
1. Update agent_view to note that the message sender has a new value
2. Check agent view


**Check agent view**
1. Try to come up with a new value that is consistent with your own nogood list, and the values of neighbours.
2. If you can't, then backtrack
3. If you can, then send an OK message to nodes with a lower rank. 


**Backtrack**
1. Generate a new nogood
2. If you can't, then terminate here. 
3. If you can, then send this new nogood to the node referenced in the nogood with the lowest rank.
4. Also then remove that node's value from agent_view, as it will change. 
5. Check agent view

The notebook implements this algorithm and demonstrates it on several examples. Here is a simple solvable problem:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img1.png" alt="ABT step 1" width="280"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img3.png" alt="ABT step 2" width="280"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img5.png" alt="ABT step 3" width="280"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img7.png" alt="ABT step 4" width="280"/>
</p>

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img9.png" alt="ABT step 5" width="280"/>
</p>
<p align="center"><em>Asynchronous backtracking progressively finding a solution through message passing.</em></p>

And here is a more complex example with more nodes and more backtracking:

<p align="center">
  <img src="../images/1 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell11_img1.png" alt="Complex ABT" width="500"/>
</p>
<p align="center"><em>A more complex problem requiring multiple rounds of nogood generation and backtracking (showing first step of many).</em></p>

The algorithm elegantly handles the distributed, asynchronous setting - agents don't need to wait for synchronization points and can make progress independently.
