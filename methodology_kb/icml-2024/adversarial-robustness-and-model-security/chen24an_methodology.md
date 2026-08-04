# Recovering Labels from Local Updates in Federated Learning

**Source**: https://proceedings.mlr.press/v235/chen24an.html

## [POSITIVE] RLU Least-Squares Label Recovery
Recovers training labels by solving a least-squares problem that exploits the correlation between local updates of the output layer's bias and the number of samples per class, using estimated erroneous confidence values.

**Delta**: outperforms baseline
**Condition**: All tested datasets, architectures, activation functions, and FL schemes

**Evidence**: "RLU outperforms the baselines in all settings. When local training consists of a single epoch, RLU achieves near-perfect accuracy across the board in terms of both cAcc and iAcc"

## [POSITIVE] Monte Carlo Erroneous Confidence Estimation
Uses a small auxiliary dataset processed through the global model to empirically estimate the mean and variance of output logit distributions, which parameterize the erroneous confidence used in label recovery.

**Delta**: outperforms baseline
**Condition**: All training stages and FL schemes

**Evidence**: "In each global round of training, the server leverages global model θ(t) to obtain estimates of the parameters in (7), µ̄n and Σ̄n, via a Monte Carlo method run on a small auxiliary dataset A"

## [POSITIVE] Dynamic Intermediate Epoch State Simulation
Recursively estimates intermediate erroneous confidence values across local epochs by simulating model parameter update dynamics, since the server cannot access intermediate local model states.

**Delta**: at least 84% cAcc and 90% iAcc on all datasets with m=10
**Condition**: Multiple local epochs (m=10) setting

**Evidence**: "RLU still outperforms the baselines, maintaining at least 84% cACC and 90% iAcc on all datasets, architectures and activation functions"

## [POSITIVE] Iterative Label Count Refinement (T=5 iterations)
Initializes a guess for per-class label counts and iteratively refines it by comparing simulated vs. actual final erroneous confidence, converging after only 5 iterations.

**Delta**: highly accurate performance after only T=5 iterations
**Condition**: Multiple local epochs setting

**Evidence**: "In our experiments, following such an initialization RLU achieves highly accurate performance after only T = 5 iterations"

## [POSITIVE] Auxiliary Dataset for Logit Distribution Estimation
Server maintains a small auxiliary dataset (100 samples per class by default) to estimate output logit distribution parameters needed for erroneous confidence computation.

**Delta**: gap of only 2.4% and 3.1% on CIFAR10 and CIFAR100 when reducing to 5 samples per class
**Condition**: Varying auxiliary dataset sizes (5, 10, 50, 100 samples per class)

**Evidence**: "there appears to be no significant performance degradation due to reduction of the auxiliary data set size. When using the smallest among the auxiliary sets, on SVHN and Tiny the proposed RLU achieves performance close to the baseline. The largest performance gap is on CIFAR10 and CIFAR100, and even there the gap is only 2.4% and 3.1%, respectively"

## [POSITIVE] Generalized FL Scheme Framework (ρ and h coefficients)
Extends label recovery to non-FedAvg FL schemes (FedProx, Scaffold, FedDyn, FedDC, SGDm, NAG) by parameterizing local update expectations with scheme-specific coefficients ρ(τ) and h_j(t).

**Delta**: RLU maintains iAcc of at least 88% when baselines severely deteriorate
**Condition**: Non-FedAvg FL schemes with regularization or momentum-based optimizers

**Evidence**: "as ρ(τ) deviates from 1 when λ = 5 and γ = 0.9, performance of the baselines severely deteriorates while RLU maintain its iAcc of at least 88%"

## [POSITIVE] RLU Integration with Gradient Inversion (IG)
Uses RLU-recovered labels as fixed inputs to gradient inversion optimization, replacing joint label+image optimization with image-only optimization.

**Delta**: higher PSNR and lower LPIPS than joint optimization baseline
**Condition**: Gradient inversion attack on CIFAR10, batch size 9

**Evidence**: "images reconstructed with the help of RLU have higher PSNR and lower LPIPS, indicating smaller distance to the original images"

## [NEGATIVE] Multiple Local Epochs (client-side)
Clients run multiple local epochs (m=10) before sending updates, which is a realistic FL setting but degrades label recovery performance for all methods.

**Delta**: performance of all methods deteriorates
**Condition**: All label recovery methods including RLU

**Evidence**: "When the clients run m = 10 local epochs, performance of all methods deteriorates (as expected based on the discussion in Section 3.2.2)"

## [NEGATIVE] Differential Privacy Noise Defense
Clients inject zero-mean Gaussian noise with variance σ² into gradients to defend against label recovery attacks.

**Delta**: iAcc drops from 0.968 to 0.812 on SVHN (1 epoch) and from 0.844 to 0.484 (10 epochs) as σ increases from 0.05 to 0.5
**Condition**: RLU attack under DP noise, more effective defense in multi-epoch settings

**Evidence**: "higher variance of DP noise enhances the level of protection, leading to less accurate label recovery attacks. Noticeably, DP noise more effectively helps mitigate the RLU attacks in multi-epoch than in single-epoch settings"

## [NEGATIVE] High Data Heterogeneity (small α)
Using Dirichlet distribution with small concentration parameter α to create highly non-i.i.d. data partitions across clients.

**Delta**: iAcc of baselines monotonically decreases; RLU maintains ≥93% iAcc even at α=0.05
**Condition**: CIFAR10 with varying α; baselines degrade more than RLU

**Evidence**: "iAcc of the three baselines monotonically decreases with the level of data heterogeneity. On the other hand, RLU demonstrate a great degree of robustness as it maintains high iAcc across the board; in particular, RLU achieves 93% or higher instance-level accuracy in all settings, including at the highest level of data heterogeneity (α = 0.05)"

## [NEGATIVE] Non-negative Activation Function Assumption (LLG+/ZLG+)
Baseline methods LLG and ZLG assume non-negative activation functions (e.g., ReLU), limiting their applicability.

**Delta**: LLG+ performance deteriorates significantly with Tanh and SELU
**Condition**: LLG+ and ZLG+ baselines when non-negative activation assumption is violated

**Evidence**: "Since LLG+ assumes non-negative activation functions, its performance deteriorates significantly with Tanh and SELU"

## [NEGATIVE] iRLG Untrained Model Assumption
iRLG assumes µn=0 (untrained model with random predictions), which does not hold for well-trained models.

**Delta**: iRLG iAcc falls below 70% on CIFAR10 and CIFAR100 with m=10; trails RLU by 16.3%, 17.3%, 23.9% at 90% model accuracy
**Condition**: iRLG baseline on trained models or multiple epoch settings

**Evidence**: "the performance of iRLG drastically deteriorates as the model's accuracy improves... iRLG's trails RLU by 16.3%, 17.3% and 23.9% on these three datasets, respectively"

## [NEGATIVE] Distribution Shift in Auxiliary Dataset
Using auxiliary data from a different but related distribution (CIFAR10.1 or CIFAR10.2) instead of the exact training distribution.

**Delta**: noticeable deterioration when only 5 samples per class used; small degradation at 10+ samples
**Condition**: RLU with out-of-distribution auxiliary data, especially at very small auxiliary set sizes

**Evidence**: "when the amount of auxiliary data is either 10, 50, or 100 samples per class, RLU experiences relatively small performance degradation compared to the results in Table 2. However, a noticeable deterioration occurs when only 5 samples per class are used"

## [NEGATIVE] Well-Trained Model Attack
Attacking models at advanced training stages where output logit magnitudes grow, causing gradient magnitudes to vanish and increasing sensitivity to noise.

**Delta**: ZLG+ iAcc is 33.3%, 21.1%, 30.1% lower than RLU at 90% model accuracy on SVHN, CIFAR10, CIFAR100
**Condition**: All label recovery methods on models with high training accuracy

**Evidence**: "All of the methods in Table 2 experience performance deterioration as the model accuracy increases... The iAcc of ZLG+ is 33.3%, 21.1% and 30.1% lower than RLU's, while iRLG's trails RLU by 16.3%, 17.3% and 23.9% on these three datasets, respectively"

## [POSITIVE] Activation-Agnostic Label Recovery Design
RLU makes no assumptions about the type of activation function used in the network, enabling it to work with ReLU, Tanh, ELU, SELU, and SiLU.

**Delta**: outperforms baseline across all activation functions tested
**Condition**: All activation functions tested across architectures and datasets

**Evidence**: "we employ a number of activation functions including ReLU, Tanh, ELU, SELU and SiLU to further evaluate robustness of our proposed method... RLU outperforms the baselines in all settings"
