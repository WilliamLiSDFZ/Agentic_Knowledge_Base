# Safe and Robust Subgame Exploitation in Imperfect Information Games

**Source**: https://proceedings.mlr.press/v235/ge24b.html

## [POSITIVE] Adaptation Safety
A redefined safety concept requiring that the exploitation strategy should be no more exploitable than the blueprint strategy, rather than benchmarking against Nash Equilibrium. Formally, exp(σ') ≤ exp(σ) for any blueprint σ.

**Delta**: outperforms baseline
**Condition**: Two-player zero-sum games where exact Nash Equilibrium is computationally infeasible

**Evidence**: "OX-Search consistently demonstrates lower exploitability compared to the blueprint strategy in both Leduc Hold'em and FHP. This suggests that the strategies derived from OX-Search are less vulnerable to worst-case opponents, thereby enhancing the safety of our opponent exploitation approach."

## [POSITIVE] OX-Search Framework
Opponent-eXploitation Search framework that integrates real-time search techniques for online opponent exploitation, maximizing exploitation against estimated opponent distribution while satisfying adaptation safety constraints at each infoset.

**Delta**: outperforms baseline
**Condition**: Online opponent exploitation in Leduc Hold'em and Flop Hold'em Poker

**Evidence**: "Empirical evaluations in popular poker games demonstrate OX-Search's superiority in both exploitability and exploitation compared to previous methods."

## [POSITIVE] Gadget Game Construction
A specialized gadget game that transforms the OX-Search optimization problem into a Nash Equilibrium finding problem, enabling use of advanced equilibrium-finding algorithms like CFR instead of Linear Programming. The game duplicates the subgame into two parts with a chance node root.

**Delta**: outperforms baseline
**Condition**: Large-scale games where LP is computationally inefficient

**Evidence**: "In order to expedite the strategy-solving process and make it compatible with advanced equilibrium-finding algorithms for extensive-form games, we need to construct a gadget game, in which the NE is the solution to objective (1) and constraint (2)... this solution can be computed efficiently in real-time, as evidenced by prior research."

## [POSITIVE] Nested OX-Search Application
Iteratively applying OX-Search at each newly encountered information set in a nested fashion, allowing continuous strategy refinement while maintaining adaptation safety.

**Delta**: outperforms baseline
**Condition**: Sequential decision-making where multiple subgames are encountered

**Evidence**: "To further exploit the opponent and amplify profit, players can employ OX-Search repeatedly at each newly encountered information set in a nested fashion, which maintains adaptation safety at the same time. The iterative use of OX-Search enables the player to continuously refine its strategy and exploit opportunities for higher payoff."

## [POSITIVE] Safety Constraints at Infosets
Per-infoset safety constraints ensuring CBV1^σ(I1_i) - CBV1^σ2^S(I1_i) ≥ 0 for all opponent infosets at the top of the subgame, preventing the refined strategy from decreasing expected payoff against optimal opponents.

**Delta**: outperforms baseline
**Condition**: Subgame solving with adaptation safety requirements

**Evidence**: "The safety constraints (2) are commonly used in safe subgame solving methods, and they ensure that the refined strategy σ2^S does not decrease the expected payoff against optimal opponent at each opponent's infoset. Additionally, the constraints prevent the opponent from gaining an advantage through altering its reach probability over I1_i."

## [POSITIVE] Lagrange Multiplier Reformulation with β Bound
Reformulating the constrained OX-Search optimization using Lagrange multipliers bounded by β, enabling the gadget game construction and allowing player 1's strategy to represent the optimal multiplier during equilibrium finding.

**Delta**: outperforms baseline
**Condition**: Gadget game construction for OX-Search

**Evidence**: "To facilitate the construction of the gadget game, similar to (Davis et al., 2019), we operate under the assumption that λ is upper-bounded, i.e., ∀i, λi ≤ β. This allows us to rewrite Equation (5)... we can treat λ as player 1's strategy for selecting each information set I1_i, and the optimal λ can be identified during the equilibrium-finding process."

## [POSITIVE] Increasing β Value Detection
A mechanism to detect when the optimal Lagrange multiplier lies outside [0,β]^k by checking if player 1 enters with 100% probability at any option node, and increasing β accordingly to maintain adaptation safety.

**Delta**: outperforms baseline
**Condition**: Cases where safety constraints may be violated due to insufficient β

**Evidence**: "Fortunately, we can identify this by examining player 1's NE at each option node and increasing the value of β if player 1 chooses to enter with a 100% probability (or very close, in the case of an approximate NE) at some option nodes, as outlined in Theorem 4.5."

## [POSITIVE] Finer-grained Abstraction in Subgame Solving
Using a finer-grained abstraction (400 buckets per public betting history) for subgame solving in Flop Hold'em Poker compared to the blueprint abstraction (200 buckets), enabling more precise opponent exploitation.

**Delta**: outperforms baseline
**Condition**: Flop Hold'em Poker with abstraction-based subgame solving

**Evidence**: "While the SES was able to reduce exploitability in FHP, it was less effective in Leduc Hold'em. This disparity in performance can be attributed to our use of a finer-grained abstraction in FHP for subgame solving, whereas in Leduc Hold'em, we implemented the strategy without employing any form of abstraction."

## [NEUTRAL] No Abstraction in Leduc Hold'em
Applying OX-Search without any abstraction technique in Leduc Hold'em, which limits the performance improvement compared to FHP where finer-grained abstraction is used.

**Delta**: lower improvement than FHP
**Condition**: Small-scale Leduc Hold'em game

**Evidence**: "This disparity in performance can be attributed to our use of a finer-grained abstraction in FHP for subgame solving, whereas in Leduc Hold'em, we implemented the strategy without employing any form of abstraction."

## [NEGATIVE] Exploitation Level Hyperparameter (SES/RNR baseline)
SES and Real-time RNR require a hyperparameter to control the level of exploitation, set to 0.3 in experiments as it yields best performance with inaccurate opponent models.

**Delta**: worse than OX-Search
**Condition**: SES and Real-time RNR baselines in Leduc Hold'em and Flop Hold'em Poker

**Evidence**: "SES requires a hyperparameter to control the level of exploitation. Identifying an optimal hyperparameter can be daunting, thereby potentially restricting the practical utility of SES... the strategy resulting from this combination may not necessarily be safer than the blueprint strategy, nor surpass the efficacy of previous strategies against the opponent."

## [NEGATIVE] Real-time RNR with Modeling Errors
Real-time search variant of p-Restricted Nash Response, which assumes the opponent follows the modeled strategy with probability p and becomes increasingly vulnerable as modeling errors grow.

**Delta**: performance significantly deteriorates with increasing errors
**Condition**: High estimation error scenarios in Leduc Hold'em and Flop Hold'em Poker

**Evidence**: "RNR shows an increase in exploitability concurrent with rising modeling errors, likely due to its assumptions about the opponent's behavior in the remainder of the subgame and its vulnerability to modeling inaccuracies... While RNR demonstrates better exploitation in Leduc Hold'em under conditions of minor modeling errors, its performance significantly deteriorates with increasing errors."

## [NEGATIVE] OX-Search Safety Constraints Against Weaker Opponents
The inherent safety constraints of OX-Search limit aggressive exploitation of weaker opponents compared to SES and Real-time RNR, trading off maximum exploitation for guaranteed safety.

**Delta**: lower exploitation than SES and RNR against weak opponents
**Condition**: Weaker opponents with PRshuffle = 0.4, 0.6, 0.8 in Leduc Hold'em

**Evidence**: "due to its inherent safety constraints, OX-Search could not exploit these opponents as aggressively as SES and Real-time RNR could, despite achieving notable utility improvements over the blueprint."

## [POSITIVE] Monte Carlo CFR Blueprint Training
Using Monte Carlo CFR to precompute the blueprint strategy offline (1,000,000 iterations for Leduc Hold'em, 100,000 for FHP), which serves as the initial strategy for OX-Search refinement.

**Delta**: outperforms baseline
**Condition**: Offline blueprint computation for both Leduc Hold'em and Flop Hold'em Poker

**Evidence**: "In contexts with a stronger blueprint, OX-Search uniquely managed to maintain safety and achieve utility improvements even with significant estimation errors (e.g., error = 1), showcasing its robustness and safety-oriented design."

## [POSITIVE] Infoset Clustering Abstraction for Blueprint (FHP)
Clustering infosets into 200 buckets per public betting history for the blueprint in Flop Hold'em Poker using abstraction techniques to handle the large state space.

**Delta**: outperforms baseline
**Condition**: Large-scale Flop Hold'em Poker game

**Evidence**: "In the case of Flop Hold'em Poker, the blueprint is solved by Monte Carlo CFR for 100,000 iterations, incorporating the abstraction technique (Johanson et al., 2013) at the flop turn. For each public betting history, the infosets are clustered into 200 buckets."

## [POSITIVE] Robust Exploitation Under Modeling Errors
OX-Search's theoretical guarantee that applying it elevates expected payoff by at least (1-ε)δ even when opponent model has estimation error ε, providing robustness against inaccurate opponent models.

**Delta**: outperforms baseline
**Condition**: Scenarios with inaccurate opponent models in both Leduc Hold'em and Flop Hold'em Poker

**Evidence**: "OX-Search maintains comparable performance to SES in Leduc Hold'em and outperforms both SES and RNR in FHP... these results suggest that OX-Search is not only as or more efficient in exploitation as other methods but also maintains its non-exploitability in worst-case scenarios."
