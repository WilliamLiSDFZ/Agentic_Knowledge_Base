# Byzantine-Robust Federated Learning: Impact of Client Subsampling and Local Updates

**Source**: https://proceedings.mlr.press/v235/allouah24a.html

## [NEGATIVE] Client Subsampling in FedRo
The server samples a subset of n_hat clients per round instead of all clients, which increases the effective fraction of Byzantine clients in each round.

**Delta**: convergence failure when sample size is too small
**Condition**: when sample size n_hat is below threshold n_hat_th

**Evidence**: "we observe that FedRo might not converge in the presence of Byzantine clients, when the server samples a small number of clients, since the subset of clients sampled might contain a majority of Byzantine clients in some learning rounds with high probability"

## [POSITIVE] Sufficient Condition on Client Subsampling Size
A condition based on KL divergence between Bernoulli distributions ensuring the number of Byzantine clients sampled per round stays below b_hat with probability at least p.

**Delta**: guarantees convergence with probability at least p
**Condition**: when n_hat and b_hat satisfy the KL divergence condition (5)

**Evidence**: "We prove that the number of Byzantine clients sampled in each round is smaller than b_hat, with probability at least p, if [KL divergence condition holds]"

## [POSITIVE] Multiple Local Steps (K > 1)
Each honest client performs K successive local gradient update steps before sending updates to the server, effectively approximating the average of K stochastic gradients.

**Delta**: asymptotic error term scales as sigma^2/K, decreasing with K
**Condition**: under careful choice of step-sizes, specifically gamma_c set as Theta(1/K)

**Evidence**: "the learning error due to Byzantine clients decreases with the number of local steps... this uncertainty decreases by increasing the number of local steps K performed by the clients, for a sufficiently small local step-size"

## [NEGATIVE] Multiple Local Steps - Additional Bias
Employing multiple local steps introduces an additional bias term in the convergence rate due to client drift.

**Delta**: additional O(T^{-2/3}) error term
**Condition**: when K > 1, but this term has more favorable dependence on T than the Byzantine error term

**Evidence**: "similar to the non-Byzantine case (Karimireddy et al., 2020), employing multiple local steps (i.e., K > 1) introduces an additional bias, resulting in the second error term in Corollary 1 which is in O(T^{-2/3})"

## [POSITIVE] Robust Aggregation Rule (FedRo)
Replacing the simple averaging in FedAvg with a (n_hat, b_hat, kappa)-robust aggregation rule to filter out Byzantine updates.

**Delta**: achieves (n, b, epsilon)-Byzantine resilience
**Condition**: when aggregation rule satisfies (n_hat, b_hat, kappa)-robustness definition

**Evidence**: "the natural approach to robustify FL against adversarial clients is to replace the simple averaging operation at the server in the standard FedAvg algorithm by a robust averaging rule"

## [POSITIVE] Coordinate-wise Trimmed Mean Aggregation
Using coordinate-wise trimmed mean as the robust aggregation rule, which achieves kappa in O(b_hat/n_hat).

**Delta**: asymptotic error in O(b/n * (sigma^2/K + zeta^2))
**Condition**: when used as the aggregation rule in FedRo

**Evidence**: "Using an aggregation function with kappa in O(b_hat/n_hat), such as coordinate-wise trimmed mean (Allouah et al., 2023), this term will be in [O(b_hat/n_hat * (sigma^2/K + zeta^2))]"

## [POSITIVE] Two-sided Step-sizes
Using both a client step-size gamma_c and a server step-size gamma_s, with gamma_c set as Theta(1/K).

**Delta**: first term of convergence rate similar to FedAvg without Byzantine clients
**Condition**: when gamma_c <= 1/16LK and gamma_c*gamma_s <= 1/36LK

**Evidence**: "The first term of the convergence rate (2) is similar to the one obtained for FedAvg with two-sided step-sizes and without the presence of Byzantine clients (Karimireddy et al., 2020)"

## [NEUTRAL] Diminishing Returns of Client Subsampling
Beyond a threshold n_hat_opt, increasing the number of sampled clients yields no further improvement in asymptotic error order.

**Delta**: performance saturates at n_hat = n_hat_opt
**Condition**: when n_hat >= n_hat_opt; specific to Byzantine FL, does not occur in non-Byzantine FL

**Evidence**: "the rate of improvement in learning accuracy diminishes with respect to the number of clients subsampled, as soon as the sample size exceeds a threshold value... Beyond this point, further increases in n_hat do not affect the error order"

## [POSITIVE] Linear Speedup in Number of Sampled Clients
FedRo preserves the linear speedup property of FedAvg with respect to the number of sampled clients n_hat.

**Delta**: leading term in O(1/sqrt(n_hat * T))
**Condition**: for the vanishing terms in the convergence rate

**Evidence**: "These terms vanish when T -> infinity with a leading term in O(1/sqrt(n_hat*T)). Hence FedRo preserves the linear speedup in n_hat of FedAvg"

## [POSITIVE] NNM + Coordinate-wise Trimmed Mean
State-of-the-art NNM robustness scheme coupled with coordinate-wise trimmed mean used in experiments.

**Delta**: FedRo fails when number of sampled clients is below 30 (validates theoretical threshold)
**Condition**: on FEMNIST dataset with n=150 clients, b=30 Byzantine clients

**Evidence**: "we use the state-of-the-art NNM robustness scheme (Allouah et al., 2023) coupled with coordinate-wise trimmed-mean (Yin et al., 2018a) and observe that FedRo fails when the number of sampled clients is below 30. This validates our theoretical result in Lemma 3"

## [POSITIVE] Optimal b_hat Selection via Binary Search
For a fixed n_hat, selecting the smallest b_hat satisfying condition (5) to minimize the asymptotic error, computable in O(log n_hat) steps.

**Delta**: minimizes asymptotic error term proportional to b_hat/n_hat
**Condition**: for a fixed n_hat satisfying the convergence threshold

**Evidence**: "we aim to select the smallest b_hat within the interval [b/n * n_hat, 1/2 * n_hat] that satisfies condition (5), thereby minimizing the asymptotic error in (6)... we can efficiently compute the solution to (7) in O(log n_hat) steps using binary search"

## [POSITIVE] Increasing Local Steps Against Byzantine Attacks (Empirical)
Varying K from 5 to 35 with gamma_c set as Theta(1/K) to assess impact on accuracy against Byzantine attacks.

**Delta**: increasing K enhances model accuracy against stronger attacks
**Condition**: on FEMNIST (b=30) and CIFAR-10 (b=15) datasets with n=150 clients, K ranging from 5 to 35

**Evidence**: "Figure 4 illustrates that increasing the number of local steps K enhances model accuracy against stronger attacks, validating our theoretical worst-case guarantees"
