# Superpoint Gaussian Splatting for Real-Time High-Fidelity Dynamic Scene Reconstruction

**Source**: https://proceedings.mlr.press/v235/wan24f.html

## [POSITIVE] Superpoint Grouping of 3D Gaussians
Clustering 3D Gaussians with similar properties (rotation, translation, location) into superpoints so that deformation is computed per-superpoint rather than per-Gaussian

**Delta**: 227 FPS at 800×800 (synthetic), 117 FPS at 536×960 (real-world), outperforms NeRF-based and D-3D-GS in speed
**Condition**: Dynamic scene rendering; applies across synthetic D-NeRF and real-world HyperNeRF/NeRF-DS datasets

**Evidence**: "We can cluster these similar 3D Gaussians together to form a superpoint so that it is no longer necessary to compute a deformation for every single 3D Gaussian, leading to a much faster rendering speed."

## [POSITIVE] Property Reconstruction Loss
A loss that enforces consistency between original Gaussian properties and properties reconstructed via the superpoint association matrix, encouraging similar Gaussians to cluster together

**Delta**: +0.39 PSNR (37.59 → 37.98), +0.0008 SSIM, -0.0008 LPIPS on D-NeRF
**Condition**: D-NeRF synthetic dataset ablation

**Evidence**: "Tab. 5 demonstrates that property reconstruction loss can improve rendering quality."

## [POSITIVE] Warm-up Training Stage
Training 3D Gaussians for the first 3k iterations without the deformation network to achieve stable positions and shapes before superpoint initialization

**Delta**: +16.42 PSNR (21.56 → 37.98), +0.0897 SSIM, -0.1281 LPIPS on D-NeRF
**Condition**: D-NeRF synthetic dataset; critical for model convergence

**Evidence**: "Table 14: Ablation study of the warm-up train stage on D-NeRF dataset. w/o warm up: PSNR 21.56, w warm-up: PSNR 37.98"

## [POSITIVE] Optional Non-Rigid Deformation Network (SP-GS+NG)
An additional small MLP (3-layer, 64 hidden neurons) that predicts per-Gaussian non-rigid deformation on top of the rigid superpoint deformation

**Delta**: +1.17 PSNR on HyperNeRF (25.61 → 26.78), +0.0516 MS-SSIM, -0.0268 LPIPS; slight improvement on D-NeRF (37.98 → 38.28 PSNR)
**Condition**: Real-world HyperNeRF and NeRF-DS datasets; trades rendering speed for quality (51.51 FPS vs 117.86 FPS on HyperNeRF)

**Evidence**: "By combining rigid motion with non-rigid deformation... SP-GS+NG (ours) 26.78 / 0.8920 / 0.1805 vs SP-GS (ours) 25.61 / 0.8404 / 0.2073 on HyperNeRF"

## [POSITIVE] Inference via Interpolation of Pre-computed Superpoint Deformations
Pre-computing superpoint deformations at all training timesteps and using linear interpolation at inference instead of running the deformation network forward pass

**Delta**: +51.94 FPS (168.01 → 219.95) with negligible quality difference (PSNR 36.2281 vs 36.2280)
**Condition**: D-NeRF dataset inference; applies when rendering at training timesteps

**Evidence**: "Table 15: using F, Eq. 6: FPS 168.01; interp, Eq. 8: FPS 219.95. two way have almost same visual quality, but the FPS of using F is lower than the FPS using interpolation"

## [POSITIVE] Learnable Association Matrix
A learnable matrix A ∈ R^(P×M) that establishes soft associations between P Gaussians and M superpoints, with K-nearest-neighbor sparsity constraint

**Delta**: Enables end-to-end differentiable superpoint grouping; outperforms baseline
**Condition**: Core component of SP-GS; used throughout training

**Evidence**: "We utilize a learnable association matrix A ∈ R^(P×M) to establish the connection between 3D Gaussians and superpoints... the associated probability aij between Gaussian Gi and superpoint Sj can be calculated as..."

## [POSITIVE] Larger Superpoint Deformation Network F
Increasing the width and depth of the MLP used to predict superpoint deformations (e.g., from width=64,depth=1 to width=256,depth=8)

**Delta**: +1.71 PSNR (34.74 → 36.45) from smallest to largest configuration on D-NeRF
**Condition**: D-NeRF dataset; width=256, depth=8 used as default

**Evidence**: "the experimental results clearly demonstrate that a larger F leads to a higher visual quality. Since we only need to predict the deformation of superpoints, increasing the model size will results in only a modest rise in computational expense during training."

## [NEGATIVE] Skip Connection at 5th Layer in Deformation Network
Following NeRF convention, adding a skip connection between inputs and the 5th fully-connected layer when network depth exceeds 4

**Delta**: PSNR drops to 27.23 for width=64, depth=5 configuration
**Condition**: Only problematic at width=64, depth=5; larger widths handle skip connection correctly

**Evidence**: "With the exception of the configuration with width=64 and depth=5, which exhibits diminished performance due to the skip concatenation"

## [POSITIVE] Farthest Point Sampling for Superpoint Initialization
Initializing superpoint canonical positions by sampling M Gaussians using farthest point sampling after warm-up training

**Delta**: Enables uniform spatial distribution of superpoints
**Condition**: Applied once after warm-up training stage

**Evidence**: "for the initialization of superpoints, M Gaussians are sampled using the farthest point sampling algorithm, and the canonical positions p^c of superpoints are equal to the centers of the sampled Gaussians."

## [POSITIVE] Positional Encoding for Deformation Network Input
Applying sinusoidal positional encoding to superpoint canonical positions (L=10) and timestep (L=6) before feeding into the deformation MLP

**Delta**: Standard component enabling high-frequency deformation modeling; no isolated ablation reported
**Condition**: Applied to all deformation network inputs

**Evidence**: "where γ denotes the positional encoding... In our experiments, we set L=10 for γ(p^c_j) and L=6 for γ(t)."

## [POSITIVE] Model Distillation from D-3D-GS into SP-GS
Using a high-quality D-3D-GS model as teacher to initialize and supervise SP-GS training, trading some quality for large speed gains

**Delta**: Student SP-GS achieves 164.04 FPS vs teacher D-3D-GS at 20.65 FPS, with PSNR drop from 26.15 to 25.68 on NeRF-DS 'As' scene
**Condition**: NeRF-DS 'As' scene; useful when a stronger teacher model is available

**Evidence**: "While D-3D-GS cannot achieve real-time rendering on V100 (20.65 FPS), our distillated student model can achieve significantly higher rendering speed (164.04 FPS)."

## [POSITIVE] Number of Superpoints Hyperparameter
The total number M of superpoints used to cluster Gaussians, ranging from 50 to 500

**Delta**: PSNR ranges from 35.69 (#sp=50) to 36.52 (#sp=500); modest improvement with more superpoints
**Condition**: D-NeRF dataset ablation; method is robust across this range

**Evidence**: "Tab. 4 shows the performance of our approach when varying these hyperparameters, and our method appears to be robust under all these variations."

## [NEUTRAL] K-Nearest Neighborhoods for Association Matrix
Restricting each Gaussian's association to only K nearest superpoints in the learnable association matrix

**Delta**: PSNR ranges from 36.09 to 36.30 across K=1 to K=6; no clear trend
**Condition**: D-NeRF dataset ablation; method is robust across K=1 to K=6

**Evidence**: "Tab. 4 shows the performance of our approach when varying these hyperparameters, and our method appears to be robust under all these variations."

## [POSITIVE] As-Rigid-As-Possible Regularization via Superpoints
Enforcing that Gaussians within the same superpoint share similar rigid deformations (translation and rotation), inspired by ARAP regularization in 3D reconstruction

**Delta**: Enables real-time rendering while maintaining quality; core design principle
**Condition**: Applied throughout training as both architectural constraint and loss term

**Evidence**: "Following the principle of As-Rigid-As-Possible, 3D Gaussians in the same superpoint Sj should have similar deformation... the more similar the Gaussian properties within the same superpoint are, the smaller this loss will be, thereby fully exploiting the As-Rigid-As-Possible feature."
