# Trust Regions for Explanations via Black-Box Probabilistic Certification

**Source**: https://proceedings.mlr.press/v235/dhurandhar24a.html

## [POSITIVE] Uniform Sampling Strategy (unif)
Simple uniform random sampling of Q examples within the region to be certified, querying fidelity for each and returning True if all meet threshold

**Delta**: best for low dimensions (up to 100)
**Condition**: Low-dimensional datasets (d ≤ 100), e.g., HELOC and Arrhythmia

**Evidence**: "Comparing between our methods it seems unif is best (and sufficient) for lowish dimensions (up to 100)"

## [POSITIVE] Uniform Incremental Strategy (unifI)
Incrementally samples prototypes uniformly and then samples examples from Gaussians centered at each prototype, doubling prototypes each iteration

**Delta**: best for intermediate dimensions (~1000)
**Condition**: Intermediate-dimensional datasets (d ≈ 1000), e.g., CIFAR10

**Evidence**: "unifI is best for CIFAR10 which has dimension close to 1000"

## [POSITIVE] Adaptive Incremental Strategy (adaptI)
Adaptively focuses queries around prototypes most likely to yield low-fidelity (violating) examples by halving the set of prototypes to the most promising ones each inner iteration

**Delta**: best for high dimensions (10000+); finds violating examples faster
**Condition**: High-dimensional datasets (d ≥ 10000), e.g., ImageNet

**Evidence**: "adaptI is best for ImageNet which has 40K+ dimensions... adaptI is generally faster in most cases because it finds the violating examples faster than the other strategies"

## [POSITIVE] Sampling Exponentially More Around Promising Prototypes
In adaptI, exponentially more samples are drawn around the most promising prototypes (those associated with lowest minimum fidelity examples)

**Delta**: more accurate estimation of minimum fidelity in high dimensions
**Condition**: High-dimensional input spaces

**Evidence**: "we sample exponentially more around the most promising prototypes (see Lemma 4 proof in Appendix), unlike the uniform strategies which do not adapt. Hence, in practice we are likely to estimate fw* more accurately with adaptI especially in high dimensions."

## [POSITIVE] Certifying Annular Regions (Between Hypercubes)
Algorithm 1 asks Algorithm 2 to certify regions between two hypercubes (lb and ub) rather than the full hypercube, avoiding redundant queries on already-certified inner regions

**Delta**: avoids wasting queries on already-certified inner region
**Condition**: All certification strategies when lb > 0

**Evidence**: "Algorithm 1 asks Algorithm 2 to certify regions between hypercubes with half-widths lb and ub. This is because the region with half-width lb has already been certified at that juncture, and hence when certifying a larger region ub we need not waste queries on examples that lie inside lb."

## [POSITIVE] Binary Search Over Half-Widths
Algorithm 1 uses a doubling/halving binary search to find the largest certified half-width, doubling ub when certified and halving when violating

**Delta**: O(log(w)) steps to certify final region
**Condition**: All strategies in Algorithm 1

**Evidence**: "Algorithm 1 doubles or halves the range every time we certify or fail to certify a region respectively. Hence, to certify the final region [−w,w]^d we will take m = O(log(w)) steps."

## [NEGATIVE] Zeroth-Order (ZO+) Optimization Baseline
Adapted ZO optimization toolbox used as a baseline for finding certified half-widths via derivative-free optimization

**Delta**: order of magnitude or more slower than proposed methods; e.g., ZO+ timing reaches 4384.76s vs <90s for proposed methods at d=10^4, Q=10^4
**Condition**: All dimensionalities; especially poor at high dimensions

**Evidence**: "our methods are an order of magnitude or more efficient than ZO+... The running times are especially higher in the LIME image cases"

## [POSITIVE] Gaussian Sampling Around Prototypes
In unifI and adaptI, examples are sampled from Gaussians centered at prototype points with σ ∝ (ub−lb)/d, focusing queries in promising subregions

**Delta**: higher lower bound on probability of correct certification when a good prototype is found near the minimum fidelity region
**Condition**: unifI and adaptI strategies

**Evidence**: "if we find a good prototype rj,k (i.e. close to fi*) then F_i^{N_{j,k}}(fw*+ε) will be high, leading to a higher (i.e., better) lower bound than in the uniform case."

## [POSITIVE] Finite Sample Exponentially Decaying Bounds (Theorem 1)
Theoretical bounds on the probability that estimated and true minimum fidelities differ by at most ε, derived for all three strategies

**Delta**: bounds converge fast to 1 especially for adaptI; efficient to compute (at most a few minutes)
**Condition**: All strategies; bounds estimated using kernel density estimation with fˆw* or θ as proxy for fw*

**Evidence**: "As can be seen the bounds converge fast to 1 especially for adaptI and are efficient to compute (at most a few minutes)."

## [NEUTRAL] Extreme Value Theory (EVT) Asymptotic Bounds
Cdf-free asymptotic bounds using EVT (Corollary 1) based on empirical minimum and second-smallest fidelity values, with exponent κ = d/2

**Delta**: meaningful for unifI and improve with increasing Q, but become looser with increasing input dimensionality
**Condition**: unif and i.i.d. unifI strategies; degrades at high dimensions

**Evidence**: "EVT bounds based on Corollary 1, shown in Table 7, are also high enough to be meaningful for unifI and improve with increasing Q, but become looser with increasing input dimensionality."

## [POSITIVE] Explanation Reuse via Trust Regions
Using certified trust regions to cover nearby examples without recomputing explanations, saving model queries

**Delta**: 80% query savings; order of magnitude fewer samples needed to cover dataset
**Condition**: HELOC dataset with LIME, adaptI strategy, Q=1000, θ=0.75

**Evidence**: "With an order of magnitude less samples and with less than 20% queries of those needed by LIME we can find explanations for the dataset."

## [POSITIVE] LIME as Explanation Method
Using LIME local linear explanations as the explanation being certified

**Delta**: LIME widths typically much larger than SHAP; explanations more generalizable beyond specific example
**Condition**: Compared against SHAP; LIME may have lower fidelity at x0 but generalizes farther

**Evidence**: "LIME widths are typically much larger than those found for SHAP, and hence the explanations are more generalizable beyond the specific example."

## [NEUTRAL] SHAP as Explanation Method
Using SHAP explanations as the explanation being certified

**Delta**: SHAP typically has fidelity of 1 at x0 but smaller trust region than LIME
**Condition**: Compared against LIME; SHAP more informative for specific example but less generalizable

**Evidence**: "SHAP typically has fidelity of 1 at x0, while LIME may have lower fidelity at x0 but generalizes farther in the sense of fidelity remaining above the threshold."

## [POSITIVE] Parallelization of Outer Loop in unifI and adaptI
The outer For loop in unifI and adaptI can be parallelized to improve computational efficiency

**Delta**: potential speedup (not quantified)
**Condition**: unifI and adaptI strategies when parallel compute is available

**Evidence**: "Moreover, the outer For loop in unifI and adaptI can be parallelized."

## [POSITIVE] Lipschitz Black-Box Exploitation
When the black-box model is known to be Lipschitz, regions can be automatically certified without querying, setting a non-trivial lb value

**Delta**: additional speedups possible by setting higher lb without queries
**Condition**: When black-box model is known to be Lipschitz

**Evidence**: "In the Lipschitz case we can automatically (i.e. without querying) certify a region and set a non-trivial lb value with additional speedups possible."

## [POSITIVE] Piecewise Linear Black-Box Early Stopping
When the black-box model is piecewise linear, the search can be stopped early rather than requiring a head start

**Delta**: early stopping reduces query budget needed
**Condition**: When black-box model is piecewise linear (e.g., ReLU networks, tree ensembles)

**Evidence**: "In the piecewise linear case instead of a head start (i.e. higher lb) we could stop our search early."

## [POSITIVE] Top-60% Feature Coverage for Explanation Reuse
A sample is considered covered by a trust region if the top 60% of its features (as ranked by LIME) fall within the certified region

**Delta**: actual fidelities of covered points satisfy θ=0.75 with high probability
**Condition**: HELOC dataset, LIME explanations, explanation reuse experiment

**Evidence**: "Figure 3(right) shows that considering the top 60% is sufficient for the actual fidelities of covered points to satisfy the threshold θ = 0.75 with high probability."

## [POSITIVE] Explanation Stability Within Trust Regions
Explanations computed for examples inside the certified trust region are more similar to the certified explanation than those outside

**Delta**: Top-5 intersection: 0.85 inside vs 0.77 outside; Spearman rank correlation: 0.74 inside vs 0.61 outside
**Condition**: HELOC dataset, LIME explanations, adaptI strategy, θ=0.75

**Evidence**: "for explanations computed outside the region (randomly chosen 100 examples), both Top-k intersection and Spearman rank correlation are much worse than those within the region"
