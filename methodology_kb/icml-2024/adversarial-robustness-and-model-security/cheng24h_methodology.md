# Efficient Black-box Adversarial Attacks via Bayesian Optimization Guided by a Function Prior

**Source**: https://proceedings.mlr.press/v235/cheng24h.html

## [POSITIVE] Prior-guided Bayesian Optimization (P-BO)
Integrates a surrogate white-box model as a global function prior into Bayesian Optimization by initializing the Gaussian process mean function with the surrogate model's loss function, rather than using a zero-mean GP.

**Delta**: 100% ASR with <20 queries on CIFAR-10; outperforms all baselines on ImageNet and VLMs
**Condition**: Black-box adversarial attacks on image classifiers and vision-language models

**Evidence**: "P-BO needs less than 20 queries on average to obtain 100% attack success rates on CIFAR-10, greatly outperforming the existing methods."

## [POSITIVE] Global Function Prior vs. Local Gradient Prior
Using the surrogate model's full loss function as a global prior instead of only its local gradient for guiding the attack optimization.

**Delta**: P-BO outperforms P-RGF (e.g., 100% vs 98.4% ASR, 15 vs 55 avg queries on ResNet-50 CIFAR-10)
**Condition**: Query-based black-box attacks where surrogate model is available

**Evidence**: "P-BO outperforms P-RGF, demonstrating the effectiveness of leveraging the surrogate model as a function prior rather than the gradient prior."

## [POSITIVE] Adaptive Integration Strategy (adaptive λ*)
Automatically adjusts a coefficient λ on the function prior by maximizing the log-likelihood of observed data, minimizing the RKHS norm between objective and prior, preventing degradation from a bad prior.

**Delta**: On ImageNet Inception-v3: 91.4% vs 60.8% ASR (P-BO λ* vs P-BO λ=1); on CIFAR-10 ResNet-50: 100% vs 99.9% ASR with 15 vs 16 avg queries
**Condition**: Especially important when surrogate and target models have lower similarity (e.g., ImageNet, different architectures)

**Evidence**: "the use of the adaptive coefficient λ* in P-BO enhances the attack success rates and reduces the average number of queries compared with λ=1, highlighting the effectiveness of using an adaptive coefficient derived by the proposed adaptive integration strategy."

## [NEGATIVE] Fixed Function Prior (λ=1)
Using the surrogate model's loss as the GP mean function with a fixed coefficient of 1, without adaptive adjustment.

**Delta**: On ImageNet Inception-v3: 60.8% ASR vs 89.2% for baseline BO; on MobileNet-v2: 78.7% vs 97.8% for BO
**Condition**: When surrogate and target models have low similarity, particularly on ImageNet with diverse architectures

**Evidence**: "fixing the adaptive integration coefficient λ=1 results in inferior performance compared with the baseline BO algorithm without incorporating priors. As discussed in Sec. 3.2, this phenomenon is attributed to the condition ∥f − f′∥k > ∥f∥k in Theorem 3.1, which may be due to the lower similarity between models on the ImageNet dataset."

## [POSITIVE] Dimensionality Reduction of Search Space
Reducing the search space dimensionality (e.g., from 224×224×3 to 56×56×3) as a data-dependent prior to improve query efficiency on high-resolution images.

**Delta**: P-BOD achieves 94.4% ASR with 81 avg queries vs 91.4% ASR with 115 avg queries for P-BO without reduction on Inception-v3
**Condition**: High-resolution image attacks (ImageNet 224×224), orthogonal to function prior

**Evidence**: "the results also validate that the data-dependent prior is orthogonal to the proposed function prior, since integrating the data-dependent prior leads to better results."

## [POSITIVE] Gaussian Process with Non-zero Mean Function
Modeling the attack objective with a GP whose mean is initialized to the surrogate model's loss f', so the GP models the residual f - f' rather than f directly.

**Delta**: Reduces regret bound by replacing ∥f∥k with ∥f - f'∥k when f' ≈ f
**Condition**: When surrogate model is similar to target model (RKHS norm condition ∥f - f'∥k < ∥f∥k satisfied)

**Evidence**: "incorporating the function prior f′ into the modeling of f using the Gaussian process GP(f′, k) involves substituting ∥f∥k with ∥f − f′∥k in the upper bound of the regret RT in BO. Consequently, when f′ ≈ f, employing the Gaussian process GP(f′, k) to model f significantly lowers the regret."

## [NEUTRAL] UCB Acquisition Function
Using Upper Confidence Bound as the acquisition function to balance exploration and exploitation when selecting the next query point.

**Delta**: Not separately quantified
**Condition**: Used as the acquisition function in both BO and P-BO for theoretical analysis and implementation

**Evidence**: "In this work, we choose UCB as the acquisition function to analyze the regret bound, which is expressed as α(x) = µT(x) + β·σT(x), where the coefficient β balances exploration and exploitation."

## [NEUTRAL] Matern-5/2 Kernel
Using the Matern-5/2 kernel function for the Gaussian process in both BO and P-BO.

**Delta**: Not separately quantified
**Condition**: Applied in both CIFAR-10 and ImageNet experiments for BO and P-BO

**Evidence**: "we set an initial dataset D containing S=10 randomly sampled points, and use the Matern-5/2 kernel."

## [POSITIVE] Normalization of Observations and Prior
Normalizing yT, y'T, and f' to a similar numerical range using mean and standard deviation before computing the posterior.

**Delta**: Not separately quantified; described as necessary for good numerical behavior
**Condition**: Applied at each iteration of P-BO to ensure stable optimization

**Evidence**: "we normalize yT, y'T, and f′ to a good and similar numerical range: yT ← (yT−µ)/σ, y'T ← (y'T−µ')/σ', f′ ← (f′−µ')/σ'"

## [POSITIVE] CW Loss Function
Using the Carlini-Wagner loss instead of cross-entropy loss as the attack objective function.

**Delta**: Not separately quantified; noted to perform better than cross-entropy on CIFAR-10
**Condition**: CIFAR-10 experiments

**Evidence**: "The loss function f is the CW loss (Carlini & Wagner, 2017) since it performs better than the cross-entropy loss on CIFAR-10."

## [POSITIVE] Adversarially Trained Surrogate for Defense Models
Using an adversarially trained model (e.g., Rice et al. 2020) as the surrogate when attacking other defense models, rather than a normally trained model.

**Delta**: P-BO achieves 36.2% ASR on Rice et al. defense vs lower rates for all baselines
**Condition**: Black-box attacks against adversarially trained defense models on CIFAR-10

**Evidence**: "We adopt Zhang et al. (2019) as the surrogate model when attacking the others, while adopting Rice et al. (2020) as the surrogate model when attacking Zhang et al. (2019), since a normally trained model can be hardly useful for attacking defenses."

## [NEUTRAL] Initial Random Dataset Construction
Constructing an initial dataset of S=10 randomly sampled points before starting the BO iterations.

**Delta**: S=10 initial queries included in total query count
**Condition**: Applied at the start of both BO and P-BO algorithms

**Evidence**: "we construct an initial dataset D = {(xi, yi)}^S_{i=1} by randomly sampling xi in the search space A and obtaining yi = f(xi)... Note that for BO and P-BO, the query count includes S=10 random queries constructing the initial dataset D."
