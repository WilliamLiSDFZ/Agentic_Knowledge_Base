# Consistent Adversarially Robust Linear Classification: Non-Parametric Setting

**Source**: https://proceedings.mlr.press/v235/dohmatob24a.html

## [POSITIVE] Gaussian Smoothing of Adversarial 0/1 Loss
Replacing the discontinuous adversarial 0/1 loss (step function at margin epsilon) with a smoothed surrogate using a survival function Q (e.g., Gaussian survival function), parameterized by bandwidth h, to make the empirical risk differentiable and tractable for optimization.

**Delta**: achieves consistency and minimax excess adversarial risk of O~(sqrt(d/n))
**Condition**: Non-parametric binary linear classification with mild regularity (small-ball) conditions on the conditional feature distribution

**Evidence**: "our proposed estimator can achieve the minimax excess adversarial risk of O~(sqrt(d/n)) for linear classifiers, at the cost of solving possibly rougher optimization problems."

## [POSITIVE] Adaptive Smoothing Bandwidth
Choosing the smoothing bandwidth hn to depend on both sample size n and input dimension d, specifically hn ≍ sqrt((d/n) log n), so that hn → 0 as n → ∞, rather than using a fixed static bandwidth.

**Delta**: achieves consistency (vanishing adversarial regret); non-adaptive bandwidth h=1 fails to converge to Bayes-optimal adversarial risk
**Condition**: Required for consistency; static bandwidth leads to inconsistency as shown empirically in Figure 4

**Evidence**: "A key idea in our work is to not consider static surrogate losses as in (Bao et al., 2020), but to adapt a smoothing bandwidth h = hn so that it vanishes with sample size n at a precise rate (20)... Non-adaptive bandwidth h = 1 corresponds to (Bao et al., 2020); unlike our proposed estimator (adaptive bandwidth hn), it fails to achieve the optimal adversarial risk."

## [POSITIVE] Non-Convex Smooth Surrogate Loss
Using non-convex but smooth loss functions (e.g., sigmoid-based or Gaussian-based surrogates) instead of convex surrogates for the adversarial 0/1 loss, since no consistent convex surrogate exists for adversarial classification.

**Delta**: provably consistent w.r.t adversarial 0/1 risk; convex surrogates are provably inconsistent
**Condition**: Adversarial classification with epsilon > 0; convex surrogates are known to be inconsistent (Bao et al., 2020)

**Evidence**: "our surrogate losses will be non-convex... for a class of non-convex smooth loss function (e.g sigmoid, Gaussian, etc.), the resulting estimator is consistent w.r.t adversarial 0/1 risk"

## [POSITIVE] Optimization on Riemannian Manifold (Trust-Region Methods)
For Euclidean-norm attacks, the optimization over the dual-norm unit sphere is cast as smooth optimization on a Riemannian manifold (sphere), solved using trust-region methods via the Manopt library.

**Delta**: enables efficient computation of the estimator for Euclidean-norm attacks
**Condition**: Euclidean-norm or Mahalanobis-norm adversarial attacks

**Evidence**: "In the case where the attack is measured w.r.t Euclidean norm, or more generally, Mahalanobis norms, (13) thus corresponds to a smooth optimization optimization on a smooth sphere-like Riemannian manifold. This is a standard problem, and there are lots of efficient algorithms (Boumal et al., 2018). We use trust-region-based methods (Absil et al., 2007) implemented in the Manopt library."

## [POSITIVE] Small-Ball (Lévy Concentration) Assumption on Feature Distribution
A mild regularity condition requiring that the margin random variable yf(x) does not concentrate too much mass near any single point, formalized via the Lévy concentration function. This is satisfied when class-conditional feature distributions have densities.

**Delta**: sufficient for consistency guarantee (Theorem 4.1) and minimax rate O~(sqrt(d/n)) (Theorem 4.2)
**Condition**: Non-parametric setting; no parametric or well-separatedness assumptions needed beyond this regularity

**Evidence**: "Assumption 4.1 is very mild, and holds under rather very general conditions... the assumption holds if the distribution of the feature vector x conditioned y = l for any fixed value l ∈ {±1} of the label y has density (w.r.t to Lebesgue measure on R^d)."

## [NEUTRAL] Bandwidth-Controlled Tradeoff Between Optimization Difficulty and Statistical Convergence
The smoothing bandwidth hn controls a tradeoff: smaller hn makes optimization harder (larger smoothness constant L = O(||Σ_n||_op / h_n^2)) but improves statistical convergence; larger hn eases optimization but degrades statistical accuracy.

**Delta**: consistency achievable with very slow hn → 0 (linear time optimization); minimax rate requires specific hn = sqrt((d/n) log n)
**Condition**: Applies generally; specific tradeoff depends on application requirements

**Evidence**: "The bandwidth parameter hn trades between ease of optimization and rate of statistical convergence of the adversarial risk estimator to the Bayes-optimal value... if we are only interested in consistency (and no quantitative rates), then our proposed estimator can be made to run in linear time (i.e fast optimization) by tuning the smoothing bandwidth hn such that hn → 0 only very slowly."

## [NEGATIVE] Extreme Smoothing (Large Bandwidth)
Using a very large smoothing bandwidth h, which makes the optimization problem easy but destroys the statistical information in the training dataset.

**Delta**: destroys information in training dataset; fails to achieve optimal adversarial risk
**Condition**: When bandwidth h does not vanish with n

**Evidence**: "Extreme smoothing (large h) makes the optimization problem very easy but essentially destroys the information contained in the training dataset Dn."

## [POSITIVE] VC Theory for Uniform Convergence Bound
Using Vapnik-Chervonenkis theory to bound the uniform convergence of the empirical adversarial risk to the population adversarial risk, leveraging the fact that the VC dimension of the linear classifier function class is at most d.

**Delta**: contributes O~(sqrt(d/n)) term to the excess adversarial risk bound
**Condition**: Used in the proof of Theorem 4.2 for the statistical analysis

**Evidence**: "The first term in the above decomposition is controlled using classical uniform convergence arguments (Vapnik & Chervonenkis, 1971; Vapnik, 2000); it is of order O(sqrt((d/n) log n)) since the VC pseudo-dimension of F_lin is at most d."

## [NEUTRAL] Kernel Density Estimation Interpretation of Smoothed Loss
When Q is a survival function of a random variable with density, the smoothed empirical adversarial risk corresponds to replacing the empirical marginal distribution of data points with a kernel density estimate (KDE) of the margin distribution.

**Delta**: provides theoretical interpretation; no separate quantitative improvement claimed
**Condition**: When Q is the survival function of a random variable with density

**Evidence**: "the smoothed loss then corresponds replacing the empirical marginal distribution of the data points x1,...,xn ∈ R^d by its kernel density estimate (KDE), constructed via the smoothing function sQ := Q′"

## [NEGATIVE] Convergence to Stationary Point Only (No Global Optimum Guarantee)
The optimization algorithm only guarantees convergence to a stationary point of the smoothed empirical risk, not the global optimum, due to non-convexity.

**Delta**: theoretical gap; empirically global optimum is observed in all experiments
**Condition**: Non-convex optimization of the smoothed adversarial risk

**Evidence**: "Note that we are only able to guarantee convergence to a stationary point of E~_{n,ϵ,h}. However, in all our experiments, we observe that the numerically obtained stationary point is also the global optimum. A rigorous study of this aspect will done in a future work."
