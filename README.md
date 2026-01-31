# Multiagent Systems

This repository contains my notes and explorations while learning from the book Multiagent Systems by Yoav Shoham and Kevin Leyton-Brown. Each folder corresponds to a chapter or topic from the book, with Jupyter notebooks working through the concepts, algorithms, and examples.

---


## 01 Distributed Constraint Satisfaction

Distributed constraint satisfaction addresses how agents with independent constraints can collectively reach a solution that satisfies all requirements.

Imagine a network of cell towers, where each tower needs to use a different frequency to those nearby. This is basically a graph coloring problem, where the frequencies are the colors.

---

### A - Domain-Pruning Algorithms

This notebook introduces domain pruning, where each node eliminates values from its domain that can't possibly work. It goes something like this:

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img1.png" alt="Filtering steps 1" width="320"/>
</p>

X3 removes red...

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img3.png" alt="Filtering steps 2" width="320"/>
</p>

X2 removes red...

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img5.png" alt="Filtering steps 3" width="320"/>
</p>

X2 removes blue...

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/A - Domain-pruning algorithms_cell10_img7.png" alt="Filtering steps 4" width="320"/>
</p>
<p align="center"><em>Filtering algorithm progressively reducing domains until a solution is found.</em></p>

This works eventually, but it can get stuck if there are multiple solutions and won't always identify if a problem has no solution.

This notebook also introduces the hyper-resolution algorithm, which uses a general rule from propositional logic. It works by having nodes generate new constraints at each step, called "nogoods", and communicate those to their neighbours.

---

### B - Introduction to Heuristic Search Algorithms

While simple domain pruning is also expensive, so heuristic alternatives are often used. 

One *centralised* strategy for solving a constraint problem is to do recursive search of values, backtracking when you find one that doesn't work. We can take that idea and try to make it work in a decentalised way by having each node simply choose a value that works with it's current neighbours.

While easy to explain, it unfortunately sometimes fails to find a solution even when there is one. e.g.,

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/B - Introduction to heuristic search algorithms_cell15_img1.png" alt="Fails in this case" width="320"/>
</p>
<p align="center"><em>The algorithm fails in this case.</em></p>

---

### C - The Asynchronous Backtracking Algorithm

The asynchonous backtracking algorithm can be thought of as a greedy version of the hyper-resolution algorithm, meeting somewhere between the two previous ideas. Essentially, we want every node to be trying values, and then backtracking with a 'nogood' when it can't.

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img1.png" alt="ABT step 1" width="700"/>
</p>

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img3.png" alt="ABT step 2" width="700"/>
</p>

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img5.png" alt="ABT step 3" width="700"/>
</p>

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img7.png" alt="ABT step 4" width="700"/>
</p>

<p align="center">
  <img src="images/01 Distributed Constraint Satisfaction/C - The asynchronous backtracking algorithm_cell9_img9.png" alt="ABT step 5" width="700"/>
</p>
<p align="center"><em>Asynchronous backtracking progressively finding a solution through message passing.</em></p>


## 02 Distributed Optimization

Distributed Optimization is about how agents with different sets of information can optimise a global objective function.

---

### A - Distributed Dynamic Programming

Dijkstra's algorithm builds paths outward from the origin by always selecting the node with the shortest distance. The asynchronous dynamic programming instead has nodes updating their distance estimates in any order. It still converge to the optimal solution. 

<p align="center">
  <img src="images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img1.png" alt="DP iteration 1" width="700"/>
</p>

node s found a new shortest path to a with length 1 <br>
node s found a new shortest path to b with length 3

<p align="center">
  <img src="images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img5.png" alt="DP iteration 3" width="700"/>
</p>

node a found a new shortest path to b with length 2 <br>
node a found a new shortest path to c with length 3 <br>
node b found a new shortest path to d with length 4

<p align="center">
  <img src="images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img9.png" alt="DP iteration 5" width="700"/>
</p>

node c found a new shortest path to t with length 4

<p align="center">
  <img src="images/02 Distributed Optimization/A - Distributed dynamic programming_cell6_img13.png" alt="DP iteration 7" width="700"/>
</p>
<p align="center"><em>Asynchronous dynamic programming progressively finding shortest paths.</em></p>

The notebook also covers Learning Real-Time A* (LRTA*), where multiple agents explore the graph simultaneously, sharing distance estimates that underestimate the true cost. When an agent repeats the same path twice, it is proven to be optimal.

---

### B - Review MDPs

This notebook reviews Markov Decision Processes (MDPs), which extend path-finding to stochastic environments. The Bellman equation provides the optimal value function and is proven to be a contraction mapping. A go-kart racing example demonstrates the concepts:

<p align="center">
  <img src="images/02 Distributed Optimization/B - Review MDPs_cell11_img1.png" alt="Go-kart MDP" width="500"/>
</p>
<p align="center"><em>Go-kart racing MDP policy with two lanes and stochastic transitions.</em></p>

---

### C - Action Selection in Multiagent MDPs

When multiple agents coordinate in an MDP, the state space becomes huge. This notebook explores variable elimination to reduce complexity by factorizing the value function when agents have sparse dependencies. The key insight is that if agent i's Q-function only depends on actions of agents i and i+1, we can pass messages forward to find optimal joint actions efficiently. An example shows agents choosing positions where each gets utility from their choice plus a bonus for aligning with the next agent:

<p align="center">
  <img src="images/02 Distributed Optimization/C - Action selection in multiagent MDPs_cell3_img1.png" alt="Multiagent coordination" width="700"/>
</p>
<p align="center"><em>Agents coordinating positions, variable elimination makes this fast to compute.</em></p>

---

### D - Review of Linear Programs

A review of linear programming and the simplex algorithm. Visualizes 2D and 3D examples of moving between vertices of the feasible region.

---

### E - Duality in Linear Programming

Every linear program has a dual formulation. The fundamental theorem: if both have optimal solutions, their values are equal. 

---

### F - Negotiations, Auctions, and Optimization

This notebook connects optimization to economics through the assignment problem, where agents must be matched to objects to maximize total value. The problem can be solved as a linear program, but remarkably also has a decentralized solution: competitive equilibrium prices exist where each agent selfishly picks their best option at those prices, yet the result is globally optimal. This leads naturally to auction mechanisms where agents bid for items, with prices rising until equilibrium is reached.

---

### G - The Scheduling Problem, Generalized Competitive Equilibrium

This notebook extends the assignment problem to scheduling, where agents need time slots to complete tasks before deadlines. Unlike simple assignment, the solutions require integer programming since agents may need multiple consecutive slots. The competitive equilibrium approach still applies: by setting appropriate prices for time slots, agents can independently choose their schedules in a way that produces globally optimal allocations. This demonstrates how price-based mechanisms can coordinate complex multiagent decisions.

---

### H - Social Laws, the Traffic Problem

This notebook explores social laws: rules that constrain agent behavior to improve global outcomes without requiring continuous coordination.


## 03 Introduction to Noncooperative Game Theory - Games in Normal Form

Here self-interested agents who have their own preferences are introduced.

---

### A - Self-Interested Agents and Utility Theory Maths

This notebook establishes the mathematical framework of utility theory. The Von Neumann-Morgenstern utility theorem shows that if preferences satisfy certain axioms, they can be represented by a utility function over lotteries. The point is to show that utility is grounded in the maths of preferences.

---

### B - Games in Normal Form

A normal-form game consists of players, actions, and payoff functions. Games are represented as matrices with utilities for each player based on action profiles. Pure strategies are introduced as well as mixed strategies, where players randomize over actions.

The notebook introduces classic games like Prisoner's Dilemma: If both cooperate they get 5 each. If one cooperates and one defects, one gets 8 and the other gets 0. If both defect they get 2. The best option is (C,C) but the outcome is (D,D). Notice below that regardless of what player 2 does, player 1 is better off defecting (and vice versa).

<p align="center">
  <img src="images/03 Introduction to Noncooperative Game Theory - Games in Normal Form/B - Games in normal form_cell3_img2.png" alt="Mixed strategy heatmap" width="700"/>
</p>
<p align="center"><em>Heatmap showing utilities for different mixed strategy combinations.</em></p>

---

### C - Analyzing Games, Optimality and Equilibrium

Talks about Nash equilibrium, which is where no player can improve by unilaterally changing their strategy. For Prisoner's Dilemma, (D,D) is the unique Nash equilibrium, even though it's not optimal.

---

### D - Further Solution Concepts for Normal-Form Games

This notebook explores refinements. Minimax strategies for zero-sum games, where each player minimizes the maximum possible loss. Correlated equilibrium, where a trusted third party recommends actions. Also discusses dominated strategies and iterated elimination of dominated strategies.


## 04 Computing solution concepts for Normal-Form games

Unfortunately, computing Nash equilibria is computationally challenging - it belongs to a class called PPAD, which is believed to grow exponentially. This section covers algorithms for finding equilibria.

---

### A - Computing Nash Equilibria

This notebook starts with the easy case: two-player, zero-sum games, where computing a Nash equilibrium reduces to solving a linear program.

It then moves to general two-player games, where equilibrium computation is harder. The notebook introduces an LCP (linear complementarity problem) formulation and the Lemke-Howson algorithm as a pivoting method for finding equilibria.

One of the key geometric ideas is the “labelling” view. At equilibrium, each mixed strategy is labelled by its zero-probability actions and the opponent’s best-response actions, which means equilibrium occurs where the combined labels cover all actions. This leads to a path-following algorithm that traces edges of the best-response polytopes to find equilibria.

The notebook visualizes this labelling process:

<p align="center">
  <img src="images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell6_img1.png" alt="Player 2 utility curves" width="400"/>
  <img src="images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell8_img1.png" alt="Player 1 labelling" width="400"/>
</p>

<p align="center">
  <img src="images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell10_img1.png" alt="Player 1 utility curves" width="400"/>
  <img src="images/04 Computing solution concepts for Normal-Form games/A - Computing Nash equilibria_cell12_img1.png" alt="Player 2 labelling" width="400"/>
</p>
<p align="center"><em>Lemke-Howson algorithm: utility curves show best responses, labelling diagrams identify equilibrium points where all actions are covered.</em></p>

---

### B - Computing Nash Equilibria, Deeper Look

This does a deeper dive into the Lemke-Howson algorithm. Explanations of pivoting too. 

---

### C - Computing Nash Equilibria as an Optimisation Problem

This notebook explores gradient-based method,s where equilibrium-finding is formulated as optimization.

---

### D - Identifying Dominated Strategies, Iterative Dominance

One way to make the computation easier is to iteratively remove dominated strategies until no more exist, this notebook looks at domination by pure and mixed strategies in detail.

---

### E - Finding Correlated Equilibria

A correlated equilibrium involves a trusted third party that recommends joint action profiles to players. Unlike Nash equilibria where players independently randomize, here players can condition on correlated signals (like traffic lights). Computing these is just a linear program - the constraints ensure no player wants to deviate from the mediator's recommendations. However, the algorithm finds many different correlated equilibria, not necessarily the intuitive ones. While every Nash equilibrium is also a correlated equilibrium, the ease of computing correlated equilibria doesn't help find Nash equilibria since Nash requires independent probability calculations.


## 05 Games with Sequential Actions

Normal-form games assume simultaneous moves. This section introduces extensive-form games for sequential decision-making using game trees.

---

### A - Perfect-Information Extensive-Form Games

Games where every player knows the complete history (like chess). The game is a tree with decision nodes, actions, and payoffs. Any extensive-form game can be converted to normal-form, but this can introduce problematic Nash equilibria involving non-credible threats. Subgame-perfect equilibrium is a refinement that requires Nash equilibrium in every subgame. Backward induction computes subgame-perfect equilibria efficiently by working backwards from the leaves:

<p align="center">
  <img src="images/05 Games with Sequential Actions/A - Perfect-information extensive-form games_cell6_img1.svg" alt="Backward induction" width="300"/>
</p>
<p align="center"><em>Backward induction solving a game tree (green annotations show calculated values).</em></p>

---

### B - Imperfect-Information Extensive-Form Games

In many games, players don't observe all previous moves (like poker). Information sets group nodes a player can't distinguish (shown as dashed blue lines):

<p align="center">
  <img src="images/05 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell3_img1.svg" alt="Information set example" width="500"/>
</p>
<p align="center"><em>Game with information sets representing imperfect information.</em></p>

A key concept is behavioral strategies: instead of mixing over complete strategies (as in normal-form), players randomize independently at each information set. For games with perfect recall (where players remember their own past actions), behavioral strategies are equivalent in expressive power to mixed strategies. Without perfect recall, some mixed strategies cannot be represented as behavioral strategies and vice versa.

---

### C - Computing Equilibria with the Sequence Form

The sequence form provides efficient computation for imperfect-information games with perfect recall. A sequence is the set of actions a player takes to reach a node. A realization plan assigns probabilities to sequences such that probabilities sum correctly up the tree. Computing best responses becomes a linear program (or its dual), dramatically more efficient than enumerating all behavioral strategies.

This notebook also covers sequential equilibria, which extend subgame-perfect equilibrium to imperfect-information games. The key challenge: when information sets group nodes together, players must form beliefs about which node they're at. Sequential equilibrium requires strategies to be optimal given these beliefs:

<p align="center">
  <img src="images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell10_img1.svg" alt="Sequential equilibrium example" width="380"/>
</p>

There are two Nash equilibria: LU and RD. But it's a bit odd! In truth player 1 would realise if they do R then player 2 will go D, which is better for player 1 than LU. The only true equilibria is then RD. We can see this if we compute the subgames. In this case the subgames are trivial as each player just makes the best decision they can:

<p align="center">
  <img src="images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell12_img1.svg" alt="Subgame values" width="380"/>
</p>

When it comes to imperfect-information games this concept is extended into "sequential equilibria" and gets a bit more complicated. Let's assume that the second player doesn't know what the first did. Then we get something more like this:

<p align="center">
  <img src="images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell14_img1.svg" alt="Imperfect information variant" width="380"/>
</p>

We can no longer just push back the values, because what player 2 will do is dependent on what player 1 does. We have to deal with a forest of subgames. Notice that the subgame from C and from R have different optimal solutions! So we can't use the subgame-perfect equilibrium logic.


## 06 Richer Representations - Beyond the Normal and Extensive Forms

Many real-world interactions don't fit one-shot normal-form games or finite extensive-form games. This section explores richer representations: repeated games, stochastic games, Bayesian games with incomplete information, and compact representations.

---

### A - Repeated Games

When agents interact repeatedly, cooperation can be sustained through future punishment threats. The folk theorem says any outcome better than minimax can be sustained as equilibrium. The notebook explores bounded rationality using finite automata to represent strategies, constraining computational complexity:

<p align="center">
  <img src="images/06 Richer Representations - Beyond the Normal and Extensive Forms/A - Repeated games_cell3_img1.svg" alt="Tit-for-Tat automaton" width="400"/>
</p>
<p align="center"><em>Classic Tit-for-Tat strategy as a finite automaton.</em></p>

The notebook demonstrates computing Nash equilibria for automata-restricted strategies in repeated games, showing that not all equilibria involve always defecting.

---

### B - Stochastic Games

A stochastic game combines game theory with MDPs - multiple states with transitions after actions. This generalizes both normal-form games (one state) and MDPs (one player). Strategies can be behavioral, Markov, or stationary. The notebook uses value iteration adapted for two players, computing Q-functions and finding Nash equilibria at each state. However, this optimizes per-state rather than globally, potentially missing some equilibria. Computing equilibria is generally much harder than single-player MDPs.

---

### C - Bayesian Games

Players have private information ("types"). For example, in auctions each bidder knows their own valuation but not others'. Three equivalent representations: information sets, extensive form with Nature making initial random choices, and epistemic types with a common prior. Expected utility can be computed ex post (knowing all types), ex interim (knowing your own type), or ex ante (knowing nothing). Mechanism design uses Bayesian games extensively.

<p align="center">
  <img src="images/06 Richer Representations - Beyond the Normal and Extensive Forms/C - Bayesian games_cell3_img1.svg" alt="Bayesian game extensive form" width="600"/>
</p>
<p align="center"><em>Extensive form representation with Nature node choosing between four games (Matching Pennies, Prisoner's Dilemma, Coordination, Battle of Sexes). Information sets show what each player knows about the game being played.</em></p>

---

### D - Congestion Games

Model shared resources like traffic or network routing where costs depend on how many agents use each resource. Key property: every congestion game is a potential game, guaranteeing a pure-strategy Nash equilibrium. The notebook proves congestion games are potential games and demonstrates myopic best-response converges to equilibrium. Price of anarchy measures how much worse equilibrium is compared to social optimum, and can grow unbounded in some networks.

---

### E - Computationally Motivated Compact Representations

For many players, full payoff matrices are intractable. This notebook covers polynomial-type games and efficient expected utility computation. Graphical games represent payoff dependencies as a graph where agents only depend on neighbors. Action-graph games compress actions rather than players. Multi-agent influence diagrams (MAIDs) combine graphical games with extensive forms. These representations enable polynomial-time algorithms for equilibria and expected utility when dependencies are sparse.

<p align="center">
  <img src="images/06 Richer Representations - Beyond the Normal and Extensive Forms/E - Computationally motivated compact representations_cell7_img1.svg" alt="MAID example" width="500"/>
</p>
<p align="center"><em>Multi-agent influence diagram showing two players (grey shades) deciding about a tree and patio. Rectangles are decisions, ovals are random events, diamonds are utilities. Dotted arrows indicate information flow; solid arrows indicate causal effects. </em></p>


## 07 Learning and Teaching

Learning in game theory involves repeated or stochastic games where agents adapt over time. The key: it's not just learning in isolation - agents are learning about other agents who are also learning. Players teach and learn with each other.

---

### A - Why the Subject of "Learning" is Complex

Learning in multiagent systems is fundamentally different from single-agent learning. The environment isn't stationary - when others change strategies, your optimal strategy changes. Additionally, intelligent agents aren't just learning but also teaching through their actions. Example: a player might play suboptimally in the short term to teach opponents they'll cooperate, enabling better long-term outcomes. 

---

### B - Fictitious Play

Fictitious play: each agent tracks the empirical frequency of opponents' past actions and best-responds to it. Agents maintain a count of how many times opponents played each action, normalize to get probabilities, then play a best response. Key properties: (1) pure-strategy Nash equilibria are steady states of fictitious play, and vice versa; (2) if empirical distributions converge, they converge to Nash equilibrium. Guaranteed convergence for: zero-sum games, games solvable by iterated elimination of strictly-dominated strategies, potential games, and 2×n games with generic payoffs. Rock-Paper-Scissors demonstrates non-steady-state convergence: no fixed pure strategies, but empirical frequencies converge to uniform (1/3, 1/3, 1/3), as expected.

---

### C - Rational Learning

Rational learning extends fictitious play by allowing agents to model entire opponent strategies (like tit-for-tat or trigger strategies) rather than just action frequencies. Players maintain beliefs over a set of possible strategies, update via Bayesian inference after observing opponent actions, and choose best responses to their beliefs. Example: in repeated Prisoner's Dilemma, if an opponent cooperates for two rounds, a rational learner eliminates "always defect" and "trigger at t=0" from consideration, concentrating beliefs on longer-horizon strategies. Can include a mistake probability to prevent beliefs from zeroing out (allowing for strategy changes). Converges to ε-equilibrium but requires careful tuning of belief updates and best-response functions.

---

### D - Reinforcement Learning

Reinforcement learning doesn't assume agents know transition probabilities or opponent payoffs. Q-learning updates action-values via Q(s,a) ← (1-α)Q(s,a) + α(r + γV(s')), with learning rate α declining as 1/t. The notebook demonstrates Q-learning on a simple 3-state MDP, showing convergence to optimal values without knowing transition matrices. For multiagent zero-sum games, extend Q to include opponent actions Q(s,a,o) and compute V via minimax: V(s) = max_a min_o Q(s,a,o).

---

### E - No-Regret Learning and Universal Consistency

Regret measures the difference between your average reward and the reward from always playing some fixed pure strategy. A no-regret algorithm guarantees non-positive regret for all pure strategies. Regret matching: at each timestep, choose actions with probability proportional to their regret (how much better that action would have been). If all players use no-regret learning, empirical action frequencies converge to correlated equilibria. 

---

### F - Evolutionary Learning and Large Population Models

When modeling many agents, use population-level dynamics with θ(a) being the fraction playing action a. The growth rate of strategy a is θ(a)(u(a) - ū), where u(a) is the payoff to a and ū is the population average. Strategies above average grow; those below shrink.


## 08 Communication

So far we've assumed agents observe actions but don't communicate directly. This section explores when and how communication matters in strategic settings.

---

### A - Doing by Talking I (Cheap Talk)

Does communication before the game change things? For Prisoner's Dilemma: well, no. Regardless of what both players say, they will each still choose to defect. Cheap talk is communication that's costless and non-binding.

<p align="center">
  <img src="images/08 Communication/A - Doing by talking I (cheap talk)_cell3_img1.svg" alt="Cheap talk game" width="500"/>
</p>
<p align="center"><em>Game tree with pre-play cheap talk communication stage.</em></p>

In games with multiple equilibria (Battle of the Sexes), cheap talk can help coordinate. You can see that doing the opposite of what was said is an equilibrium too... How confusing!

---

### B - Talking by Doing (Signalling Games)

Signalling games model asymmetric information: Nature chooses a game type, Player 1 observes it and takes an action, Player 2 observes only the action (not the game type) and responds. Player 1's action serves as a signal about the hidden information. Unlike cheap talk, signals can be credible because they're costly or constrained.

<p align="center">
  <img src="images/08 Communication/B - Talking by doing (signalling games)_cell3_img1.svg" alt="PD/Stag signaling game" width="600"/>
</p>
<p align="center"><em>Nature chooses between Prisoner's Dilemma and Stag Hunt. Player 1 sees the game and chooses C or D. Player 2 observes only Player 1's action (shown by information sets) and must respond without knowing which game is being played.</em></p>

The challenge: Player 1's optimal action depends on what Player 2 will do, but Player 2's optimal response depends on inferring which game is being played from Player 1's action. Simple Bayesian reasoning fails because Player 1 anticipates Player 2's inference.

<p align="center">
  <img src="images/08 Communication/B - Talking by doing (signalling games)_cell5_img1.svg" alt="Zero-sum signaling game" width="600"/>
</p>
<p align="center"><em>Two zero-sum games where Player 1 can signal the game type through action choice. If Player 1 always plays B, they average 2.5 regardless of Player 2's response, better than playing each game's Nash equilibrium (which would average 1.5).</em></p>

---

### C - Doing by Talking II (Speech-Act Theory)

Speech-act theory distinguishes three aspects of speech: locutionary (literal content), illocutionary (speaker intention), and perlocutionary (effect on listener). Grice's cooperative principles govern conversation: Quantity (provide needed information), Quality (be truthful), Relation (be relevant), and Manner (be clear). These principles explain implicature - how "Harry hasn't gone to prison yet" conveys more than its literal meaning.

<p align="center">
  <img src="images/08 Communication/C- Doing by talking II (speech-act theory)_cell3_img1.svg" alt="Chair ambiguity game" width="600"/>
</p>
<p align="center"><em>Signaling game modeling ambiguous language. Nature determines whether a wooden chair or the meeting chair is coming. The speaker chooses clarity level (costly to be more specific). The listener infers meaning from ambiguous statements. Optimal strategy: be clear for the less likely event, use shorthand for the more likely one.</em></p>

Tied up with the value of information.


## 09 Aggregating preferences, social choice

Everything before has assumed clear utility functions. But in many cases you can't get utilities without them being gamed or misreported. Instead you can ask for preferences, i.e., choose A or B.

---

### A - Models and Voting, Social Functions, Ranking Systems

This notebook explores what properties we want from voting systems and why that's surprisingly difficult.

A sensible approach is to meet the Condorcet condition, where an option is selected if it beats every other in pairwise majority comparisons. But this doesn't always work, often there is no Condorcet winner. Plurality voting, Borda voting, pairwise elimination, and approval voting are explored.

Arrow's Impossibility Theorem is presented, where any social welfare function that produces a full ranking of outcomes must violate at least one of three basic fairness properties: Pareto efficiency (if everyone prefers A to B, rank A higher), independence of irrelevant alternatives (the ranking of A vs B shouldn't depend on C), or non-dictatorship (no single person determines everything). The proof shows that any decisive coalition, one that can force a ranking, can be split into smaller decisive coalitions recursively until you reach a single dictator.

There are some positive results if you restrict the problem. If outcomes are just the agents themselves and each agent has binary preferences (approve/disapprove), then approval voting satisfies analogous fairness conditions. For ranking systems in this setting, you can build iterative algorithms where votes propagate through the preference graph, achieving weaker but still meaningful fairness properties.


## 10 Protocols for Strategic Agents - Mechanism Design

Mechanism design is about getting agents to behave in desirable ways. E.g., to be truthful. While game theory analyzes existing games, mechanism design inverts the question: what game should we design to achieve desired outcomes?

---

### A - Mechanism Design with Unrestricted Preferences

A mechanism consists of messages agents can send and an outcome function. A social choice function specifies what outcome should occur for each preference profile. Can we design a mechanism that implements this?

The revelation principle: Any mechanism can be converted to a direct mechanism where agents report types truthfully. Because the original mechanism is designed such that agents have dominant strategies there is no reason to lie.

Vickrey auction: Second-price sealed-bid where highest bidder pays second-highest bid. Truthful bidding is dominant!
