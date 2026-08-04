# Prototypical Transformer As Unified Motion Learners

**Source**: https://proceedings.mlr.press/v235/han24d.html

## [POSITIVE] Cross-Attention Prototyping
Reformulates conventional self-attention into a prototypical cross-attention mechanism optimized via Expectation-Maximization (EM) clustering. Iteratively updates prototype assignments (E-step) and prototype centroids (M-step) to capture representative motion characteristics.

**Delta**: 0.55 → 0.51 on Sintel clean EPE
**Condition**: Optical flow estimation; ablation study on Sintel benchmark

**Evidence**: "After adding Cross-Attention Prototyping, substantial improvements are observed (i.e., 0.55 → 0.51 in clean pass), suggesting the efficacy of prototyping updating even without explicit prototype-feature assignment."

## [POSITIVE] Latent Synchronization
A masked cross-attention mechanism combined with Feed-Forward Networks that synchronizes feature representations with updated prototypes, building prototype-feature associations to reduce motion ambiguity.

**Delta**: 0.81 → 0.77 on Sintel final EPE
**Condition**: Optical flow estimation; ablation study on Sintel benchmark

**Evidence**: "Incorporating Latent Synchronization into Base can observe a noticeable performance gain (i.e., 0.81 → 0.77 in final pass)."

## [POSITIVE] Combined Cross-Attention Prototyping + Latent Synchronization
Integration of both Cross-Attention Prototyping and Latent Synchronization into the full ProtoFormer model.

**Delta**: 0.48 clean / 0.69 final on Sintel (vs base 0.55 / 0.81)
**Condition**: Optical flow estimation; full model on Sintel benchmark

**Evidence**: "Finally, the integration of the two techniques culminates in peak performance."

## [POSITIVE] EM-based Prototype Updating (vs Cosine Similarity)
Using EM clustering-based cross-attention prototyping instead of cosine similarity for prototype updates.

**Delta**: 0.48/0.69 vs 0.51/0.75 on Sintel clean/final
**Condition**: Optical flow; ablation comparing prototype updating strategies

**Evidence**: "From the efficient and effective perspectives, Cross-Attention Prototyping outperforms competitive methods (see Table 3b)."

## [POSITIVE] EM-based Prototype Updating (vs Vanilla Cross-Attention)
Using EM clustering-based cross-attention prototyping instead of vanilla cross-attention (Vaswani et al., 2017).

**Delta**: 0.48/0.69 vs 0.50/0.73 on Sintel clean/final
**Condition**: Optical flow; ablation comparing prototype updating strategies

**Evidence**: "Cross-Attention Prototyping outperforms competitive methods (see Table 3b)."

## [POSITIVE] EM-based Prototype Updating (vs Criss Cross-Attention)
Using EM clustering-based cross-attention prototyping instead of Criss Cross-Attention.

**Delta**: 0.48/0.69 vs 0.50/0.72 on Sintel clean/final
**Condition**: Optical flow; ablation comparing prototype updating strategies

**Evidence**: "Cross-Attention Prototyping outperforms competitive methods (see Table 3b)."

## [POSITIVE] EM-based Prototype Updating (vs K-Means)
Using EM clustering-based cross-attention prototyping instead of K-Means clustering.

**Delta**: 0.48/0.69 vs 0.49/0.71 on Sintel clean/final
**Condition**: Optical flow; ablation comparing prototype updating strategies

**Evidence**: "Cross-Attention Prototyping outperforms competitive methods (see Table 3b)."

## [POSITIVE] Number of EM Iterations N=3
Setting the number of EM clustering iterations to 3 as a balance between performance and computational cost.

**Delta**: 0.48 clean / 0.69 final (N=3 vs 0.52/0.75 at N=1)
**Condition**: Optical flow; ablation on number of iterations

**Evidence**: "the error progressively decreases from 0.52 to 0.48 when increasing N from 1 to 4, and saturates at 4. Considering the computation time, we set N=3 to strike the balance between performance and computational cost."

## [POSITIVE] Number of EM Iterations N=4
Using 4 EM iterations instead of 3.

**Delta**: 0.48/0.68 vs 0.48/0.69 at N=3
**Condition**: Optical flow; marginal improvement over N=3 but at higher computational cost

**Evidence**: "the error progressively decreases from 0.52 to 0.48 when increasing N from 1 to 4, and saturates at 4."

## [POSITIVE] Number of Prototypes K=100
Using 100 prototypes as the default cluster count for motion feature grouping.

**Delta**: 0.48/0.69 (K=100) vs 0.53/0.78 (K=10)
**Condition**: Optical flow; ablation on number of prototypes

**Evidence**: "The number of prototypes K plays a pivotal role in defining the central grouping points for motion features. We therefore investigate the variant of K in Table 3d."

## [NEUTRAL] Number of Prototypes K=200
Using 200 prototypes instead of 100.

**Delta**: 0.49/0.71 vs 0.48/0.69 at K=100
**Condition**: Optical flow; ablation on number of prototypes; more parameters but slightly worse performance

**Evidence**: "Table 3d shows K=200 yields 0.49/0.71 vs K=100 at 0.48/0.69, with more parameters (14.21M vs 11.90M)."

## [POSITIVE] Latent Synchronization with Masked Cross-Attention (vs None)
Applying the full Latent Synchronization with masked cross-attention and prototype anchoring versus no prototype-feature correspondence.

**Delta**: 0.74 → 0.69 on Sintel final
**Condition**: Optical flow; ablation on Latent Synchronization variants

**Evidence**: "With a standard setting without any prototype-feature corresponding (i.e., None), the model reports 0.74 in final pass... our proposed Latent Synchronization with carefully anchored prototypes yields advanced performance across all ablative methods (i.e., 0.69)."

## [POSITIVE] Latent Synchronization with Vanilla FC Layer
Using a vanilla fully-connected layer to update features instead of the full Latent Synchronization.

**Delta**: 0.74 → 0.73 on Sintel final (vs 0.69 with full Latent Synchronization)
**Condition**: Optical flow; ablation on Latent Synchronization variants; inferior to full method

**Evidence**: "After applying a vanilla fully-connected layer to update the feature, the error decreases to 0.73. Though inspiring, our proposed Latent Synchronization with carefully anchored prototypes yields advanced performance across all ablative methods (i.e., 0.69)."

## [POSITIVE] Latent Synchronization with FC + Similarity (Ma et al., 2023)
Using FC with similarity-based feature update instead of the full Latent Synchronization.

**Delta**: 0.49/0.71 vs 0.48/0.69 with full Latent Synchronization
**Condition**: Optical flow; ablation on Latent Synchronization variants; inferior to full method

**Evidence**: "Table 3e shows FC w/ Similarity yields 0.49/0.71 vs Ours (Eq. 7) at 0.48/0.69."

## [POSITIVE] Cross-Attention Prototyping Computational Efficiency
Cross-Attention Prototyping operates with time complexity O(NKHWD) compared to O(H²W²D) for standard self-attention, due to NK ≪ HW.

**Delta**: NK=60 vs HW=25920 in first stage with 960×432 resolution
**Condition**: Computational efficiency; especially pronounced in pyramid architectures and early network stages

**Evidence**: "Cross-Attention Prototyping operates with a time complexity of O(NKHWD), showing a significant improvement over the self-attention mechanism with O(H²W²D) (see §4.3). The foundation lies in the relationship that NK ≪ HW (e.g., 60 vs 25920 in the first stage with image of 960×432 resolution)."

## [NEUTRAL] Twins Architecture as Backbone
ProtoFormer is built upon the Twins architecture with two stages using window sizes of 4 and 8 for feature encoding.

**Delta**: None
**Condition**: Base architecture choice; used throughout all experiments

**Evidence**: "ProtoFormer is built upon Twins architecture (Chu et al., 2021). Detailed training and testing configurations are provided in §S1."

## [POSITIVE] Unified Training on C+T+S+K+H
Fine-tuning on a large combination of datasets (FlyingChairs, FlyingThings, Sintel, KITTI, HD1K) for optical flow.

**Delta**: 0.48/0.69 Sintel clean/final, 4.35 KITTI F1-epe; outperforms CRAFT by 0.48 and 0.69 on clean and final
**Condition**: Optical flow; full training setting C+T+S+K+H

**Evidence**: "our approach distinctly outperforms CRAFT, achieving 0.48 and 0.69 on the clean and final pass of Sintel, respectively."

## [POSITIVE] Prototype Learning for Depth Estimation
Applying ProtoFormer's prototype-based approach to scene depth estimation tasks.

**Delta**: 18.6% improvement in Sintel compared to AdaBins
**Condition**: Scene depth estimation on Sintel and KITTI benchmarks

**Evidence**: "we further show the superior performance on depth scene estimation (e.g., 18.6% improvement in Sintel compared to AdaBins)."

## [POSITIVE] Softmax Operator Modification (HW to K dimension)
Modifying the default softmax operator to normalize over K prototypes instead of HW spatial positions, mimicking EM clustering behavior.

**Delta**: None
**Condition**: Cross-Attention Prototyping layer design

**Evidence**: "We also modify the default softmax operator from HW to K, mimicking the EM clustering."

## [POSITIVE] Selective Key/Value Matrix Computation
In each EM iteration, only the query matrix Q is updated while key K and value V matrices are computed just once, reducing computational load.

**Delta**: None
**Condition**: Cross-Attention Prototyping; computational efficiency

**Evidence**: "In each iteration, only the query matrix Q requires an update; the key K and value V matrices are computed just once. This selective updating significantly reduces the computational load particularly beneficial in handling large-scale data in high-dimensional feature spaces."
