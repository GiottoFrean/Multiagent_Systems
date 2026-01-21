# Distributed Optimization

Distributed Optimization is about how independent agents can optimise a global objective function. In the previous chapter we had some variables we need to set, subject to some constraints. Now we look at how good those different solutions are.

---

## A - Distributed Dynamic Programming

This notebook looks at path-finding problems using dynamic programming. Dijkstra's algorithm builds up the minimum path from the origin outwards, but requires a large number of separate processes. The notebook introduces **asynchronous dynamic programming** where nodes can be updated in any order and still converge:

<p align="center">
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img1.png" alt="DP iteration 1" width="350"/>
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img5.png" alt="DP iteration 3" width="350"/>
</p>

<p align="center">
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img9.png" alt="DP iteration 5" width="350"/>
  <img src="../images/2 Distributed Optimization/A - Distributed dynamic programming_cell6_img13.png" alt="DP iteration 7" width="350"/>
</p>
<p align="center"><em>Asynchronous dynamic programming progressively finding shortest paths.</em></p>

---

## B - Review MDPs

This notebook reviews **Markov Decision Processes (MDPs)** which extend path-finding to stochastic environments. The **Bellman equation** provides the optimal value function and is proven to be a contraction mapping. A go-kart racing example demonstrates the concepts:

<p align="center">
  <img src="../images/2 Distributed Optimization/B - Review MDPs_cell7_img1.png" alt="Go-kart MDP" width="500"/>
</p>
<p align="center"><em>Go-kart racing MDP with two lanes and stochastic transitions.</em></p>

---

## C - Action Selection in Multiagent MDPs

When multiple agents coordinate in an MDP, the state space becomes huge. This notebook explores **variable elimination** to reduce complexity by factorizing the value function when agents have sparse dependencies.

---

## D - Review of Linear Programs

A review of **linear programming** and the **simplex algorithm**. Visualizes 2D and 3D examples of moving between vertices of the feasible region.

---

## E - Duality in Linear Programming

Every linear program has a **dual** formulation. The fundamental theorem: if both have optimal solutions, their values are equal. This has deep implications for game theory and economics.

---

## F - Negotiations, Auctions, and Optimization

Connects optimization to economics through the **assignment problem**. A key result: competitive equilibrium prices exist that decentralize the optimal assignment, leading to auction mechanisms.

---

## G - The Scheduling Problem, Generalized Competitive Equilibrium

Extends the assignment problem to more complex scenarios. Many multiagent coordination problems can be formulated as finding competitive equilibrium prices.

---

## H - Social Laws, the Traffic Problem

Considers **social laws** - rules that constrain agent behavior to improve global outcomes. The classic example is traffic: if all agents drive on the right (or left), collisions are avoided.