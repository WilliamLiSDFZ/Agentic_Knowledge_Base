# Stereo Risk: A Continuous Modeling Approach to Stereo Matching

**Source**: https://proceedings.mlr.press/v235/liu24af.html

## [POSITIVE] L1 Risk Minimization
Formulating disparity prediction as minimization of L1 norm risk function over continuous disparity distribution, finding the weighted median rather than weighted mean

**Delta**: Middlebury >1px NOC: 9.88 -> 9.32, >2px NOC: 4.92 -> 4.49 vs expectation baseline
**Condition**: Applied at both training and test time in stereo matching networks

**Evidence**: "if we use the L1-norm risk minimization at both train time and test time, the best accuracy is achieved under all metrics"

## [NEGATIVE] L2 Expectation-based Disparity (baseline)
Computing disparity as weighted average (expectation) of discrete disparity hypotheses, equivalent to L2 risk minimization

**Delta**: Middlebury >1px NOC: 9.88 vs 9.32 for L1-risk
**Condition**: Multi-modal disparity distributions, e.g., pixels at object boundaries

**Evidence**: "it is well known that the L2 norm is not robust to outliers. As an example, in Fig. 2 (b) it can be observed that the estimated expectation is inaccurate when there are multiple modes in the distribution"

## [POSITIVE] Laplacian Kernel Interpolation for Continuous PDF
Interpolating discrete disparity probability mass function using Laplacian kernels to obtain a continuous probability density function

**Delta**: Enables continuous risk minimization and derivative computation
**Condition**: Required for continuous L1 risk minimization over discrete disparity hypotheses

**Evidence**: "we propose to interpolate the discrete distribution via Laplacian kernel, and compute the probability density function... such a continuous modeling enable us to compute derivative of the proposed stereo risk function"

## [POSITIVE] Implicit Function Theorem for Backward Propagation
Using the implicit function theorem to compute gradients through the non-differentiable binary search forward pass, enabling end-to-end training

**Delta**: Enables end-to-end training with L1 risk minimization
**Condition**: Required for end-to-end training with non-differentiable binary search optimization

**Evidence**: "to enable end-to-end training, we have to compute dy/dp_m to propagate the gradient backward. Now, since G(y, p_m) ≡ 0 at the optimal y, we obtain the following via use of Implicit Function Theorem"

## [POSITIVE] Binary Search for L1 Risk Minimization
Using binary search to find the zero of the first derivative of the L1 risk function (the weighted sign function), exploiting convexity of the risk function

**Delta**: O(log N) time complexity for N disparity hypotheses
**Condition**: Forward prediction of optimal disparity during inference

**Evidence**: "We find the optimal disparity, i.e., the zero point of G(y, p_m), by binary search, as shown in Algorithm 1. For N disparity hypotheses, the binary search algorithm can find the optimal solution with time complexity of O(log N)"

## [POSITIVE] L1 Risk at Test Time Only (no retraining)
Applying L1 risk minimization only at test time while keeping expectation-based training, without retraining the network

**Delta**: ACVNet: >1px NOC 22.68->22.32, >2px NOC 13.54->13.13; PCWNet: >1px NOC 16.80->16.53, >2px NOC 8.93->8.65
**Condition**: Applied to existing networks (ACVNet, PCWNet) without retraining

**Evidence**: "Even with expectation minimization at train time, we slightly improve the matching accuracy with L1-norm risk minimization at test time... Our proposed method improves the accuracy under all metrics without re-training"

## [POSITIVE] Cascade Two-Stage Network Architecture
Two-stage coarse-to-fine network: coarse stage at 1/4 resolution with 192 uniform hypotheses, refined stage at 1/2 resolution with 16 hypotheses sampled around coarse prediction

**Delta**: Reduces time and memory cost while keeping matching accuracy
**Condition**: Applied throughout the full network pipeline

**Evidence**: "our network consists of two stages one to predict and other to refine the disparity map. This hierarchical design reduces the time and memory cost, while keeping the matching accuracy"

## [POSITIVE] Stacked Hourglass Cost Aggregation
Using three stacked 3D hourglass networks to aggregate matching costs across multiple scales in the cost volume

**Delta**: Aggregates information across various scales
**Condition**: Applied in both coarse and refined stages

**Evidence**: "We use the stacked hourglass architecture (Newell et al., 2016) to transform the stereo cost volume and aggregate the matching cost... This procedure helps aggregate information across various scales"

## [POSITIVE] Spatial Pyramid Pooling on Feature Maps
Applying spatial pyramid pooling on 1/4-resolution feature maps to enlarge the receptive field before fusing with 1/2-resolution features

**Delta**: Enlarges receptive field for feature extraction
**Condition**: Feature extraction module

**Evidence**: "we apply the spatial pyramid pooling (Zhao et al., 2017) on the 1/4-resolution feature map from the fourth stage to enlarge the receptive field"

## [POSITIVE] Gradient Clipping in Backward Pass
Clipping the denominator in the implicit function theorem gradient computation to be no less than 0.1 to avoid large gradients

**Delta**: Prevents training instability from large gradients
**Condition**: Backward propagation through risk minimization module

**Evidence**: "we clip the denominator sum_j p_j^m exp(-|y-d_j|/sigma) in the above equation to be no less than 0.1 to avoid large gradients"

## [POSITIVE] Weighted Loss with Coarse and Refined Stages
Total loss combining coarse stage loss (weight 0.1) and refined stage loss (weight 1.0) using smooth L1 loss

**Delta**: Enables multi-stage supervision
**Condition**: Training with two-stage network

**Evidence**: "We apply the above loss function to the predicted disparities from both the coarse and refined stages, and obtain L_coarse and L_refined, respectively. The total loss is thus defined as L = 0.1 * L_coarse + 1.0 * L_refined"

## [POSITIVE] Image Augmentation during Training
Applying color transformation, occlusion simulation, and spatial transformation augmentations during training to avoid overfitting

**Delta**: Avoids overfitting
**Condition**: Training on SceneFlow dataset

**Evidence**: "Following RAFT-Stereo (Lipson et al., 2021), we apply various image augmentations during training to avoid the over-fitting problem. Specifically, the augmentations include (a) color transformation, (b) occlusion, and (c) spatial transformation"

## [POSITIVE] Binary Search Tolerance tau=0.1
Setting binary search stopping tolerance to 0.1, requiring approximately 11 iterations to converge

**Delta**: >1px NOC: 9.32 vs 9.36 for tau=0.3; no improvement vs tau=0.01
**Condition**: Binary search forward prediction

**Evidence**: "when decreasing the value of tau, the search algorithm will iterate for more times to search for the optimal solution. And the error of the predicted disparity is reduced. When tau >= 0.1, the algorithm achieves the best accuracy"

## [NEUTRAL] Concatenation-based Cost Volume
Constructing 4D stereo cost volume by concatenating features from left and right images along the channel dimension for each disparity hypothesis

**Delta**: Standard approach used in prior work
**Condition**: Matching module in both coarse and refined stages

**Evidence**: "The features at each pair of candidates pixels for matching will be concatenated along the channel dimension, which forms a 4D stereo cost volume (feature x disparity x height x width)"

## [POSITIVE] Non-uniform Hypothesis Sampling in Refined Stage
In the refined stage, sampling 16 disparity hypotheses within a local 12x12 window around the coarse prediction instead of uniform sampling

**Delta**: Reduces search space for efficient high-resolution matching
**Condition**: Refined stage of cascade network

**Evidence**: "In the refined stage, we reduce the sampling space according to the predicted disparity from the coarse stage. Concretely, for each pixel we sample 16 hypotheses between the minimum and maximum disparity in the local window of size 12x12"
