# PruNeRF: Segment-Centric Dataset Pruning via 3D Spatial Consistency

**Source**: https://proceedings.mlr.press/v235/jung24b.html

## [POSITIVE] Influence Functions for pixel-wise distraction
Using Influence Functions (approximation of Leave-One-Out retraining) to measure the influence of individual train pixels on each other, identifying distractor pixels by their high self-influence scores

**Delta**: +0.11 to +0.52 PSNR over loss/gradnorm baselines at 5-10% pruning
**Condition**: Pixel-wise distraction measurement on NeRF training datasets with distractors

**Evidence**: "As shown in Table 1, Influence Function achieves higher performance than others in natural scenes. Additionally, Figure 2d demonstrates that Influence Function excels in highlighting distracting regions compared with loss and gradient-norm."

## [NEGATIVE] Loss-based distraction metric
Using sample-wise loss from a trained model's output space to identify distractor pixels

**Delta**: Lower PSNR than Influence Functions across all datasets
**Condition**: Pixel-wise distraction measurement; fails to distinguish hard-to-learn regions from distractors

**Evidence**: "In Figure 2b and Figure 2c, when using loss or gradient-norm, some distractor pixels show high values while others do not within distractors. Moreover, these metrics exhibit high values in hard-to-learn regions, such as the semi-transparent curtain and tablecloth patterns."

## [NEGATIVE] Gradient-norm distraction metric
Using sample-wise gradient-norm with respect to trained model parameters to identify distractor pixels

**Delta**: Lower PSNR than Influence Functions across all datasets
**Condition**: Pixel-wise distraction measurement; fails to distinguish hard-to-learn regions from distractors

**Evidence**: "In Figure 2b and Figure 2c, when using loss or gradient-norm, some distractor pixels show high values while others do not within distractors. Moreover, these metrics exhibit high values in hard-to-learn regions."

## [POSITIVE] 3D spatial consistency via depth-based reprojection
Assessing 3D spatial consistency by projecting query pixels to 3D surface points using estimated depth, then reprojecting to other views to estimate a distribution of self-influence scores and identify outliers

**Delta**: +1.03 PSNR on Statue, +0.70 on Android, +0.92 on BabyYoda over IF alone
**Condition**: Applied after pixel-wise distraction measurement; improves 3D-aware distractor identification

**Evidence**: "As shown in Table 4, while incorporating Influence Functions alone leads to performance improvement, achieving more accurate results necessitates considering 3D spatial consistency and applying pixel-to-segment refinement."

## [POSITIVE] Pixel-to-segment refinement via SAM
Using Segment Anything Model (SAM) for zero-shot segmentation to refine distractor identification from pixel-level to segment-level, filtering segments by ratio of distracting pixels

**Delta**: +0.38 PSNR on Statue, +0.29 on Android, +0.41 on BabyYoda over IF+3D consistency alone
**Condition**: Applied as final refinement step; addresses pixel-level noise and inaccuracies within objects

**Evidence**: "As shown in Table 4, while incorporating Influence Functions alone leads to performance improvement, achieving more accurate results necessitates considering 3D spatial consistency and applying pixel-to-segment refinement. Additionally, the qualitative results in Figure 6 also show that adding these components progressively leads to clearer removal of distractors."

## [POSITIVE] Arnoldi full-model Influence Function approximation
Using Arnoldi method for full-model parameter approximation of Influence Functions instead of limiting Hessian computation to the last layer only

**Delta**: +0.15 PSNR on Statue, +0.11 on Android, +0.20 on BabyYoda over last-layer IF
**Condition**: Alternative to last-layer-only Hessian computation; more accurate for NeRF network structures

**Evidence**: "The results indicate that using Arnoldi provides further improvement compared with using loss and gradnorm across three natural scenes."

## [NEUTRAL] Last-layer Hessian approximation for Influence Functions
Limiting Hessian inverse computation to only the last layer of the model to reduce computational cost of Influence Functions

**Delta**: Lower than Arnoldi but higher than loss/gradnorm baselines
**Condition**: Computational cost reduction; less accurate for NeRF than full-model approximation

**Evidence**: "While this approach is common in 2D image classification where the last layer typically serves as the classifier, it may lead to inaccuracies due to the different network structures in NeRF."

## [POSITIVE] Charbonnier loss for training stability
Using Charbonnier loss instead of L1 or L2 loss to enhance training stability in the base NeRF model

**Delta**: mip-NeRF360(Ch.) outperforms mip-NeRF360(L2) and mip-NeRF360(L1) on most datasets
**Condition**: Base NeRF training; used consistently across all PruNeRF experiments

**Evidence**: "To enhance training stability, we utilize the Charbonnier loss (Charbonnier et al., 1994)."

## [POSITIVE] Otsu algorithm for IF threshold selection
Using Otsu's method to automatically determine the threshold for Self-Influence scores for pruning, dividing data into two distributions by maximizing inter-class variance

**Delta**: +0.26 PSNR on Statue, +0.70 on Android, +5.18 on BabyYoda over mip-NeRF360 baseline
**Condition**: Used when applying Influence Functions alone without 3D consistency; reduces need for manual threshold selection

**Evidence**: "When evaluating the contribution of Influence Functions, denoted as '+IF' in Table 4, we employ the Otsu algorithm (Otsu, 1979) to determine the threshold of Self-Influence scores for pruning. This well-known method divides data into two distributions by maximizing inter-class variance, thereby reducing the reliance on human intervention in threshold selection."

## [NEGATIVE] Top-k% pruning with fixed threshold
Pruning the top-k% of pixels ranked by distraction metric score, requiring manual selection of hyperparameter k

**Delta**: Requires expensive hyperparameter search per dataset
**Condition**: Used for metric comparison experiments; not used in final PruNeRF method

**Evidence**: "It is also important to highlight that the top-k% pruning approach poses a challenge. This challenge arises from the significant cost required to search the optimal hyperparameter k for each dataset, particularly given the unknown types and numbers of distractors."

## [POSITIVE] Occlusion/depth error mitigation in reprojection
Filtering reprojected pixel correspondences by requiring Euclidean distance between source and projected depth points to fall below threshold θ=0.1

**Delta**: Not quantified separately
**Condition**: Applied during 3D spatial consistency assessment to improve reliability of correspondences

**Evidence**: "To mitigate occlusion and depth error issues, we estimate depth points at both the source and projected viewpoints and use points whose Euclidean distance between them falls below a threshold θ. We set θ to 0.1 for all datasets."

## [POSITIVE] Segment threshold ε for noise filtering
Filtering out segments containing a small number of noisy pixels using threshold ε=0.1 applied consistently across all datasets

**Delta**: Not quantified separately
**Condition**: Applied during pixel-to-segment refinement; consistent across datasets without per-dataset tuning

**Evidence**: "Threshold ε is used to filter out segments containing a small number of noisy pixels. Although dataset-specific tuning could offer further improvements, we set ε to 0.1 consistently across all datasets, as our target problem involves unknown types and quantities of distractors."
