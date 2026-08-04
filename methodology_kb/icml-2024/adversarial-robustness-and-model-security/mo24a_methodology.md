# TERD: A Unified Framework for Safeguarding Diffusion Models Against Backdoors

**Source**: https://proceedings.mlr.press/v235/mo24a.html

## [POSITIVE] Unified Loss for Trigger Reversion
Derives a unified backdoor loss formulation covering all current attacks (BadDiffusion, TrojDiff, VillanDiffusion) by applying triangle inequality to eliminate dependency on inaccessible attack-specific coefficients

**Delta**: l2 norm reduced from 32.90 to 20.69 (BadDiffusion), 22.60 to 4.26 (TrojDiff), 43.03 to 30.03 (VillanDiffusion) vs Elijah baseline
**Condition**: Trigger reversion across all pixel-level backdoor attacks on diffusion models

**Evidence**: "Note that Equation 12 unifies the expression of all current attacks from the reversed loss, free of the trade-off between the detailed formulations."

## [POSITIVE] Trigger Estimation (TE) via Surrogate Distribution
Approximates unknown target images by sampling from a standard Gaussian prior distribution, exploiting the theoretical property that backdoor diffusion processes converge to the prior at large timesteps

**Delta**: TE alone achieves l2 norm of 21.90, TPR 100%, TNR 94.44% for input detection, TPR 33.33% TNR 88.89% for model detection
**Condition**: First stage of two-stage trigger reversion; effective when t is close to T

**Evidence**: "Therefore, we can substitute x0 with a surrogate image xˆ0 sampled from a substitute distribution, e.g., the standard gaussian distribution pˆprior, to estimate xt."

## [POSITIVE] Trigger Refinement (TR) via Differential Multi-step Samplers
Refines the estimated trigger using differentiable n-step DDIM/Heun samplers to obtain a more precise representation of the target image x0, leveraging both ending and beginning constraints of the diffusion process

**Delta**: TR alone achieves l2 norm of 23.56, TPR 100%, TNR 100% for input detection, TPR 100% TNR 77.78% for model detection
**Condition**: Second stage of two-stage trigger reversion; uses n=10 steps DDIM sampler

**Evidence**: "it motivates us to estimate xt with multi-step generations... we can obtain the target image x0 with the trigger r"

## [POSITIVE] Combined TE + TR (Two-stage Trigger Reversion)
Sequential combination where Trigger Estimation initializes the trigger with a rough estimate, which then serves as initialization for Trigger Refinement, reducing randomness and optimization difficulty

**Delta**: Combined achieves l2 norm of 18.33 (best), 100% TPR and TNR across all detection tasks
**Condition**: Full TERD framework on CIFAR-10 across BadDiffusion, TrojDiff, VillanDiffusion

**Evidence**: "combining them together can obtain a more powerful defense: lower l2 norm between the reversed and the original trigger, both TPR and TNR reaches 100%"

## [POSITIVE] L1 Norm Regularization on Trigger
Adds L1 norm penalty on the reversed trigger with trade-off coefficient lambda to prevent the trigger from collapsing to the zero vector during optimization

**Delta**: prevents degenerate solution; enables accurate trigger recovery
**Condition**: Applied during both trigger estimation and refinement stages

**Evidence**: "To avoid r collapses to the full-zero vector, we introduce l1 norm for penalization and λ as the trade-off coefficient"

## [POSITIVE] Input Detection via Distribution Probability Comparison
Detects backdoor inputs by comparing the probability of an input noise under the benign distribution N(0,I) versus the reversed backdoor distribution N(r, gamma^2), filtering inputs where backdoor probability exceeds benign probability

**Delta**: 100% TPR and TNR for input detection across all attacks and datasets
**Condition**: Inference-time input detection for diffusion models; first such method proposed for diffusion models

**Evidence**: "Empirically, if ε¯ is a backdoor input, Φbd(ε¯) will be greater than Φbe(ε¯) and vice versa."

## [POSITIVE] Model Detection via KL Divergence in Trigger Space
Detects backdoor models by computing KL divergence between the reversed trigger distribution N(r, gamma^2) and benign distribution N(0,I), extracting mean (Mr) and variance (Vr) of dimensional-wise divergence as features

**Delta**: 100% TPR and TNR for model detection vs Elijah's 100%/51.67% TPR/TNR on BadDiffusion, 0%/100% on TrojDiff, 3%/62.33% on VillanDiffusion
**Condition**: Model-level backdoor detection; outperforms Elijah especially on TrojDiff and VillanDiffusion

**Evidence**: "our proposed model detection method is performed in the trigger space rather than the image space... we introduce Kullback-Leibler (KL) divergence, a metric that measures the distance between the reversed distribution N(r, γ2) and benign distribution N(0, I)"

## [POSITIVE] Benign-Only (BO) Model Detection with 3-sigma Criterion
When only benign models are available, uses 3-sigma statistical criterion on Mr and Vr computed from benign models to set detection thresholds, flagging models exceeding mean + 3*std as backdoored

**Delta**: 100% TPR and TNR in BO setting vs Elijah's 68%/21.55% (BadDiffusion), 60%/47.50% (TrojDiff), 50%/58.33% (VillanDiffusion)
**Condition**: Benign-only scenario where no backdoor models are available for training a detector

**Evidence**: "According to the 3σ criterion, any model that achieves Mr > µm + 3 ∗ γm or Vr > µv + 3 ∗ γv will be regarded as the backdoor model."

## [POSITIVE] Dataset-Agnostic Feature Extraction for Model Detection
The Mr and Vr features for model detection are agnostic to image size, allowing a detector trained on small datasets (CIFAR-10) to transfer to large datasets (CelebA, CelebA-HQ) without retraining

**Delta**: 100% TPR and TNR on CelebA and CelebA-HQ using detector trained on CIFAR-10
**Condition**: Cross-dataset generalization; reduces computational cost for large-scale datasets

**Evidence**: "Since our extracted features for model detection are agnostic to the image size, we use the same detection model and the threshold adopted by the CIFAR-10 dataset."

## [NEGATIVE] Elijah's Heuristic d(t)=0.5 Assumption
Baseline method Elijah assumes d(t)=0.5 as a trade-off between BadDiffusion and TrojDiff formulations rather than deriving a unified loss

**Delta**: Elijah achieves 0% TPR on TrojDiff model detection, 3% TPR on VillanDiffusion model detection
**Condition**: Elijah baseline applied to TrojDiff and VillanDiffusion attacks

**Evidence**: "In Elijah (An et al., 2023), they heuristically assume d(t) = 0.5 and make a trade-off between BadDiffusion and TrojDiff... This could lead to the failure of defense, particularly in some difficult cases."

## [NEGATIVE] Elijah's Image-Space Model Detection
Elijah detects backdoor models by generating target images with reversed triggers and checking for high similarity, which fails when target images are diverse or when trigger quality is poor

**Delta**: Elijah TPR: 100%/51.67% TNR on BadDiffusion, 0%/100% on TrojDiff, 3%/62.33% on VillanDiffusion for model detection
**Condition**: Elijah baseline; fails particularly on TrojDiff which supports diverse multi-image targets

**Evidence**: "the quality of generated images with the reversed triggers by Elijah will severely decline in some circumstances. Instead of detecting the poisoned models with the generated images, our proposed TERD performs model detection with the KL divergence of the reversed trigger."

## [NEGATIVE] Adaptive Attack with Scaled Trigger
Adversarial scaling of trigger by factor eta to bring backdoor distribution closer to benign distribution, attempting to bypass distribution-based detection

**Delta**: TERD performance degrades when eta is extremely low (e.g., 0.1 for TrojDiff)
**Condition**: Adaptive attack scenario; however at very low eta the attack itself becomes ineffective due to loss of benign utility

**Evidence**: "we observe that when η is extremely low, e.g. 0.1 for TrojDiff, the performance of TERD will degrade."

## [POSITIVE] SDE-based Framework Generalization
TERD's unified SDE-based formulation allows it to be applied to other SDE-based generative models beyond standard diffusion models, including score-based models and consistency models

**Delta**: 100% TPR and TNR on Score-based Model and Consistency Model
**Condition**: Applied to Score-based Models and Consistency Models under VillanDiffusion attack

**Evidence**: "Surprisingly, we show that TERD can be flexibly adapted and safeguard those models... This demonstrates the good transferability of TERD to SDE-based models and its excellent scalability even for some unknown models designed with similar principles."

## [NEUTRAL] Cosine Learning Rate Schedule with SGD
Uses SGD optimizer with learning rate 0.5 adaptively adjusted via cosine schedule for trigger optimization

**Delta**: part of overall system achieving 100% TPR/TNR
**Condition**: Trigger estimation and refinement optimization on CIFAR-10 and larger datasets

**Evidence**: "We choose SGD as our optimizer with 0.5 learning rate which is adaptively adjusted with the cosine learning rate schedule."

## [POSITIVE] Varied Trigger Size and Poison Rate Robustness
TERD evaluated across four different trigger sizes and four different poison rates (minimum 2%) to test adaptability

**Delta**: 100% successful detection rates in all settings
**Condition**: Ablation study on CIFAR-10 with BadDiffusion, TrojDiff, VillanDiffusion

**Evidence**: "The results demonstrate that TERD obtains 100% successful detection rates in all settings. It reveals that TERD exhibits excellent adaptability to attack with different configurations."
