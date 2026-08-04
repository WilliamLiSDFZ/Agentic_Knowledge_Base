# Coarse-To-Fine Tensor Trains for Compact Visual Representations

**Source**: https://proceedings.mlr.press/v235/loeschcke24a.html

## [POSITIVE] Coarse-to-Fine Tensor Train Learning (PuTT)
A hierarchical optimization strategy that starts training at a coarse resolution and progressively refines the QTT representation through upsampling steps, creating a sequence of incrementally refined tensor trains.

**Delta**: +2.5 PSNR, +0.1 SSIM over baselines at 16k resolution
**Condition**: 2D image compression, especially at high resolutions (16k)

**Evidence**: "At 16k resolution, PuTT significantly outperforms baselines, showing an advantage of over 2.5 in PSNR and 0.1 in SSIM."

## [POSITIVE] Prolongation MPO Upsampling
A Matrix Product Operator (MPO) with fixed bond dimension of 3 that performs linear interpolation globally in QTT format, doubling the resolution of the tensor train representation at each upsampling step.

**Delta**: PSNR from 1.87 to 28.73, SSIM from 0.0018 to 0.7349 with 7 upsampling steps on 1% training data
**Condition**: Learning from incomplete/missing data

**Evidence**: "Without upsampling, training on just 1% of the input, PuTT gets a PSNR of 1.87 and SSIM of 0.0018. However, applying seven upsampling steps enhances the results to a PSNR of 28.73 and SSIM of 0.7349."

## [POSITIVE] Quantized Tensor Train (QTT) Format
A tensor format that uses mode quantization to decompose scaling dimensions in powers of two, enabling hierarchical structuring with O(d log(L) R^2) scaling in side length.

**Delta**: More than 1 PSNR improvement and nearly 0.005 SSIM improvement over CP/Tucker at 1024^3 resolution
**Condition**: 3D compression at large resolutions (1024^3)

**Evidence**: "Yet, for 1024^3, PuTT significantly outshines the other methods, leading to more than 1 PSNR improvement and nearly 0.005 improvement in SSIM."

## [POSITIVE] TT-SVD Rank Truncation after Upsampling
After applying the prolongation MPO, TT-SVD is used to compress the expanded bond dimensions back to a maximum rank R_max, preventing exponential rank growth.

**Delta**: Controlled ranks R_i <= R_max
**Condition**: After each upsampling step in PuTT

**Evidence**: "This reduction is critical since the ranks expand exponentially in the number of upsampling steps. The outcome is a compressed QTT, T_{D+1}, with controlled ranks R_i <= R_max, ensuring an efficient representation of the upsampled object."

## [POSITIVE] Trapezoid Rank Structure
A rank structure for the tensor train where bond dimensions increase to a maximum, remain constant, then decrease, forming a trapezoid shape.

**Delta**: outperforms baseline
**Condition**: General PuTT training

**Evidence**: "Throughout the learning, we adopt a trapezoid structure (Oseledets, 2011) for the tensor train ranks, where ranks increase to a maximum (forming the trapezoid's ascending edge), remain constant (trapezoid's top), and then decrease (its descending edge)."

## [POSITIVE] Upsampling for Denoising
Applying the coarse-to-fine upsampling strategy when training on noisy data, which acts as an implicit regularizer preventing overfitting to noise.

**Delta**: +0.1 SSIM improvement for noise levels exceeding 0.2 sigma
**Condition**: Denoising tasks with Gaussian or Laplacian noise

**Evidence**: "Notably, the application of upsampling not only avoids overfitting to noisy samples but also consistently outperforms the non-upsampling approach. Fig. 10(b) underscores the clear benefits of employing upsampling strategies. This is particularly evident in PuTT, where upsampling yields an SSIM score improvement of more than 0.1 for noise levels exceeding 0.2 sigma."

## [POSITIVE] Coarse-to-Fine Training Efficiency
Using upsampling steps to reduce the number of gradient iterations needed to reach convergence.

**Delta**: 1024 iterations with 4 upsampling steps achieves comparable PSNR/SSIM to 16k iterations without upsampling
**Condition**: Ablation study on iteration count vs upsampling steps

**Evidence**: "using just 1024 iterations with four upsampling steps, we achieve comparable PSNR and SSIM to training without upsampling for 16k iterations. Beyond 4k iterations, there is no significant improvement in quality. Without upsampling this plateau is not reached even after 32k iterations."

## [POSITIVE] Upsampling for Initialization Robustness
The coarse-to-fine upsampling strategy makes QTT training robust to different initialization standard deviations.

**Delta**: PSNR stable between 36.100 and 36.116 for std 0.001 to 0.5 with PuTT, vs 34.958 to 12.320 without upsampling
**Condition**: Varying initialization standard deviations

**Evidence**: "Without upsampling, QTT training is sensitive to initialization standard deviation, with PSNR fluctuating between 34.958 (std 0.05) and 12.320 (std 0.5) for a 512x512 RGB image. In contrast, PuTT's PSNR remains stable between 36.100 and 36.116 for std values from 0.001 to 0.5."

## [NEGATIVE] QTT Without Coarse-to-Fine (Baseline TT)
Training a QTT directly without the coarse-to-fine upsampling strategy, used as a baseline comparison.

**Delta**: PSNR 25.7, SSIM 0.70 vs PuTT PSNR 26.3, SSIM 0.72 at 16k
**Condition**: 16k image compression

**Evidence**: "PuTT PSNR 26.3, SSIM 0.72 | TT No Upsampling PSNR 25.7, SSIM 0.70"

## [NEGATIVE] VM Decomposition for 3D
Vector-Matrix decomposition for 3D tensors, which has quadratic dependency on side length.

**Delta**: relatively poor performance compared to PuTT
**Condition**: 3D compression at high compression ratios

**Evidence**: "VM's performance is less substantial due to its quadratic dependency on the side length, unlike the linear dependency of CP and Tucker and the logarithmic dependency of QTT. VM shows relatively poor performance. This is attributable to the high compression setting of our experiment, coupled with VM's quadratic dependency on side length."

## [POSITIVE] Novel View Synthesis with QTT Grids
Using two QTT-format voxel grids (one for density, one for color) with trilinear interpolation and differentiable volume rendering for NeRF-style novel view synthesis.

**Delta**: +1 PSNR over small baselines on NSVF dataset at 7MB; 7MB PuTT matches Large baselines (>60MB) on NSVF and TanksTemples
**Condition**: Novel view synthesis at small and medium model sizes

**Evidence**: "Our 12MB PuTT model, despite having six times fewer parameters, matches the performance of the Large baselines on the NSVF and TanksTemples datasets. Moreover, our 7MB PuTT model outperforms Small baselines by over one PSNR on the NSVF dataset."

## [POSITIVE] Masked Average Pooling for Incomplete Data Downsampling
A custom downsampling method for incomplete data that averages only non-zero values in each window when creating lower-resolution training targets.

**Delta**: outperforms baseline
**Condition**: Learning from incomplete/missing data with coarse-to-fine training

**Evidence**: "we use a custom masked average pooling method, averaging only the non-zero values in each window, sized according to the downsampling factor. The resulting downsampled image, I_{D-l,p}, thus contains aggregated information within each patch of size 2^l x 2^l of I_{D,p}."

## [NEUTRAL] PuTT at Low Compression / Small Tensor Sizes
Applying PuTT to scenarios with low compression ratios or small tensor sizes where QTT advantages are less pronounced.

**Delta**: performance converges with CP, Tucker, VM
**Condition**: Low compression settings, small tensors (e.g., 1k resolution)

**Evidence**: "their effectiveness tends to converge with other methods like CP, Tucker, and VM in less compressed settings with smaller tensor sizes. For example, in the case of 1k resolution images, we noted that the performance benefits of using QTTs were less pronounced."

## [NEGATIVE] PuTT SSIM at 16k Resolution vs TT-SVD
At 16k resolution, PuTT's SSIM performance relative to the analytical TT-SVD baseline.

**Delta**: TT-SVD exhibits better SSIM at 16k
**Condition**: 2D compression at 16k resolution, SSIM metric

**Evidence**: "At 16k resolution, TT-SVD exhibits better SSIM, indicating the challenges in capturing structural image properties as the resolution and the ratio between batch size and image size increase."

## [POSITIVE] Upsampling Steps for SSIM Improvement
Each additional upsampling step provides incremental SSIM gains due to improved learning of global features like mean, standard deviation, and luminance.

**Delta**: more pronounced SSIM improvement with each upsampling step
**Condition**: Ablation study varying upsampling steps on noisy inputs

**Evidence**: "The SSIM plot, on the RHS, reveals a more pronounced improvement with each upsampling step, indicating the effectiveness of upsampling in enhancing the model's ability to learn global features."

## [POSITIVE] Near vs Far View Performance
PuTT's improvement over TensoRF is more pronounced for nearby views than far views in novel view synthesis.

**Delta**: +1.53 PSNR near vs +0.44 PSNR far on all scenes (Blender)
**Condition**: Novel view synthesis, near vs far test views

**Evidence**: "Our improvement is more pronounced at nearby views, indicating our ability to capture fine details better than TensoRF."
