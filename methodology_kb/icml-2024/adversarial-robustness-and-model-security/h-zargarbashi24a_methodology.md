# Robust Yet Efficient Conformal Prediction Sets

**Source**: https://proceedings.mlr.press/v235/h-zargarbashi24a.html

## [POSITIVE] CDF-Aware Bound (CAS)
Uses the cumulative distribution function (CDF) of smooth scores to obtain tighter upper bounds on worst-case conformity scores, rather than only using the mean of randomized scores as in RSCP.

**Delta**: set size doubled or tripled improvement over RSCP at larger radii, especially on ImageNet and Cora-ML
**Condition**: Evasion attacks on continuous and discrete data; all datasets (CIFAR-10, ImageNet, Cora-ML)

**Evidence**: "In Fig. 2 we see that CAS's results in smaller prediction sets, across all radii, and all nominal 1−α values, and as in Fig. 3 (left) all scores. The improvement is substantial and also grows with r – for larger radii it is doubled or even tripled, especially on ImageNet and Cora-ML."

## [NEGATIVE] Mean-Only Baseline Bound (RSCP)
Bounds the worst-case smooth score using only the expected (mean) smoothed score, discarding distributional information beyond the mean.

**Delta**: larger sets than CAS; set size nearly reaches all classes (|Y|=10) for large radii with finite-sample correction
**Condition**: Evasion attacks; compared to CDF-based bound across all datasets and radii

**Evidence**: "This bound discards a lot of information about the distribution of scores around the given x. ... In Fig. 4 (right) we see that the size for RSCP quickly explodes, reaching almost all classes (|Y| = 10) for large radii, while CAS maintains low average size."

## [POSITIVE] Calibration-Time Evasion Certificate
Computes lower bounds on conformity scores only for calibration points (not test points), using a conservative quantile threshold at calibration time rather than computing upper bounds for all classes at test time.

**Delta**: substantially faster, especially for large datasets like ImageNet; smaller sets when correcting for finite samples
**Condition**: Evasion robustness; particularly beneficial for datasets with many classes (e.g., ImageNet with 1000 classes)

**Evidence**: "In addition to being significantly faster (especially for large datasets like ImageNet), our calibration-time algorithm also leads to smaller sets when correcting for finite samples."

## [POSITIVE] Finite-Sample Correction via DKW Inequality
Corrects for finite-sample approximation errors in Monte-Carlo estimation of smooth scores using the Dvoretzky–Kiefer–Wolfowitz inequality, adjusting the calibration level to α' = α − η.

**Delta**: CAS maintains low average set size with correction; RSCP set size explodes to nearly all classes at large radii
**Condition**: Required for valid (non-asymptotic) certificates; applied to both evasion and feature poisoning

**Evidence**: "In Fig. 4 (right) we see that the size for RSCP quickly explodes, reaching almost all classes (|Y| = 10) for large radii, while CAS maintains low average size. Moreover, CAS has smaller standard deviation across test inputs."

## [POSITIVE] Bernstein Bound for Test Score Correction
Uses the tighter Bernstein confidence interval instead of Hoeffding's inequality to correct the MC-estimated test score upper bound.

**Delta**: tighter than Hoeffding bound (qualitative)
**Condition**: Finite-sample correction for test-time evasion certificate in CAS

**Evidence**: "Instead of a Hoeffding bound we can use the tighter Bernstein bound for ŝ+(xn+1, y) since we have access to it."

## [POSITIVE] Poisoning-Aware Threshold via MILP
Derives a conservative calibration threshold robust to feature or label poisoning by solving a mixed-integer linear program that finds the worst-case quantile shift under adversarial calibration set perturbation.

**Delta**: maintains ≥1−α coverage even under infinite poisoning budget; small set size increase for small k
**Condition**: Feature poisoning attacks on calibration set; CIFAR-10 with σ=0.25

**Evidence**: "Fig. 5 (middle) shows the robustness of CAS even under an infinite budget which verifies Prop. 3.2. We also show the set size of robust CP in Fig. 5 (right). We see that as expected a smaller budget k leads to less conservative sets which translates to smaller set sizes."

## [POSITIVE] Label Poisoning Robustness
Certifies robustness to adversarial label flipping of calibration points by solving an optimization problem for the most conservative quantile under worst-case label perturbations.

**Delta**: robust coverage maintained at ~0.900 even with k=2 label flips vs. vanilla coverage dropping to 0.859
**Condition**: Label poisoning attacks; CIFAR-10; small k values

**Evidence**: "Table 1 shows that adversarial label noise can break the guarantee even for small budget k. ... k=2: Vanilla Cov. (Pert) = 0.859, Robust Cov. (Pert) = 0.901"

## [POSITIVE] Sparse Smoothing for Discrete/Graph Data
Extends CDF-based bounds to binary/sparse data using sparse randomized smoothing (flipping zeros and ones with probabilities p0 and p1), enabling robustness certificates for graph neural networks.

**Delta**: CAS outperforms RSCP on Cora-ML graph dataset; improvement grows with radius
**Condition**: Node classification on graph data (Cora-ML); binary/sparse threat model

**Evidence**: "For discrete/graph data we extend the bounds of Bojchevski et al. (2020). ... In Fig. 2 we see that CAS's results in smaller prediction sets, across all radii, and all nominal 1−α values ... especially on ImageNet and Cora-ML."

## [POSITIVE] Adaptive Prediction Sets (APS) Score Function
Uses APS as the conformity score, which sums probabilities of classes predicted more likely than y, with randomized tie-breaking, to avoid over/under-coverage of TPS.

**Delta**: smaller set sizes compared to TPS (shown in Fig. 3 left for r=0.12)
**Condition**: Main experiments on CIFAR-10; compared against TPS score function

**Evidence**: "We use APS as the main score function. ... [Fig. 3 Left] Set size for r=0.12 with different scores [showing APS produces smaller sets than TPS for both RSCP and CAS]"

## [POSITIVE] Combined Evasion and Poisoning Robustness
Simultaneously achieves robustness to both evasion and poisoning by combining the CDF-based upper bound on test scores with the conservative poisoning-aware threshold.

**Delta**: provides simultaneous guarantees (qualitative, no separate quantitative comparison given)
**Condition**: Scenarios with both evasion and poisoning threats simultaneously

**Evidence**: "Since robustness to evasion and poisoning are independent, we can achieve simultaneous robustness to both evasion and poisoning via Cα = {y : scdf(x, y) ≥ qα}."

## [NEUTRAL] Smaller Smoothing Parameter σ
Using a smaller Gaussian noise scale σ in randomized smoothing results in smaller sets for small certified radii but rapidly growing sets for larger radii.

**Delta**: smaller sets at small r but rapidly growing sets at larger r compared to larger σ
**Condition**: Ablation study on CIFAR-10; trade-off depends on target certified radius

**Evidence**: "A smaller amount of smoothing results in a smaller set size in the beginning, but the set sizes grows rapidly by increasing the certified radius."

## [NEGATIVE] Larger Poisoning Budget k
Allowing the adversary to perturb more calibration points (larger k) leads to more conservative thresholds and larger prediction sets.

**Delta**: set size increases with k; for k=|D_cal| (infinite budget) set size increases substantially at larger r (e.g., 3.17 vs 1.84 at r=0.12)
**Condition**: Feature poisoning robustness; CIFAR-10 with σ=0.25

**Evidence**: "In Table 2 ... k=|D_cal|, r=0.12: Ave. Set Size With correction = 3.17 vs k=3: 1.84. We see that as expected a smaller budget k leads to less conservative sets which translates to smaller set sizes."
