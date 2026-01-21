# Communication

So far we've assumed agents observe actions but don't communicate directly. This section explores when and how communication matters in strategic settings.

The notebooks roughly split communication into *informational* views (messages update beliefs) and *motivational/strategic* views (messages/actions are chosen to influence others).

---

## A - Doing by Talking I (Cheap Talk)

Does communication before the game change things? For Prisoner's Dilemma: well, no. Regardless of what both players say, they will each still choose to defect. Cheap talk is communication that's costless and non-binding.

<p align="center">
  <img src="../images/08 Communication/A - Doing by talking I (cheap talk)_cell3_img1.svg" alt="Cheap talk game" width="500"/>
</p>
<p align="center"><em>Game tree with pre-play cheap talk communication stage.</em></p>

In games with multiple equilibria (Battle of the Sexes), cheap talk can help coordinate. You can see that doing the opposite of what was said is an equilibrium too... How confusing! Giotto's thought: communication is probably only applicable in repeated games.

---

## B - Talking by Doing (Signalling Games)

Signalling games model asymmetric information: Nature chooses a game type, Player 1 observes it and takes an action, Player 2 observes only the action (not the game type) and responds. Player 1's action serves as a signal about the hidden information. Unlike cheap talk, signals can be credible because they're costly or constrained.

<p align="center">
  <img src="../images/08 Communication/B - Talking by doing (signalling games)_cell3_img1.svg" alt="PD/Stag signaling game" width="600"/>
</p>
<p align="center"><em>Nature chooses between Prisoner's Dilemma and Stag Hunt. Player 1 sees the game and chooses C or D. Player 2 observes only Player 1's action (shown by information sets) and must respond without knowing which game is being played.</em></p>

The challenge: Player 1's optimal action depends on what Player 2 will do, but Player 2's optimal response depends on inferring which game is being played from Player 1's action. Simple Bayesian reasoning fails because Player 1 anticipates Player 2's inference.

<p align="center">
  <img src="../images/08 Communication/B - Talking by doing (signalling games)_cell5_img1.svg" alt="Zero-sum signaling game" width="600"/>
</p>
<p align="center"><em>Two zero-sum games where Player 1 can signal the game type through action choice. If Player 1 always plays B, they average 2.5 regardless of Player 2's response, better than playing each game's Nash equilibrium (which would average 1.5).</em></p>

Separating equilibria reveal information (different actions signal different types), while pooling equilibria hide it (same action regardless of type). Classic examples: education signaling ability (Spence), warranties signaling quality, peacock tails signaling fitness.

---

## C - Doing by Talking II (Speech-Act Theory)

Speech-act theory distinguishes three aspects of speech: locutionary (literal content), illocutionary (speaker intention), and perlocutionary (effect on listener). Grice's cooperative principles govern conversation: Quantity (provide needed information), Quality (be truthful), Relation (be relevant), and Manner (be clear). These principles explain implicature - how "Harry hasn't gone to prison yet" conveys more than its literal meaning.

<p align="center">
  <img src="../images/08 Communication/C- Doing by talking II (speech-act theory)_cell3_img1.svg" alt="Chair ambiguity game" width="600"/>
</p>
<p align="center"><em>Signaling game modeling ambiguous language. Nature determines whether a wooden chair or the meeting chair is coming. The speaker chooses clarity level (costly to be more specific). The listener infers meaning from ambiguous statements. Optimal strategy: be clear for the less likely event, use shorthand for the more likely one.</em></p>

Game-theoretic view: Model conversation as a signaling game where speakers trade off clarity costs against listener comprehension. When the wooden chair is rare, speakers say "the wooden chair..." but shorten to "the chair..." for the common case (meeting chair), with listeners inferring accordingly. The equilibrium minimizes expected communication cost while avoiding costly misunderstandings.

Applications: TRAINS/TRIPS dialog systems, workflow systems with speech acts (report/acknowledge), agent communication languages (XML-based), and rational programming languages where code can make commitments (Agent0, Elephant2000).