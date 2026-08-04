# Precise Accuracy / Robustness Tradeoffs in Regression: Case of General Norms

**Source**: https://proceedings.mlr.press/v235/dohmatob24c.html

## [POSITIVE] Regularized Model for Optimal Robustness
Using a proximal/regularized version of the generative model w_prox(λ) with explicit regularization parameter λ=r² to achieve optimal adversarial risk

**Delta**: attains optimal adversarial risk E_opt(r) up to multiplicative absolute constants
**Condition**: Linear regression under any attack norm and general covariance matrix

**Evidence**: "With λ = r², it holds that Eopt(r) ≍ E(w^prox(λ), r) ≍ σ² + F(r, r²). That is, up to within multiplicative absolute constants, w^prox(λ = r²) attains the optimal adversarial risk Eopt(r)."

## [POSITIVE] Ridge Regression for Euclidean-Norm Attacks
In the special case of Euclidean-norm attacks, the optimal robust model reduces to a ridge estimator w_opt(r) = (Σ + λI)^{-1}Σw_0 with explicit ridge parameter λ=r²

**Delta**: achieves optimal adversarial risk with explicit closed-form parameter vs implicit fixed-point equation in prior work
**Condition**: Euclidean-norm attacks on linear regression

**Evidence**: "our result above gives a much clearer understanding, since it proposes to use the explicit ridge parameter λ = r², which clearly highlights the dependence on the attack strength r"

## [POSITIVE] Free Lunch Threshold for Robustness
Identifying a threshold ε_FL(r) on excess risk above which no accuracy/robustness tradeoff is needed; models with ε ≥ ε_FL(r) can achieve optimal robustness without sacrificing accuracy

**Delta**: E_opt(r,ε) ≍ E_opt(r) when ε ≥ ε_FL(r), meaning no tradeoff penalty
**Condition**: Any attack norm and general covariance matrix when excess risk tolerance exceeds the free lunch threshold

**Evidence**: "If ε ≥ ε_FL(r), then it holds that Eopt(r, ε) ≍ Eopt(r). That is, no accuracy / robustness tradeoff is needed when the excess risk level ε is greater than the threshold ε_FL(r): there is always an ε-accurate model which achieves the absolute optimal adversarial risk Eopt(r)."

## [POSITIVE] Lagrangian Duality Analysis
Using basic Lagrangian duality instead of Gordon's Comparison Inequality to derive analytic results for general norms and covariance matrices

**Delta**: produces analytic results for general norms where Gordon's inequality fails
**Condition**: General attack norms and covariance matrices; Gordon's inequality only works for Euclidean-norm attacks on isotropic features

**Evidence**: "our analysis is based on basic Langrangian duality. It relies on some approximations which turn out to only introduce multiplicative absolute constants in the final result, but are completely harmless for the final analysis and interpretation"

## [NEGATIVE] Gordon's Comparison Inequality (prior work approach)
Using Gordon's Comparison Inequality for analysis of regularized estimators, as done in prior works like Javanmard et al. 2020

**Delta**: fails to produce analytic results outside Euclidean-norm attacks on isotropic features
**Condition**: Non-Euclidean attack norms or non-isotropic feature covariance matrices

**Evidence**: "the analysis in the latter is based on Gordon's Comparison Inequality (Gordon & Milman, 1988; Thrampoulidis et al., 2015; 2018), which is a very versatile tool in the analysis of regularized estimators but fails to produce analytic results when one deviates from the setting of Euclidean-norm attacks on isotropic features"

## [POSITIVE] Adversarial Risk Proxy Approximation
Using multiplicative approximations Ẽ(w,r) and Ê(w,r) of the adversarial risk E(w,r) to make the optimization tractable

**Delta**: introduces only multiplicative absolute constants, harmless for final analysis
**Condition**: General linear regression setting with any attack norm

**Evidence**: "The multiplicative approximations given in Lemma 3.1 suffice for our purposes whereby we only are interested in the orders of magnitude of the adversarial risk of models relative to the optimum value Eopt(r), as a function of the attack strength r."

## [NEUTRAL] Polynomial Spectral Decay with Source Condition
Modeling feature covariance eigenvalues and generative model alignment coefficients with power-law scalings λ_k ∝ k^{-β} and c_k ∝ k^{-δ/2-β/2}

**Delta**: phase transition at δ=1: free lunch for δ>1, unavoidable tradeoff for δ∈[0,1)
**Condition**: Euclidean-norm attacks on linear regression with polynomially-decaying spectral and source conditions

**Evidence**: "Thus, as regards robustness, δ = 1 is a critical value for the source exponent in (17): For δ ∈ [0, 1], accuracy (controlled by the excess risk tolerance ε) has to be traded for robustness, while for δ ∈ (1, ∞), the generative model w_0 is so smooth that robustness and accuracy are aligned."

## [POSITIVE] Smooth Ground-Truth Model (δ>1 regime)
When the source exponent δ>1, the generative model w_0 is sufficiently smooth that robustness and accuracy are simultaneously achievable

**Delta**: free lunch: E(w_0, r) ≍ E_opt(r), no tradeoff needed
**Condition**: Euclidean-norm attacks, polynomial spectral decay with source exponent δ>1

**Evidence**: "for δ ∈ (1, ∞), the generative model w_0 is so smooth that robustness and accuracy are aligned... for δ > 1, w_0 becomes robust to small adversarial perturbations (blue curve and broken black line coincide) as predicted"

## [NEGATIVE] Non-Smooth Ground-Truth Model (δ∈[0,1) regime)
When the source exponent δ∈[0,1), accurate models including the generative model w_0 itself are non-robust, requiring a tradeoff

**Delta**: E_opt(r,ε) ≍ σ² + ε² + r²ε^{-2φ}, power-law degradation with 1/ε
**Condition**: Euclidean-norm attacks, polynomial spectral decay with source exponent δ∈[0,1)

**Evidence**: "In the regime 0 ≤ δ < 1, the theorem predicts that even though robustness to imperceptible attacks is achievable in this setting, accurate models (especially the generative model w_0 itself) are non-robust."

## [NEUTRAL] OLS Estimator for Empirical Verification
Using ordinary least-squares (OLS) estimator to empirically verify theoretical predictions about adversarial risk tradeoffs

**Delta**: empirical results conform with theoretical predictions across all tested settings
**Condition**: Simulated data experiments verifying Theorems 5.1 and 5.2

**Evidence**: "Notice the conformity with the theorem's predictions... As n→∞, the adversarial risk E(w̃_n, r) of the estimator w̃_n approaches that of the ground-truth model, namely E(w_0, r); we see from the figure that is optimal in the smooth regime where δ > 1, but catastrophic in the non-smooth regime (δ ∈ [0, 1))"

## [POSITIVE] Early Stopping of Gradient Descent
For Euclidean-norm attacks, stopping gradient descent at an intermediate time corresponds to using the optimal ridge regularization parameter λ=r², achieving optimal robustness

**Delta**: GD+ run for time O(1/r²) achieves optimal adversarial risk E_opt(r) up to multiplicative absolute constants
**Condition**: Euclidean-norm attacks on linear regression using gradient descent

**Evidence**: "In the case of Euclidean-norm attacks, this translates to early-stopping gradient-descent at an intermediate-time... GD+ started from zero and run for time O(1/r²) achieves the optimal adversarial risk Eopt(r) (up to within multiplicative absolute constants)."

## [POSITIVE] Low-Dimensional Structure in Latent Models
When data enjoys a low-dimensional structure, the accuracy-robustness tradeoff is mitigated

**Delta**: tradeoff is mitigated (qualitative, from cited prior work)
**Condition**: Latent models where data has low-dimensional structure

**Evidence**: "(Javanmard & Mehrabi, 2021) also revisited this tradeoff for latent models and show that this tradeoff is mitigated when the data enjoys a low-dimensional structure."

## [NEUTRAL] Sparse Generative Model with ℓp-norm Attacks
Analyzing linear regression where the generative model w_0 is s-sparse under ℓp-norm attacks, yielding explicit phase-transition diagrams

**Delta**: E_opt(r) = σ² + (s/d)·min(r/r_0(p), 1)² with r_0(p) = s^{1/p-1/2}/√d
**Condition**: Isotropic features Σ=I_d with s-sparse generative model under ℓp-norm attacks

**Evidence**: "For ℓ∞-norm attacks of strength r, the adversarial risk of the generative mode w_0 is given by E(w_0, r) = σ² + r²∥w_0∥₁² = σ² + s²r²"

## [NEGATIVE] Harmonic Generative Model under ℓ∞-norm Attacks
Setting where w_0 has harmonically-decaying coefficients and features are isotropic, showing non-robustness of the generative model even when robustness is achievable

**Delta**: E(w_0, r) ≫ E_opt(r) for r ≍ 1/log d even with σ²=o(1)
**Condition**: ℓ∞-norm attacks with isotropic features and harmonically-distributed generative model coefficients

**Evidence**: "for r ≍ 1/log d and σ² = o(1), it holds that [E(w_0,r) ≫ E_opt(r)]. That is, even though robustness is achievable, the generative model w_0 is itself non-robust."

## [POSITIVE] General Covariance Matrix Extension
Extending analysis from isotropic (Σ=I_d) to general positive-definite covariance matrices Σ

**Delta**: covers all prior special cases and yields new results for non-isotropic settings
**Condition**: Linear regression with general feature distributions

**Evidence**: "unlike previous works like (Javanmard et al., 2020; Xing et al., 2021), our analysis applies to general attack norms (not just Euclidean) and covariance matrices (not just isotropic)"

## [POSITIVE] Restricting Optimization to a Chord (Shrinkage)
Restricting the search for optimal robust model to models co-linear with the generative model w_0 (i.e., scaled versions tw_0) to make the optimization tractable

**Delta**: gives correct value of K_opt(r,ε) up to multiplicative constants
**Condition**: Well-conditioned problems where r_0 ≍ r_1 in the proof of Theorem E.2

**Evidence**: "we will restrict the optimization to a line / chord in W_ε, parallel to the generative model w_0. It will turn out that up to within multiplicative constants, this strategy gives the correct value of K_opt(r, ε) as a function of all relevant problem parameters."
