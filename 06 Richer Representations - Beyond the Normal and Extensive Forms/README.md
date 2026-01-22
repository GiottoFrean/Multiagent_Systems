# Richer Representations - Beyond the Normal and Extensive Forms

Many real-world interactions don't fit one-shot normal-form games or finite extensive-form games. This section explores richer representations: repeated games, stochastic games, Bayesian games with incomplete information, and compact representations.

---

## A - Repeated Games

When agents interact repeatedly, cooperation can be sustained through future punishment threats. The folk theorem says any outcome better than minimax can be sustained as equilibrium. The notebook explores bounded rationality using finite automata to represent strategies, constraining computational complexity:

<p align="center">
  <img src="../images/06 Richer Representations - Beyond the Normal and Extensive Forms/A - Repeated games_cell3_img1.svg" alt="Tit-for-Tat automaton" width="400"/>
</p>
<p align="center"><em>Classic Tit-for-Tat strategy as a finite automaton.</em></p>

The notebook demonstrates computing Nash equilibria for automata-restricted strategies in repeated games, showing that not all equilibria involve always defecting.

---

## B - Stochastic Games

A stochastic game combines game theory with MDPs - multiple states with transitions after actions. This generalizes both normal-form games (one state) and MDPs (one player). Strategies can be behavioral, Markov, or stationary. The notebook uses value iteration adapted for two players, computing Q-functions and finding Nash equilibria at each state. However, this optimizes per-state rather than globally, potentially missing some equilibria. Computing equilibria is generally much harder than single-player MDPs.

---

## C - Bayesian Games

Players have private information ("types"). For example, in auctions each bidder knows their own valuation but not others'. Three equivalent representations: information sets, extensive form with Nature making initial random choices, and epistemic types with a common prior. Expected utility can be computed ex post (knowing all types), ex interim (knowing your own type), or ex ante (knowing nothing). Mechanism design uses Bayesian games extensively.

<p align="center">
  <img src="../images/06 Richer Representations - Beyond the Normal and Extensive Forms/C - Bayesian games_cell3_img1.svg" alt="Bayesian game extensive form" width="600"/>
</p>
<p align="center"><em>Extensive form representation with Nature node choosing between four games (Matching Pennies, Prisoner's Dilemma, Coordination, Battle of Sexes). Information sets show what each player knows about the game being played.</em></p>

---

## D - Congestion Games

Model shared resources like traffic or network routing where costs depend on how many agents use each resource. Key property: every congestion game is a potential game, guaranteeing a pure-strategy Nash equilibrium. The notebook proves congestion games are potential games and demonstrates myopic best-response converges to equilibrium. Price of anarchy measures how much worse equilibrium is compared to social optimum, and can grow unbounded in some networks.

---

## E - Computationally Motivated Compact Representations

For many players, full payoff matrices are intractable. This notebook covers polynomial-type games and efficient expected utility computation. Graphical games represent payoff dependencies as a graph where agents only depend on neighbors. Action-graph games compress actions rather than players. Multi-agent influence diagrams (MAIDs) combine graphical games with extensive forms. These representations enable polynomial-time algorithms for equilibria and expected utility when dependencies are sparse.

<p align="center">
  <img src="../images/06 Richer Representations - Beyond the Normal and Extensive Forms/E - Computationally motivated compact representations_cell7_img1.svg" alt="MAID example" width="500"/>
</p>
<p align="center"><em>Multi-agent influence diagram showing two players (grey shades) deciding about a tree and patio. Rectangles are decisions, ovals are random events, diamonds are utilities. Dotted arrows indicate information flow; solid arrows indicate causal effects. </em></p>