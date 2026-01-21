# Richer Representations - Beyond the Normal and Extensive Forms

Many real-world interactions don't fit one-shot normal-form games or finite extensive-form games. This section explores richer representations: repeated games, stochastic games, Bayesian games with incomplete information, and compact representations.

---

## A - Repeated Games

When agents interact repeatedly, cooperation can be sustained through future punishment threats. The **folk theorem** says any outcome better than minimax can be sustained as equilibrium. **Finite automata** represent strategies:

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/A - Repeated games_cell3_img1.svg" alt="Tit-for-Tat automaton" width="400"/>
</p>
<p align="center"><em>Classic Tit-for-Tat strategy as a finite automaton.</em></p>

Interestingly, when discount factor gets close to 1, computing a best-response turing machine becomes impossible.

---

## B - Stochastic Games

A **stochastic game** combines game theory with MDPs - multiple states with transitions after actions. This generalizes both normal-form games (one state) and MDPs (one player). Finding equilibria is much harder.

---

## C - Bayesian Games

Players have private information ("types"). For example, in auctions each bidder knows their own valuation but not others'. Three equivalent views: information sets, extensive form with Nature, and epistemic types. Mechanism design uses Bayesian games extensively.

---

## D - Congestion Games

Model shared resources like traffic or network routing. Key property: **congestion games always have a pure-strategy Nash equilibrium**. **Price of anarchy** measures how much worse equilibrium is compared to social optimum.

---

## E - Computationally Motivated Compact Representations

For many players, full payoff matrices are intractable. **Graphical games** have players as nodes where payoffs depend only on neighbors. **Symmetric games** specify payoffs by action counts. These are crucial for scaling to hundreds or thousands of agents.