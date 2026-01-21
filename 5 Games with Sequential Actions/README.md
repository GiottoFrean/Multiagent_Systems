# Games with Sequential Actions

Normal-form games assume players choose actions simultaneously. But many real-world interactions involve sequential moves - players observe what others have done before deciding their own actions.

This section introduces **extensive-form games**, which represent sequential decision-making using game trees. These are fundamental for modeling negotiations, bargaining, repeated interactions, and any scenario where timing and information matter.

An overview of each notebook is given below.

---

## A - Perfect-Information Extensive-Form Games

A **perfect-information extensive-form game** is one where every player knows the complete history of play when making decisions. Classic examples include chess, checkers, and tic-tac-toe.

The game is represented as a tree where:
- Nodes represent decision points
- Edges represent actions
- Leaves contain payoffs for each player
- Each node is labeled with which player moves

The notebook visualizes games using Graphviz, with black nodes for player 1 and red nodes for player 2:

<p align="center">
  <img src="../images/5 Games with Sequential Actions/A - Perfect-information extensive-form games_cell3_img1.svg" alt="Simple game tree" width="450"/>
</p>
<p align="center"><em>A simple sequential game with two players.</em></p>

**Strategies in extensive form** are more complex than in normal form. A strategy must specify what to do at *every* decision point, even ones that might never be reached given earlier choices. This is a complete contingency plan.

**Backward induction** solves perfect-information games by working backwards from the leaves. At each node, assume the player will choose the action leading to their best outcome (given optimal play afterward). Green annotations show calculated values:

<p align="center">
  <img src="../images/5 Games with Sequential Actions/A - Perfect-information extensive-form games_cell6_img1.svg" alt="Backward induction 1" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/A - Perfect-information extensive-form games_cell8_img1.svg" alt="Backward induction 2" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/A - Perfect-information extensive-form games_cell10_img1.svg" alt="Backward induction 3" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/A - Perfect-information extensive-form games_cell12_img1.svg" alt="Backward induction 4" width="450"/>
</p>
<p align="center"><em>Backward induction solving various game trees.</em></p>

**Subgame-perfect equilibrium** is a refinement of Nash equilibrium. It requires that strategies form a Nash equilibrium in *every subgame*, not just the whole game. This rules out non-credible threats.

Consider a game where player 1 can choose A (ending with payoffs 2,1) or B (letting player 2 choose between C giving (3,3) or D giving (0,0)). The normal-form representation has (A,D) as a Nash equilibrium - player 2 threatens to play D if given the chance. But this isn't credible! If player 1 actually plays B, player 2 should play C. Subgame perfection rules out (A,D).

**Criticisms of backward induction**: The centipede game shows a paradox. Notice that backward induction provides the green values, which leads to player 1 making the decision to go A straight away. This seems wrong! The rewards for both players are much higher later on.

---

## B - Imperfect-Information Extensive-Form Games

In many games, players don't observe all previous moves. Poker is the classic example - you don't know your opponents' cards.

**Information sets** group together nodes that a player can't distinguish between. These are shown as dashed blue lines connecting nodes. When a player is at an information set, they don't know which specific node they're at, only that they're somewhere in that set.

<p align="center">
  <img src="../images/5 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell3_img1.svg" alt="Information set example 1" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell5_img1.svg" alt="Information set example 2" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell7_img1.svg" alt="Information set example 3" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/B - Imperfect-information extensive-form games_cell9_img1.svg" alt="Information set example 4" width="450"/>
</p>
<p align="center"><em>Games with information sets (blue dashed lines) representing imperfect information.</em></p>

A strategy must choose the same action at all nodes within an information set (since the player can't tell them apart).

Backward induction doesn't work straightforwardly anymore. Computing equilibria in imperfect-information games is much harder than perfect-information games.

---

## C - Computing Equilibria with the Sequence Form

For imperfect-information games, especially zero-sum games, the **sequence form** provides an efficient computational approach.

Instead of representing strategies as mappings from information sets to actions, the sequence form represents them as probability distributions over sequences of actions. This leads to a linear program that's much more compact than the normal-form representation.

The notebook demonstrates the sequence form on progressively complex games:

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell3_img1.svg" alt="Sequence form game 1" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell10_img1.svg" alt="Sequence form game 2" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell12_img1.svg" alt="Sequence form game 3" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell14_img1.svg" alt="Sequence form game 4" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell16_img1.svg" alt="Sequence form game 5" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell18_img1.svg" alt="Sequence form game 6" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell20_img1.svg" alt="Sequence form game 7" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell22_img1.svg" alt="Sequence form game 8" width="400"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell24_img1.svg" alt="Sequence form game 9" width="400"/>
</p>
<p align="center"><em>Computing equilibria using the sequence form representation for various imperfect-information games.</em></p>

The notebook also includes computational results showing equilibrium strategies:

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell26_img1.png" alt="Equilibrium computation 1" width="450"/>
</p>

<p align="center">
  <img src="../images/5 Games with Sequential Actions/C - computing equilibria with the sequence form_cell28_img1.png" alt="Equilibrium computation 2" width="450"/>
</p>
<p align="center"><em>Computed mixed-strategy equilibria showing probabilities for different action sequences.</em></p>

The sequence form is the foundation for modern poker-solving algorithms and has been crucial for developing AIs that can beat human experts at games like Texas Hold'em.