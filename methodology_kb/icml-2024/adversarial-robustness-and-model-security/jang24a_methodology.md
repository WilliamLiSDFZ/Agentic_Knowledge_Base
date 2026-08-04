# Rethinking DP-SGD in Discrete Domain: Exploring Logistic Distribution in the Realm of signSGD

**Source**: https://proceedings.mlr.press/v235/jang24a.html

## [POSITIVE] Logistic Mechanism for DP-SIGNSGD
Replacing Gaussian noise with additive Logistic noise before the sign function in DP-SIGNSGD, derived from an exponential mechanism formulation of the sign sampling problem

**Delta**: outperforms baseline across all hyperparameter combinations
**Condition**: Applied to SIGNSGD with differential privacy guarantees on MNIST and CIFAR-10 datasets

**Evidence**: "Our extensive experiments show that the classification accuracy of DP-SIGNLOSGD is higher than that of DP-SIGNSGD across all hyperparameter combinations, under the same privacy budget."

## [POSITIVE] Exponential Mechanism for Sign Sampling
Formulating the SIGNSGD update as a sign sampling problem and applying the exponential mechanism with score function s(g_B, v) = -v^T * g_B over the discrete set {-α, α}^N

**Delta**: theoretically equivalent to Logistic noise addition; enables (ε,0)-DP
**Condition**: Theoretical foundation for DP-SIGNLOSGD; motivates the Logistic noise derivation

**Evidence**: "Our motivation is that the exponential mechanism can be used as a foundation mechanism... we design the exponential mechanism E for solving the problem (8) by letting the score function as s(˜g_B, v) = −v^T ˜g_B"

## [POSITIVE] Tighter MGF Bound with Logistic Noise
The moment generating function (MGF) of the Logistic mechanism is bounded by λ(λ+1)q²/(50s²), significantly tighter than the Gaussian bound of λ(λ+1)q²/((1-q)σ²) in DP-SIGNSGD

**Delta**: MGF bound ~50x tighter; enables up to 1.5x more training epochs in practice
**Condition**: Under assumption s < √3/(16πq), compared to Gaussian with σ < 1/(16q)

**Evidence**: "we show that the MGF is bounded by λ(λ+1)q²/50s² under this assumption, which is significantly tighter than that of DP-SIGNSGD... with the numeric integration of MGF, the proposed method can have 1.5x more training epochs"

## [POSITIVE] More Trainable Epochs via Tighter Privacy Loss
Due to tighter privacy accounting, DP-SIGNLOSGD can train for more epochs under the same privacy budget compared to DP-SIGNSGD

**Delta**: 22–110 more training epochs depending on noise level and ε
**Condition**: Measured via moments accountant with noise std fixed at 3.0 or 6.0, ε ∈ {2.0, 4.0}, δ=1e-5

**Evidence**: "With the noise std of 3.0... the proposed method can have 22 and 71 more training epochs than the DP-SIGNSGD for ϵ of 2.0 and 4.0, respectively. Similarly, if the noise std is fixed to 6.0, the proposed method has 32 and 110 more training epochs"

## [POSITIVE] Lower Sign Error Rate with Logistic Noise
Logistic mechanism achieves a lower sign error rate compared to Gaussian and Laplace mechanisms under the same privacy budget, due to smaller required noise standard deviation

**Delta**: 9 percentage points lower error rate; std of 1.17 vs 1.48 (Gaussian) vs 70.7 (Laplace)
**Condition**: Under (ε=4.0, δ=1e-5)-DP, single parameter setting

**Evidence**: "the proposed method has the smallest error rate of selecting the sign of the gradient... The standard deviation (std) of the additive Logistic, Gaussian, and Laplace mechanisms are 1.17, 1.48, and 70.7, respectively... Proposed method has 9%p lower error rate"

## [POSITIVE] Faster Convergence via Lower Noise Variance
DP-SIGNLOSGD requires approximately 20x smaller noise variance than DP-SIGNSGD, reducing the additive noise term in the ℓ1 convergence bound

**Delta**: ~20x smaller noise variance; faster convergence
**Condition**: Theoretical convergence analysis under β-smoothness assumption for SIGNSGD with additive noise

**Evidence**: "Our focus is on the second term, in which the proposed method requires a smaller noise variance (≈ 20 times) compared to the DP-signSGD. Thus, the proposed method can have much faster convergence."

## [NEGATIVE] Gaussian Noise in DP-SIGNSGD (Baseline)
Using Gaussian noise (designed for continuous-valued gradient perturbation in DP-SGD) as the noise mechanism in DP-SIGNSGD

**Delta**: loose privacy loss; lower accuracy than Logistic mechanism
**Condition**: Applied to SIGNSGD where discrete sign output makes Gaussian noise suboptimal

**Evidence**: "the Gaussian noise, designed for perturbing continuous-valued gradient, leads to a loose privacy loss, thereby destroying the utility of the learned model."

## [NEGATIVE] Laplace Mechanism for DP-SIGNSGD
Using Laplace noise as an alternative to Gaussian noise in DP-SIGNSGD

**Delta**: std of 70.7 vs 1.17 (Logistic) and 1.48 (Gaussian) under same privacy budget
**Condition**: Composition setting (multiple training steps); moments accountant with ε=4.0, δ=1e-5

**Evidence**: "Since the Laplace mechanism is vulnerable to guarantee a tight privacy loss in the composition setting, we only compare DP-SIGNSGD using the Gaussian mechanism in the remainder part."

## [NEUTRAL] ℓ2 Gradient Clipping
Clipping per-sample gradients by ℓ2 norm with threshold C to bound sensitivity before noise addition

**Delta**: standard ingredient; C=30 used as reference value
**Condition**: Applied in both DP-SIGNSGD and DP-SIGNLOSGD; clipping constant C does not significantly affect results when sufficient epochs are given

**Evidence**: "Similar to DP-SGD, we employ ℓ2-clipping with a threshold C... the gradient clipping constant and the number of epochs do not significantly affect the trained model if a sufficient number of epochs are given."

## [POSITIVE] Moments Accountant for Privacy Tracking
Using the moments accountant (Abadi et al., 2016) to track accumulated privacy loss across training steps via MGF composition

**Delta**: enables tighter privacy accounting for Logistic mechanism vs Gaussian
**Condition**: Used for both DP-SIGNLOSGD and DP-SIGNSGD; Logistic mechanism benefits more due to tighter MGF bound

**Evidence**: "The moments accountant has been widely used to track the privacy loss across multiple perturbed training steps with additive noises... we empirically compare the proposed method and the DP-SIGNSGD with the gradient accuracy (in Figure 1) and accumulated privacy loss (in Figure 2)."

## [NEUTRAL] Batch Normalization Replacement with Group Normalization
Replacing batch normalization with group normalization to enable per-sample gradient computation via torch.func.vmap

**Delta**: no accuracy degradation observed
**Condition**: Implementation requirement for DP training with per-sample gradients in PyTorch

**Evidence**: "because torch.func.vmap does not support the batch normalization module, we replace all the batch normalization modules with group normalization. We confirm that this modification does not degrade the accuracy of the trained model."

## [NEUTRAL] Cosine Learning Rate Scheduler
Using a cosine annealing schedule to decay the learning rate during training

**Delta**: used as standard training setup; no ablation reported
**Condition**: Applied in both MNIST and CIFAR-10 experiments for both proposed and baseline methods

**Evidence**: "The cosine learning rate scheduler is used."

## [POSITIVE] Batch Size Selection (|B| ≈ √N)
Following the batch size recommendation from Abadi et al. (2016) of setting batch size approximately equal to √N (number of training samples)

**Delta**: optimal accuracy observed at this batch size
**Condition**: MNIST experiments with varying batch sizes

**Evidence**: "In this figure, we can find that the batch size suggestion in (Abadi et al., 2016) still holds (|B| ≈ √N)."

## [POSITIVE] Fine-tuning with Pre-trained Weights
Fine-tuning pre-trained ImageNet models (ResNet, ViT) with DP-SIGNLOSGD instead of training from scratch

**Delta**: ViT-B-16 proposed: 90.51%/94.27% train/test vs DP-SIGNSGD: 83.86%/87.31% at ε=6.4
**Condition**: CIFAR-10 fine-tuning experiments at ε=6.4, δ=1e-5

**Evidence**: "Even if the neural network model is pre-trained with a large dataset (ImageNet), the proposed method still outperforms DP-SIGNSGD."

## [POSITIVE] Adding Small Noise Before Sign Function (P-SIGNSGD effect)
Adding a small amount of noise before the sign function can enhance convergence of SIGNSGD even without privacy requirements, as shown by P-SIGNSGD outperforming standard SIGNSGD

**Delta**: P-SIGNSGD outperforms SIGNSGD without DP in fine-tuning experiments
**Condition**: Fine-tuning large neural network models (ResNet, ViT) on CIFAR-10

**Evidence**: "the proposed sometimes outperforms the SIGNSGD, even though it does not add any noise to the gradient... we additionally compare the P-SIGNSGD method with the standard SIGNSGD method, which shows that the adding small amount of noise before sign function can enhance the convergence of the SIGNSGD."

## [POSITIVE] Larger Privacy Budget (Higher ε) Amplifies Logistic Advantage
The performance gap between DP-SIGNLOSGD and DP-SIGNSGD increases as the privacy budget ε increases, due to proportionally larger noise reduction

**Delta**: At ε=6.4: noise std ratio (B-A)/A = 1.00; at ε=25.6: ratio = 3.45
**Condition**: CIFAR-10 experiments across ε ∈ {0.4, 0.8, 1.6, 3.2, 6.4, 12.8, 25.6}

**Evidence**: "the proportional gap of the variance becomes larger as ϵ increases, indicating that the proposed method efficiently secures privacy loss... when ϵ=25.6, the gap is much larger (B−A)/(A) = 3.45. Thus, our method have a more significant improvement for larger ϵ."
