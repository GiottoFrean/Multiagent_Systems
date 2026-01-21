# Games with Sequential Actions

Normal-form games assume simultaneous moves. This section introduces extensive-form games for sequential decision-making using game trees.

---

## A - Perfect-Information Extensive-Form Games

Games where every player knows the complete history (like chess). The game is a tree with decision nodes, actions, and payoffs. Any extensive-form game can be converted to normal-form, but this can introduce problematic Nash equilibria involving non-credible threats. Subgame-perfect equilibrium is a refinement that requires Nash equilibrium in every subgame. Backward induction computes subgame-perfect equilibria efficiently by working backwards from the leaves:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/A - Perfect-information extensive-form games_cell6_img1.svg" alt="Backward induction" width="500"/>
</p>
<p align="center"><em>Backward induction solving a game tree (green annotations show calculated values).</em></p>

---

## B - Imperfect-Information Extensive-Form Games

In many games, players don't observe all previous moves (like poker). Information sets group nodes a player can't distinguish (shown as dashed blue lines):

<p align="center">
  <img src="../images/05 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell3_img1.svg" alt="Information set example" width="500"/>
</p>
<p align="center"><em>Game with information sets representing imperfect information.</em></p>

A key concept is behavioral strategies: instead of mixing over complete strategies (as in normal-form), players randomize independently at each information set. For games with perfect recall (where players remember their own past actions), behavioral strategies are equivalent in expressive power to mixed strategies. Without perfect recall, some mixed strategies cannot be represented as behavioral strategies.

---

## C - Computing Equilibria with the Sequence Form

The sequence form provides efficient computation for imperfect-information games with perfect recall. A sequence is the set of actions a player takes to reach a node. A realization plan assigns probabilities to sequences such that probabilities sum correctly up the tree. Computing best responses becomes a linear program (or its dual), dramatically more efficient than enumerating all behavioral strategies:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell3_img1.svg" alt="Sequence form game" width="450"/>
</p>
<p align="center"><em>Game solved using the sequence form representation.</em></p>

This notebook also covers sequential equilibria, which extend subgame-perfect equilibrium to imperfect-information games. The key challenge: when information sets group nodes together, players must form beliefs about which node they're at. Sequential equilibrium requires strategies to be optimal given these beliefs:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell10_img1.svg" alt="Sequential equilibrium example" width="380"/>
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell12_img1.svg" alt="Subgame values" width="380"/>
</p>

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell14_img1.svg" alt="Imperfect information variant" width="380"/>
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell18_img1.svg" alt="Belief probabilities" width="380"/>
</p>
<p align="center"><em>Sequential equilibrium: subgame-perfect equilibrium extended to imperfect information using belief probabilities.</em></p>

The sequence form is the foundation for modern poker-solving algorithms.