# Effects of Exponential Gaussian Distribution on (Double Sampling) Randomized Smoothing

**Source**: https://proceedings.mlr.press/v235/shu24a.html

## [NEUTRAL] Exponential Standard Gaussian (ESG) smoothing distribution
A family of distributions generalizing Gaussian by varying the exponent η from 2 to any positive real number, used as the smoothing distribution in Randomized Smoothing

**Delta**: almost identical certification across different η values
**Condition**: High-dimensional settings (e.g., CIFAR-10, ImageNet) for both RS and DSRS frameworks

**Evidence**: "the certification provided by ESG distributions is highly insensitive to the alternation of η, which echos our theoretical analysis in Section 5. Currently, the mainstream view believes Gaussian is the best distribution to provide the ℓ2 certified radius for RS, and our results show many ESG can provide the best as well."

## [POSITIVE] Exponential General Gaussian (EGG) smoothing distribution
A family of distributions generalizing General Gaussian by varying the exponent η, used as the smoothing distribution in DSRS to address the curse of dimensionality

**Delta**: up to +6.4% certified accuracy on ImageNet compared to primitive DSRS
**Condition**: DSRS framework on real-world datasets (CIFAR-10 and ImageNet)

**Evidence**: "EGG brings a significant improvement to the DSRS certification, but the mechanism can be different when the classifier properties are different. Compared to the primitive DSRS, the increase in certified accuracy provided by EGG is prominent, up to 6.4% on ImageNet."

## [POSITIVE] Larger exponent η in EGG for real classifiers
Using EGG with larger η (e.g., η=8.0) as the smoothing distribution when real classifiers do not satisfy the concentration property

**Delta**: EGG η=8.0 outperforms DSRS baseline (EGG η=2.0) at all certified radii on both CIFAR-10 and ImageNet
**Condition**: Real classifiers that do not perfectly satisfy the concentration property

**Evidence**: "Table 3 reveals the phenomenon that certified accuracy at r increases with the η of EGG. On both CIFAR10 and ImageNet, our strategy to use EGG with a larger η (8.0 in the tables) performs obviously better than General Gaussian (EGG with η = 2.0) used in DSRS (Li et al., 2022). This is different from our theoretical analysis in 6, because real classifiers do not perfectly satisfy the concentration property."

## [POSITIVE] Smaller exponent η in EGG under concentration property
Using EGG with smaller η ∈ (0,2) when the base classifier satisfies the concentration property, providing tighter constant factors for Ω(√d) lower bounds

**Delta**: tighter constant factor µ for Ω(√d) lower bound; µ grows monotonically as η decreases for most d−2k ∈ [1,30]
**Condition**: Theoretical setting where base classifier satisfies the (σ,p,2)-concentration property

**Evidence**: "for values of d − 2k except 1, the tight constant factor µ increases monotonically as the η decreases. Essentially, these results demonstrate that the solution to the curse of dimensionality provided by Li et al. (2022) (with General Gaussian, namely η = 2 in EGG) can be improved by choosing smaller η ∈ (0, 2), for most d − 2k ∈ [1, 30] ∩ N."

## [NEGATIVE] Smaller exponent η in EGG on real classifiers
Using EGG with very small η (e.g., η=0.25) on real classifiers that do not satisfy the concentration property

**Delta**: EGG η=0.25 achieves only 7.1% certified accuracy at r=1.25 on ImageNet vs 28.9% for DSRS baseline (η=2.0)
**Condition**: Real classifiers on CIFAR-10 and ImageNet that do not satisfy the concentration property

**Evidence**: "Table 3 reveals the phenomenon that certified accuracy at r increases with the η of EGG. On both CIFAR10 and ImageNet, our strategy to use EGG with a larger η (8.0 in the tables) performs obviously better than General Gaussian (EGG with η = 2.0) used in DSRS"

## [POSITIVE] Double Sampling Randomized Smoothing (DSRS) with EGG
Using EGG as the smoothing distribution P and Truncated EGG (TEGG) as the supplementary distribution Q in the DSRS framework

**Delta**: DSRS with EGG η=8.0 outperforms NP with EGG at all radii, though the growth from DSRS relative to NP shrinks with increasing η
**Condition**: Real-world datasets with larger η values in EGG

**Evidence**: "For EGG, though the certification improves with η, Figure 5b reveals the growth brought by DSRS relative to NP shrinks with η, despite the fact that certified accuracy provided by DSRS keeps increasing."

## [NEUTRAL] Analytic formula approximation for ESG certified radius
Deriving a closed-form analytic relation between sampling probability A and certified radius ρ for ESG under high-dimensional assumptions, converging to Cohen et al. (2019)'s Gaussian formula

**Delta**: formula converges to Cohen et al. (2019) as d increases; verified experimentally on CIFAR-10 (d=3072) and ImageNet (d=150224)
**Condition**: High-dimensional settings satisfying d ≫ η and σ ∈ (0,1]

**Evidence**: "our analytic formula for ESG highly approximates Cohen et al. (2019)'s at a sufficiently large dimension... Interestingly, though the exponent η is a significant parameter for the derivation on ESG, this estimation (14) is irrelevant to η."

## [POSITIVE] Linear Numerical Integration (LNI) method
A custom numerical integration method that uniformly segments the integration interval using the concentration property of the gamma distribution, replacing scipy for large parameter regimes

**Delta**: segs=256 curves almost overlap with Cohen's formula on ImageNet; segs≥128 sufficient for CIFAR-10
**Condition**: ESG experiments where scipy loses precision for Γ(a,1) with large parameters (a>500)

**Evidence**: "we implement a Linear Numerical Integration (LNI) method to compute the expectations fast and accurately based on Lemma 5.6... we find the LNI method that uniformly segments the integration interval provides good precision for certifications on CIFAR-10 and ImageNet."

## [POSITIVE] Concentration property assumption for EGG theoretical analysis
Assuming the base classifier satisfies the (σ,p,η)-concentration property, meaning it predicts almost perfectly on examples perturbed by noise with ‖z‖₂ < T

**Delta**: enables proof that EGG with η ∈ (0,2) certifies Ω(√d) lower bounds with tighter constant factors than DSRS baseline
**Condition**: Theoretical analysis; idealized classifiers satisfying concentration property

**Evidence**: "when the base classifier satisfies the concentration property, EGG with η ∈ (0, 2) brings significant enhancement for the lower bound of the certified radius offered by DSRS (Li et al., 2022). Obviously, it is hard for the realistic model to be perfectly concentrated, thus EGG takes different effects under real classifiers."

## [NEUTRAL] Fixed formal variance across distributions
Setting formal variance σs and σg such that E[r²] is constant across all smoothing distributions for fair comparison

**Delta**: enables fair comparison across different η values and distribution families
**Condition**: All experiments comparing ESG and EGG distributions with different exponents η

**Evidence**: "Following the settings in the previous studies (Yang et al., 2020; Li et al., 2022), we set the formal variance to ensure E r² is a constant for all the smoothing distributions."

## [NEUTRAL] EGG improvement upper bound convergence
The observation that EGG's certified accuracy improvement over NP diminishes with increasing η and appears to converge toward Gaussian's certification level

**Delta**: growth of DSRS relative to NP shrinks with η; upper bound appears to be Gaussian's certification
**Condition**: EGG under DSRS framework as η increases beyond 2.0

**Evidence**: "For EGG, though the certification improves with η, Figure 5b reveals the growth brought by DSRS relative to NP shrinks with η, despite the fact that certified accuracy provided by DSRS keeps increasing. Furthermore, we see there is likely to be an upper bound for the DSRS certification: Gaussian's certification (in this work, η = 2 for ESG)."
