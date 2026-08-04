# Collective Certified Robustness against Graph Injection Attacks

**Source**: https://proceedings.mlr.press/v235/lai24a.html

## [POSITIVE] Collective Certification via LP
Certifies a set of target nodes simultaneously by formulating the problem as an optimization over a shared perturbed graph, rather than verifying each node independently.

**Delta**: certified ratio from 0.0% to 81.2% at rho=5% graph size on Citeseer
**Condition**: large attack budgets (large rho); GIA threat model on Cora-ML and Citeseer datasets

**Evidence**: "by solving the LP within 1 minute on the Citeseer dataset, we achieve a significant increase in the certified ratio from 0.0% to 81.2% when the injected node number is 5% of the graph size"

## [NEGATIVE] Sample-wise Certification
Verifies each target node independently, assuming the attacker can craft a different perturbed graph for each node.

**Delta**: 0.0% certified ratio at rho=140 on Citeseer
**Condition**: large attack budgets (large rho); becomes pessimistic as rho grows

**Evidence**: "in the Citeseer dataset, when rho=140, our Collective-LP1 and Collective-LP2 have the certified ratios of 73.0%, and 81.2%, while sample-wise can certify 0.0% nodes"

## [POSITIVE] Customized Linear Relaxation (Collective-LP2)
Introduces an intermediate variable z := A2^T 1_rho to reduce quadratic terms before linearization, requiring only O(rho|T|) extra variables instead of O(rho^2|T|).

**Delta**: +216% certified ratio improvement over Collective-LP1 at pe=0.7, pn=0.9, rho=140 on Cora-ML
**Condition**: large rho; compared to standard LP relaxation (Collective-LP1)

**Evidence**: "in the Cora-ML dataset, when pe=0.7, pn=0.9, and rho=140, Collective-LP2 improves the certified ratio by 216% compared to Collective-LP1"

## [POSITIVE] Standard Linear Relaxation (Collective-LP1)
Replaces quadratic terms in the BQCLP by introducing O(rho^2|T|) slack variables and relaxing binary constraints to [0,1] box constraints.

**Delta**: 73.0% certified ratio vs 0.0% sample-wise at rho=140 on Citeseer
**Condition**: large attack budgets; less efficient than Collective-LP2 for large rho

**Evidence**: "in the Citeseer dataset, when rho=140, our Collective-LP1 and Collective-LP2 have the certified ratios of 73.0%, and 81.2%, while sample-wise can certify 0.0% nodes"

## [NEGATIVE] LP Relaxation Integrality Gap
Relaxing the binary integer quadratic constrained program to LP introduces an integrality gap, causing the LP to overestimate non-robust nodes and underestimate the certified ratio.

**Delta**: approximately 5% decline in certified ratio compared to solving the original BQCLP
**Condition**: small attack budgets (small rho); where sample-wise certificate is still effective

**Evidence**: "the certified ratio of Collective-LP2 undergoes a decline of approximately 5%. This decrease in certified performance is attributed to the sacrifice made in the relaxation process of the LP formulation"

## [POSITIVE] Node-aware Bi-smoothing
Randomized smoothing scheme combining edge deletion smoothing (each edge deleted with probability pe) and node deletion smoothing (each node deleted with probability pn) to build a smoothed classifier.

**Delta**: outperforms baseline
**Condition**: GIA threat model; foundation for both sample-wise and collective certification

**Evidence**: "We adopt node-aware bi-smoothing (Lai et al., 2023), which was proposed to certify against the GIA perturbation, as our smoothed classifier."

## [POSITIVE] GNN Locality Property Exploitation
Leverages the k-hop receptive field property of message-passing GNNs so that injected edges only affect a subset of nodes, enabling collective certification.

**Delta**: outperforms baseline
**Condition**: message-passing GNNs with fixed k layers; enables model-agnostic collective certification

**Evidence**: "we leverage the inherent locality property of GNNs, where the prediction of a node in a k-layer message-passing GNN is influenced solely by its k-hop neighbors. This ensures that injected edges by the attacker only impact a subset of the nodes."

## [POSITIVE] Combining Sample-wise and Collective Certificates
Using both sample-wise and collective certificates together, sharing the same smoothed model to avoid extra computation, to achieve stronger performance across all attack budget sizes.

**Delta**: outperforms baseline
**Condition**: practical deployment; both small and large rho regimes

**Evidence**: "in practical scenarios, we can easily combine the sample-wise and collective certificates with minimal effort to achieve stronger certified performance in both small and large attack budgets. Since the sample-wise and collective models share the same smoothed model, we only need to estimate the smoothing prediction once to avoid extra computation."

## [NEUTRAL] Monte Carlo Smoothing Estimation
Uses N=100,000 Monte Carlo samples to estimate the smoothed classifier probabilities, with Clopper-Pearson confidence intervals and Bonferroni correction at alpha=0.01.

**Delta**: N/A
**Condition**: standard evaluation setup following prior work

**Evidence**: "we employ Monte Carlo to estimate the smoothed classifier with a sample size of N=100,000. We apply the Clopper-Pearson confidence interval with Bonferroni correction to obtain the lower bound of pA and upper bound of pB. We set the confidence level as alpha=0.01."

## [POSITIVE] Worst-case Attacker Assumption for Message Interference
Assumes that if a node receives even a single message from any injected node, its prediction will be altered, overestimating attack impact to ensure soundness of the certificate.

**Delta**: outperforms baseline
**Condition**: theoretical guarantee; applies to all message-passing GNNs

**Evidence**: "The derivation of the robustness certificate relies on a worst-case assumption: in the message-passing process, if a node receives even a single message from any injected node, its prediction will be altered. It is important to note that this assumption exaggerates the impact of the attack, thereby validating the guarantee of the defense."

## [NEGATIVE] Path Independence Assumption for Upper Bound
Assumes independence among paths from injected nodes to target nodes to derive a tractable upper bound on the message interference probability p(Ev).

**Delta**: outperforms baseline
**Condition**: theoretical derivation; introduces looseness in the bound but ensures soundness

**Evidence**: "we have an upper bound for p(Ev) <= p(Ev) by assuming the independence among the paths"

## [NEUTRAL] Random Noise Augmentation Training
Trains the base GNN model with random noise augmentation to improve compatibility with the randomized smoothing certification framework.

**Delta**: N/A
**Condition**: training phase; follows prior work setup

**Evidence**: "We also train the base model with random noise augmentation following (Lai et al., 2023)."
