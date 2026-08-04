# Sparse-to-dense Multimodal Image Registration via Multi-Task Learning

**Source**: https://proceedings.mlr.press/v235/zhang24ar.html

## [POSITIVE] Sparse-to-Dense (S2D) Registration Pipeline
A two-stage pipeline that first performs sparse feature matching (SM) to get an initial homography estimate, then refines it via dense alignment (DA). SM provides initialization for DA, combining efficiency of sparse methods with accuracy of dense methods.

**Delta**: outperforms baseline
**Condition**: Multimodal image registration across MSCOCO, GoogleEarth, VIS-NIR, VIS-IR-drone datasets

**Evidence**: "Our novel S2D pipeline yields lower APEs, i.e., higher accuracy, than the sparse-only and dense-only methods in most cases. This demonstrates the superiority of our S2D pipeline, i.e., SM serves as a robust initialization for DA, with DA subsequently refining the outcomes from SM."

## [POSITIVE] Multi-Task Learning (MTL) Network (SDME)
A unified network with shared encoder and task-specific decoders that simultaneously predicts features for both sparse matching (Task 1) and dense alignment (Task 2), reducing parameters and improving efficiency through shared representations.

**Delta**: 1.07M parameters, total pipeline under 100ms
**Condition**: Applied across all datasets; compared to separate single-task models

**Evidence**: "Our model comprises 1.07M parameters and the S2D pipeline operates within 100 ms, which strikes a balance between accuracy and efficiency."

## [POSITIVE] Modality-Invariant Transformer Block (MITB)
An attention mechanism applied between descriptors and a set of learnable modality-invariant elements to enlarge the receptive field of descriptors efficiently, helping descriptors attend to different areas in images across modalities.

**Delta**: slight performance improvement
**Condition**: Sparse branch descriptor learning; ablation on GoogleEarth and VIS-IR-drone (Model A vs Model B in Table 4)

**Evidence**: "We observed that MITB can bring a slight performance improvement since it enhances descriptors with a broader global receptive field."

## [POSITIVE] Multiple Gradient Descent Algorithm - Upper Bound (MGDA-UB)
A multi-objective optimization algorithm that dynamically determines gradient weights for the shared encoder by finding a descent direction that improves both tasks simultaneously, preventing one task from dominating the other during training.

**Delta**: +27% on GoogleEarth, +10% on VIS-IR-drone
**Condition**: Training the multi-task network; compared to fixed-weight combination (α=β=0.5) in ablation study

**Evidence**: "Compared model B with model C in Table 4, we find that MGDA-UB can improve the performance by 27% and 10% on GoogleEarth and VIS-IR-drone, respectively."

## [NEGATIVE] Fixed Weight Multi-Task Loss Combination
Using a fixed weighted combination αL_s + βL_d to balance sparse and dense branch losses during training, without dynamic gradient adjustment.

**Delta**: suboptimal; larger weight on one branch impairs the other
**Condition**: Multi-task training without MGDA-UB; tested with (α,β) = (0.1,0.9), (0.5,0.5), (0.9,0.1) in Table 5

**Evidence**: "It can be seen that larger weight of one branch will impair the performance of the other branch, and it is an expensive operation to search the optimal combination."

## [POSITIVE] Mutual Guidance: Task 2 (DA) Guides Task 1 (SM)
Uses the single-channel feature map X from the dense branch (which highlights modality-invariant structures) to guide keypoint heatmap learning in the sparse branch via a guidance loss L_guide, steering keypoint detection toward modality-invariant structures.

**Delta**: significant MMA performance boost across 1-10 pixel thresholds
**Condition**: Sparse branch keypoint learning in multimodal scenarios; evaluated on VIS-IR-drone and GoogleEarth

**Evidence**: "The introduction of the mutual guidance strategy leads to a significant performance boost, with our features achieving the highest level of performance. As shown in the red boxes in Fig. 7, this phenomenon can be attributed to the modality-invariant structures highlighted by the dense branch, which effectively guide the detection of keypoints across these structures."

## [POSITIVE] Mutual Guidance: Task 1 (SM) Guides Task 2 (DA)
Weights the feature-metric objective function in DA by the product of heatmap scores from both images, so that pixels with high repeatability contribute more to optimization and ambiguous areas are down-weighted.

**Delta**: APE 2.96→2.75 on VIS-IR-drone, APE 1.52→1.38 on GoogleEarth
**Condition**: Dense alignment refinement step; evaluated in Table 6 on VIS-IR-drone and GoogleEarth

**Evidence**: "It is evident that incorporating information from the sparse branch into the DA objective function steers the optimization towards more accurate outcomes."

## [POSITIVE] Average Precision (AP) Ranking Loss for Descriptors
Maximizes the Average-Precision metric for local descriptors using positive/negative samples within defined radius neighborhoods and random distractors, ensuring discriminative descriptors for sparse matching.

**Delta**: descriptive
**Condition**: Sparse branch descriptor learning; positive samples within 3 pixels radius, negatives between 5-7 pixels

**Evidence**: "We maximize the Average-Precision (AP) metric for all local descriptors in D... to ensure that local descriptors are accurate enough for SM."

## [POSITIVE] Single-Channel Feature Map for Dense Alignment
Transforms 128-dimensional feature vectors into a single-channel feature map by computing covariance matrices in 3×3 patches and taking the ratio of max/min row sums to trace, reducing time complexity from O(128³) to O(1).

**Delta**: time complexity reduced from O(128³) to O(1)
**Condition**: Dense alignment branch; applied during both training and inference

**Evidence**: "Directly using F_d for Eq. (2) results in O(128³) time complexity for the calculation of G_i^{-1}. To reduce the complexity... This process... builds a single-channel feature map X ∈ R^{H×W} for each image... the time complexity decreases from O(128³) to O(1)."

## [POSITIVE] Modality Consistency Loss (L_mc)
A loss that builds connection between different modalities in the dense branch by enforcing feature consistency across modalities using ground truth homography.

**Delta**: descriptive
**Condition**: Dense branch training for multimodal image registration

**Evidence**: "Besides, a modality consistency loss L_mc is introduced to build connection between different modalities."

## [POSITIVE] Contrastive Learning for Multimodal Descriptors
Uses contrastive learning (via AP loss) with small-radius negative sampling to ensure accuracy of sparse matching features, resulting in sharp feature-metric residuals near ground truth.

**Delta**: descriptive
**Condition**: Sparse branch training; negative samples sampled between radius 5 and 7 pixels

**Evidence**: "This can be attributed to the fact that the sparse branch is trained with contrastive learning (L_AP in Eq. (7)), where negative samples are found within a small radius from the positive samples. This ensures the accuracy of SM."

## [POSITIVE] Fine-tuning Pre-trained Single-Modal Model on Small Multimodal Datasets
Pre-training the model on a large single-modal dataset (MSCOCO) and then fine-tuning on only 10% of multimodal training data, enabling practical deployment when multimodal data is scarce.

**Delta**: VIS-NIR: APE 1.86→1.35, GoogleEarth: APE 1.87→1.49, VIS-IR-drone: APE 4.06→3.18
**Condition**: Transfer learning scenario; using only 10% of multimodal training data for fine-tuning

**Evidence**: "It shows performance is improved after fine-tuning on small datasets. This further shows the practicability of our method, since in practice single-modal datasets are easier to acquire than the multimodal ones."

## [POSITIVE] MNN + MAGSAC++ for Sparse Matching
Uses mutually nearest neighbor matching for building putative correspondences, followed by MAGSAC++ robust estimator with 1-pixel reprojection threshold and up to 10K iterations for homography estimation.

**Delta**: outperforms SuperGlue and LoFTR-based matchers in APE
**Condition**: Sparse matching stage; compared against SuperPoint+SuperGlue, ReDFeat+SuperGlue, LoFTR in Table 3

**Evidence**: "It can be seen that although our method only involves the simplest matcher (i.e., MNN), it still outperforms the sophisticated GNN- or Transformer-based matchers. This occurs as matchers merely offer an initial setup with limited accuracy, and the substantial enhancement in accuracy is derived from DA in our case."

## [POSITIVE] Inverse Compositional Lucas-Kanade (ICLK) for Dense Alignment
Applies warp increments on the template image instead of the input image, allowing the Jacobian to be pre-computed and reused across iterations, improving computational efficiency of the iterative optimization.

**Delta**: descriptive
**Condition**: Dense alignment optimization; maximum 15 iterations during inference

**Evidence**: "Following (Chang et al., 2017; Zhao et al., 2021), we use Inverse Compositional Lucas-Kanade (ICLK) to improve the efficiency of optimization."

## [NEGATIVE] Coarse-to-Fine Feature Pyramid in Dense Alignment (DeepLK baseline)
DeepLK constructs a feature pyramid with three unshared networks and optimizes homography in a coarse-to-fine manner using single-channel feature maps.

**Delta**: descriptive
**Condition**: Dense-only baseline (DeepLK); without good initialization from sparse matching

**Evidence**: "Although this single-channel feature map improves optimization efficiency, its convergence is limited and highly dependent on initialization conditions."
