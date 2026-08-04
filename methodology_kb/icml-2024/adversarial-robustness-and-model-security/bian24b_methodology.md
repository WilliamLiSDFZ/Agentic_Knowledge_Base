# Naive Bayes Classifiers over Missing Data: Decision and Poisoning

**Source**: https://proceedings.mlr.press/v235/bian24b.html

## [POSITIVE] Certifiable Robustness Decision Algorithm (Iterate+Index)
An algorithm that builds an offline index over the incomplete dataset to efficiently check whether multiple test points are all certifiably robust for NBC, avoiding redundant recomputation across test points. The index Ei,j[xj] stores counts of data points per label and attribute value, enabling O(nd + kmd) total runtime.

**Delta**: ~20x faster than Iterate baseline
**Condition**: Decision problem for multiple test points on NBC over incomplete datasets

**Evidence**: "we observe that Iterate+Index is almost 20× faster than Iterate and much faster than the straightforward solution AD, which nonetheless does not have correctness guarantees."

## [POSITIVE] Index-based Multi-Test-Point Extension
Precomputing an index Ei,j[xj] once in O(nd) time and reusing it for each of k test points, reducing per-test-point cost to O(md) instead of O(nd).

**Delta**: 10x speedup over Iterate for 16 test points
**Condition**: Multiple test points; benefit grows with number of test points

**Evidence**: "For 16 test points, we see that Iterate+Index outperforms Iterate by 10×."

## [NEGATIVE] Approximate Decision (AD) Baseline
Samples 100 possible worlds uniformly at random and returns certifiably robust if NBC prediction agrees across all sampled worlds; may return false positives and has no correctness guarantees.

**Delta**: slower than Iterate+Index and lacks correctness guarantees
**Condition**: Decision problem baseline; used for comparison only

**Evidence**: "Iterate+Index is almost 20× faster than Iterate and much faster than the straightforward solution AD, which nonetheless does not have correctness guarantees."

## [NEGATIVE] Iterative Algorithm without Index (Iterate)
Runs Algorithm 1 independently for each test point without indexing, resulting in O(knd) total runtime for k test points.

**Delta**: running time grows linearly with number of test points; 10-20x slower than Iterate+Index
**Condition**: Decision problem for multiple test points

**Evidence**: "We observe that the running time of AD and Iterate grows almost linearly with the number of test points, whereas the running time of Iterate+Index remains almost the same regardless of the number of test points."

## [POSITIVE] Greedy Search Poisoning (GS) for Single Test Point
An optimal greedy algorithm (Algorithm 2/3) that solves the data poisoning problem for a single test point by iteratively applying either operation A1 (increase Pr(t|l)) or A2 (decrease Pr(t|l*)) and selecting the sequence requiring fewer alterations.

**Delta**: achieves minimum poisoning rate; significantly faster than RP and marginally faster than SR
**Condition**: Single test point data poisoning problem

**Evidence**: "the running time of GS is significantly faster than RP and marginally faster than SR over most datasets... Note that RP and SR always have a higher poisoning rate compared to GS over Single Point Data Poisoning Problem. Since GS is provably optimal when we are given a single test point, it has the smallest poisoning rate across all algorithms for the same dataset."

## [NEGATIVE] Random Poisoning (RP) Baseline
Randomly selects cells to mark as NULL iteratively until the test point becomes certifiably non-robust; no strategic guidance.

**Delta**: higher poisoning rate and slower than GS
**Condition**: Single test point data poisoning baseline

**Evidence**: "RP and SR always have a higher poisoning rate compared to GS over Single Point Data Poisoning Problem."

## [NEGATIVE] Smarter Random Poisoning (SR)
Fixes a target label and randomly applies operation A1 or A2 until the test point becomes certifiably non-robust; uses optimal operations but not in optimal sequence.

**Delta**: higher poisoning rate than GS; marginally slower than GS
**Condition**: Single test point data poisoning; uses correct operations but suboptimal ordering

**Evidence**: "the running time of GS is significantly faster than RP and marginally faster than SR over most datasets... RP and SR always have a higher poisoning rate compared to GS over Single Point Data Poisoning Problem."

## [NEUTRAL] Closed-World Semantics for Missing Value Imputation
Missing values (NULL) are replaced only with domain values already observed in the incomplete dataset, constraining the set of possible worlds.

**Delta**: None
**Condition**: Defines the possible worlds model used throughout the paper

**Evidence**: "a possible world can be obtained by replacing each attribute value marked with NULL with a domain value that exists in D□. This follows the so-called closed-world semantics of incomplete data."

## [NEUTRAL] Numerical Feature Discretization into Bins
Continuous features are discretized into 5 equal-size bins using sklearn's KBinsDiscretizer to satisfy the categorical feature assumption of NBC.

**Delta**: None
**Condition**: Preprocessing step for all ten real-world datasets in experiments

**Evidence**: "We first preprocess every dataset so that it contains only categorical features by partitioning each numerical feature into 5 segments (or bins) of equal size using sklearn's KBinsDiscretizer."

## [NEGATIVE] NP-completeness of Multi-Point Data Poisoning
The data poisoning problem for multiple test points is NP-complete for datasets with at least 3 features, meaning no polynomial-time optimal algorithm exists unless P=NP.

**Delta**: intractable for multiple test points with d>=3
**Condition**: Multiple test points, datasets with at least 3 dimensions

**Evidence**: "For every d ≥ 3, CR-NaiveBayes† is NP-complete on datasets with d dimensions and multiple test points."

## [NEUTRAL] Union Heuristic for Multi-Point Poisoning (Algorithm 4)
Heuristic that runs the single-point greedy algorithm (Algorithm 2) for each test point independently and takes the union of all poisoned cells; not guaranteed to be optimal.

**Delta**: None
**Condition**: Multiple test points data poisoning; used as practical heuristic given NP-hardness

**Evidence**: "A simple heuristic algorithm simply iteratively runs Algorithm 2 over every test point ti and then take the union of all the missing cells found... the number of poisoned cells is not necessarily minimal."

## [POSITIVE] Support Value Extremes for Certifiability Check
Instead of enumerating all exponentially many possible worlds, the algorithm computes only the minimum and maximum support values for each label by assigning all missing cells to disagree or agree with the test point, enabling polynomial-time certifiability checking.

**Delta**: O(md + nd) time with no asymptotic overhead over standard NBC training
**Condition**: Decision problem for NBC; exploits structure of NBC support value computation

**Evidence**: "our algorithm exhibits no asymptotic overhead and provides a much stronger guarantee of the classification result compared to the original NBC... it suffices to inspect only the 'extreme' possible world that is the worst and best for li, respectively."
