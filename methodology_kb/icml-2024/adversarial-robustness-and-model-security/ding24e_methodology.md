# Robust Stable Spiking Neural Networks

**Source**: https://proceedings.mlr.press/v235/ding24e.html

## [POSITIVE] Dynamic LIF (DLIF) Neuron
A modified LIF neuron with a trainable dynamic parameter a[l][t] added to each time step input, replacing the fixed leaky factor with a learnable one to better minimize L2 gain of perturbation dynamics.

**Delta**: outperforms baseline LIF in most attack scenarios
**Condition**: Applied across CIFAR-10 and CIFAR-100 with VGG11 and WRN16 architectures

**Evidence**: "For VGG11 on CIFAR-10 and CIFAR-100, SNN with DLIF outperforms SNN with vanilla LIF in most cases of attack. This implies that DLIF itself has the capability of improving robustness, though it is not significant."

## [POSITIVE] MS-MPPD Minimization (ρ=1)
Minimizing the mean square of membrane potential perturbation dynamics (MS-MPPD) for the last spiking neuron layer as an auxiliary loss term to align internal representations between clean and perturbed inputs.

**Delta**: +8.49% PGD10 (29.06% to 37.55%), +10.2% APGD10_CE (23.05% to 33.25%), +9.8% APGD10_DLR (29.88% to 39.68%) for DLIF VGG11 AT on CIFAR-10
**Condition**: Most effective when combined with adversarial training; also improves Gaussian noise training

**Evidence**: "For VGG11 with DLIF, training with ρ = 1 improves the performance of PGD10, APGD10 CE, and APGD10 DLR from 29.06%, 23.05%, and 29.88%, respectively, to 37.55%, 33.25%, and 39.68%, respectively, compared with those when ρ = 0."

## [POSITIVE] Adversarial Training (AT)
Training with adversarially perturbed inputs using RFGSM with initial random step of 0.001 and fast-gradient-sign step with ε=4/255, combining clean and adversarial losses via mixup.

**Delta**: DLIF VGG11 AT ρ=0 achieves PGD7=30.57% vs 0.09% for natural training on CIFAR-10
**Condition**: Applied on CIFAR-10 and CIFAR-100 with VGG11 and WRN16

**Evidence**: "DLIF, VGG11, AT, ρ=0.0 achieves PGD7 of 30.57 compared to DLIF, VGG11, Natural which achieves 0.09 on CIFAR-10."

## [POSITIVE] Adversarial Training + Regularizer (AT+Reg)
Combining the proposed MS-MPPD framework with the spectral norm regularizer from SNN-RAT (Ding et al., 2022), as the two methods are orthogonal and have consistent optimization goals.

**Delta**: PGD7 of 56.71% for WRN16 and 49.02% for VGG11 on CIFAR-10 vs 45.23% for SNN-RAT baseline
**Condition**: CIFAR-10 and CIFAR-100 with VGG11 and WRN16

**Evidence**: "Our regularized model with ρ = 1 gives PGD7 accuracy of 49.02% and 56.71% for VGG11 and WRN16, respectively, on CIFAR-10, higher than 45.23% of SNN-RAT."

## [POSITIVE] Membrane Potential Perturbation Dynamics (MPPD) as Metric
Using the simplified membrane potential perturbation dynamics (without spike reset effects) as a continuous-space metric for measuring perturbation intensity, replacing discrete spike-based metrics like TASAD and STD.

**Delta**: Training with MS-MPPD achieves PGD7=28.33% vs TASAD=27.80% and STD=26.82% in ablation study
**Condition**: Ablation study on VGG-5 CIFAR-10 with adversarial training, ρ=1

**Evidence**: "Training with TASAD or STD is not as effective at increasing robustness as training with MS-MPPD."

## [POSITIVE] Gaussian Noise Training
Training with Gaussian noise perturbation (ε=8/255) as an alternative to adversarial training to improve robustness.

**Delta**: +3.94% improvement for VGG11 and +1.99% for WRN16 on CIFAR-10 when ρ=1 vs ρ=0
**Condition**: CIFAR-10 dataset with DLIF neurons

**Evidence**: "When training with Gaussian noise, the performance of DLIF improves more when ρ = 1. For example, the improvement is 3.94% for VGG11 and 1.99% for WRN16 on the CIFAR-10 dataset."

## [POSITIVE] ρ Hyperparameter Tuning
The scalar ρ controls the intensity of the MS-MPPD regularization term in the total loss. Values tested: 0.0, 0.5, 1.0, 2.0.

**Delta**: ρ=1.0 achieves best PGD7=28.33% for DLIF; ρ=2.0 with LIF causes clean accuracy collapse to 64.62%
**Condition**: Optimal at ρ=1; ρ=2 is harmful for LIF neurons but not DLIF

**Evidence**: "We can observe that, compared with the performance of ρ = 0, the robustness of ρ ≠ 0 all increases. And ρ = 1 achieves the best performance among the choices."

## [NEGATIVE] High ρ with Vanilla LIF
Setting ρ=2.0 with standard LIF neurons (without DLIF) causes training instability and clean accuracy degradation.

**Delta**: Clean accuracy drops to 64.62% and PGD7 drops to 22.42% for LIF ρ=2.0 vs 85.61% clean and 27.54% PGD7 for LIF ρ=0
**Condition**: LIF neurons without DLIF modification on VGG-5 CIFAR-10

**Evidence**: "When ρ increases, the clean accuracy goes down. However, DLIF SNN almost remains the same... LIF, AT, ρ=2.0, MS-MPPD achieves clean accuracy of 64.62 and PGD7 of 22.42."

## [NEGATIVE] TASAD as Training Objective
Using time-averaged spiking activity distance (TASAD) as the perturbation regularization loss instead of MS-MPPD.

**Delta**: PGD7=27.80% vs MS-MPPD PGD7=28.33% for DLIF AT ρ=1
**Condition**: Ablation study on VGG-5 CIFAR-10 with adversarial training, ρ=1

**Evidence**: "Training with TASAD or STD is not as effective at increasing robustness as training with MS-MPPD."

## [NEGATIVE] STD as Training Objective
Using spike train distance (STD) as the perturbation regularization loss instead of MS-MPPD.

**Delta**: PGD7=26.82% vs MS-MPPD PGD7=28.33% for DLIF AT ρ=1
**Condition**: Ablation study on VGG-5 CIFAR-10 with adversarial training, ρ=1

**Evidence**: "Training with TASAD or STD is not as effective at increasing robustness as training with MS-MPPD."

## [NEUTRAL] Triangle-like Surrogate Function
Using triangle-like surrogate functions (Deng et al., 2021) for backpropagation through the non-differentiable Heaviside spike function, with parameter ω=1.

**Delta**: None
**Condition**: Used throughout all experiments as the standard surrogate gradient method

**Evidence**: "In this paper, we use the triangle-like surrogate functions (Deng et al., 2021)... where ω = 1 by default. Note that the triangle-like surrogate function is also used to craft white-box adversarial examples in the proposed framework or robustness evaluation."

## [NEUTRAL] Mixup Task Loss Strategy
Combining clean loss and adversarial/perturbed loss with a mixture parameter χ=0.5 as the task loss during training.

**Delta**: None
**Condition**: Applied in all adversarial and Gaussian noise training settings

**Evidence**: "Following a mixup strategy (Zhang et al., 2018; Wang et al., 2019), the task loss can be expressed as: [mixture of clean and perturbed losses] where χ is a mixture parameter, which is 0.5 by default."

## [NEGATIVE] Natural Training (No Robustness Defense)
Training SNN with only clean data and no adversarial or noise augmentation.

**Delta**: PGD7 near 0% (0.03% for LIF VGG11, 0.00% for LIF WRN16 on CIFAR-10)
**Condition**: Evaluated under PGD and APGD attacks with ε=8/255

**Evidence**: "For both CIFAR-10 and CIFAR-100, SNNs with natural training are vulnerable to strong PGD or APGD attacks."

## [POSITIVE] L2 Input-Output Stability via Spectral Norm Bound
Theoretical result showing the L2 gain of membrane potential perturbation dynamics is bounded by sqrt(1/(1-λ)) * spectral_norm(W), motivating minimization of weight spectral norm and leaky factor to improve robustness.

**Delta**: None
**Condition**: Theoretical bound applicable to all SNN layers with LIF/DLIF neurons

**Evidence**: "Theorem 3.1 suggests a promoting mechanism to maximize the capability of controlling the L2 gain... γ[l] = sqrt(1/(1−λ)) ∥W[l]∥ and β[l] = 0. ∥W[l]∥ is the spectral norm of the weight."
