# Richer Representations - Beyond the Normal and Extensive Forms

So far we've looked at one-shot normal-form games and finite extensive-form games. But many real-world interactions don't fit these templates. What about repeated interactions? What about uncertainty? What about games with thousands of players?

This section explores richer game representations that can capture more complex multiagent scenarios. These include repeated games, stochastic games, Bayesian games with incomplete information, and computationally compact representations.

An overview of each notebook is given below.

---

## A - Repeated Games

When agents interact repeatedly, new strategic possibilities emerge. Cooperation can be sustained through the threat of future punishment, even in games like Prisoner's Dilemma where one-shot play leads to defection.

The **folk theorem** says that in infinitely repeated games (or with unknown endpoints), any outcome that's strictly better than the minimax values for all players can be sustained as an equilibrium using trigger strategies.

The notebook introduces **finite automata** as a way to represent strategies in repeated games:

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/A - Repeated games_cell3_img1.svg" alt="Tit-for-Tat automaton" width="400"/>
</p>
<p align="center"><em>This is a representation of the classic Tit-for-Tat strategy. An automaton is just a specification of a list of states, an action to take each state, and a transition function for every action taken (including other player's).</em></p>

When both players are restricted to finite automata, we can compute equilibria:

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/A - Repeated games_cell9_img1.png" alt="Automata payoff matrix" width="450"/>
</p>

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/A - Repeated games_cell10_img1.png" alt="Automata equilibria" width="450"/>
</p>
<p align="center"><em>Payoffs for different automata combinations and which pairs form equilibria (boolean matrix showing True for equilibrium pairs).</em></p>

Interestingly it can be proved that when a discount factor gets sufficiently close to 1 it is not possible to compute a best-response turing machine at all (nevermind, compute in NP time).

---

## B - Stochastic Games

A **stochastic game** (or Markov game) combines game theory with MDPs. There are multiple states, and after players choose actions, they receive rewards and transition to a new state (possibly stochastically).

This generalizes both:
- Normal-form games (one state, no transitions)
- MDPs (one player)

Finding equilibria in stochastic games is much harder than either problem alone. The notebook covers:

**Stationary strategies**: Policies that depend only on the current state, not on history.  
**Markov-perfect equilibrium**: A refinement where strategies form an equilibrium in every state.

**Contraction properties**: Under what conditions do iterative algorithms converge to equilibrium values?

---

## C - Bayesian Games

In **Bayesian games**, players have private information. Each player has a "type" drawn from some distribution, known only to them. For example, in an auction, each bidder knows their own valuation but not others'.

There are three equivalent views:

1. **Information set view**: Types correspond to information sets in an extensive-form game
2. **Extensive form with Nature**: An initial "Nature" player draws types, players observe only their own type
3. **Epistemic types**: Players have beliefs about other players' types, beliefs about beliefs, etc.

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/C - Bayesian games_cell3_img1.svg" alt="Bayesian game tree" width="500"/>
</p>
<p align="center"><em>Extensive-form representation of a Bayesian game with Nature choosing types.</em></p>

**Utility evaluation timing**:
- **Ex ante**: Before types are revealed, expected over all type realizations
- **Ex interim**: After learning your own type but before learning others'
- **Ex post**: After all types are revealed

Mechanism design (covered in section 10) uses Bayesian games extensively.

---

## D - Congestion Games

When many agents use shared resources, congestion occurs. Congestion games model scenarios like:
- Traffic (roads get slower when crowded)
- Network routing (links have capacity constraints)
- Resource allocation (servers slow down under load)

A key property: **congestion games always have a pure-strategy Nash equilibrium**. This is proved using potential functions.

The notebook demonstrates congestion with visualizations:

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/D - Congestion games_cell8_img1.png" alt="Congestion example 1" width="450"/>
</p>

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/D - Congestion games_cell11_img1.svg" alt="Network congestion" width="400"/>
</p>

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/D - Congestion games_cell13_img1.png" alt="Congestion example 2" width="450"/>
</p>

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/D - Congestion games_cell16_img1.svg" alt="Routing game" width="400"/>
</p>
<p align="center"><em>Congestion games with traffic networks and resource allocation.</em></p>

**Price of anarchy**: How much worse is the Nash equilibrium compared to the social optimum? For congestion games, this ratio is bounded but can be significant.

---

## E - Computationally Motivated Compact Representations

For games with many players, writing out the full payoff matrix is intractable. This notebook explores compact representations:

**Graphical games**: Players are nodes in a graph, and each player's payoff depends only on their neighbors' actions. This can reduce the representation from exponential to polynomial size.

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/E - Computationally motivated compact representations_cell4_img1.svg" alt="Graphical game 1" width="400"/>
</p>

<p align="center">
  <img src="../images/6 Richer Representations - Beyond the Normal and Extensive Forms/E - Computationally motivated compact representations_cell7_img1.svg" alt="Graphical game 2" width="400"/>
</p>
<p align="center"><em>Graphical game representations showing dependency structures between players.</em></p>

**Action-graph games**: Actions themselves form a graph, representing similar actions compactly.

**Symmetric games**: When all players are identical, we only need to specify payoffs as a function of action counts, not which specific players chose them.

These representations are crucial for scaling game-theoretic analysis to realistic multiagent systems with hundreds or thousands of agents.