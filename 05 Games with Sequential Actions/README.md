# Games with Sequential Actions

Normal-form games assume simultaneous moves. This section introduces extensive-form games for sequential decision-making using game trees.

---

## A - Perfect-Information Extensive-Form Games

Games where every player knows the complete history (like chess). The game is a tree with decision nodes, actions, and payoffs. Any extensive-form game can be converted to normal-form, but this can introduce problematic Nash equilibria involving non-credible threats. Subgame-perfect equilibrium is a refinement that requires Nash equilibrium in every subgame. Backward induction computes subgame-perfect equilibria efficiently by working backwards from the leaves:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/A - Perfect-information extensive-form games_cell6_img1.svg" alt="Backward induction" width="300"/>
</p>
<p align="center"><em>Backward induction solving a game tree (green annotations show calculated values).</em></p>

---

## B - Imperfect-Information Extensive-Form Games

In many games, players don't observe all previous moves (like poker). Information sets group nodes a player can't distinguish (shown as dashed blue lines):

<p align="center">
  <img src="../images/05 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell3_img1.svg" alt="Information set example" width="500"/>
</p>
<p align="center"><em>Game with information sets representing imperfect information.</em></p>

A key concept is behavioral strategies: instead of mixing over complete strategies (as in normal-form), players randomize independently at each information set. For games with perfect recall (where players remember their own past actions), behavioral strategies are equivalent in expressive power to mixed strategies. Without perfect recall, some mixed strategies cannot be represented as behavioral strategies and vice versa.

---

## C - Computing Equilibria with the Sequence Form

The sequence form provides efficient computation for imperfect-information games with perfect recall. A sequence is the set of actions a player takes to reach a node. A realization plan assigns probabilities to sequences such that probabilities sum correctly up the tree. Computing best responses becomes a linear program (or its dual), dramatically more efficient than enumerating all behavioral strategies.

This notebook also covers sequential equilibria, which extend subgame-perfect equilibrium to imperfect-information games. The key challenge: when information sets group nodes together, players must form beliefs about which node they're at. Sequential equilibrium requires strategies to be optimal given these beliefs:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell10_img1.svg" alt="Sequential equilibrium example" width="380"/>
</p>

There are two Nash equilibria: LU and RD. But it's a bit odd! In truth player 1 would realise if they do R then player 2 will go D, which is better for player 1 than LU. The only true equilibria is then RD. We can see this if we compute the subgames. In this case the subgames are trivial as each player just makes the best decision they can:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell12_img1.svg" alt="Subgame values" width="380"/>
</p>

When it comes to imperfect-information games this concept is extended into "sequential equilibria" and gets a bit more complicated. Let's assume that the second player doesn't know what the first did. Then we get something more like this:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell14_img1.svg" alt="Imperfect information variant" width="380"/>
</p>

We can no longer just push back the values, because what player 2 will do is dependent on what player 1 does. We have to deal with a forest of subgames. Notice that the subgame from C and from R have different optimal solutions! So we can't use the subgame-perfect equilibrium logic.