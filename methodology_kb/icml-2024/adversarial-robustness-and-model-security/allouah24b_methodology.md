# The Privacy Power of Correlated Noise in Decentralized Learning

**Source**: https://proceedings.mlr.press/v235/allouah24b.html

## [POSITIVE] Pairwise-Canceling Correlated Gaussian Noise
Connected users securely exchange randomness seeds to generate pairwise-canceling correlated Gaussian noise terms (v_ij = -v_ji) injected before gossip averaging to protect local models

**Delta**: matches CDP optimal privacy-utility trade-off, n times better than LDP
**Condition**: arbitrary connected graphs under SecLDP against external eavesdropper and non-colluding curious users

**Evidence**: "DECOR matches the central DP optimal privacy-utility trade-off... this improves by factor n over the trade-off achieved by LDP algorithms"

## [POSITIVE] Uncorrelated Gaussian Noise (CDP noise)
Independent Gaussian noise v_i ~ N(0, sigma_cdp^2 I_d) added to protect the gossip-averaged local model after averaging

**Delta**: drives dominant convergence terms with sigma_cdp^2 = O(1/n) dependence matching CDP
**Condition**: applied at every iteration alongside correlated noise

**Evidence**: "sigma_cdp^2 drives the dominant convergence terms, so its dependence on n is crucial"

## [POSITIVE] Gradient Clipping
Clipping stochastic gradients at threshold C (Clip(g;C) = min(1, C/||g||)*g) to bound sensitivity for differential privacy

**Delta**: enables DP guarantees by bounding gradient sensitivity
**Condition**: required for DP guarantees; bounded gradient assumption used to ignore clipping effect in analysis

**Evidence**: "The clipping operation ensures that the sensitivity of the gradient, to a change in data, is bounded as required by DP."

## [POSITIVE] SecLDP Privacy Framework
New relaxation of local DP that protects communications against external eavesdroppers and curious users assuming every pair of connected users shares a secret (randomness seed)

**Delta**: achieves CDP-level privacy-utility trade-off vs n times worse under LDP
**Condition**: requires every pair of connected users to share a secret; one round of encrypted communication for seed exchange

**Evidence**: "the best achievable mean squared error under LDP is n times worse than under CDP... DECOR matches the optimal CDP privacy-utility trade-off, under SecLDP against both an external eavesdropper and non-colluding curious users"

## [POSITIVE] SecRDP Privacy Accountant (Algorithm 2)
Practical privacy accounting method computing tight per-step SecRDP bounds by inverting a modified graph Laplacian matrix

**Delta**: provides tighter bounds than theoretical Theorem 1 for practical use
**Condition**: used for practical deployment; efficient for large sparse graphs via Laplacian solvers

**Evidence**: "The theoretical privacy bound from Theorem 1 may be too loose for practical use. Thus, we devise a privacy accounting method, described in Algorithm 2, which allows computing tight privacy bounds for a single step of DECOR."

## [NEGATIVE] Correlated Noise Accumulation on Sparse Graphs
On sparse graphs, correlated noise terms do not fully cancel after gossip averaging, leading to residual noise accumulation across iterations proportional to H_G(W)

**Delta**: slowdown term proportional to H_G(W)*sigma_cor^2, non-dominant in T but non-zero for sparse graphs
**Condition**: sparse graphs (e.g., ring, grid); zero for complete graph where H_G(W)=0

**Evidence**: "the term that depends on the correlated noise scales as [H_G(W)*sigma_cor^2 term]... The above term quantifies a slowdown effect of correlated noise."

## [POSITIVE] Gossip Averaging (D-SGD mixing)
Weighted averaging of neighboring local models using doubly stochastic mixing matrix W after local gradient updates

**Delta**: cancels correlated noise terms partially or fully depending on graph connectivity; complete cancellation on fully-connected graph
**Condition**: degree of cancellation depends on graph topology; full cancellation only on complete graph

**Evidence**: "The motivation for injecting correlated noise in (3) is that the gossip averaging in (4) will cancel out part or all correlated noise terms. For example, if G is the fully connected graph... (3) cancels out all correlated noise terms."

## [NEUTRAL] 2-Connectivity Requirement for Curious User Protection
Graph must be 2-connected (remains connected after removing any vertex) to guarantee SecLDP against honest-but-curious non-colluding users

**Delta**: necessary structural condition; without it privacy guarantees degrade
**Condition**: applies specifically to adversary type II (honest-but-curious non-colluding users); only connectivity required for external eavesdropper

**Evidence**: "for non-colluding curious users, Corollary 3 assumes the graph to be 2-connected... We believe this condition to be necessary: in the worst-case where a curious user i is the unique neighbor of another user j, then i can subtract the correlated noise injected by user j"

## [POSITIVE] Algebraic Connectivity-Based Noise Scaling
Correlated noise variance sigma_cor^2 scaled as Omega(1/a(G)) where a(G) is the algebraic connectivity of the graph, linking privacy to graph structure

**Delta**: enables CDP-matching trade-off for arbitrary connected graphs vs Network DP which only matches CDP for well-connected graphs
**Condition**: connected graphs; disconnected graphs require sigma_cor=0 falling back to LDP baseline

**Evidence**: "our trade-off matches CDP for arbitrary connected graphs... for comparison, Cyffers et al. (2022) derive a privacy-utility trade-off... Their trade-off matches CDP for well-connected graphs such as expanders, but degrades with poorer connectivity, e.g., O(1/n*epsilon^2) for the ring graph"

## [POSITIVE] Shared Randomness Seeds via One-Round Encrypted Communication
Secrets implemented as randomness seeds exchanged in a single round of encrypted communications, enabling correlated noise generation without ongoing cryptographic overhead

**Delta**: one-time communication cost vs ongoing secure aggregation overhead
**Condition**: one-time setup cost; avoids need for central entity or repeated secure aggregation

**Evidence**: "we consider the secrets to be shared randomness seeds exchangeable in one round of encrypted communications... our correlated Gaussian noise technique... without using secure aggregation, by having connected users exchange pairwise cancelling Gaussian noise"

## [POSITIVE] Example-Level DP via Privacy Amplification by Subsampling
Extension of user-level DP to example-level DP using privacy amplification by subsampling for non-convex tasks

**Delta**: gap between CDP and LDP almost 10 accuracy points for lowest privacy budget on MNIST; DECOR on ring vs CDP less than 1 accuracy point
**Condition**: non-convex tasks (MNIST neural network); example-level privacy

**Evidence**: "the gap of CDP with LDP is almost 10 accuracy points for the lowest privacy budget, as suggested by the theory, while the gap between DECOR on the ring topology and the CDP baseline, or DECOR on the grid topology, is less than 1 accuracy point"

## [NEUTRAL] Metropolis-Hastings Mixing Matrix
Mixing weights W_ij = 1/(deg(i)+1) for neighbors, used in experiments across ring, grid, and fully-connected topologies

**Delta**: H_G(W) <= 1/(2*k_min) showing correlated noise residual decreases with minimum degree
**Condition**: used in all empirical evaluations; theoretical bound on residual correlated noise depends on minimum graph degree

**Evidence**: "We use the Metropolis-Hastings (Boyd et al., 2006) mixing matrix... H_G(W) decreases with the minimal degree as H_G(W) <= 1/(2*k_min), when using uniform mixing weights"

## [POSITIVE] RDP-based Privacy Analysis (SecRDP)
Using Renyi Differential Privacy as the base for SecLDP analysis, providing stronger guarantees than standard DP and enabling composition

**Delta**: stronger guarantee than DP-based analysis of prior work (Sabater et al. 2022)
**Condition**: applies to all adversary types; enables straightforward composition for full training via RDP composition properties

**Evidence**: "we compare our privacy analysis of a single step of DECOR with its counterpart in the work of Sabater et al. (2022). Their Theorem 1 states a DP guarantee, while DECOR guarantees RDP, which is stronger (Mironov, 2017)."
