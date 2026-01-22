# Distributed Optimization

Distributed Optimization is about how agents with different sets of information can optimise a global objective function.

---

## A - Distributed Dynamic Programming

Dijkstra's algorithm builds paths outward from the origin by always selecting the node with the shortest distance. The asynchronous dynamic programming instead has nodes updating their distance estimates in any order. It still converge to the optimal solution. 

<p align="center">
  <img src="../images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img1.png" alt="DP iteration 1" width="700"/>
</p>

node s found a new shortest path to a with length 1
node s found a new shortest path to b with length 3

<p align="center">
  <img src="../images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img5.png" alt="DP iteration 3" width="700"/>
</p>

node a found a new shortest path to b with length 2
node a found a new shortest path to c with length 3
node b found a new shortest path to d with length 4

<p align="center">
  <img src="../images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img9.png" alt="DP iteration 5" width="700"/>
</p>

node c found a new shortest path to t with length 4

<p align="center">
  <img src="../images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img13.png" alt="DP iteration 7" width="700"/>
</p>
<p align="center"><em>Asynchronous dynamic programming progressively finding shortest paths.</em></p>

The notebook also covers Learning Real-Time A* (LRTA*), where multiple agents explore the graph simultaneously, sharing distance estimates that underestimate the true cost. When an agent repeats the same path twice, it is proven to be optimal.

---

## B - Review MDPs

This notebook reviews Markov Decision Processes (MDPs), which extend path-finding to stochastic environments. The Bellman equation provides the optimal value function and is proven to be a contraction mapping. A go-kart racing example demonstrates the concepts:

<p align="center">
  <img src="../images/02 Distributed Optimization/B - Review MDPs_cell11_img1.png" alt="Go-kart MDP" width="500"/>
</p>
<p align="center"><em>Go-kart racing MDP policy with two lanes and stochastic transitions.</em></p>

---

## C - Action Selection in Multiagent MDPs

When multiple agents coordinate in an MDP, the state space becomes huge. This notebook explores variable elimination to reduce complexity by factorizing the value function when agents have sparse dependencies. The key insight is that if agent i's Q-function only depends on actions of agents i and i+1, we can pass messages forward to find optimal joint actions efficiently. An example shows agents choosing positions where each gets utility from their choice plus a bonus for aligning with the next agent:

<p align="center">
  <img src="../images/02 Distributed Optimization/C - Action selection in multiagent MDPs_cell3_img1.png" alt="Multiagent coordination" width="700"/>
</p>
<p align="center"><em>Agents coordinating positions, variable elimination makes this fast to compute.</em></p>

---

## D - Review of Linear Programs

A review of linear programming and the simplex algorithm. Visualizes 2D and 3D examples of moving between vertices of the feasible region.

---

## E - Duality in Linear Programming

Every linear program has a dual formulation. The fundamental theorem: if both have optimal solutions, their values are equal. 

---

## F - Negotiations, Auctions, and Optimization

This notebook connects optimization to economics through the assignment problem, where agents must be matched to objects to maximize total value. The problem can be solved as a linear program, but remarkably also has a decentralized solution: competitive equilibrium prices exist where each agent selfishly picks their best option at those prices, yet the result is globally optimal. This leads naturally to auction mechanisms where agents bid for items, with prices rising until equilibrium is reached.

---

## G - The Scheduling Problem, Generalized Competitive Equilibrium

This notebook extends the assignment problem to scheduling, where agents need time slots to complete tasks before deadlines. Unlike simple assignment, the solutions require integer programming since agents may need multiple consecutive slots. The competitive equilibrium approach still applies: by setting appropriate prices for time slots, agents can independently choose their schedules in a way that produces globally optimal allocations. This demonstrates how price-based mechanisms can coordinate complex multiagent decisions.

---

## H - Social Laws, the Traffic Problem

This notebook explores social laws: rules that constrain agent behavior to improve global outcomes without requiring continuous coordination. 