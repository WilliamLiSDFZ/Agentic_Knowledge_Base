# Adversarial Attacks on Combinatorial Multi-Armed Bandits

**Source**: https://proceedings.mlr.press/v235/balasubramanian24a.html

## [POSITIVE] Polynomial Attackability Definition
Redefining attackability for CMAB to require attack cost that is both sublinear in time horizon T and polynomial in number of base arms m, rather than allowing exponential dependence on m as in vanilla MAB attackability

**Delta**: reduces attack cost bound from exponential in m to polynomial in m
**Condition**: When analyzing attackability of CMAB instances with exponentially many super arms

**Evidence**: "Directly applying the MAB concept of attackability to CMAB is tempting... However, it leads to a sublinear cost bound in T but exponential in the number of base arms m. This approach follows the same attack strategy as in MAB. However, in practice, the exponential cost in m is undesirable, and can even exceed T, resulting in vacuous results."

## [POSITIVE] Algorithm 1: Zero-Out Non-Target Base Arms
Attack algorithm that sets outcomes of base arms not associated with the target super arm to 0, effectively making the target super arm appear optimal to the CUCB algorithm

**Delta**: attack cost bounded by poly(m, K, 1/p, 1/Δ)·log(T) when victim is CUCB
**Condition**: When CMAB instance is polynomially attackable (ΔM > 0) and environment parameters are known

**Evidence**: "The main idea is to reduce the reward of base arms that are not associated with the target super arms to 0... If we specify the victim algorithm to be CUCB... the attack cost can be bounded by poly(m, K, 1/p, 1/Δ)·log(T)."

## [POSITIVE] Gap Condition (ΔM > 0) as Sufficient Attackability Criterion
Using the sign of the gap ΔM (difference between target super arm reward and optimal reward under masked mean vector) as a sufficient and necessary condition for polynomial attackability

**Delta**: provides exact characterization: ΔM > 0 implies attackable, ΔM < 0 implies unattackable
**Condition**: Known environment setting for any CMAB instance satisfying Monotonicity and 1-Norm TPM Bounded Smoothness assumptions

**Evidence**: "Theorem 3.6: Given a particular CMAB instance and the target set of super arms M to attack. If ΔM > 0, then the CMAB instance is polynomially attackable. If ΔM < 0, the instance is polynomially unattackable."

## [POSITIVE] CUCB with Greedy Oracle for PMC Attackability
Using CUCB algorithm paired with a Greedy approximation oracle for the Probabilistic Maximum Coverage problem, showing the greedy oracle acts like an exact oracle when observations are sufficient

**Delta**: PMC with CUCB+Greedy is polynomially attackable when ΔM > 0; experimentally cost grows sublinearly while target arm pulls grow linearly
**Condition**: Probabilistic Maximum Coverage problem solved with CUCB and Greedy oracle

**Evidence**: "The intuition of the proof is that although the Greedy oracle is an approximation oracle, by using CUCB, it 'acts' like an exact oracle when the number of observations for each base arm is large enough, and thus we can follow the proof idea for Theorem 3.6."

## [NEGATIVE] Unknown Environment (Black-Box) Attack Setting
Adversary attempts to attack CMAB without knowledge of environment parameters μ, relying only on observed outcomes

**Delta**: can require exponential cost 1/ε^Ω(m) in hard instances, making polynomial attack impossible
**Condition**: Hard CMAB instances in unknown/black-box environment settings

**Evidence**: "we discovered that for the same CMAB instance, polynomial attackability is not always the same, but is conditioned on whether the bandit environment is known or unknown to the adversary... the instance is polynomially attackable if the environment is known to the adversary but polynomially unattackable if it is unknown to the adversary in advance."

## [NEGATIVE] Hard Example Construction for Unknown Environment
Constructing a specific CMAB instance with 2n base arms and n+2 super arms that blocks simultaneous exploration, requiring exponential cost to attack in unknown environment

**Delta**: attack cost at least 1/ε^Ω(n) = 1/ε^Ω(m) in unknown environment, violating polynomial attackability
**Condition**: Specific hard CMAB instance Ii in unknown environment with CUCB algorithm

**Evidence**: "the total cost is at least 1/ε^Ω(n) = 1/ε^Ω(m) since m = 2n... This hardness result suggests that adversarial attacks on CMAB may be extremely difficult in practice and a general attack strategy for any CMAB instance does not exist since the environment is usually unknown to the adversary."

## [POSITIVE] Reduction of Episodic RL to CMAB Attackability
Reducing white-box episodic reinforcement learning reward poisoning attacks to CMAB framework, enabling instance-level attackability characterization for RL

**Delta**: first instance-level attackability result on reinforcement learning
**Condition**: Episodic RL with known transition probabilities (white-box setting)

**Evidence**: "our work... get the first 'instance'-level attackability result on reinforcement learning... the simple version of episodic RL (white-box) is reduced to CMAB, and one can also verify that Assumption 2.1 and Assumption 2.2 hold."

## [NEUTRAL] Exclusion of (α,β)-Approximation Oracle from General Attackability
Deliberately not considering (α,β)-approximation oracles in the general attackability framework because algorithms with (α,β)-regret are not no-regret algorithms and can be made unattackable trivially

**Delta**: prevents general characterization but avoids vacuous results; requires case-by-case analysis per application
**Condition**: CMAB instances solved with approximation oracles

**Evidence**: "The fundamental problem for algorithms with (α,β)-regret is that the algorithms are not 'no-regret' algorithms... it is always possible to change an (α,β)-oracle to (α,β−ε)-oracle by applying the original oracle with probability 1−ε and do the random exploration with probability ε, which would make the problem unattackable."

## [NEGATIVE] Extended Target Set Heuristic for Influence Maximization Attack
Attack heuristic for online influence maximization that avoids attacking edges within distance ℓ of target nodes, parameterized by ℓ to balance attack scope

**Delta**: no target arm pulled for majority of experiment across ℓ=1,2,3; no increasing trend in target node selection unlike PMC
**Condition**: Online influence maximization with IMM (α,β)-approximation oracle

**Evidence**: "for the online influence maximization problem, the algorithm selects none or 20% of the target node set for ℓ=1,2,3 for a majority of the experiment, and there is no trend indicating that the number of target nodes selected would increase... This finding corroborates our claim that when the oracle for a CMAB instance is not exact (α-approximation oracle), we need to analyze the instance case by case."

## [POSITIVE] 1-Norm TPM Bounded Smoothness Assumption
Standard CMAB assumption bounding the difference in expected reward between two distributions by the 1-norm of their mean vector differences weighted by triggering probabilities

**Delta**: enables regret upper bounds and attack cost analysis for general CMAB
**Condition**: Required for CUCB regret bounds and attack cost analysis across all CMAB applications

**Evidence**: "Assumption 2.2 (1-Norm TPM Bounded Smoothness). For any two distributions D, D′ with expectation vectors µ and µ′ and any super arm S ∈ S, there exists a B ∈ R+ such that [smoothness bound]... When combined with the two assumptions above, a legitimate CUCB algorithm's regret... can typically be upper bounded."

## [NEUTRAL] Probabilistically Triggered Arms Model
CMAB model where selecting a super arm triggers only a random subset of base arms for observation, generalizing standard semi-bandit feedback

**Delta**: introduces p* dependency in attackability bounds; p* may be exponentially small requiring separate analysis
**Condition**: CMAB instances with probabilistically triggered base arms

**Evidence**: "In general, the probability p* may be exponentially small, and there already exists analysis for the combinatorial semi-bandit (Wang & Chen, 2017) that can remove this p* dependence. However, there are still some differences between the original CMAB setting and our attack setting. The following example shows the necessity of the term p*."

## [NEUTRAL] Reward Poisoning as Threat Model (vs. Environment/Action Poisoning)
Focusing exclusively on reward poisoning attacks where adversary modifies observed base arm outcomes, rather than environment poisoning or action poisoning

**Delta**: limits generalizability; environment poisoning is more powerful and would invalidate ΔM analysis
**Condition**: Applies to reward poisoning threat model only; does not extend to environment poisoning

**Evidence**: "One limitation of our findings is that our attackability characterization is limited to one threat model: reward poisoning attacks. The characterization cannot be directly generalized to environment poisoning attacks... Environment poisoning is more powerful than reward poisoning and perturbation in environment will invalidate our analysis regarding ΔM."
