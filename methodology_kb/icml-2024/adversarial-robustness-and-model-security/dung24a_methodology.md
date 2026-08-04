# Sharpness-Aware Data Generation for Zero-shot Quantization

**Source**: https://proceedings.mlr.press/v235/dung24a.html

## [POSITIVE] Sharpness-Aware Data Generation (SADAG)
A zero-shot quantization method that generates synthetic calibration data by minimizing quantized model sharpness, approximated via gradient matching between each generated sample and its neighbors using a SAM-like optimization.

**Delta**: +0.69% to +1.08% Top-1 accuracy over Genie (SOTA) across settings
**Condition**: Low-bit quantization settings (2/2, 3/3, 2/4, 4/4) on CIFAR-100 and ImageNet with ResNet-18, ResNet-50, MobileNetV2, ResNet-20

**Evidence**: "The results in Table 3 show that our method SADAG consistently outperforms previous approaches, including the current best method Genie (Jeon et al., 2023) on all bit-width settings and all considered model architectures. The improvements of our method over Genie are more clear in the 2/2 setting, i.e., the improvements are 0.77%, 0.74%, and 1.08% for the ResNet-18, ResNet-50, and MobileNetV2, respectively."

## [POSITIVE] Gradient Matching Loss
Maximizing the cosine similarity between gradients of the reconstruction loss evaluated on generated training samples and real validation data (or neighbor approximations) to reduce quantized model sharpness.

**Delta**: +2.79% to +35.46% Top-1 accuracy over random data selection depending on sample count
**Condition**: Applied during calibration data selection/generation for ResNet-18 on ImageNet; more impactful with smaller calibration sets

**Evidence**: "The results presented in Table 1 show that the gradient matching loss (15) consistently improves the performance of the quantized model. The improvements are more significant when the number of samples is small."

## [POSITIVE] Neighbor-based Gradient Matching Approximation
Approximating gradient matching with the real validation set by instead matching each generated sample's gradient with the gradient of its most dissimilar neighbor in embedding space, circumventing the need for real validation data.

**Delta**: outperforms baseline (Genie) across all settings
**Condition**: Zero-shot quantization setting where no real validation data is available

**Evidence**: "We then circumvent the problem of the gradient matching without real validation set by approximating it with the gradient matching between each generated sample and its neighbors, which can be done through an SAM-like optimization."

## [POSITIVE] Gradient Diversity Loss
A regularization term that encourages gradients of different generated samples to be orthogonal (near-zero cosine similarity), promoting diversity in the calibration set.

**Delta**: contributes to overall SADAG improvement; λ2=0 gives 53.74% vs λ2=1 gives 54.51%
**Condition**: Applied during synthetic data generation; evaluated on ResNet-18 ImageNet 2/2 setting

**Evidence**: "This loss encourages gradients of samples xi and xj (i≠j) to be orthogonal when ζ is close to 0. Consequently, it encourages the calibration set to be diverse."

## [POSITIVE] BatchNorm Statistics Matching (BN Loss)
Generating synthetic data such that the mean and standard deviation of feature activations at each BN layer match the stored BatchNorm statistics of the full-precision model.

**Delta**: contributes to overall SADAG improvement; λ1=0 gives 54.14% vs λ1=1 gives 54.51%
**Condition**: Used as part of the combined SADAG loss; evaluated on ResNet-18 ImageNet 2/2 setting

**Evidence**: "we also want the generated samples to follow the distribution of original data. Particularly, we encourage X(T) to have similar BN statistics stored in the BN layers of the full-precision model θFP, by introducing the BN loss LBN"

## [NEUTRAL] Warm-up Stage with Generator
An initial warm-up phase using a generator network and 256-dimensional embedding vectors to produce an initial synthetic dataset before applying the sharpness-aware refinement.

**Delta**: no standalone delta reported; serves as initialization for SADAG refinement
**Condition**: Applied as initialization step before SADAG gradient matching optimization

**Evidence**: "Initially, we need to warm up the calibrated set X(T) using a data generation method. After the warm-up stage, we acquire the final calibration set X(T) by minimizing the loss in Eq. (21) over the warm-up data."

## [POSITIVE] Adaptive Rounding for Weight Quantization
Using a learnable rounding function h(v) ∈ [0,1] that converges to 0 or 1 instead of standard round-to-nearest, improving uniform quantization performance.

**Delta**: adopted from prior SOTA; no standalone delta reported in this paper
**Condition**: Applied to all weight quantization experiments in this paper

**Evidence**: "The recent state-of-the-art post training quantization (PTQ) approaches have adopted adaptive rounding (Nagel et al., 2020) to improve the performance of uniform quantization further... In this work, we also adopt the adaptive rounding (Nagel et al., 2020) for weight quantization."

## [NEUTRAL] Diagonal Hessian Approximation
Approximating the Hessian matrix of the fully-connected layer as a scaled identity matrix (diagonal with constant value) to make gradient matching computationally tractable.

**Delta**: enables tractable optimization; no direct accuracy delta reported
**Condition**: Required approximation for gradient matching optimization; acknowledged as a limitation

**Evidence**: "Similar to AdaRound (Nagel et al., 2020), we assume that H(L)(θQ) is a diagonal matrix with the same main diagonal value... A noticeable weakness of the framework is that it requires the relaxation for the Hessian matrix."

## [NEUTRAL] Final Fully-Connected Layer Gradient Focus
Restricting gradient matching computation to the final fully-connected layer rather than the whole network, chosen because it has far more parameters than the first convolutional layer and its Jacobian is easy to compute.

**Delta**: no direct delta; acknowledged as a limitation with potential for improvement
**Condition**: Applied to all SADAG experiments; noted as a limitation to be addressed in future work

**Evidence**: "we choose to use the fully-connected layer for our estimation, as it usually has a far higher number of parameters (more influence) than the first convolutional layer... Another limitation is that our current method only takes into account the gradient of the final fully-connected layer instead of the whole model."

## [POSITIVE] Increasing Number of Generated Images
Generating more synthetic calibration images (128 to 1024) to improve quantized model performance.

**Delta**: +3.71% from 128→256 images, +1.94% from 256→512 images (diminishing returns)
**Condition**: ResNet-18 on ImageNet, 2/2 bit-width setting

**Evidence**: "The results show that increasing the number generated images improves the model's performance. However, the performance gain is smaller when the number of images increase, e.g., for the proposed method, the performance gains are 3.71% and 1.94% when increasing the number of images from 128 to 256, and from 256 to 512, respectively."

## [POSITIVE] Balanced Loss Hyperparameters (λ1=λ2=1)
Setting both the gradient matching loss weight λ1 and diversity loss weight λ2 to 1 in the combined SADAG objective.

**Delta**: λ1=1 gives 54.51% vs 54.14% (λ1=0) and 53.85% (λ1=5); λ2=1 gives 54.51% vs 53.74% (λ2=0) and 53.77% (λ2=5)
**Condition**: ResNet-18 on ImageNet, 2/2 bit-width setting with 1024 generated images

**Evidence**: "As we can see, the model's performance degrades with larger or smaller λ1 and λ2. Therefore, we simply keep both of them at value 1."

## [POSITIVE] First-order Approximation of Second-order Objective
Replacing the computationally expensive second-order SAM optimization with a first-order gradient matching approximation to reduce computational cost.

**Delta**: only ~1.5x slower than Genie (fastest ZSQ method) instead of prohibitive second-order cost
**Condition**: Applied throughout SADAG to make sharpness-aware data generation computationally feasible

**Evidence**: "Although the second-order objective in Eq. (7) is computationally intensive, we have successfully reduced the computational expense by approximating it with another first-order optimization in Eq. (15). Our proposed method operates at a speed that is approximately 1.5 times slower than Genie."

## [POSITIVE] Fixed High-bit First and Last Layers
Keeping the first convolutional layer and last fully-connected layer at 8-bit precision while quantizing other layers to the target low bit-width.

**Delta**: standard practice adopted from SOTA; no standalone delta reported
**Condition**: Applied in all low-bit quantization experiments (2/2, 3/3, 2/4, 4/4 settings)

**Evidence**: "the bit-widths of the first layer and the last layer are fixed at 8 bits, which is similar to recent SOTA methods for PTQ (Jeon et al., 2023; Li et al., 2021)."
