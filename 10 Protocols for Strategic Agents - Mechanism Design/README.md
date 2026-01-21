# Protocols for Strategic Agents - Mechanism Design

Mechanism design is about getting agents to behave in desirable ways. E.g., to be truthful.

While game theory takes games as given and analyzes what agents will do, mechanism design inverts the question: what game should we design to achieve desired outcomes? This is sometimes called "reverse game theory" or "economic engineering."

The classic application is auctions: how do you design an auction so that bidders reveal their true valuations and the item goes to whoever values it most?

An overview of each notebook is given below.

---

## A - Mechanism Design with Unrestricted Preferences

A **mechanism** consists of:
1. A set of possible messages each agent can send
2. An outcome function that maps message profiles to outcomes

A **social choice function** specifies what outcome should occur for each profile of agent preferences. The question: can we design a mechanism that implements this social choice function?

**Implementation in dominant strategies**: The strongest form of implementation. We want truth-telling to be a dominant strategy - optimal regardless of what others do.

**The revelation principle**: Any mechanism can be converted to a direct mechanism where agents simply report their types truthfully. This is a fundamental result that simplifies mechanism design - we only need to consider truthful direct mechanisms.

Because the original mechanism is designed such that agents have dominant strategies there is no reason to lie about your utilities. Lying would imply that you might prefer to play $s'$ instead of $s$, which can't be true.

**Gibbard-Satterthwaite theorem**: With three or more outcomes and unrestricted preferences, the only dominant-strategy implementable social choice functions are dictatorships. This is another impossibility result!

<p align="center">
  <img src="../images/10 Protocols for Strategic Agents - Mechanism Design/A - Mechanism design with unrestricted preferences_cell3_img1.svg" alt="Mechanism design network" width="500"/>
</p>
<p align="center"><em>Network diagram showing a routing mechanism design problem.</em></p>

**Escaping impossibility**:
- Restrict the domain of preferences (e.g., single-peaked preferences)
- Use money/transfers (Vickrey-Clarke-Groves mechanisms)
- Weaken the solution concept (Nash implementation instead of dominant strategies)
- Accept approximate truthfulness

Of course, saying something like *if both players prefer A then they get A* is just more social choice bogus. A more sensible way to think about it is that we have our own utility function that depends on the success of the players.

**Vickrey auction**: A second-price sealed-bid auction where the highest bidder wins but pays the second-highest bid. Truthful bidding is a dominant strategy! This is a special case of the VCG mechanism.

**VCG (Vickrey-Clarke-Groves) mechanisms**: A general class of mechanisms that are:
- Dominant-strategy incentive compatible (truthful)
- Efficient (maximize social welfare)
- Individually rational (agents willingly participate)

The key: each agent pays their "externality" - the harm they impose on others by participating.

The notebook implements several mechanism design examples showing when truthful implementation is possible and when it breaks down.