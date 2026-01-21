# Games with Sequential Actions

Normal-form games assume simultaneous moves. This section introduces extensive-form games for sequential decision-making using game trees.

---

## A - Perfect-Information Extensive-Form Games

Games where every player knows the complete history (like chess). The game is a tree with decision nodes, actions, and payoffs. Backward induction solves by working backwards from the leaves:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/A - Perfect-information extensive-form games_cell6_img1.svg" alt="Backward induction" width="500"/>
</p>
<p align="center"><em>Backward induction solving a game tree (green annotations show calculated values).</em></p>

Subgame-perfect equilibrium rules out non-credible threats. The centipede game shows a paradox - backward induction leads to immediate termination even though waiting would be better for everyone.

---

## B - Imperfect-Information Extensive-Form Games

In many games, players don't observe all previous moves (like poker). Information sets group nodes a player can't distinguish (shown as dashed blue lines):

<p align="center">
  <img src="../images/05 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell3_img1.svg" alt="Information set example" width="500"/>
</p>
<p align="center"><em>Game with information sets representing imperfect information.</em></p>

Computing equilibria is much harder than perfect-information games.

---

## C - Computing Equilibria with the Sequence Form

The sequence form provides efficient computation for imperfect-information games. Instead of mapping information sets to actions, it uses probability distributions over action sequences, leading to a compact linear program:

<p align="center">
  <img src="../images/05 Games with Sequential Actions/C - computing equilibria with the sequence form_cell3_img1.svg" alt="Sequence form game" width="450"/>
</p>
<p align="center"><em>Game solved using the sequence form representation.</em></p>

The sequence form is the foundation for modern poker-solving algorithms.