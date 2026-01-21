# Communication

So far we've assumed agents observe actions but don't communicate directly. But in many scenarios, agents can talk before or during the game. Does this change outcomes?

The answer is subtle: sometimes communication helps, sometimes it doesn't, and sometimes it's just "cheap talk" with no effect. This section explores when and how communication matters in strategic settings.

An overview of each notebook is given below.

---

## A - Doing by Talking I (Cheap Talk)

Does communication before the game change things? For Prisoner's Dilemma: well, no. Regardless of what both players say, they will each still choose to defect. Any talk about cooperating is cheap and non-credible.

**Cheap talk** is communication that's costless and non-binding. The key question: when does cheap talk affect equilibrium outcomes?

**Crawford-Sobel result**: In sender-receiver games, cheap talk can transmit information only if the sender's and receiver's interests are sufficiently aligned. With conflicting interests, communication becomes uninformative babbling.

The notebook includes visualizations of extensive-form games with communication stages:

<p align="center">
  <img src="../images/8 Communication/A - Doing by talking I (cheap talk)_cell3_img1.svg" alt="Cheap talk game 1" width="500"/>
</p>

<p align="center">
  <img src="../images/8 Communication/A - Doing by talking I (cheap talk)_cell5_img1.svg" alt="Cheap talk game 2" width="500"/>
</p>
<p align="center"><em>Game trees with pre-play communication stages (cheap talk).</em></p>

**Coordination with cheap talk**: In games with multiple equilibria (like Battle of the Sexes), cheap talk can help players coordinate on a particular equilibrium. If both players say "let's go to the opera" and both prefer coordination to miscoordination, this becomes self-fulfilling.

You can see that doing the opposite of what was said is an equilibrium too... How confusing!

Giotto's thought: In truth, communication is probably only an applicable concept in some kind of repeated-game.

---

## B - Talking by Doing (Signalling Games)

**Signalling games** involve players with private information choosing actions that reveal (signal) something about their type. Unlike cheap talk, signals are costly or binding, making them credible.

Classic examples:
- **Education as a signal**: Even if education doesn't increase productivity, it might signal innate ability if high-ability workers find it less costly to obtain
- **Warranty offers**: A company offering a long warranty signals confidence in product quality
- **Peacock tails**: Costly displays signal genetic fitness

The notebook formalizes this with **Bayesian signaling games**:
1. Nature draws a type for player 1 (informed player)
2. Player 1 observes their type and chooses a signal
3. Player 2 observes the signal (but not the type) and chooses an action
4. Payoffs are realized

<p align="center">
  <img src="../images/8 Communication/B - Talking by doing (signalling games)_cell3_img1.svg" alt="Signaling game 1" width="500"/>
</p>

<p align="center">
  <img src="../images/8 Communication/B - Talking by doing (signalling games)_cell5_img1.svg" alt="Signaling game 2" width="500"/>
</p>
<p align="center"><em>Signaling games showing information asymmetry and belief updating.</em></p>

**Separating vs pooling equilibria**:
- **Separating**: Different types choose different signals, fully revealing information
- **Pooling**: All types choose the same signal, revealing nothing
- **Semi-separating**: Partial information revelation

Which equilibrium emerges depends on beliefs and costs. The notebook explores when each type of equilibrium exists.

---

## C - Doing by Talking II (Speech-Act Theory)

**Speech-act theory** (from philosophy) studies how utterances can perform actions. Saying "I promise" doesn't just describe - it creates a commitment.

In game theory terms, some communication is:
- **Self-committing**: The act of saying something binds you to a course of action
- **Self-revealing**: Your statement credibly reveals private information

Examples:
- Burning bridges to commit to an aggressive strategy
- Public announcements that create reputational costs if violated
- Contracts that become enforceable once signed

<p align="center">
  <img src="../images/8 Communication/C- Doing by talking II (speech-act theory)_cell3_img1.svg" alt="Speech act game" width="500"/>
</p>
<p align="center"><em>Game with speech acts that commit or reveal information.</em></p>

The notebook explores:
- When can players credibly commit through communication?
- How do commitment opportunities change equilibria?
- What institutions make commitments credible (courts, reputation, etc.)?

**Connection to mechanism design**: Designing communication protocols is related to designing games. We can create institutions that make certain types of communication credible and valuable.