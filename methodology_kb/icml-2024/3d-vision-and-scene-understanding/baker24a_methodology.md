# An Explicit Frame Construction for Normalizing 3D Point Clouds

**Source**: https://proceedings.mlr.press/v235/baker24a.html

## [POSITIVE] Asymmetric Unit Normalization (ASUN)
A training-free, explicit frame construction algorithm that uses asymmetric units extracted from a minimal deterministic finite automaton (DFA) to normalize 3D point clouds. It selects linearly independent vectors from the asymmetric unit to define a canonical orientation frame.

**Delta**: outperforms baseline
**Condition**: Applied to QM9 molecular alignment and ModelNet40 shape classification across all point cloud ranks and symmetry groups

**Evidence**: "ASUN performs the best of all methods across all ranks of the dataset as indicated in boldface."

## [NEGATIVE] PCA-based Frame Construction
Uses Principal Component Analysis to derive a reference frame and align 3D point clouds to a canonical representation.

**Delta**: 0.82758 EMD error at rank 3 vs 0.02826 for ASUN
**Condition**: Fails particularly for rank 3 data and point clouds with high degrees of symmetry (e.g., NH3 molecule)

**Evidence**: "PCA performs well for rank 1 data, but significantly underperforms for rank 3 data... the PCA model is prone to failure given rank 3 data with a high degree of symmetry."

## [NEGATIVE] Learning-based Auto-Encoder (AE) Frame Construction
A neural network-based approach that simultaneously learns invariant embeddings and frames by learning an equivariant function from input embedding space to an intermediate homogeneous space.

**Delta**: 1.15122 EMD error at rank 1 vs 0.00014 for ASUN; RMSE of 0.0924 vs 0.0 for ASUN
**Condition**: Fails for rank 1 and rank 2 data; also lacks generalizability to unseen symmetry groups not present in training data

**Evidence**: "AE performs poorly for rank 1 data with an error of 1.2Å... the data is only consistent up to the error of the learning-based method, which makes each of the normalized data in Figure 1 easily distinguishable."

## [NEUTRAL] Frame Averaging (FA)
A systematic framework for adapting architectures to become invariant or equivariant by averaging over a set of frames including all sign change choices.

**Delta**: None
**Condition**: Used as a baseline comparison; cannot handle cases when eigenvalues of covariance matrices are not distinct

**Evidence**: "We compare ASUN against PCA (Bellekens et al., 2014), the auto-encoder (AE) as described in (Winter et al., 2022), and frame-averaging (FA) (Puny et al., 2021)."

## [POSITIVE] Relaxed G-Equivariance Condition
A relaxed version of equivariance that allows output transformations to differ by elements within stabilizers, enabling frame construction for symmetric inputs with nontrivial stabilizers.

**Delta**: None
**Condition**: Applied when constructing frames for point clouds with inherent symmetries where strict equivariance is impossible

**Evidence**: "The relaxed equivariance grants a certain flexibility in output transformations, allowing them to differ by elements within stabilizers. Importantly, the relaxed equivariance implies that the function µ: X → X defined by µ(x) := F(x)^{-1}x ∈ X is group invariant."

## [POSITIVE] Universality via Orthogonal Representations (Theorem 3.3)
An alternative universality guarantee that leverages the orthogonality of group representations to ensure universal approximation capability even without continuous canonicalization functions.

**Delta**: None
**Condition**: Applies when group actions are defined by orthogonal representations, specifically for O(n) and SO(n)

**Evidence**: "Our established Theorem 3.3 offers an alternative path toward expressiveness guarantees, even in the absence of continuous canonicalization functions."

## [NEUTRAL] Discontinuous Frame Construction
Explicit acknowledgment and proof that continuous frames are impossible for point clouds in R^{n×m} with m,n≥3 under E(n), SE(n), O(n), or SO(n), motivating a manually designed rather than learned frame.

**Delta**: None
**Condition**: Theoretical constraint affecting all frame construction methods for 3D point clouds under isometry groups

**Evidence**: "For point clouds in R^{n×m} with m, n ≥ 3, it is impossible to construct a frame F: R^{n×m} → G that is continuous across the entire domain when G = E(n), SE(n), O(n) or SO(n)."

## [POSITIVE] ASUN-Invariant Architecture (Positional Data as Node Features)
Using ASUN normalization to enable positional data to be used directly as node features in non-equivariant GNNs (e.g., GCN, GCNII, SchNet-pos, EGNN-pos), making them effectively invariant.

**Delta**: GCN: 13.57% (z/SO(3)) → 18.19% (ASUN/ASUN); GCNII: 21.3% → 30.75%; SchNet-pos: 28.40% → 42.79%; EGNN-pos: 29.94% → 53.36%
**Condition**: Applied to ModelNet40 shape classification with ASUN/ASUN train/test augmentation

**Evidence**: "When positional data is used as a node feature, ASUN significantly improves the accuracy of all models, showing the benefit of ASUN – it allows the positional data to be used directly while maintaining invariance."

## [POSITIVE] Unit-Sphere Representation
Projects each point onto the unit sphere and records radial distances, creating a concise representation that preserves the core symmetry of the point cloud.

**Delta**: None
**Condition**: Used as Step A in the ASUN algorithm for all point clouds; points at the origin are excluded

**Evidence**: "The unit-sphere representation {z_j, R_j} holds a remarkable ability: it preserves the core symmetry of a point cloud while offering a more concise and manageable structure."

## [POSITIVE] Directed Labeled Graph + Hopcroft DFA Minimization
Converts the unit-sphere representation into a directed labeled graph and applies Hopcroft's algorithm to find a unique minimal DFA, which encodes all asymmetric units with O(m log m) time complexity.

**Delta**: None
**Condition**: Used as Steps B and C in the ASUN algorithm to extract asymmetric units for frame construction

**Evidence**: "This algorithm is specifically designed to uncover the inherent symmetries of a point cloud through a process of graph simplification... with a time complexity of O(m log m)."

## [POSITIVE] Point Feature Hashing for Augmented Point Clouds
Treats additional point features (e.g., atom types) as tokens and uses a hash function to generate unique indices, redefining radial distance sets to incorporate feature information.

**Delta**: None
**Condition**: Applied when point clouds have additional per-point features beyond spatial coordinates, such as molecular atom types

**Evidence**: "In cases where points may possess additional features, denoted as f_i (e.g., atom features in molecules), our frame determination remains applicable with a slight adjustment. Specifically, we treat f_i s as tokens and use a hash function to generate unique indices for these tokens."

## [POSITIVE] Centering Point Cloud at Origin
Addresses translational variation by centering the point cloud at the origin before orientation normalization, decomposing E(n) into O(n) and translational components.

**Delta**: None
**Condition**: Applied as a preprocessing step for all point clouds before orientation frame construction

**Evidence**: "Shifts in positions of a point cloud can be addressed by centering the point cloud at the origin... we may focus on frames that relocate the center of the point cloud to the origin."

## [NEUTRAL] Invariant/Equivariant Neural Network Architectures (SchNet, EGNN, MACE)
State-of-the-art GNNs with built-in invariance or equivariance properties that maintain consistent accuracy regardless of input orientation augmentation.

**Delta**: SchNet: 29.74% (z/SO(3)) vs 28.93% (ASUN/ASUN); EGNN: 22.61% vs 25.41%
**Condition**: Applied to ModelNet40 classification; accuracy is consistent across augmentations but does not benefit from ASUN normalization

**Evidence**: "Invariant/equivariant models consistently maintain accuracy across augmentations, as expected, since the output remains invariant under transformations, including the application of ASUN."

## [NEGATIVE] AE Generalizability Testing on Unseen Symmetry Groups
Evaluating the learned AE frame method on point groups not seen during training to test out-of-distribution generalization.

**Delta**: AE: 0.240 EMD for C∞,v vs ASUN: 0.001; AE: 0.037 for Cs vs ASUN: 0.004
**Condition**: Tested on QM9 molecules with symmetry groups C∞,v, Cs, D6,h, and Td withheld from training

**Evidence**: "AE outperforms PCA, which is generally incapable of handling data with high degrees of symmetry. However, it does not have strong generalizations like the data-free ASUN method."
