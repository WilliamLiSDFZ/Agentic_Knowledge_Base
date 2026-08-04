# Unmasking Vulnerabilities: Cardinality Sketches under Adaptive Inputs

**Source**: https://proceedings.mlr.press/v235/ahmadian24a.html

## [POSITIVE] Single-batch attack on standard estimators
Algorithm 1: fixes a ground set N, issues r queries where each key is included independently with probability 1/2, computes average sufficient statistic score per key, and returns keys ordered by score as adversarial input. All queries issued in one batch; only post-processing is adaptive.

**Delta**: 40% overestimation or underestimation of cardinality with 4k queries on HLL++
**Condition**: Against standard/optimal cardinality estimators (e.g., HLL++) that report a sufficient statistic

**Evidence**: "The results reported in Section 5 show that even with a single-batch attack using 4k queries, we can consistently construct adversarial inputs on which the estimator substantially overestimates or underestimates the cardinality by 40%."

## [POSITIVE] Score-based key ranking via sufficient statistic
Each key x in the ground set N is assigned a score A[x] = average value of T(S_rho(U)) over all query subsets containing x. Keys are then ordered by this score to identify low-priority (adversarial) keys.

**Delta**: O(k) queries suffice to construct adversarial input biased up by factor Omega(1/alpha)
**Condition**: k-mins or bottom-k sketches with standard estimators

**Evidence**: "We establish that scores are correlated with the priorities of keys – the keys with lowest priorities have in expectation lower scores. Therefore a prefix of the order will contain disproportionately more of them and overestimate the cardinality and a suffix will contain disproportionately fewer of them and underestimate the cardinality."

## [POSITIVE] Linear query complexity attack (O(k) queries)
The single-batch attack on standard estimators requires only O(k) queries (linear in sketch size k) to construct an adversarial input, matching the straightforward upper bound of using disjoint sketch components.

**Delta**: Attack size O(k) matches upper bound; empirically 4k queries suffice
**Condition**: Against standard estimators; single-batch setting

**Evidence**: "The attack uses linearly many queries O(k) in the sketch size and importantly, issues all queries in a single batch... The linear size of the attack matches the straightforward upper bound of using disjoint components of the sketch for different queries."

## [POSITIVE] Adaptive multi-batch attack on arbitrary estimators (Algorithm 4)
Maintains a growing mask set M; query sets have the form M union U where U is sampled from D0. Keys are added to M when their score separates from the median. The mask poisons larger sets so that S(M union U) ≈ S(M), making any estimator ineffective.

**Delta**: O~(k^2) queries suffice, matching the generic quadratic upper bound
**Condition**: Against any correct query response algorithm applied to known sketch structures

**Evidence**: "In Section 6 and Section 7, we present an attack that broadly applies against any correct query response algorithm... Our attack uses O~(k^2) adaptive queries. We show that multiple batches are necessary against strategic query response algorithms. This quadratic attack size matches the generic quadratic upper bound construction of Hassidim et al. (2020)."

## [POSITIVE] Mask set construction for poisoning
The product of the adaptive attack is a small mask set M such that S_rho(M union U) ≈ S_rho(M) for any large set U, making it impossible to recover an estimate of the true cardinality of U.

**Delta**: |M| < alpha*n (sublinear in ground set size)
**Condition**: Adaptive attack (Algorithm 4) against any correct QR algorithm

**Evidence**: "The product of our attack is a small mask set M that can poison larger sets U in the sense that S(M∪U) ≈ S(M), making any estimator ineffective."

## [POSITIVE] Single-batch attack on symmetric QR (Algorithm 3)
A single-batch variant that works against symmetric query response algorithms (those that treat sketch components as an unordered set and are monotone). Uses sampled rate q and scores keys by the QR response Z.

**Delta**: r = O~(k^2) queries suffice for symmetric QR algorithms
**Condition**: Against symmetric and monotone query response algorithms

**Evidence**: "Algorithm 3 specifies a single-batch attack. We establish that the attack succeeds when we set the size r = O~(k^2) and QR is constrained to be symmetric."

## [NEGATIVE] Multiple query batches requirement
Showing that any polynomial-size attack on a soft threshold estimator must use multiple batches, because a single batch leaks information only about a small O(log(r/delta)) component of the sketch.

**Delta**: Single-batch attacks require exponential queries in k against general QR algorithms
**Condition**: Against general (non-symmetric) correct query response algorithms

**Evidence**: "Lemma 6.5 (Multiple batches are necessary). Any attack of polynomial size in k on a soft threshold estimator must use multiple batches. When there is a single batch of r queries, we can apply the standard estimator while accessing only a 'component' of the sketch that is of size k' = O(log(r/delta))... an exponential number of queries in k is needed in order to construct an adversarial input in a single batch."

## [NEUTRAL] Rank-domain sketch representation
Reformulating sketches in terms of rank order of keys by hash values rather than actual hash values, simplifying analysis by factoring out hash values. Rank-domain sketches S^R(U) have the form (Y_1,...,Y_k) where Y_i are positive integers.

**Delta**: Analytical simplification only
**Condition**: Used in proof of Theorem 7.1 for single-batch attack on symmetric QR

**Evidence**: "We work with the rank-domain representations of the sketches with respect to the ground set N. This representation simplifies our analysis as it only depends on the rank order of keys by their hash values and by that factors out the hash values."

## [POSITIVE] Increasing number of queries improves attack efficacy
Empirical finding that using more queries in Algorithm 1 produces more effective adversarial inputs, with diminishing returns beyond a certain point.

**Delta**: For k=104, good degree of error achieved with 4096 queries; gains become marginal beyond that
**Condition**: HLL++ sketch, fixed sketch size, varying query count

**Evidence**: "We can see that as we increase the number of queries, the gap between estimated value and the y=x line (actual value) widens... Our algorithm is able to construct more effective adversarial input with a larger number of queries. However the gain in effectiveness becomes marginal at some point. For example, for k=104, we already see good degree of error in estimation with 4096 queries."

## [POSITIVE] Linear query scaling with sketch size (4k queries)
Empirical evaluation showing that using 4k queries (linear in sketch size) consistently produces adversarial inputs across different sketch sizes k.

**Delta**: Consistent ~40% cardinality estimation error across sketch sizes k=2^6 to k=2^11
**Condition**: HLL++ sketch, varying sketch sizes k=2^6 to k=2^11

**Evidence**: "In Figure 3, we report the ratio of estimated size to actual size of the set for all subsets constructed as a prefix of the order on keys, sorted by increasing average scores A[x] for a fixed number of queries set to 4k... by running attacks with enough number of queries (linear in the size of sketch), we are able to identify keys with low-priority and then trick the estimator to give an estimate for a set much higher than the actual size."

## [POSITIVE] Soft threshold problem formulation
Simplifying the attack target from full cardinality estimation to a binary soft threshold problem (return 0 if |U|<=A, return 1 if |U|>=2A), which is easier for the QR algorithm but the attack still succeeds.

**Delta**: Attack applies even against this weaker/easier-for-QR task
**Condition**: General attack framework against any QR algorithm

**Evidence**: "Moreover, the task of the QR algorithm is the following problem that is more specialized than cardinality estimation: Problem 6.1 (Soft Threshold A). Return 0 when |U|≤A and 1 when |U|≥2A... it applies even when the response is tailored to the attack algorithm and its internal state including the distribution from which the query sets are selected at each step."

## [NEGATIVE] Composability requirement fixing randomness across queries
The design requirement that the same internal randomness rho is used across all queries (necessary for composability in streaming/distributed settings) is what enables adaptive attacks to leak information about rho.

**Delta**: Enables all described attacks; without fixed rho, attacks would not work
**Condition**: All composable cardinality sketch designs in practice

**Evidence**: "Importantly, the use of the same internal randomness ρ across all queries is necessary for composability and therefore in typical use cases it is fixed across a system... information on the randomness ρ may leak from query responses, and the union bound argument does not hold."

## [NEUTRAL] Chebyshev/Chernoff concentration bounds in attack analysis
Using Chebyshev's Inequality to bound the number of rounds needed for score separation, and Chernoff bounds to show that score gaps concentrate, establishing the O(k) and O(k^2) query complexity bounds.

**Delta**: Theoretical tool establishing attack query complexity bounds
**Condition**: Theoretical analysis of attack algorithms

**Evidence**: "We then apply Chebyshev's Inequality to bound the number of rounds that is needed so that enough of the low priority keys have lower average scores A[u] than 'most' other keys... Setting λ=cr/k separates a key in N_0* from a key in N' with probability 1−2e^{−2c^2r/k^2}. Choosing r=O(k^2 log|N|) we get that the order separates out with high probability all the keys N_0* from all the keys N'."
