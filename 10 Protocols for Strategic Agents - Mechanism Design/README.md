# Protocols for Strategic Agents - Mechanism Design

Mechanism design is about getting agents to behave in desirable ways. E.g., to be truthful. While game theory analyzes existing games, mechanism design inverts the question: what game should we design to achieve desired outcomes?

---

## A - Mechanism Design with Unrestricted Preferences

A mechanism consists of messages agents can send and an outcome function. A social choice function specifies what outcome should occur for each preference profile. Can we design a mechanism that implements this?

Implementation in dominant strategies: Truth-telling is optimal regardless of what others do.

The revelation principle: Any mechanism can be converted to a direct mechanism where agents report types truthfully. Because the original mechanism is designed such that agents have dominant strategies there is no reason to lie.

Gibbard-Satterthwaite theorem: With three or more outcomes and unrestricted preferences, the only dominant-strategy implementable social choice functions are dictatorships. Another impossibility result!

Escaping impossibility: Restrict preference domains, use money/transfers (VCG mechanisms), weaken solution concept, or accept approximation.

Vickrey auction: Second-price sealed-bid where highest bidder pays second-highest bid. Truthful bidding is dominant!

<p align="center">
  <img src="../images/10 Protocols for Strategic Agents - Mechanism Design/A - Mechanism design with unrestricted preferences_cell3_img1.svg" alt="Mechanism design example" width="500"/>
</p>
<p align="center"><em>Visual representation of mechanism design concepts.</em></p>

VCG (Vickrey-Clarke-Groves) mechanisms: Dominant-strategy incentive compatible, efficient, and individually rational. Each agent pays their "externality" - the harm they impose on others.

Of course, saying something like *if both players prefer A then they get A* is just more social choice bogus. A more sensible way to think about it is that we have our own utility function that depends on the success of the players.