# PID: Prompt-Independent Data Protection Against Latent Diffusion Models

**Source**: https://proceedings.mlr.press/v235/li24ay.html

## [POSITIVE] Prompt-Independent Defense (PID)
A defense method that manipulates the visual encoder's latent distribution (both mean and variance) using the Ladd-log loss, completely independent of textual prompts, to protect images against LDM fine-tuning misuse.

**Delta**: FDS 0.205 vs 0.330-0.344 for best baseline (cprot=cexplo, frozen TE, SD v1.5); FID 411.990 vs 295.415 for best baseline
**Condition**: Both prompt-matched and prompt-mismatched scenarios on CelebA-HQ with SD v1.5 and v2.1

**Evidence**: "Remarkably, despite consuming significantly less computational resources (approximately 20% GPU memory, 5G v.s. 24G), PID achieves comparable, if not superior, performance compared to the three algorithms incorporating UNet across all four training configurations."

## [POSITIVE] Ladd-log Loss
A joint optimization target that simultaneously maximizes the distance between the mean and the log-variance of the perturbed and clean latent distributions, addressing the magnitude disparity between mean (~10^2) and variance (~10^-3).

**Delta**: FDS 0.329 vs 0.377 for Lmean/Lsample/Ladd; FID 411.990 vs ~265-271 for alternatives
**Condition**: Visual encoder perturbation for data protection against LDM fine-tuning

**Evidence**: "Ladd-log (the purple line in Figure 5a and Figure 5b) is the only defense target that shifts both statistics away from their normal values significantly with averaged l2 distance of the mean being 3.5 and 0.06 for variance."

## [NEGATIVE] Prompt-Mismatch Exploitation
Data exploiters use different textual prompts during fine-tuning than those used by data protectors during the protection stage, breaking the prompt-consistency assumption of existing defenses.

**Delta**: FDS increases 35% (0.277 to 0.387); FID decreases 30% (307.421 to 203.916) for FSGM
**Condition**: Applied to prompt-dependent defenses FSGM and ASPL on CelebA-HQ

**Evidence**: "when the fine-tuning prompts do not match the protecting prompts, the metric FDS increases over 35% (0.277→0.387) and the metric FID decreases 30% (307.421→203.916)."

## [POSITIVE] Variance Manipulation (Lvar)
Maximizing the distance between the variances of the clean and perturbed latent distributions to disrupt LDM fine-tuning.

**Delta**: FDS 0.329 vs 0.480 clean; FID 265.337 vs 144.570 clean
**Condition**: Standalone visual encoder perturbation; outperforms mean manipulation on FDS and FID metrics

**Evidence**: "a large variance significantly prohibits the model from grasping the core concepts of the images (low FDS and high FID)."

## [POSITIVE] Mean Manipulation (Lmean)
Maximizing the l2 distance between the mean of the perturbed and clean latent distributions to disrupt LDM fine-tuning.

**Delta**: FDS 0.370 vs 0.480 clean; FID 243.292 vs 144.570 clean, but weaker than Lvar
**Condition**: Standalone visual encoder perturbation; primarily affects texture rather than semantic content

**Evidence**: "a large mean difference with the clean images mainly influences the texture of the output images, making them appear covered with heavy noise (low IQS and high BRISQUE)."

## [POSITIVE] PID Hybridization with Existing Defenses
Combining PID (Ladd-log) with prompt-dependent defenses (ASPL, FSGM) via weighted joint optimization with tradeoff coefficient lambda=0.05.

**Delta**: ASPL+PID FDS 0.254 vs ASPL 0.370 (frozen TE); FID 352 vs 271 for ASPL alone
**Condition**: Prompt-mismatched scenario on SD v1.5 with lambda*=0.05

**Evidence**: "ASPL+PID is much more robust than ASPL regardless of whether the text encoder is frozen or not, as supported by the notably lower FDS (0.254 v.s. 0.370, 0.335 v.s. 0.412) and higher FID (352 v.s. 271, 208 v.s. 199)."

## [NEUTRAL] FSGM+PID Joint Optimization
Combining FSGM with PID via weighted combination; improves semantic protection but fails to improve image quality metrics.

**Delta**: Lower FDS than FSGM alone, but fails to improve IQS
**Condition**: Prompt-mismatched scenario; sub-optimal lambda or joint optimization difficulty

**Evidence**: "We do not ignore the fact that combining PID with FSGM fails to do better in image quality, which might be attributed to a sub-optimal λ* choice or the difficulty of joint optimization."

## [NEUTRAL] Lsample Loss
Disrupting the sampled latent representations z=E(x,epsilon) including the reparameterization noise, as used in prior work (Liang et al., 2023).

**Delta**: FDS 0.377, FID 265.588 vs Ladd-log FDS 0.329, FID 411.990
**Condition**: Visual encoder perturbation; suboptimal because it does not significantly perturb variance

**Evidence**: "The loss functions adopted by previous literature, Lmean, LT_mean, and Ladd, exhibit sub-optimal performance compared to Ladd-log. The similar behaviors of Lmean, Lsample, and Ladd can be well explained by observations in Figure 5a and Figure 5b, as all of them mostly focus on the mean value."

## [NEUTRAL] Ladd Loss (excluding reparameterization noise)
Variant of Lsample that excludes epsilon from the optimization to reduce randomness, optimizing mean+variance without log scaling.

**Delta**: FDS 0.377, FID 268.260 vs Ladd-log FDS 0.329, FID 411.990
**Condition**: Visual encoder perturbation; similar to Lsample, mostly affects mean not variance

**Evidence**: "The loss functions adopted by previous literature, Lmean, LT_mean, and Ladd, exhibit sub-optimal performance compared to Ladd-log."

## [NEUTRAL] Targeted Mean Manipulation (LT_mean)
Manipulating the mean of the latent distribution toward a specific target image (as done in Mist/Liang & Wu 2023).

**Delta**: FDS 0.377, FID 271.540 vs Ladd-log FDS 0.329, FID 411.990
**Condition**: Visual encoder perturbation; suboptimal compared to Ladd-log

**Evidence**: "The loss functions adopted by previous literature, Lmean, LT_mean, and Ladd, exhibit sub-optimal performance compared to Ladd-log."

## [POSITIVE] Cross-Model Transferability of PID
PID perturbations generated on one SD version (v1.5 or v2.1) transfer to protect against fine-tuning on the other version.

**Delta**: PID FDS 0.268 (v2.1->v1.5) and 0.265 (v1.5->v2.1) vs baselines 0.311-0.371 and 0.372-0.407
**Condition**: Cross-model transfer between SD v1.5 and SD v2.1 with frozen text encoder

**Evidence**: "PID enjoys great transferability between the two model versions as shown in Table 5, which might be due to the similarity in the condensed representations of images."

## [NEGATIVE] Zero Sigma Adaptive Attack
Adaptive attack that fixes the standard deviation of the perturbed latent distribution to zero during fine-tuning to counteract PID's variance manipulation.

**Delta**: PID still achieves FDS=0.253, IQS=-9.313 under this attack
**Condition**: Adaptive attack against PID; attack is ineffective because zero variance causes overfitting

**Evidence**: "a zero standard value will make the finetuning process easier to overfit and lead to inferior generation results. Our results also reveal that PID works very well in such training settings with FDS=0.253 and IQS=−9.313."

## [NEGATIVE] Clipped/Fixed Sigma Adaptive Attack
Adaptive attack that clips or fixes the standard deviation to a small normal value (e.g., 10^-7) rather than zero to mitigate PID's variance disruption.

**Delta**: Weakens PID's IQS influence but FDS remains below 0.3
**Condition**: Adaptive attack against PID on SD v1.5; partially reduces image quality degradation but not semantic protection

**Evidence**: "Adopting the attack, we observe PID's influence on image quality is weakened, with the improved IQS and decreased FID shown in Table 6. However, the FDS is still very low (<0.3), rendering the attack ineffective."

## [NEGATIVE] JPEG Compression Data Corruption
Post-processing the protected images with JPEG compression before fine-tuning, which can degrade adversarial perturbations.

**Delta**: PID FDS 0.345, FID 221.601 under compression vs FDS 0.246, FID 275.468 under cropping
**Condition**: Data corruption robustness evaluation; JPEG compression is PID's weakest scenario

**Evidence**: "PID shows comparable performance to the AdvDM and FSGM even in its worst case, the JPEG compression. However, the huge performance drop when compressed still signals the need to design more robust protection algorithms against image compression."

## [NEUTRAL] Random Resizing and Cropping Corruption
Applying random resize and crop to protected images before fine-tuning as a data corruption attack.

**Delta**: PID FDS 0.246, FID 275.468 under cropping, still best among all defenses
**Condition**: Data corruption robustness; PID maintains best FDS among all defenses

**Evidence**: "PID, the simplest defense among the four algorithms, withstands all four corruptions as evidenced by consistently low FDS and high FID."

## [NEGATIVE] Prompt Ensemble for Prompt-Independent Defense
Naive approach of aggregating across multiple prompts during optimization to reduce prompt dependency of existing defenses.

**Delta**: Does not fundamentally resolve prompt dependency issue
**Condition**: Alternative approach to prompt-independent defense; computationally expensive and ineffective

**Evidence**: "aggregating through k prompts increases the computational cost by k times and makes the objective even harder to solve. In Table 10, we show that a naive ensembling of prompts to generate the perturbations won't fundamentally resolve the issue."

## [POSITIVE] Visual Encoder Focus (vs UNet)
Using only the visual encoder (VAE) for computing protection perturbations instead of backpropagating through the full UNet.

**Delta**: ~20% GPU memory usage (5GB vs 24GB) with comparable or superior protection performance
**Condition**: Computational efficiency; enables protection on lower-resource hardware

**Evidence**: "despite consuming significantly less computational resources (approximately 20% GPU memory, 5G v.s. 24G), PID achieves comparable, if not superior, performance compared to the three algorithms incorporating UNet across all four training configurations."

## [NEGATIVE] Unfreezing Text Encoder During Fine-tuning
Fine-tuning both the UNet and text encoder simultaneously during the exploitation stage, as opposed to freezing the text encoder.

**Delta**: PID FDS increases from 0.205 to 0.257 (cprot=cexplo, SD v1.5) when text encoder is unfrozen
**Condition**: Fine-tuning configuration; unfreezing text encoder slightly reduces PID effectiveness but PID still outperforms baselines

**Evidence**: "when the text encoder is frozen, i.e., not trained, during finetuning, PID consistently prohibits the LDMs from learning useful semantical information, resulting in notably poor facial similarity (0.254 for SD v1.5 and 0.285 for SD v2.1)."

## [POSITIVE] PGD1000 Optimization for Perturbation Generation
Using 1000-step PGD with l-infinity constraint (epsilon=0.05) to optimize the protective perturbations.

**Delta**: Achieves strong protection (FDS 0.205, FID 411.990) with perturbation budget 0.05
**Condition**: Default configuration for PID generation

**Evidence**: "We generate PID with PGD1000 (Madry et al., 2018) and the perturbation budget is set to epsilon_inf = 0.05."

## [POSITIVE] PNG Format for Saving Perturbed Images
Saving protected images in lossless PNG format to preserve adversarial perturbations.

**Delta**: Preserves full perturbation effect; JPEG compression causes notable performance drop
**Condition**: Image storage format; lossless format preserves perturbations unlike JPEG

**Evidence**: "The perturbation budget is set to 0.05 and the perturbed images are saved in PNG format in this paper unless otherwise specified."
