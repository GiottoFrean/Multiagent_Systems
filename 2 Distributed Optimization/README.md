# Distributed Optimization

Distributed Optimization is about how independent agents can optimise a global objective function. In the previous chapter we had some variables we need to set, subject to some constraints. Now we look at how good those different solutions are.

The key difference from constraint satisfaction is that we care about finding the *best* solution according to some metric, not just any solution that works. This involves topics like path-finding, Markov Decision Processes (MDPs), linear programming, auctions, and mechanism design.

An overview of each notebook is given below.

---

## A - Distributed Dynamic Programming

To illustrate the concepts in distributed dynamic programming we look at path-finding problems. A path finding problem is where you have a directed graph with weighted edges, and want to know the path from one node to another that has the lowest cumulative weight.

Dynamic programming has a solution to the shortest path problem. If $C(x,y)$ is the minimum cost of getting from node $x$ to node $y$, then $C(x,y)=\min_z C(x,z)+W(z,y)$ where $z$ is an upstream neighbour of $y$ and $W$ is the weight. This leads to **Dijkstra's algorithm**, where we build up the minimum path from the origin outwards.

The problem with this algorithm is that it requires a large number of seperate processes (one for each node). For some problems this is impractical. E.g., imagine finding the shortest number of moves to get from one chess board position to another, where each position is a node.

The notebook introduces **asynchronous dynamic programming** where nodes can be updated in any order. The key insight: if there were a shorter path, deviating at some node $j$ instead of $k$, then we must incorrectly have an estimate somewhere. The algorithm will eventually converge.

Visualizations show the algorithm working on directed graphs:

<p align="center">
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img1.png" alt="DP iteration 1" width="380"/>
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img3.png" alt="DP iteration 2" width="380"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img5.png" alt="DP iteration 3" width="380"/>
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img7.png" alt="DP iteration 4" width="380"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img9.png" alt="DP iteration 5" width="380"/>
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img11.png" alt="DP iteration 6" width="380"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img13.png" alt="DP iteration 7" width="380"/>
</p>
<p align="center"><em>Asynchronous dynamic programming progressively finding shortest paths (red labels show current estimates).</em></p>

The notebook also covers **Learning Real-Time A\* (LRTA\*)**, a variant useful when you don't know the graph structure ahead of time and need to explore.

---

## B - Review MDPs

This notebook reviews **Markov Decision Processes (MDPs)**, which extend path-finding to stochastic environments. An MDP is defined by states, actions, a transition function $T(s,a,s')$ giving the probability of reaching state $s'$ from state $s$ via action $a$, and a reward function $R(s,a,s')$.

The goal is to find a policy $\pi(s)$ that maximizes expected cumulative reward. The **Bellman equation** provides the optimal value function:

$$V^*(s) = \max_a \sum_{s'} T(s,a,s')[R(s,a,s') + \gamma V^*(s')]$$

where $\gamma$ is the discount factor. The notebook proves this is a **contraction mapping**, guaranteeing convergence of value iteration.

A go-kart racing example demonstrates the concepts:

<p align="center">
  <img src="../images/2 Distributed Optimization/B - Review MDPs_cell7_img1.png" alt="Go-kart MDP" width="500"/>
</p>
<p align="center"><em>Go-kart racing MDP with two lanes and stochastic transitions.</em></p>

<p align="center">
  <img src="../images/2 Distributed Optimization/B - Review MDPs_cell11_img1.png" alt="Value iteration" width="500"/>
</p>
<p align="center"><em>Value iteration converging to optimal policy.</em></p>

---

## C - Action Selection in Multiagent MDPs

When multiple agents need to coordinate in an MDP, the state space becomes combinatorially large. This notebook explores **variable elimination** to reduce computational complexity.

The key insight: when agents have sparse dependencies (e.g., only interact with nearby agents), we can factorize the value function and use message-passing algorithms to compute optimal joint actions without enumerating all possibilities.

<p align="center">
  <img src="../images/2 Distributed Optimization/C - Action selection in multiagent MDPs_cell3_img1.png" alt="Multiagent MDP" width="500"/>
</p>
<p align="center"><em>Heatmap showing agent positions and their utility calculations.</em></p>

---

## D - Review of Linear Programs

This notebook reviews **linear programming (LP)**, which will be used extensively in later sections. An LP has the form:

Maximize $c^T x$ subject to $Ax \leq b$ and $x \geq 0$

The notebook covers the **simplex algorithm** (moving between vertices of the feasible region) and visualizes 2D and 3D examples:

<p align="center">
  <img src="../images/2 Distributed Optimization/D - Review of linear programs_cell8_img1.png" alt="2D LP" width="350"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/D - Review of linear programs_cell9_img2.png" alt="3D LP step 1" width="350"/>
  <img src="../images/2 Distributed Optimization/D - Review of linear programs_cell9_img4.png" alt="3D LP step 2" width="350"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/D - Review of linear programs_cell9_img6.png" alt="3D LP step 3" width="350"/>
</p>
<p align="center"><em>Visualizing linear programs in 2D and 3D with feasible regions and simplex iterations.</em></p>

---

## E - Duality in Linear Programming

Every linear program has a **dual** formulation. If the primal is maximizing $c^T x$ subject to $Ax \leq b$, the dual is minimizing $b^T y$ subject to $A^T y \geq c$ and $y \geq 0$.

The fundamental theorem: if both have optimal solutions, their values are equal. This has deep implications for game theory and economics.

The notebook demonstrates duality on multiple examples with visualizations:

<p align="center">
  <img src="../images/2 Distributed Optimization/E - Duality in linear programming_cell3_img1.png" alt="Primal problem" width="350"/>
  <img src="../images/2 Distributed Optimization/E - Duality in linear programming_cell5_img1.png" alt="Dual problem" width="350"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/E - Duality in linear programming_cell7_img1.png" alt="Another primal" width="350"/>
  <img src="../images/2 Distributed Optimization/E - Duality in linear programming_cell9_img1.png" alt="Another dual" width="350"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/E - Duality in linear programming_cell11_img1.png" alt="Primal 3" width="350"/>
  <img src="../images/2 Distributed Optimization/E - Duality in linear programming_cell13_img1.png" alt="Dual 3" width="350"/>
</p>
<p align="center"><em>Primal and dual linear programs showing complementary slackness.</em></p>

---

## F - Negotiations, Auctions, and Optimization

This notebook connects optimization to economics. The **assignment problem** asks how to optimally assign agents to tasks. A key result: competitive equilibrium prices exist that decentralize the optimal assignment.

If agent $i$ is assigned to task $j$ with value $v_{ij}$, and tasks have prices $p_j$, then at equilibrium each agent chooses the task maximizing $v_{ij} - p_j$, and the market clears.

This leads to **auction mechanisms** where agents bid on tasks, and prices adjust until an equilibrium is reached. The notebook covers several auction formats and their properties.

---

## G - The Scheduling Problem, Generalized Competitive Equilibrium

This extends the assignment problem to more complex scenarios where agents have multiple time slots, resources are divisible, and constraints are more intricate.

The key insight: many multiagent coordination problems can be formulated as finding competitive equilibrium prices. When such prices exist, agents can optimize locally while achieving global efficiency.

---

## H - Social Laws, the Traffic Problem

The final notebook considers **social laws** - rules that constrain agent behavior to improve global outcomes. The classic example is traffic: if all agents drive on the right (or left), collisions are avoided.

The challenge: how do we design rules that agents will voluntarily follow (or that can be enforced efficiently)? This connects to mechanism design and the next chapters on game theory.