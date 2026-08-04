# Make-A-Shape: a Ten-Million-scale 3D Shape Model

**Source**: https://proceedings.mlr.press/v235/hui24a.html

## [POSITIVE] Wavelet-tree representation
A novel 3D representation that encodes high-resolution SDF shapes using multi-scale wavelet coefficients (coarse C0 and detail D0, D1) organized in a hierarchical tree structure, enabling nearly lossless compression.

**Delta**: IoU 0.9956 vs 0.9531 for coarse-only baseline
**Condition**: 3D shape encoding and reconstruction from 256^3 TSDF grids

**Evidence**: "our wavelet-tree representation...does not only achieve both a significant compression (reducing to 1/15 in size) and an impressive mean IoU of 99.56%"

## [POSITIVE] Subband coefficient filtering
A pre-processing step that selectively retains information-rich wavelet coefficients: all C0 coefficients are kept, D2 coefficients are discarded, and top-K coordinates from D0/D1 are retained based on magnitude.

**Delta**: 44.5% speed-up in streaming and loading; compression to 1/15 size with 99.56% IoU
**Condition**: Data preprocessing for large-scale training on millions of 3D shapes

**Evidence**: "It does not only achieve both a significant compression (reducing to 1/15 in size) and an impressive mean IoU of 99.56%, but also leads to a 44.5% speed-up in streaming and loading, a critical factor for large-scale training."

## [POSITIVE] Subband coefficient packing
Reshapes and concatenates wavelet coefficient volumes (C0, D0, D1) into a compact regular grid format with increased channels but manageable spatial resolution (46^3), making it compatible with standard U-Net diffusion models.

**Delta**: ~64x reduction in GPU memory usage; ~cubic-order speedup compared to naive arrangement
**Condition**: Diffusion model training on wavelet-tree representations

**Evidence**: "This strategy can lead to an approximate cubic-order speedup and a significant reduction in GPU memory usage, estimated to be around 64x compared to when applied to the same network architecture."

## [POSITIVE] Subband adaptive training strategy
A training loss that prioritizes high-magnitude detail coefficients (those above 1/32 of max in a subband) while maintaining equal supervision for less important coefficients, addressing imbalanced channel dimensions and coefficient sparsity.

**Delta**: LFD 2611.60 vs 3191.49 (MSE) and 2824.28 (subband-based MSE); IoU 0.6105 vs 0.5474 (MSE) and 0.5898 (subband-based MSE)
**Condition**: Training diffusion model on wavelet-tree representation with imbalanced subbands

**Evidence**: "both of the two strategies using the MSE loss lead to a notable performance drop, demonstrating the effectiveness of our adaptive training strategy"

## [NEGATIVE] Standard MSE loss on full coefficients
Applying standard Mean Squared Error loss simultaneously to all coefficient volumes (C0, D0, D1) as in standard DDPM, without subband-specific weighting.

**Delta**: LFD 3191.49 vs 2611.60 (ours); IoU 0.5474 vs 0.6105 (ours)
**Condition**: Training on wavelet-tree representation with imbalanced subband channels

**Evidence**: "both of the two strategies using the MSE loss lead to a notable performance drop, demonstrating the effectiveness of our adaptive training strategy"

## [NEGATIVE] Subband-based MSE loss
Computing separate MSE losses on C0, D0, and D1 individually and averaging the three terms, without prioritizing high-magnitude detail coefficients.

**Delta**: LFD 2824.28 vs 2611.60 (ours); IoU 0.5898 vs 0.6105 (ours)
**Condition**: Training on wavelet-tree representation as alternative to adaptive strategy

**Evidence**: "both of the two strategies using the MSE loss lead to a notable performance drop, demonstrating the effectiveness of our adaptive training strategy"

## [NEGATIVE] Coarse-only representation (C0 only)
Using only the coarse wavelet coefficient C0 for shape representation, omitting detail coefficients D0 and D1, as in prior work (Hui et al., 2022).

**Delta**: IoU 0.5919 vs 0.6105 (ours); LFD 2855.41 vs 2611.60 (ours)
**Condition**: Ablation comparison for 3D shape generation quality

**Evidence**: "The results presented in the first and last rows of Table 5 underscore the improved representational capacity of our wavelet tree representation compared to the baseline that uses only the C0 coefficients."

## [POSITIVE] Discarding D2 detail coefficients
Empirically determined that D2 coefficients contribute minimally to shape reconstruction and can be set to zero, reducing representation size without significant quality loss.

**Delta**: 99.64% IoU when D2 set to zeros on 1000 random shapes
**Condition**: Subband coefficient filtering preprocessing step

**Evidence**: "Most coefficients in D2 are insignificant. By empirically setting them to zeros in inverse wavelet transforms, we can reconstruct the TSDFs faithfully for 1,000 random shapes with 99.64% IoU."

## [NEGATIVE] Multi-branch network for mixed regular/irregular structures
Directly treating the mix of regular (C0) and irregular (X0, D0', D1') structures as diffusion targets using a multi-branch network.

**Delta**: model training collapse
**Condition**: Attempted approach for diffusion model training on wavelet-tree representation

**Evidence**: "this approach exhibited convergence issues, resulting in model training collapse"

## [NEGATIVE] Naive large-grid arrangement of wavelet volumes
Reassigning filtered coefficients back to zero-initialized volumes of original size (D0, D1) and arranging them in a spatially large grid for U-Net processing.

**Delta**: out-of-memory issues and inefficient GPU utilization
**Condition**: Attempted approach for diffusion model training on wavelet-tree representation

**Evidence**: "using the U-Net architecture, commonly employed in diffusion models, on this spatially large structure leads to memory-intensive feature maps, causing out-of-memory issues and inefficient GPU utilization"

## [POSITIVE] Classifier-free guidance
Using classifier-free guidance mechanism (Ho & Salimans, 2021) for conditional generation across various input modalities.

**Delta**: empirically demonstrated greater effectiveness in conditional settings
**Condition**: Conditional generation with image, point cloud, and voxel inputs

**Evidence**: "We also use a classifier-free guidance mechanism (Ho & Salimans, 2021), which has empirically demonstrated greater effectiveness in conditional settings."

## [POSITIVE] Multi-view conditioning (4 views)
Conditioning the generative model on multiple views (4 images) instead of a single view to provide more information for 3D reconstruction.

**Delta**: IoU 0.7460 vs 0.5748 (single-view) on GSO; LFD 1890.85 vs 3198.28 on GSO; CD 0.00337 vs 0.01303 on GSO
**Condition**: Image-to-3D generation when multiple views are available

**Evidence**: "Upon incorporating three additional views, our multi-view model demonstrates notable enhancements in performance, as evidenced in Table 3"

## [POSITIVE] Exponential moving average (EMA) during training
Using EMA with decay rate 0.9999 to stabilize training, consistent with large-scale 2D diffusion models.

**Delta**: training stabilization (qualitative)
**Condition**: Large-scale diffusion model training on 10M shapes

**Evidence**: "To stabilize the training, we employ an exponential moving average with a decay rate of 0.9999, in line with existing 2D large-scale diffusion models"

## [NEGATIVE] Detail coefficient predictor from coarse coefficients
An additional network that regresses detail coefficients D0 from coarse coefficients, as used in prior work (Hui et al., 2022).

**Delta**: does not converge even on ShapeNet subset
**Condition**: Attempted approach for detail coefficient generation in large-scale training setting

**Evidence**: "in (Hui et al., 2022), an additional detail predictor is adopted to regress (predict) the detail coefficients D0 based on the coarse coefficients. We empirically find that this strategy does not converge well even in a subset of our dataset"

## [POSITIVE] Fixed-size binary mask for loss computation
Using a fixed-size binary mask to represent coordinate sets for efficient PyTorch compilation, enabling MSE loss calculation by masking generation targets and network predictions without irregular operations.

**Delta**: efficient code compilation (qualitative)
**Condition**: Subband adaptive training loss computation

**Evidence**: "For efficient code compilation in PyTorch, we utilize a fixed-size binary mask to represent the coordinate set. This allows us to calculate the MSE loss by masking both the generation target and network prediction, eliminating the need for irregular operations."

## [POSITIVE] Large-scale diverse training dataset (10M shapes)
Training on over 10 million 3D shapes aggregated from 18 publicly-available sub-datasets, enabling large-scale generalization.

**Delta**: ~2x to 6x more training shapes per day per GPU vs prior methods
**Condition**: Large-scale 3D generative model training

**Evidence**: "On average, we can process approximately 2x to 6x more training shapes in one day than prior methods, despite using a less powerful GPU (A10G vs. A100)"

## [POSITIVE] PointNet + Permutation Invariant Set Attention encoder
Using PointNet combined with a Permutation Invariant Set Attention (PMA) block as encoder for point cloud conditioning, supporting arbitrary number of points at inference.

**Delta**: consistent performance across diverse object categories (qualitative)
**Condition**: Point-cloud-to-3D conditional generation

**Evidence**: "we utilize PointNet (Qi et al., 2017a) combined with a Permutation Invariant Set Attention (PMA) block (Lee et al., 2019) as our encoder, which takes 25,000 points during the training phase and can accommodate an arbitrary number of points during inference"

## [POSITIVE] Compact model size (25M parameters)
Make-A-Shape uses approximately 25M parameters, significantly fewer than competing methods like OpenLRM (260M) and LRM/Instant3D (500M each).

**Delta**: similar or better performance vs OpenLRM (260M params) with only 1/10 the parameters
**Condition**: Image-to-3D generation task comparison

**Evidence**: "our model demonstrates similar or better performance for different metrics, despite that it has only one tenth of the model parameters (25M vs 260M, see Table 4), highlighting its high efficiency"
