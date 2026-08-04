# 3D Geometric Shape Assembly via Efficient Point Cloud Matching

**Source**: https://proceedings.mlr.press/v235/lee24s.html

## [POSITIVE] Proxy Match Transform (PMT)
A low-complexity high-order feature transform layer that approximates conventional high-order convolution with sub-quadratic complexity by using a shared low-dimensional proxy tensor to exchange information between two feature sets, avoiding direct construction of memory-intensive pairwise correlation scores.

**Delta**: outperforms baseline
**Condition**: 3D geometric shape assembly task, both coarse- and fine-level matching

**Evidence**: "The experiments demonstrate that our method outperforms existing approaches by a significant margin while being computationally efficient compared to the baselines."

## [POSITIVE] Shared Proxy Tensor
A single proxy tensor P shared between the two independent PMT transforms for source and target features, enabling information exchange between the feature pair without computing pairwise correlations.

**Delta**: CRD: 0.53->0.39, CD: 0.47->0.25, RMSE(R): 21.04->17.14, RMSE(T): 6.93->5.53
**Condition**: Ablation on everyday subset of Breaking Bad dataset; compared to no proxy and unshared proxy

**Evidence**: "By sharing proxy tensor in each Proxy Match Transform layer, two independent feature transforms share information, yielding the highest score."

## [NEGATIVE] No Proxy Tensor (baseline)
Removing the proxy tensor entirely from PMT, so no information exchange occurs between source and target features.

**Delta**: CRD: 0.39->0.53, CD: 0.25->0.47, RMSE(R): 17.14->21.04, RMSE(T): 5.53->6.93
**Condition**: Ablation study on everyday subset of Breaking Bad dataset

**Evidence**: "The results, summarized in Tab. 2, clearly indicate that both removing the proxy and not sharing it lead to a significant decline in assembly performance."

## [NEGATIVE] Unshared Proxy Tensor
Using two different proxy tensors for the source and target PMT transforms instead of a single shared one.

**Delta**: CRD: 0.39->0.44, CD: 0.25->0.31, RMSE(R): 17.14->18.66, RMSE(T): 5.53->5.97
**Condition**: Ablation study on everyday subset of Breaking Bad dataset

**Evidence**: "The results, summarized in Tab. 2, clearly indicate that both removing the proxy and not sharing it lead to a significant decline in assembly performance."

## [POSITIVE] Orthonormal Loss (L_orth)
Auxiliary training loss that enforces orthonormality constraint on proxy tensors (P^(i)^T P^(j) = I when i=j), enabling PMT to approximate high-dimensional convolution.

**Delta**: RMSE(R): 18.82->17.87 (with L_orth alone); best when combined with L_zero
**Condition**: Ablation on everyday subset of Breaking Bad dataset

**Evidence**: "as evident from the table, the best performance is achieved when both losses are incorporated. This highlights that the significance of these constraining conditions for PMT, as they are crucial in enabling PMT to effectively approximate the high-dimensional convolution."

## [POSITIVE] Zero Loss (L_zero)
Auxiliary training loss that enforces zero-matrix constraint on proxy tensors (P^(i)^T P^(j) = 0 when i≠j), enabling PMT to approximate high-dimensional convolution.

**Delta**: CD: 0.31->0.27 (with L_zero alone); best when combined with L_orth
**Condition**: Ablation on everyday subset of Breaking Bad dataset

**Evidence**: "as evident from the table, the best performance is achieved when both losses are incorporated. This highlights that the significance of these constraining conditions for PMT, as they are crucial in enabling PMT to effectively approximate the high-dimensional convolution."

## [POSITIVE] Combined L_orth and L_zero
Using both orthonormal and zero auxiliary losses together to constrain proxy tensors to satisfy conditions for approximating high-dimensional convolution.

**Delta**: CRD: 0.43->0.39, CD: 0.31->0.25, RMSE(R): 18.82->17.14, RMSE(T): 6.23->5.53
**Condition**: Ablation on everyday subset of Breaking Bad dataset; compared to using neither or only one loss

**Evidence**: "the best performance is achieved when both losses are incorporated."

## [POSITIVE] Coarse-to-Fine Matching Framework (PMTR)
A hierarchical matching pipeline using PMT at both coarse and fine levels, where coarse-level matching localizes mating surfaces and fine-level matching refines correspondences for precise geometric alignment.

**Delta**: CRD: 0.53->0.39, CD: 0.43->0.25, RMSE(R): 20.70->17.14, RMSE(T): 6.63->5.53
**Condition**: Pairwise shape assembly on everyday subset of Breaking Bad dataset; compared to coarse-only PMT

**Evidence**: "incorporating the PMT layer as both fine and coarse matcher consistently leads to superior performance, affirming its superiority over the state-of-the-art matching layers"

## [POSITIVE] Fine-level PMT Matcher
Applying PMT layers at the fine (high-resolution) matching stage to refine correspondences identified at the coarse level.

**Delta**: consistently improves over no fine matcher across all coarse matcher types
**Condition**: Ablation study (Table 5) across various coarse-level matchers on everyday subset of Breaking Bad dataset

**Evidence**: "As evident from the tables, incorporating the PMT layer as both fine and coarse matcher consistently leads to superior performance"

## [NEGATIVE] High-Dimensional Convolution (HDC) at Fine Level
Using vanilla high-order convolution (Min et al., 2021) as the fine-level matcher, which has quadratic complexity O(|X|·|Y|).

**Delta**: out-of-memory error
**Condition**: Fine-level matching with large input spatial resolutions (|X|, |Y| > 1500)

**Evidence**: "While the matching layers of HDC and GeoTr cause out-of-memory-error due to their quadratic complexity, being unable to be incorporated at fine-level with large input spatial resolutions"

## [NEGATIVE] GeoTransformer (GeoTr) at Fine Level
Using GeoTransformer (Qin et al., 2022) as the fine-level matcher, which has quadratic complexity.

**Delta**: out-of-memory error
**Condition**: Fine-level matching with large input spatial resolutions (|X|, |Y| > 1500)

**Evidence**: "While the matching layers of HDC and GeoTr cause out-of-memory-error due to their quadratic complexity, being unable to be incorporated at fine-level with large input spatial resolutions"

## [NEGATIVE] No Fine-Level Matcher
Using only coarse-level matching without any fine-level refinement step.

**Delta**: CRD: 0.39->0.53, CD: 0.25->0.43, RMSE(R): 17.14->20.70, RMSE(T): 5.53->6.63
**Condition**: Ablation study on fine-level matcher choice, everyday subset of Breaking Bad dataset

**Evidence**: "Undoubtedly, the layers without any information exchange between source and target features, e.g., None, Linear, and MLP, show dramatic drops in performance."

## [NEGATIVE] Linear Transform at Fine Level
Using a single linear transformation as the fine-level matcher, without cross-feature information exchange.

**Delta**: CRD: 0.39->0.47, CD: 0.25->0.37, RMSE(R): 17.14->17.55, RMSE(T): 5.53->5.68
**Condition**: Ablation study on fine-level matcher, everyday subset of Breaking Bad dataset

**Evidence**: "the layers without any information exchange between source and target features, e.g., None, Linear, and MLP, show dramatic drops in performance."

## [NEGATIVE] MLP at Fine Level
Using a multi-layer perceptron as the fine-level matcher, without cross-feature information exchange.

**Delta**: CRD: 0.39->0.49, CD: 0.25->0.38, RMSE(R): 17.14->17.35, RMSE(T): 5.53->5.69
**Condition**: Ablation study on fine-level matcher, everyday subset of Breaking Bad dataset

**Evidence**: "the layers without any information exchange between source and target features, e.g., None, Linear, and MLP, show dramatic drops in performance."

## [POSITIVE] Local (Sparse) Attention in PMT
Using sparse local attention for the attention matrices A_X and A_Y by collecting attention scores only for neighborhood points, reducing complexity from O(|X|x|X|) to O(|X|xε) where ε is the number of neighbors.

**Delta**: avoids quadratic complexity
**Condition**: Implementation of PMT attention matrices to avoid quadratic complexity

**Evidence**: "This method significantly reduces the computational complexity typically associated with full pairwise attention, which would otherwise be quadratic, i.e., |X| × |X|."

## [POSITIVE] KPConv-FPN Backbone
A U-Net shaped feature extraction network based on KPConv with FPN that generates three pairs of point cloud features at different spatial resolutions for coarse-to-fine matching.

**Delta**: outperforms baseline
**Condition**: Feature extraction stage of PMTR framework

**Evidence**: "The feature extraction network generates three pairs of features, each at distinct spatial resolutions. These feature pairs are subsequently fed to a corresponding PMT layer, which facilitates both coarse-level matching (for mating surface localization) and fine-level matching (for geometric matching)."

## [POSITIVE] Point-to-Node Grouping
Clustering fine-level features that are spatially proximate to coarse matches to sharpen broad coarse-level correspondences into more precise fine-level ones.

**Delta**: outperforms baseline
**Condition**: Transition from coarse to fine matching in PMTR

**Evidence**: "we employ the point-to-node grouping method (Yu et al., 2021), which clusters fine-level features that are spatially proximate to the coarse matches, effectively sharpening the broad coarse-level correspondence into more precise fine-level ones."

## [POSITIVE] Optimal Transport Layer
Applying an optimal transport layer (Sinkhorn) to fine-level matches to obtain final correspondences for transformation prediction.

**Delta**: outperforms baseline
**Condition**: Fine-level matching stage of PMTR

**Evidence**: "We then incorporate an optimal transport layer (Sarlin et al., 2020) to the fine-level matches to obtain final correspondences for the subsequent transformation prediction."

## [POSITIVE] Relative Transformation Prediction
Predicting relative transformation between input parts (setting largest fracture as anchor) instead of absolute pose prediction used by prior methods.

**Delta**: outperforms baseline
**Condition**: Evaluation and training of correspondence-based assembly methods

**Evidence**: "we suggest to predict the relative transformation between input parts, allowing us to focus solely on the assembly rather than the predefined absolute poses."

## [POSITIVE] Overlap-Aware Circle Loss (L_oc)
Training objective for coarse-level correspondence matching adopted from Qin et al. (2022).

**Delta**: outperforms baseline
**Condition**: Training of PMTR for coarse-level matching

**Evidence**: "Following the previous 3D matching literatures, we adopt overlap-aware circle loss L_oc (Qin et al., 2022), and point matching loss L_p (Sarlin et al., 2020), as our main training objectives for coarse- and fine-level correspondence matching respectively."

## [POSITIVE] Point Matching Loss (L_p)
Training objective for fine-level correspondence matching adopted from Sarlin et al. (2020).

**Delta**: outperforms baseline
**Condition**: Training of PMTR for fine-level matching

**Evidence**: "Following the previous 3D matching literatures, we adopt overlap-aware circle loss L_oc (Qin et al., 2022), and point matching loss L_p (Sarlin et al., 2020), as our main training objectives for coarse- and fine-level correspondence matching respectively."

## [POSITIVE] Pose Graph with Transformation Averaging for Multi-Part Assembly
Extending pairwise assembly to multi-part scenarios by constructing a pose graph of pairwise relative transformations and optimizing it using Shonan rotation averaging.

**Delta**: CRD: 6.51 vs 14.13 (Jigsaw), CD: 5.56 vs 11.82, RMSE(R): 31.57 vs 41.12, RMSE(T): 9.95 vs 11.74, PACRD: 66.95% vs 52.48%, PACD: 70.56% vs 60.26% on everyday
**Condition**: Multi-part assembly evaluation on Breaking Bad dataset

**Evidence**: "our method significantly surpasses all baselines on all metrics on the multi-part assembly, demonstrating robust generalization to multiple input scenarios."

## [NEGATIVE] Global Embedding Regression (baseline)
Encoding each part as a global embedding and directly regressing absolute transformations using MLP, as done by prior methods (Global, LSTM, DGL, NSM, Wu et al.).

**Delta**: RMSE(R) ~83-110 degrees vs 17.14 for PMTR on everyday subset
**Condition**: Pairwise shape assembly on Breaking Bad dataset; compared to correspondence-based methods

**Evidence**: "The global encoding strategy for each part, while simplifying the process, greatly limits local information by collapsing spatial resolutions, which is necessary to localize mating surface."

## [POSITIVE] Group Normalization in PMT Layers
Applying group normalization after each PMT layer in the coarse and fine matchers.

**Delta**: outperforms baseline
**Condition**: Architecture of PMTR coarse and fine matchers

**Evidence**: "Each of both coarse-level and fine-level matchers consists of 2 PMT(·) layers (Nt = 2) with nonlinearity and group norm (Wu & He, 2018)."
