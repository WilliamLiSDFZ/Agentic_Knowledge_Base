# PointMC: Multi-instance Point Cloud Registration based on Maximal Cliques

**Source**: https://proceedings.mlr.press/v235/wu24k.html

## [POSITIVE] Local Spatial Consistency (LSC)
Graph-based method that confines correspondences within a single instance by measuring geometric compatibility within local regions, rather than globally across all correspondences

**Delta**: +1.54% MR, +0.37% MP on ModelNet40; +1.9% MR, +1.4% MP on Scan2CAD
**Condition**: Multi-instance point cloud registration, especially scenes with multiple overlapping instances

**Evidence**: "PointMC combined with local spatial consistency improved the average recall rate by 1.54% and the average accuracy by 0.37% on the ModelNet40 dataset, and increased the average recall rate by 1.9% and the average accuracy by 1.4% on the Scan2CAD dataset."

## [NEGATIVE] Global Spatial Consistency (GSC)
Traditional approach ensuring distance between each pair of points is preserved under rigid transformation, used as baseline comparison

**Delta**: -1.54% MR, -0.37% MP on ModelNet40 vs LSC; -1.9% MR, -1.4% MP on Scan2CAD vs LSC
**Condition**: Multi-instance registration with overlapping instances; reliability decreases with dense noisy correspondences

**Evidence**: "due to the ambiguity of global spatial consistency, they struggle to effectively differentiate multiple overlapping instances in multi-instance registration scenarios"

## [POSITIVE] Second-Order Compatibility Measure (SOC)
Encodes richer information beyond first-order measurements by considering commonly compatible matches in the correspondence set, promoting sparsity in the compatibility graph

**Delta**: +1.61% MR, +0.51% MP, -0.02s on ModelNet40; +2.39% MR, +2.47% MP, -0.03s on Scan2CAD
**Condition**: Compatibility graph construction, especially in scenarios with high outlier rates

**Evidence**: "Combining second-order compatibility measure, PointMC achieved an average recall improvement of 1.61% and an average precision improvement of 0.51% on the ModelNet40 dataset. It also reduced the runtime by 0.02s. On the Scan2CAD dataset, it achieved an average recall improvement of 2.39% and an average precision improvement of 2.47%. The runtime was reduced by 0.03s."

## [NEGATIVE] First-Order Compatibility Measure (FOC)
Standard pairwise geometric compatibility measure between correspondences without higher-order information

**Delta**: -1.61% MR, -0.51% MP on ModelNet40; -2.39% MR, -2.47% MP on Scan2CAD vs SOC
**Condition**: High outlier rate scenarios; less sparse graph slows maximal clique search

**Evidence**: "By utilizing SOC to construct the compatibility graph, not only does it consider the geometric consistency of correspondences, but it also focuses on the commonly compatible matches in the correspondence set, making it more robust compared to FOC, especially in scenarios with high outlier rates."

## [POSITIVE] Maximal Cliques Search Strategy
Searches for all maximal cliques (not just maximum clique) on the correspondence compatibility graph to generate multiple pose hypotheses, one per instance

**Delta**: +1.75% MF, -0.01s vs closest competitor on ModelNet40; +25.94% MR, +21.92% MP, +25.81% MF average improvement on Scan2CAD
**Condition**: Multi-instance point cloud registration; more suitable than maximum clique for multi-instance scenarios

**Evidence**: "A large number of maximal cliques in an undirected graph are associated with multiple instances, while a small number of maximum cliques are likely to be associated with only one instance. Therefore, adopting a maximal cliques search strategy is more suitable for multi-instance point cloud registration tasks."

## [POSITIVE] Low-Dimensional Transformation Clustering
Clustering 6D or 7D pose vectors instead of high-dimensional correspondence features to group transformations into per-instance clusters

**Delta**: outperforms baseline; faster runtime
**Condition**: Post-hypothesis generation step; compared to spectral clustering of high-dimensional features

**Evidence**: "Compared to clustering the high-dimensional correspondence features, clustering the low-dimensional pose vectors is computationally more efficient, and the final transformations can be obtained without the need for iterative optimization."

## [POSITIVE] DBSCAN Clustering Algorithm
Density-based clustering algorithm applied to low-dimensional rigid transformation vectors for grouping transformations by instance

**Delta**: -42.9% runtime on ModelNet40; -36.4% runtime on Scan2CAD vs Chameleon; slightly lower accuracy than Chameleon
**Condition**: Large-scale datasets where efficiency is prioritized over marginal accuracy gains

**Evidence**: "PointMC combined with DBSCAN algorithm had a 42.9% reduction in runtime on ModelNet40 datasets and a 36.4% reduction on Scan2CAD datasets."

## [POSITIVE] Chameleon Clustering Algorithm
Hierarchical clustering algorithm using two-step strategy with merging to explore hidden clusters in low-dimensional transformation data

**Delta**: +0.26% MR, +0.03% MP on ModelNet40; +1.88% MR, +2.76% MP on Scan2CAD vs DBSCAN; +0.03-0.04s runtime overhead
**Condition**: Real-world datasets with complex clustering structures; when accuracy is prioritized over speed

**Evidence**: "PointMC combined with Chameleon algorithm improved the average recall rate by 0.26% and the average accuracy by 0.03% on ModelNet40 dataset, and the average recall rate by 1.88% and the average accuracy by 2.76% on Scan2CAD dataset."

## [POSITIVE] Graph-Based Correspondence Embedding Module
Stack of spatial-consistency-aware self-attention (SCASA) modules that refine correspondence features using local spatial consistency for inlier/outlier discrimination

**Delta**: outperforms baseline methods
**Condition**: Feature extraction stage for putative correspondences in multi-instance registration

**Evidence**: "the extracted discriminative features empower the network to circumvent missed pose detection in scenarios involving multiple overlapping instances"

## [POSITIVE] Binary Focal Loss for Correspondence Classification
Focal loss used to supervise confidence scores for inlier/outlier classification of correspondences

**Delta**: not quantified separately
**Condition**: Training the correspondence classification head

**Evidence**: "We adopt the binary focal loss to supervise the confidence scores"

## [POSITIVE] Correspondence Filtering with Confidence Threshold
Correspondences with confidence scores above threshold τ=0.6 are kept as inliers; others removed as outliers before graph construction

**Delta**: not quantified separately
**Condition**: Pre-processing step before compatibility graph construction

**Evidence**: "The correspondences with confidence scores higher than the threshold τ are considered inliers, while the remaining correspondences are treated as outliers and removed."

## [NEGATIVE] Spectral Clustering on High-Dimensional Features (PointCLM approach)
Clustering high-dimensional correspondence features using spectral clustering algorithm to group correspondences by instance

**Delta**: lower MF than PointMC; higher runtime
**Condition**: Multi-instance registration; particularly costly with large numbers of correspondences

**Evidence**: "the utilization of spectral clustering algorithms incurs high computational costs when clustering high-dimensional features, leading to longer registration times... the learned high-dimensional features provide limited improvement to the overall results, while the process of clustering such features proves to be time-consuming"

## [POSITIVE] SVD-Based Transformation Estimation per Clique
Applying SVD or weighted SVD algorithm to each maximal clique's compatible correspondences to generate transformation hypotheses as low-dimensional vectors

**Delta**: not quantified separately
**Condition**: Transformation generation from maximal cliques

**Evidence**: "By applying the SVD algorithm or the weighted SVD algorithm to each set of compatible correspondences, we can obtain a collection of transformations Tall composed of 7D or 6D vectors."

## [POSITIVE] Improved Bron-Kerbosch Algorithm with igraph
Parallelizable backtracking algorithm for complete maximal clique enumeration, encapsulated in igraph C++ library

**Delta**: not quantified separately
**Condition**: Maximal clique search step; benefits from parallel computing environments

**Evidence**: "It guarantees completeness in finding all maximal cliques, and its backtracking technique helps optimize the search process. Additionally, the algorithm's recursive nature presents opportunities for parallelization, potentially improving performance in parallel computing environments."

## [POSITIVE] Clique Filtering by Node Uniqueness
Enforcing each node to belong only to the maximal clique with maximum weight, reducing the clique set size below total node count

**Delta**: not quantified separately
**Condition**: Post-search filtering to reduce computational cost of subsequent steps

**Evidence**: "Since a node may exist in multiple maximal cliques, we enforce it to belong only to the one with the maximum weight, while deleting the remaining maximal cliques that contain the same node. This filtering process ensures that the resulting set of maximal cliques, denoted as MACflt, contains fewer maximal cliques than the total number of nodes in the graph."
