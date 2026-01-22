# Protocols for Strategic Agents - Mechanism Design

Mechanism design is about getting agents to behave in desirable ways. E.g., to be truthful. While game theory analyzes existing games, mechanism design inverts the question: what game should we design to achieve desired outcomes?

---

## A - Mechanism Design with Unrestricted Preferences

A mechanism consists of messages agents can send and an outcome function. A social choice function specifies what outcome should occur for each preference profile. Can we design a mechanism that implements this?

The revelation principle: Any mechanism can be converted to a direct mechanism where agents report types truthfully. Because the original mechanism is designed such that agents have dominant strategies there is no reason to lie.

Vickrey auction: Second-price sealed-bid where highest bidder pays second-highest bid. Truthful bidding is dominant!