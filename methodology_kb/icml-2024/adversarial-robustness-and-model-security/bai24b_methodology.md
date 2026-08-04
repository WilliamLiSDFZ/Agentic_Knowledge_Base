# Diffusion Models Demand Contrastive Guidance for Adversarial Purification to Advance

**Source**: https://proceedings.mlr.press/v235/bai24b.html

## [POSITIVE] Contrastive Guidance for Diffusion-Based Adversarial Purification
Using the gradient of a contrastive loss (InfoNCE or hard negative mining) to guide the reverse diffusion process, facilitating evolution towards the signal direction and pushing purified samples toward clean data distribution

**Delta**: +12.17% robust accuracy on CIFAR-10 WideResNet-28-10 vs best baseline (AutoAttack ℓ∞), +11.52% on WideResNet-70-16
**Condition**: CIFAR-10 dataset, AutoAttack ℓ∞ (ϵ=8/255), WideResNet-28-10 and WideResNet-70-16 classifiers

**Evidence**: "The results in Tables 1 indicate that our method outperforms adversarial training methods and DiffPure with the state-of-the-art performance defending against the AutoAttack ℓ∞ threat model (ϵ = 8/255) evaluated by classifiers WideResNet-28-10 and WideResNet-70-16 on the robust accuracy by 12.17% and 11.52%, respectively."

## [POSITIVE] Contrastive Guidance on CIFAR-10 ℓ2 Threat Model
Applying contrastive guidance in the reverse diffusion process against ℓ2 adversarial attacks

**Delta**: +0.7% robust accuracy over best baseline on WideResNet-28-10
**Condition**: CIFAR-10 dataset, AutoAttack ℓ2 (ϵ=0.5), WideResNet-28-10 classifier

**Evidence**: "Table 2 shows that our method can still achieve better performance than adversarial training methods and DiffPure with the state-of-the-art performance against ℓ2 threat model (ϵ = 0.5) evaluated by WideResNet-28-10 by 0.7% in terms of the robust accuracy, with comparable performance to the state-of-the-art on standard accuracy."

## [POSITIVE] Contrastive Guidance on GTSRB Dataset (AutoAttack ℓ∞)
Applying contrastive guidance for adversarial purification on the German Traffic Sign Recognition Benchmark dataset

**Delta**: +27.34% robust accuracy, +1.56% standard accuracy over DiffPure
**Condition**: GTSRB dataset, AutoAttack ℓ∞ (ϵ=8/255), ResNet-18 classifier

**Evidence**: "our method outperforms DiffPure (Nie et al., 2022) for both standard accuracy and robust accuracy by 1.56% and 27.34%, respectively against AutoAttacks with ℓ∞ perturbations, ϵ = 8/255."

## [POSITIVE] Contrastive Guidance on GTSRB Dataset (AutoAttack ℓ2)
Applying contrastive guidance for adversarial purification on GTSRB against ℓ2 attacks

**Delta**: +11.97% robust accuracy, -3.13% standard accuracy vs DiffPure
**Condition**: GTSRB dataset, AutoAttack ℓ2 (ϵ=0.5), ResNet-18 classifier

**Evidence**: "For AutoAttack with ℓ2 perturbations, ϵ = 0.5, our method achieves higher robust accuracy than DiffPure by 11.97% with 3.13% lower standard accuracy."

## [NEUTRAL] Contrastive Guidance on GTSRB Dataset (BPDA+EOT)
Applying contrastive guidance for adversarial purification on GTSRB against BPDA+EOT attack

**Delta**: -0.18% robust accuracy vs DiffPure (within randomness margin)
**Condition**: GTSRB dataset, BPDA+EOT attack (ℓ∞, ϵ=8/255), ResNet-18 classifier

**Evidence**: "Against BPDA+EOT with ℓ∞ perturbations with ϵ = 8/255, our method has the same standard accuracy with DiffPure, with 0.18% lower robust accuracy than DiffPure. This minor inferiority may be due to randomness."

## [POSITIVE] Contrastive Guidance on CIFAR-100 (Ablation)
Adding contrastive guidance to diffusion model for adversarial purification on CIFAR-100

**Delta**: +15.62% robust accuracy (8.60% → 24.22%), -4.68% standard accuracy (62.50% → 57.82%)
**Condition**: CIFAR-100 dataset, AutoAttack ℓ∞ (ϵ=8/255), WideResNet-28-10 classifier

**Evidence**: "Comparisons on CIFAR-100, depicted in Table 6b, reveal the baseline method's superior standard accuracy, yet the proposed method outperforms in robust accuracy."

## [POSITIVE] Proper Forward Diffusion Noise Level (t*) Selection
Theoretically derived stopping time t* for the forward diffusion process that balances removing adversarial perturbations while preserving semantic label information, rather than diffusing all the way to t=1

**Delta**: outperforms baseline; enables correct classification recovery
**Condition**: Forward diffusion process for adversarial purification across all datasets

**Evidence**: "we aim to stop the forward process at t* ∈ (0, 1) to obtain a balance between removing local adversarial attacks and preserving global label semantics... Hence, the classification results are more likely to be correct, compared to the case where the reverse process starts at x(1) ∼ N(0, Id)."

## [NEUTRAL] VP-SDE vs VP-ODE Diffusion Type
Comparison of variance-preserving stochastic differential equation (VP-SDE) versus ordinary differential equation (VP-ODE) solvers for the reverse diffusion process

**Delta**: VP-SDE: 91.67% std / 82.81% robust; VP-ODE: 93.75% std / 69.79% robust
**Condition**: CIFAR-10 dataset, AutoAttack ℓ∞ (ϵ=8/255), WideResNet-28-10, t*=0.1; trade-off between standard and robust accuracy

**Evidence**: "Table 6a assesses the influence of various diffusion types, VP-SDE and VP-ODE, on our method in CIFAR-10. VP-SDE exhibits higher standard accuracy, while VP-ODE excels in robust accuracy."

## [POSITIVE] InfoNCE Loss for Contrastive Guidance
Using InfoNCE contrastive loss to compute guidance gradients during the reverse diffusion process, theoretically guaranteed to converge to exact guidance under unlimited model capacity

**Delta**: outperforms baseline DiffPure
**Condition**: Reverse diffusion process guidance; theoretical guarantee from Lu et al. (2023)

**Evidence**: "we first adopt the InfoNCE loss for ℓ(x(t), x(t)p; τ), because it is derived to be the theoretical guaranteed loss to enhance the learning direction of signal."

## [POSITIVE] Hard Negative Mining (HNM) Contrastive Loss
Using hard negative mining criterion to construct contrastive guidance, emphasizing negative pairs whose representations are currently very similar to enhance dissimilarity between different classes

**Delta**: empirically powerful (qualitative claim)
**Condition**: Reverse diffusion guidance; empirical performance improvement

**Evidence**: "We also adopt the hard negative mining loss for ℓ(x(t)a, x(t)p; τ) because of its empirical powerfulness (Ouyang et al., 2023)."

## [NEGATIVE] Attacker Access to Purifier Gradients
Allowing attackers to access gradients of the diffusion-based purifier during adaptive attacks, enabling stronger attacks against the purification model

**Delta**: DiffPure: 89.52% std / 81.70% robust (grad on) vs 89.78% std / 84.44% robust (grad off)
**Condition**: PGD+EOT attack, WideResNet-28-10, CIFAR-10, t*=100, ϵ=8/255

**Evidence**: "The results demonstrate that turning on the gradients of purifiers, i.e., accesses to the gradient of purifiers, can allow the attackers to attack the purifiers as well and hence reduce the effect of the purifiers, where the standard accuracy and the robust accuracy are both lower than the cases of no access to the gradients of purifiers."

## [POSITIVE] Contrastive Guidance Against Unseen Threat Models
Evaluating contrastive guided diffusion purification against adversarial attacks not seen during training, including both ℓ∞ and ℓ2 threat models on ResNet-50

**Delta**: Ours: 96.36% std, 73.44% ℓ∞ robust, 79.12% ℓ2 robust vs DiffPure: 88.20% std, 70.00% ℓ∞ robust, 70.90% ℓ2 robust
**Condition**: CIFAR-10, ResNet-50, unseen threat models (AutoAttack ℓ∞ ϵ=8/255 and ℓ2 ϵ=1), t*=0.125

**Evidence**: "As adversarial training methods have seen adversarial attacks during training, it is impressive that our method outperform them without knowing the adversarial attacks beforehand. This is also validated in Table 3."

## [NEUTRAL] Contrastive Guidance Against PGD+EOT on CIFAR-100
Applying contrastive guided diffusion purification against PGD+EOT attack on CIFAR-100 without attacker access to purifier gradients

**Delta**: Ours: 50.20% std / 34.70% robust vs DiffPure: 50.20% std / 34.64% robust
**Condition**: CIFAR-100 dataset, PGD+EOT attack (ℓ∞, ϵ=8/255), WideResNet-28-10, no gradient access to purifier

**Evidence**: "Table 9: DiffPure 50.20±1.27 / 34.64±0.09, GDMP 50.13±1.21 / 34.90±1.04, Ours 50.20±1.27 / 34.70±1.13"

## [NEUTRAL] Contrastive Guidance Against PGD+EOT on ImageNet
Applying contrastive guided diffusion purification against PGD+EOT attack on ImageNet without attacker access to purifier gradients

**Delta**: Ours (ResNet-50): 70.41% std / 41.70% robust vs DiffPure: 70.41% std / 42.58% robust; Ours (xcit): 76.56% std / 55.47% robust vs DiffPure: 76.56% std / 55.57% robust
**Condition**: ImageNet dataset, PGD+EOT attack (ℓ∞, ϵ=4/255), ResNet-50 and xcit-small-24-p16-224, no gradient access to purifier

**Evidence**: "Table 10 shows DiffPure ResNet-50: 70.41±0.29 / 42.58±0.20, Ours ResNet-50: 70.41±0.29 / 41.70±0.10; DiffPure xcit: 76.56±0.59 / 55.57±0.10, Ours xcit: 76.56±0.59 / 55.47±0.59"

## [NEGATIVE] Standard Accuracy vs Robust Accuracy Trade-off
The proposed contrastive guided diffusion model tends to improve robust accuracy at some cost to standard accuracy compared to adversarial training baselines

**Delta**: Lower standard accuracy than top adversarial training methods (e.g., 91.41% vs 93.69% on WideResNet-28-10 CIFAR-10)
**Condition**: CIFAR-10, all classifiers; general observation across experiments

**Evidence**: "It indicates that the trade-off between the standard accuracy and the robust accuracy still is still unsolved by our methods and remains an interesting topic to study in the future work. Besides, for the same threat model, our method obtains higher robust accuracy and comparable standard accuracy to DiffPure, but lower standard accuracy and comparable robust accuracy to the state-of-the-art performance by adversarial training methods."
