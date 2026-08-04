# SignSGD with Federated Defense: Harnessing Adversarial Attacks through Gradient Sign Decoding

**Source**: https://proceedings.mlr.press/v235/park24h.html

## [POSITIVE] signSGD with Federated Defense (signSGD-FD)
A novel distributed learning aggregation method that uses weighted majority voting (WMV) with dynamically estimated log-likelihood ratio (LLR) weights, leveraging gradient information from both honest and adversarial workers rather than discarding adversarial contributions.

**Delta**: outperforms baseline
**Condition**: Distributed learning with mixture of honest and adversarial workers, as long as honest workers outnumber adversarial workers

**Evidence**: "Experimental results demonstrate that signSGD-FD achieves superior convergence rates compared to traditional algorithms in various adversarial attack scenarios."

## [POSITIVE] Weighted Majority Voting (WMV) with LLR weights
Aggregation method where the server computes log-likelihood ratio weights for each worker based on estimated cross-over probabilities, then performs weighted majority voting instead of simple majority voting.

**Delta**: outperforms baseline
**Condition**: Server-side gradient aggregation in distributed learning under adversarial attacks

**Evidence**: "the proposed signSGD-FD algorithm can achieve the highest test accuracy compared to other signSGD-style robust optimizers."

## [POSITIVE] Harnessing adversarial worker gradients with negative weights
Instead of discarding gradients from identified adversarial workers, signSGD-FD assigns them negative LLR weights (when estimated cross-over probability exceeds 1/2), effectively flipping their contribution to aid correct decoding.

**Delta**: convergence rate remains invariant under SIA (r=1)
**Condition**: When adversarial workers perform sign inversion attack (r=1) and honest workers outnumber adversarial workers

**Evidence**: "our federated defense mechanism demonstrates that this elimination strategy is notably sub-optimal. To achieve optimal ML decoding performance, it is crucial to utilize the cross-over probabilities of all workers. These probabilities are imperative because the sign of the estimated LLR weights of compromised workers can automatically change if p̂_m,n > 1/2."

## [POSITIVE] Iterative cross-over probability estimation
The server estimates workers' cross-over probabilities by comparing decoded gradient signs with each worker's transmitted signs across all coordinates, updating estimates recursively after an initial phase.

**Delta**: accurate estimation reduces decoding error probability
**Condition**: Server-side weight estimation during training iterations

**Evidence**: "This observation confirms that the accurate p̂_m,n estimation helps to reduce the decoding error probability."

## [POSITIVE] Initial phase WMV aggregation (vs. MV)
During the initial phase, using WMV aggregation (with weights) rather than plain MV aggregation for cross-over probability estimation.

**Delta**: negligible degradation vs. accuracy deterioration with MV
**Condition**: Initial phase of signSGD-FD under sign inversion attack (r=1)

**Evidence**: "the original signSGD-FD using WMV aggregation has negligible degradation due to attacks, but the accuracy deterioration begins to emerge as we employ the MV aggregation. This is expected to result in inaccurate weight estimation in the initial phase because the majority voting is greatly affected by the attack of r=1."

## [NEUTRAL] Initial phase duration T_in selection
The length of the initial phase during which cross-over probabilities are estimated by counting sign errors across all coordinates.

**Delta**: no significant effect unless T_in is too short (e.g., T_in=10)
**Condition**: Initial phase of signSGD-FD; effect is neutral for reasonable T_in values

**Evidence**: "The effect of the initial phase duration can be seen in Figure 4-(b), and this shows us that T_in does not affect significantly unless the duration is not too short to collect the error samples, such as T_in = 10."

## [POSITIVE] Sign quantization (one-bit gradient compression)
Each worker quantizes its locally computed stochastic gradient to only its sign (one bit per coordinate) before transmitting to the server, reducing communication costs.

**Delta**: 30x communication cost reduction vs. Multi-Krum SGD
**Condition**: Communication efficiency in distributed learning

**Evidence**: "The results demonstrate that signSGD-type algorithms can significantly reduce communication costs by 30x compared to the Multi-Krum algorithm."

## [NEGATIVE] Stochastic Sign Flip Attack (SSFA) with r=1/2
Adversarial attack where compromised workers flip gradient signs with probability r=1/2, representing the worst-case attack scenario for signSGD-FD.

**Delta**: exponent term decreases from M/(M-L)
**Condition**: SSFA with r=1/2 applied to L compromised workers

**Evidence**: "when r=1/2, the exponent term decreases from M/(M-L), which slows down the convergence rate. From this result, we also observe that the worst-case attack scenario is to use the sign flip probability of r=1/2."

## [NEGATIVE] Sign Inversion Attack (SIA, r=1) on signSGD-MV
Adversarial attack where compromised workers fully invert their gradient signs; significantly degrades signSGD-MV convergence.

**Delta**: significant degradation of convergence rate for signSGD-MV
**Condition**: signSGD-MV under sign inversion attack with increasing number of adversarial workers

**Evidence**: "Unlike our signSGD-FD method, when r=1, the convergence rate of signSGD-MV is significantly degraded by SSFA because the decoding error bound increases considerably."

## [NEGATIVE] Increasing number of adversarial workers L on signSGD-MV
As the number of compromised workers increases, signSGD-MV test accuracy deteriorates rapidly.

**Delta**: rapid deterioration of test accuracy
**Condition**: signSGD-MV under SIA with increasing L

**Evidence**: "The general trend of results is that signSGD-MV deteriorates significantly as the number of compromised workers L increases, while signSGD-FD can achieve almost the same accuracy as in the absence of attacks if L < M/2."

## [NEGATIVE] signSGD-FD under L >= M/2 adversarial workers
When the number of adversarial workers equals or exceeds the number of honest workers, signSGD-FD fails to converge.

**Delta**: fails to converge at L=9 (M=15)
**Condition**: signSGD-FD when adversarial workers L >= M/2

**Evidence**: "it can be seen that signSGD-FD fails to converge in the L=9 case. This can be considered that the decoding error probability becomes greater than 1/2 in this case, making it no longer possible to perform the accurate p̂_m,n estimation."

## [POSITIVE] BSC coding-theoretical interpretation of gradient signs
Modeling the stochastic gradient sign computation as transmission through binary symmetric channels (BSCs), enabling use of optimal ML decoding (WMV with LLR weights) for gradient aggregation.

**Delta**: enables optimal aggregation and invariant convergence under SIA
**Condition**: Theoretical framework underpinning signSGD-FD design

**Evidence**: "Building upon this novel interpretation, we introduce a progressive weighted majority voting (WMV) method that dynamically adjusts weights throughout iterations."

## [POSITIVE] Recursive cross-over probability update after initial phase
After the initial phase, the server recursively updates cross-over probability estimates per coordinate in parallel, rather than recomputing from scratch.

**Delta**: enables accurate ongoing weight estimation
**Condition**: Post-initial-phase iterations of signSGD-FD

**Evidence**: "After the initial phase t > T_in, the cross-over probability estimation rule is changed to recursively update p̂_m,n in parallel for each coordinate."

## [NEUTRAL] IID data distribution among workers
Each worker is assumed to have the same number of image samples for all classes (IID setting).

**Delta**: not quantified
**Condition**: Experimental setup; results may differ under non-IID conditions

**Evidence**: "The data distribution for workers is assumed to be IID that each worker has the same number of image samples for the entire classes of each dataset."

## [NEGATIVE] Top-K SGD with Multi-Krum defense
Sparsified gradient method selecting top 10% of gradient components, combined with Multi-Krum robust aggregation.

**Delta**: requires 10x more communication costs than signSGD-FD
**Condition**: Communication cost comparison under Gaussian Byzantine attack

**Evidence**: "Top-K SGD-based multi-Krum requires 3x fewer costs than SGD but still needs 10x more costs than our proposed algorithm, which reveals the superiority of signSGD-FD."
