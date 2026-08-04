# GaussianPro: 3D Gaussian Splatting with Progressive Propagation

**Source**: https://proceedings.mlr.press/v235/cheng24f.html

## [POSITIVE] Progressive Gaussian Propagation
A strategy inspired by multi-view stereo that propagates depth and normal information from well-modeled regions to under-modeled regions using patch matching, then initializes new Gaussians at pixels where propagated depth significantly differs from rendered depth.

**Delta**: +0.49 dB PSNR on Waymo (from 33.53 to 34.02)
**Condition**: Ablation on Waymo dataset; most effective in large-scale scenes with textureless surfaces

**Evidence**: "the progressive propagation strategy (the third row) brings significant improvement compared with the baseline. This improvement can be attributed to its ability to refine the geometric representation of the scene, particularly in regions where the initial 3DGS exhibits significant errors"

## [POSITIVE] Planar Constraint Loss
A loss combining L1 and angular loss to enforce consistency between rendered normals and propagated normals, plus a scale regularization loss to flatten Gaussians toward planar shapes.

**Delta**: +0.46 dB PSNR on Waymo (from 34.02 to 34.48 with propagation; full model reaches 34.68)
**Condition**: Ablation on Waymo dataset; particularly effective for scenes with planar structures like roads

**Evidence**: "The planar constraint can further enhance the rendering quality by accurately modeling the normals of the planes, as shown in the third row of Figure 6."

## [POSITIVE] Hybrid Geometric Representation (2D depth/normal maps from 3D Gaussians)
Rendering depth and normal maps from 3D Gaussians via alpha-blending to create structured 2D representations that enable efficient neighbor search and geometric propagation.

**Delta**: outperforms baseline
**Condition**: Core component enabling the propagation strategy; applied throughout training

**Evidence**: "Due to the irregular distribution and absence of connectivity among 3D Gaussians, it is challenging to perceive the connectivity of geometries... we propose to tackle this challenge by mapping the 3D Gaussians into structured 2D image space. This mapping allows us to efficiently determine the neighbors of the Gaussians and propagate geometric information among them."

## [POSITIVE] Patch Matching for Candidate Selection
Using NCC-based homography patch matching to evaluate color consistency between reference and neighboring views, selecting the best plane candidate (depth and normal) for each pixel.

**Delta**: outperforms baseline
**Condition**: Applied during progressive propagation step every 50 iterations

**Evidence**: "we employ patch matching (Bleyer et al., 2011) to propagate the depth and normals from neighboring pixels to the current pixel, producing new depths and normals (named as propagated depth/normal)."

## [POSITIVE] Multi-view Geometric Consistency Filtering
Filtering out inaccurate propagated depths and normals by checking geometric consistency across multiple target views, retaining pixels that appear consistent in at least τ target views.

**Delta**: outperforms baseline
**Condition**: Applied after propagation to ensure quality of new Gaussian initialization

**Evidence**: "Due to the inevitable errors in the propagated results, we filter out inaccurate depth and normal through multi-view geometric consistency check (Schönberger et al., 2016) and obtain filtered depth and normal maps."

## [NEUTRAL] Propagation Interval (m=50)
Running the progressive propagation strategy every 50 training iterations as a balance between rendering quality and training time.

**Delta**: 36.08 PSNR at m=50 vs 36.11 at m=10 (best quality), 48min at m=90 vs 56min at m=50
**Condition**: Ablation on propagation interval; trade-off between quality and training time

**Evidence**: "Table 8 illustrates that the quality of rendering improves as the interval between Gaussian propagation decreases, eventually converging when the interval reaches 50. Shorter intervals lead to more frequent propagation... However, an increase in the total number of propagation iterations also leads to higher time costs."

## [POSITIVE] Number of Propagation Iterations (u=3)
Iterating the propagation of plane candidates 3 times to transmit geometric information over larger regions.

**Delta**: 35.80 PSNR at u=1 vs 36.08 at u=3; quality stabilizes after 3 iterations
**Condition**: Ablation on propagation iterations; diminishing returns beyond u=3

**Evidence**: "Table 9 shows that an increase in propagation times u of plane candidates results in improved rendering quality, which stabilizes after reaching 3 iterations. Increasing the number of iterations allows candidate planes for a pixel to be propagated from more distant areas, enabling better error correction over larger areas."

## [POSITIVE] Number of Neighboring Pixels (8 neighbors)
Using 8 neighboring pixels following the checkerboard pattern from ACMH as propagation candidates.

**Delta**: 35.42 PSNR with 1 neighbor vs 36.08 with 8 neighbors; no additional training time cost
**Condition**: Ablation on neighbor count; all configurations have same training time due to parallelism

**Evidence**: "Since the propagation of neighboring points is computed in parallel, the number of neighboring points does not affect the time consumption. A sparse selection of points cannot cover the entire neighboring areas, thus limiting the improvement in rendering quality. As the number of neighboring points increases, the rendering quality improves and finally converges."

## [POSITIVE] Sky Masking
Using Segformer to segment and mask sky regions during propagation and plane constraint to avoid incorrect Gaussian densification in geometrically undefined regions.

**Delta**: not quantified separately
**Condition**: Applied only for outdoor datasets like Waymo

**Evidence**: "For outdoor datasets like Waymo, we use Segformer (Xie et al., 2021) to segment the sky region. Since the sky lacks precise geometric structure, we mask the sky during the propagation process to avoid Gaussian densification and plane constraint."

## [NEGATIVE] MVS Point Cloud Initialization for 3DGS
Directly initializing 3DGS with dense MVS-generated point clouds instead of sparse SfM points.

**Delta**: Street: 36.13 PSNR but 250min training and 75 FPS vs GaussianPro's 36.08 PSNR, 56min, 108 FPS
**Condition**: Comparison baseline; trade-off heavily favors GaussianPro in efficiency

**Evidence**: "directly inputting the MVS point cloud significantly increases the training time (approximately 4 times) due to the additional MVS process and the large number of initial Gaussians. Moreover, the number of Gaussians increases significantly, and the rendering speed noticeably decreases, despite a slight improvement in rendering quality."

## [POSITIVE] Increased Gaussian Count via Lower Gradient Threshold (3DGS*)
Retraining 3DGS with a lower gradient threshold for densification to generate more Gaussians, testing whether quantity alone explains quality improvements.

**Delta**: +0.36 dB PSNR on Waymo (33.53 to 33.89) but still 0.79 dB below GaussianPro with fewer Gaussians
**Condition**: Ablation on Waymo; demonstrates quality improvement is not merely due to more Gaussians

**Evidence**: "even when the number of Gaussians in 3DGS* is larger than ours, its rendering quality remains significantly lower than ours. This highlights the importance of our strategy in densifying Gaussians with accurate positions and orientations."

## [POSITIVE] Better SfM Point Cloud Initialization
Retraining 3DGS with improved SfM point clouds generated using COLMAP with better settings.

**Delta**: +0.67 dB PSNR on MipNeRF360 (27.21 to 27.88) with fewer Gaussians (3009k vs 3362k)
**Condition**: Applied on MipNeRF360; shows initialization quality matters significantly

**Evidence**: "the retrained 3DGS (mentioned in results on MipNeRF360 of Section 5.2) achieves better rendering quality due to more accurate SfM point clouds, even with fewer Gaussians."

## [POSITIVE] GaussianPro on Textureless Large-Scale Scenes
Applying the full GaussianPro method (propagation + planar constraint) on large-scale urban scenes with textureless surfaces.

**Delta**: +1.15 dB PSNR on Waymo dataset over 3DGS baseline
**Condition**: Waymo large-scale urban dataset with textureless road surfaces

**Evidence**: "compared to the baseline 3DGS, our method significantly improves PSNR by 1.15 dB."

## [NEUTRAL] GaussianPro on Small-Scale Textured Scenes
Applying the full GaussianPro method on small-scale scenes with rich textures.

**Delta**: +0.04 dB PSNR on MipNeRF360 over retrained 3DGS (27.88 to 27.92)
**Condition**: MipNeRF360 dataset; limited benefit in texture-rich small-scale scenes

**Evidence**: "Our method achieves comparable results with 3DGS with a slight improvement. The MipNeRF360 dataset contains quite small-scale natural and indoor scenes with rich textures, so the SfM techniques usually provide a high-quality point cloud for initialization and the simple clone and split densification strategies don't show a bottleneck in the small-scale scenes."

## [POSITIVE] Robustness to Sparse Training Images
Evaluating GaussianPro with reduced training image sets (30%, 50%, 70%, 100%) compared to 3DGS.

**Delta**: At 30%: 28.64 vs 28.45 PSNR; at 100%: 31.98 vs 31.71 PSNR consistently across all ratios
**Condition**: Room scene of MipNeRF360 with varying training image ratios

**Evidence**: "our method consistently achieves superior rendering results compared to 3DGS across different percentages of training images."

## [POSITIVE] Geometry Accuracy Improvement
GaussianPro's propagation strategy improves the accuracy of rendered depth maps as measured by standard depth evaluation metrics.

**Delta**: Abs Rel: 0.081 vs 0.349; MAE: 1.97m vs 6.11m; δ1: 0.933 vs 0.570
**Condition**: Waymo dataset depth evaluation

**Evidence**: "The results clearly show a significant improvement in common depth evaluation metrics (Laina et al., 2016)."
