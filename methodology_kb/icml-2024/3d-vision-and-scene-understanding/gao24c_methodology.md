# An Intrinsic Vector Heat Network

**Source**: https://proceedings.mlr.press/v235/gao24c.html

## [POSITIVE] Vector-Valued Neurons
Using complex-valued neurons throughout the architecture to maintain vector nature of data, treating tangent vectors as complex numbers rather than independent scalar channels

**Delta**: outperforms baseline
**Condition**: Processing tangent vector fields on manifold surfaces

**Evidence**: "Maintaining the vector nature of our data throughout results in an architecture that is invariant to isometries, rigid transformations, and the choice of tangent bases (see Sec. 5)"

## [POSITIVE] Trainable Vector Heat Diffusion
A learnable heat diffusion module using the connection Laplacian with trainable time-step sizes to spatially propagate vector-valued features across the surface

**Delta**: outperforms baseline
**Condition**: Spatial propagation of vector features across mesh surfaces

**Evidence**: "Inspired by (Sharp et al., 2022), we treat time-step size s in Eq. 5 as trainable parameters. Intuitively, the network learns whether to diffuse the vectors over a small or large local neighborhood."

## [POSITIVE] Spectral Acceleration via Eigendecomposition
Using k=128 lowest-frequency eigenvectors of the connection Laplacian to approximate vector diffusion, replacing expensive linear solves with matrix multiplications

**Delta**: significantly faster for small k
**Condition**: Computational efficiency of vector heat diffusion

**Evidence**: "Such a spectral acceleration replaces linear solves with matrix multiplications, thus is significantly faster for small k. In our implementation, we set k = 128."

## [POSITIVE] Deterministic Connection Laplacian
Using a pre-determined connection Laplacian derived from differential geometry (parallel transport) rather than learning a graph-specific one

**Delta**: superior generalization across triangle meshes
**Condition**: Generalization across different mesh triangulations

**Evidence**: "Our architecture with a deterministic connection Laplacian leads to superior generalization across triangle meshes, compared to approaches that rely on learning graph-specific Laplacians."

## [POSITIVE] Implicit Euler Integration
Using implicit Euler method instead of forward Euler for solving the vector heat equation to ensure stability under large time steps

**Delta**: stable under large time steps
**Condition**: Numerical stability of vector heat diffusion

**Evidence**: "As the forward Euler method is well-known to be unstable under large time steps, we compute the numerical solution to the vector heat equation using the implicit Euler method."

## [POSITIVE] Parallel Transport in Connection Laplacian
Baking parallel transport into the connection Laplacian to ensure invariance to choice of local tangent bases

**Delta**: zero error on tangent basis change vs high error for baseline
**Condition**: Invariance to arbitrary choice of local tangent bases

**Evidence**: "Our architecture is invariant to the choice of tangent bases because the Vector Heat Diffusion module has parallel transport baked in (see Sec. 3.2), making it invariant to the bases."

## [POSITIVE] Intrinsic Architecture Design
All operations (gradient, heat diffusion, per-vertex linear layer) are intrinsic to the manifold, making the architecture invariant to how the mesh sits in 3D space

**Delta**: zero error on rigid transformation vs high error for baseline
**Condition**: Rigid motion and isometric deformation invariance

**Evidence**: "These invariances arise from the fact that all of our operations (gradient, heat diffusion, and the per-vertex linear layer) are intrinsic, which implies that our architecture is invariant to how the mesh sits in the space."

## [POSITIVE] Complex Number Representation for N-Rosy Fields
Raising complex number representations to the power N to factor out N-way rotational symmetry for N-Rosy field learning

**Delta**: enables 4-Rosy cross field output for quad meshing
**Condition**: Learning N-Rosy fields for quadrilateral mesh generation

**Evidence**: "Since multiplication with (unit) complex numbers represents rotations, raising a complex number to the power of N factors out all the N-ways rotational symmetry... Thus, to measure the difference between, e.g., 4-Rosy fields, one simply measures the difference between u^4"

## [POSITIVE] Skip Connections in Vector Diffusion Blocks
Adding skip connections between Vector Heat Diffusion and Vector MLP modules in each block

**Delta**: not quantified
**Condition**: Architecture design for deep vector heat networks

**Evidence**: "our method consists of several layers of the Vector Diffusion Block (N) ... Vector Heat Diffusion (red) and Vector MLP (blue) with skip connections"

## [POSITIVE] Magnitude-Based Non-linearity (Vector ReLU)
Applying ReLU activation on the magnitude of complex features rather than on real/imaginary parts independently, preserving vector direction while gating by magnitude

**Delta**: not quantified
**Condition**: Non-linearity in vector-valued MLP layers

**Evidence**: "we follow the idea presented by (Wiersma et al., 2022) to apply non-linearities σ (e.g., ReLU) on the magnitude of each complex feature... if the complex feature norm ∥Z^l_ij∥ is smaller than the bias b^l_j, the complex feature is set to 0, otherwise it is unchanged"

## [POSITIVE] Dropout Regularization
Applying dropout with rate 0.5 in Vector MLP layers to mitigate overfitting

**Delta**: mitigates overfitting
**Condition**: Training on limited mesh dataset

**Evidence**: "In the Vector MLP layer, we use Dropout (Srivastava et al., 2014) set to 0.5, and L2 regularization (weight decay) with a value of 1e−3, which mitigates overfitting."

## [POSITIVE] L2 Regularization (Weight Decay)
Applying L2 weight decay of 1e-3 to mitigate overfitting during training

**Delta**: mitigates overfitting
**Condition**: Training on limited mesh dataset

**Evidence**: "we use Dropout (Srivastava et al., 2014) set to 0.5, and L2 regularization (weight decay) with a value of 1e−3, which mitigates overfitting."

## [POSITIVE] Heat Kernel Signature Gradient as Input Features
Using per-channel gradients of the first 15 channels of the Heat Kernel Signature as input vector features

**Delta**: direction loss 0.106±0.278, magnitude loss 0.077±0.148 (best overall)
**Condition**: Input feature selection for quadrilateral remeshing task

**Evidence**: "We find that ∇HKS leads to best overall performance. While ∇MC performs best on the directional loss component only, it displays high variance in the magnitude loss component."

## [NEUTRAL] Mean Curvature Gradient as Input Features
Using gradient of mean curvature as input vector features

**Delta**: direction loss 0.105±0.276 (best direction), magnitude loss 0.077±0.514 (high variance)
**Condition**: Input feature selection for quadrilateral remeshing task

**Evidence**: "∇MC performs best on the directional loss component only, it displays high variance in the magnitude loss component."

## [NEGATIVE] Gaussian Curvature Gradient as Input Features
Using gradient of Gaussian curvature as input vector features

**Delta**: direction loss 0.139±0.312, magnitude loss 0.096±0.261 (worst overall)
**Condition**: Input feature selection for quadrilateral remeshing task

**Evidence**: "Input features are evaluated by comparing their mean test loss... ∇GC [direction loss] 0.139±0.312 [magnitude loss] 0.096±0.261"

## [NEGATIVE] Principal Curvature Directions as Input Features
Using scaled principal curvature directions as input vector features

**Delta**: direction loss 0.128±0.313, magnitude loss 0.090±0.288
**Condition**: Input feature selection for quadrilateral remeshing task

**Evidence**: "Input features are evaluated by comparing their mean test loss... PCD [direction loss] 0.128±0.313 [magnitude loss] 0.090±0.288"

## [POSITIVE] Rotated Feature Augmentation (π/2 rotation concatenation)
Rotating each input feature channel by π/2 radians and concatenating with original to span the full local tangent space

**Delta**: not quantified
**Condition**: Input feature preprocessing for all non-PCD feature types

**Evidence**: "for all feature types except PCD, we also rotate each channel by π/2 radians, and concatenate these rotated vector features along the channel dimension. In principle, this means that each input feature channel and its rotated counterpart span the local tangent space, allowing the network to better exploit all degrees of freedom."

## [POSITIVE] Parallel Transport for Vertex-to-Face Vector Transport
Using angular difference between vertex and face tangent planes to correctly transport predicted vertex vectors to face tangent planes before averaging

**Delta**: enables correct face-level cross field for downstream quad meshing
**Condition**: Converting per-vertex predictions to per-face cross fields for quad meshing

**Evidence**: "Naively averaging the three vector predictions from a given face's three incident vertices will not produce a correct result, as the vectors are expressed with respect to their individual vector tangent planes, so they cannot be averaged directly. We must therefore account for the parallel transport from each of the vertex tangent planes to the face tangent plane."

## [POSITIVE] Combined Magnitude and Direction Loss
Loss function combining MSE on magnitude difference and cosine similarity on direction for 4-Rosy field supervision

**Delta**: not quantified
**Condition**: Training for quadrilateral remeshing with 4-Rosy field output

**Evidence**: "In addition to measuring errors on the directions, we also want to measure errors on the magnitude of the cross field (smaller crosses lead to smaller polygon). Combining the two leads to our following loss function"

## [POSITIVE] Custom Dataset with ARAP Deformation Augmentation
Using artist-created avatar heads with 100-1000 ARAP-based deformation augmentations instead of DFAUST dataset to expand training distribution

**Delta**: expands training data distribution away from parametric SMPL model
**Condition**: Training data preparation for character head quad meshing

**Evidence**: "for each of the template meshes, we create 100 − 1, 000 augmentations/variations, using a custom tool for deforming faces, based upon normal-driven ARAP deformation (Liu & Jacobson, 2021). This expands the training data distribution away from the parametric SMPL model."

## [NEGATIVE] Scalar-Valued Architecture for Vector Fields (Baseline)
Treating vector field channels as independent scalar channels using standard scalar neural network architectures (Dielen et al. 2021 approach)

**Delta**: high error on rigid transformation and tangent basis change
**Condition**: Baseline comparison for tangent vector field learning

**Evidence**: "Previous methods such as (Dielen et al., 2021) rely on scalar-valued architectures to output multiple scalar channels that are naively interpreted as vectors. Such approaches treat each channel independently and thus fail to capture key invariances (see Sec. 5). This severely hinders generalization to unseen triangulations and shapes."
