# Towards Optimal Adversarial Robust Q-learning with Bellman Infinity-error

**Source**: https://proceedings.mlr.press/v235/li24cl.html

## [POSITIVE] Consistency Assumption of Policy (CAP)
An assumption that optimal actions of all states within the MDP exhibit consistency despite adversarial disturbance, meaning adversaries cannot alter the essence of state observations (the intrinsic state).

**Delta**: enables proof of ORP existence and alignment with Bellman optimal policy
**Condition**: Theoretical foundation for SA-MDP; empirically validated against FGSM and PGD attacks where the state set violating CAP is nearly empty

**Evidence**: "Building upon CAP, we crucially prove the existence of a deterministic and stationary ORP that aligns with the Bellman optimal policy."

## [POSITIVE] Bellman Infinity-error (L∞-norm) Minimization
Minimizing the Bellman error in the L∞ norm space rather than L1 or L2, which theoretically guarantees adversarial robustness by bounding ∥Q - Q*∥∞.

**Delta**: µ(S_adv^Q) = 2ε + O(δ) vs µ(S_adv^Q) = µ(S) for L^p with p < ∞
**Condition**: Adversarial robustness in value-based DRL; applies when ∥Q - Q*∥∞ ≤ δ for sufficiently small δ

**Evidence**: "the second statement points out that through minimizing ∥Q − Q∗∥ in the L∞-norm space, we can avoid the vulnerability and attain a policy with both natural and robust capabilities."

## [NEGATIVE] L1-norm Bellman Error (conventional DRL)
Standard deep Q-learning objective minimizing Bellman error under L1 (or equivalently L^p for finite p) norm, as used in DQN and related algorithms.

**Delta**: µ(S_adv^Q) = µ(S), i.e., adversarial examples exist near almost all states
**Condition**: Conventional DRL training without adversarial robustness objectives; results in poor robustness despite good natural performance

**Evidence**: "For any 1 ≤ p < ∞ and δ > 0, there exists a function Q ∈ L^p(S × A) satisfying ∥Q − Q∗∥p ≤ δ such that µ(S_sub^Q) = O(δ) yet µ(S_adv^Q) = µ(S)."

## [POSITIVE] CAR-DQN (Consistent Adversarial Robust DQN)
A DQN variant that minimizes a surrogate objective of Bellman Infinity-error using a soft L∞ seminorm, built on Double Dueling DQN, to achieve both natural and robust performance.

**Delta**: 110% higher reward on RoadRunner vs SA-DQN (PGD); 60% higher robust rewards under MinBest attack on Freeway
**Condition**: Atari game benchmarks (Pong, Freeway, BankHeist, RoadRunner) with perturbation radius ε=1/255

**Evidence**: "CAR-DQN (PGD) outperforms SA-DQN (PGD) in all metrics and achieves remarkably better robustness (110% higher reward) on RoadRunner. CAR-DQN (cov) outperforms baselines in a majority of cases."

## [POSITIVE] Soft CAR Objective with Coefficient λ
A soft version of the CAR loss that assigns differentiated weights to samples in a batch, controlled by coefficient λ, to fully utilize each sample rather than only using the worst-case sample.

**Delta**: λ=1 achieves ~49500 natural and ~48230 PGD return on RoadRunner vs ~25160 and ~24540 for λ=0
**Condition**: RoadRunner environment; optimal range 0.5 ≤ λ ≤ 10; λ=0 causes poor performance on complex games due to inadequate sample utilization

**Evidence**: "the agents exhibit similar capabilities when 0.5 ≤ λ ≤ 10, indicating that the learned policies are not sensitive to the soft coefficient within this range."

## [NEGATIVE] λ=0 (Hardest Sample Only)
Setting soft coefficient to 0, which uses only the sample with the largest adversarial TD-error from a batch, equivalent to a hard L∞ approximation.

**Delta**: ~25160 natural return and ~24540 PGD return on RoadRunner vs ~49500 and ~48230 for λ=1
**Condition**: Complex environments like RoadRunner; works adequately on simpler games (Pong, BankHeist, Freeway)

**Evidence**: "In the RoadRunner, the case λ = 0 yields poor performance, achieving returns around 25000 due to inadequate utilization of the samples."

## [NEGATIVE] λ=∞ (Uniform Averaging over Batch)
Setting soft coefficient to infinity, which averages over all samples in a batch equally, equivalent to L1/L2 norm behavior.

**Delta**: worse robustness compared to intermediate λ values; ~36760 PGD return on RoadRunner vs ~48230 for λ=1
**Condition**: All Atari environments tested; particularly notable degradation on RoadRunner

**Evidence**: "The case λ = ∞ results in worse robustness compared to other cases with differentiated weights. This suggests that each sample in a batch plays a distinct role in robust training."

## [POSITIVE] PGD Solver for Inner Optimization
Using Projected Gradient Descent to solve the inner maximization problem in the CAR-DQN objective, providing a lower bound surrogate of the loss.

**Delta**: CAR-DQN (PGD) achieves ~45000 return on RoadRunner, outperforming SA-DQN (PGD)
**Condition**: PGD solver provides lower bound surrogate; relatively weaker ACR compared to convex relaxation solver

**Evidence**: "our proposed loss function coupled with the PGD solver, achieves a remarkable return of around 45000 on the RoadRunner environment, outperforming the SA-DQN with the PGD approach."

## [POSITIVE] IBP/Convex Relaxation Solver for Inner Optimization
Using Interval Bound Propagation (cheap convex relaxation) to solve the inner optimization in the CAR-DQN objective, providing an upper bound surrogate of the loss.

**Delta**: CAR-DQN (conv) achieves best natural reward on BankHeist (1349.6) and RoadRunner (49398) among convex relaxation methods
**Condition**: Convex relaxation group comparison; IBP gives upper bound which better ensures ACR certification

**Evidence**: "CAR-DQN (cov) outperforms baselines in a majority of cases."

## [NEUTRAL] Double Dueling DQN Architecture
CAR-DQN is implemented on top of Double Dueling DQN as the base architecture.

**Delta**: not separately quantified
**Condition**: Base architecture choice; effect relative to other architectures not ablated

**Evidence**: "We implement CAR-DQN based on Double Dueling DQN (Van Hasselt et al., 2016; Wang et al., 2016)"

## [NEUTRAL] Huber Loss Replacement for Absolute Value
Using Huber loss instead of the absolute value function in the CAR-DQN objective for numerical stability.

**Delta**: not separately quantified
**Condition**: Implementation detail for numerical stability; no ablation provided

**Evidence**: "We use Huber loss to replace the absolute value function"

## [POSITIVE] Gradual Perturbation Schedule (ε Annealing)
Increasing the attack perturbation ε from 0 to 1/255 over the first 4 million training steps, then continuing with fixed ε for 0.5 million steps.

**Delta**: consistent with prior work; enables stable convergence
**Condition**: Training schedule for all robust DQN methods; standard practice in the field

**Evidence**: "We increase the attack ε from 0 to 1/255 in the first 4 million steps using the same smoothed schedule as in Zhang et al. (2020); Oikarinen et al. (2021); Liang et al. (2022), and then continue training with a fixed ε for the remaining 0.5 million steps."

## [POSITIVE] CAR Operator (Tcar)
A novel consistent adversarial robust operator for computing the adversarial Q function, whose fixed point under CAP is exactly Q*, enabling theoretical proof of ORP existence.

**Delta**: proves Q* = Q^(π*∘ν*(π*)), establishing ORP = Bellman optimal policy
**Condition**: Theoretical tool; requires CAP to hold; not directly contractive but convergent in smooth environments

**Evidence**: "under CAP, we identify its fixed point as exactly Q∗, thereby proving the existence of a deterministic and stationary ORP."

## [NEGATIVE] KL-based Regularization (SA-DQN baseline)
Prior method using KL divergence regularization to balance robustness and natural returns, without theoretical guarantees for ORP.

**Delta**: SA-DQN (PGD) achieves ~20482 PGD return on RoadRunner vs ~43286 for CAR-DQN (PGD)
**Condition**: Compared against CAR-DQN on Atari benchmarks; SA-DQN training costs ~27 hours vs ~14 hours for CAR-DQN

**Evidence**: "the robust curves of SA-DQN and WocaR-DQN on BankHeist tend to decline. This discrepancy primarily stems from their robustness objectives, which diverge from the standard training loss and consequently result in learning sub-optimal actions."

## [NEGATIVE] L2-norm Bellman Error
Training DQN agents using Bellman error under L2 norm as an intermediate case between L1 and L∞.

**Delta**: near-zero PGD return on RoadRunner (0±0) vs ~48230 for L∞
**Condition**: Ablation study on Atari games; consistent with Theorem 5.1 predictions

**Evidence**: "all agents perform well without attacks in the four games. However, the performance of (1, d^π_µ0)-norm and (2, d^π_µ0)-norm agents highly degrades under strong attacks, receiving episode rewards close to the lowest in each game."
