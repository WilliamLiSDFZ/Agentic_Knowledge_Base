# NeuralIndicator: Implicit Surface Reconstruction from Neural Indicator Priors

**Source**: https://proceedings.mlr.press/v235/huang24b.html

## [POSITIVE] Smooth Indicator Function (SIF)
A smooth version of the indicator function obtained by applying smooth constraints on the gradient domain, encoding both global indicative priors and local SDFs of the entire input point cloud.

**Delta**: outperforms baseline
**Condition**: Core component of NeuralIndicator framework for unsupervised surface reconstruction from unorganized point clouds

**Evidence**: "our approach consistently outperforms those previous approaches for surface reconstruction from point cloud in both quantitatively and qualitatively, even when input point clouds are incomplete and/or noisy with complex topology structure."

## [POSITIVE] Global Shape Priors via Indicator Function
Using the smooth indicator function to encode global geometry and topology priors of the entire shape, rather than local shape priors used by previous approaches.

**Delta**: outperforms baseline
**Condition**: Especially beneficial for incomplete and/or noisy point clouds with complex topology structure

**Evidence**: "Different from previous approaches that use local shape priors, our motivation is to explore more effective global shape priors from the entire shape itself, to regularize the neural implicit function learning."

## [POSITIVE] Differentiable Smooth Indicator Function Generation (SIFG)
A differentiable module that generates smooth indicator functions from oriented points using FFT-based PDE solving and trilinear interpolation, enabling end-to-end learning.

**Delta**: outperforms baseline
**Condition**: Used as part of the NeuralIndicator joint learning framework

**Evidence**: "we also propose a differentiable generation module, which enables differentiable smooth indicator function generation (SIFG) from a set of oriented points, with the oriented points served as learning parameters."

## [POSITIVE] SIFG Resolution 128x
Setting the voxel resolution of the SIFG module to 128x as a balance between reconstruction quality and computational efficiency.

**Delta**: CD1: 1.30, CD2: 0.56 (vs 1.47/1.05 at 32x)
**Condition**: Chosen as default resolution; 256x gives marginal improvement at much higher cost

**Evidence**: "Considering that SIFG-256 will takes much time cost than SIFG-128 but doesn't achieve significant surface reconstruction quality improvement, we adopt to set the SIFG resolution to 128 for a better balance of both surface reconstruction quality and efficiency in our full system."

## [POSITIVE] SIFG Resolution 256x
Setting the voxel resolution of the SIFG module to 256x for maximum reconstruction quality.

**Delta**: CD1: 1.28, CD2: 0.51 (marginal improvement over 128x: 1.30/0.56)
**Condition**: Diminishing returns compared to 128x; not used as default due to time cost

**Evidence**: "both the CD1 and CD2 numerical values decrease from sparse to dense voxel resolutions, which means that the more dense SIFG resolution will lead to the better surface reconstruction quality for our approach. But the accuracy in both CD1 and CD2 only get slight improvement from 128× to 256×."

## [POSITIVE] Indicator Loss (Lind)
Binary cross entropy loss to regularize the signed part of the neural implicit function using the indicator function, encouraging correct inside/outside classification.

**Delta**: removing it: CD1 1.38, CD2 0.72 vs full: CD1 1.31, CD2 0.59
**Condition**: Minor but positive contribution to the full system

**Evidence**: "We can see that Ludf, Lsdf, LCD will make major influence on the final surface reconstruction quality, while Lind and Lek make minor influence."

## [POSITIVE] Absolute Distance Loss (Ludf)
Loss that regularizes the absolute part of the SDF by projecting on-surface points from the indicator function onto the zero level set of the neural implicit function and measuring distance to the input point cloud.

**Delta**: removing it: CD1 1.67, CD2 2.13 vs full: CD1 1.31, CD2 0.59
**Condition**: Major contributor; removing it causes the largest degradation in CD2

**Evidence**: "We can see that Ludf, Lsdf, LCD will make major influence on the final surface reconstruction quality"

## [POSITIVE] SDF Loss (Lsdf)
Regularization loss that encourages projected on-surface points to lie on the zero level set of the signed distance function.

**Delta**: removing it: CD1 1.41, CD2 0.90 vs full: CD1 1.31, CD2 0.59
**Condition**: Major contributor to reconstruction quality

**Evidence**: "We can see that Ludf, Lsdf, LCD will make major influence on the final surface reconstruction quality"

## [POSITIVE] Chamfer Distance Loss (LCD)
Chamfer Distance loss between on-surface points from the indicator function and the input point cloud, used to regularize the smooth indicator function learning (not the neural implicit function directly).

**Delta**: removing it: CD1 1.52, CD2 1.21 vs full: CD1 1.31, CD2 0.59
**Condition**: Major contributor; primarily regularizes the smooth indicator function

**Evidence**: "LCD takes effects for more reliable smooth indicator function χP learning, which subsequently helps for more accurate neural implicit function f(x, θ) learning."

## [POSITIVE] Eikonal Loss (Lek)
Regularization loss that enforces the Eikonal equation on projected on-surface points, encouraging the neural implicit function to behave as a proper signed distance function.

**Delta**: removing it: CD1 1.32, CD2 0.67 vs full: CD1 1.31, CD2 0.59
**Condition**: Minor but positive contribution to the full system

**Evidence**: "We can see that Ludf, Lsdf, LCD will make major influence on the final surface reconstruction quality, while Lind and Lek make minor influence."

## [POSITIVE] Differential Projection for On-Surface Points
Projecting on-surface points extracted from the indicator function onto the zero level set of the neural implicit function using gradient-based projection, enabling differentiable backpropagation.

**Delta**: outperforms baseline
**Condition**: Enables end-to-end training of the absolute distance loss

**Evidence**: "Since the gradient ∂f/∂p(x,θ) can be achieved by the network backward propagation during the neural implicit function learning, such projection Γ : Ps→Ps′ is a differential projection that can be further used in the end-to-end neural implicit function learning."

## [POSITIVE] Flying Edges for On-Surface Point Extraction
Using the Flying Edges method instead of Marching Cubes for zero level set extraction from the indicator function, providing ~10x speedup.

**Delta**: ~10x time efficiency over Marching Cubes
**Condition**: Used for efficient on-surface point extraction during training

**Evidence**: "we leverage Flying Edges method (Schroeder et al., 2015) to generate the on-surface points Ps from the indicator function χP, which is a state-of-the-art zero level set extraction approach with about 10× time efficiency than Marching Cubes"

## [POSITIVE] FFT-based PDE Solver for Indicator Field
Using Fast Fourier Transform (FFT) to solve the PDE for smooth indicator field estimation over a uniform voxel grid, leveraging GPU-optimized implementations.

**Delta**: outperforms baseline
**Condition**: Enables efficient differentiable smooth indicator function generation

**Evidence**: "we adopt the spectrum method (Canuto et al., 2007) i.e. Fast Fourier Transform (FFT) to solve the above PDE over a uniform voxel grid, which have already been optimized to support GPUs, TPU and mainstream deep learning framework."

## [POSITIVE] Trilinear Interpolation for Continuous Indicator Function
Recovering a continuous indicator function from the discrete indicator field by trilinearly interpolating voxel corner values.

**Delta**: outperforms baseline
**Condition**: Enables continuous and differentiable indicator function for any 3D position

**Evidence**: "we propose to recover the continues indicator function by linearly interpolating the indicator filed... In this way, we obtain the final continues indicator function χP that is generated from an oriented point set P."

## [POSITIVE] Unsupervised Learning without Point Normals
Learning oriented point normals implicitly as trainable parameters rather than requiring ground truth point normals as input.

**Delta**: outperforms baseline
**Condition**: Enables surface reconstruction without any normal information, unlike PSR which requires ground truth normals

**Evidence**: "During the learning of f(x, θ), we don't explicitly compute point normals for the input point cloud, but learn to optimize the oriented point set P = {(pi, ni)} to generate smooth indicator function... we don't need any point normal input for the point cloud."

## [POSITIVE] Joint Learning of SIF and Neural Implicit Function
Simultaneously optimizing both the smooth indicator function and the neural implicit function in an end-to-end framework, with the indicator function providing global priors to regularize the SDF learning.

**Delta**: outperforms baseline
**Condition**: Core design of NeuralIndicator; both components are trained together

**Evidence**: "The joint learning of both smooth indicator function and neural implicit function enables reliable surface reconstruction, even for incomplete and/or noisy scanned point clouds with complex topology structure."

## [NEUTRAL] Grid-based Learning for Large Scale Scenes
Adopting a grid-based learning strategy (similar to LIG) to apply NeuralIndicator to large-scale scenes by processing geometry grid-by-grid.

**Delta**: similar to PCP, much better than PSR
**Condition**: Applied to 3D Scene dataset for large-scale reconstruction; limits performance due to cross-grid inconsistency

**Evidence**: "our approach achieves the similar level of surface reconstruction accuracy as PCP (Ma et al., 2022a), but is much better than PSR... One possible reason that our approach doesn't significantly outperform PCP, would due to the independent geometry learning for each grid voxel as LIG (Jiang et al., 2020) did, which often leads to in-consistent geometry reconstruction across grid neighbors thus decreasing the total surface reconstruction accuracy."

## [NEGATIVE] Naive Indicator Function (baseline comparison)
Using a discontinuous indicator function without smooth constraints, as done in SAP/Peng et al. 2021.

**Delta**: leads to unsatisfied surface reconstruction results
**Condition**: Used as motivation for the smooth indicator function; not used in NeuralIndicator

**Evidence**: "a naive indicator function (Peng et al., 2021) is discontinues without exact gradient definition, which would easily introduce discontinues surface reconstruction for the neural implicit function learning."

## [POSITIVE] Supervised Learning Approaches
Data-driven supervised methods (LIG, NDC, NKSR) that use ground truth labels for training.

**Delta**: NDC mean CD2: 12.4 vs Ours: 77.0 (×10^4) on average across datasets
**Condition**: Better than NeuralIndicator on datasets they were trained on, but performance degrades significantly on unseen datasets

**Evidence**: "The state-of-the-art supervised approaches like LIG, NDC and NKSR can achieve better surface reconstruction accuracy than our approach. This is reasonable since supervised learning approaches would obtain data-driven information from dataset to enhance the individual surface reconstruction quality"

## [POSITIVE] Gaussian Smoothing Kernel in SIFG
Applying a Gaussian smoothing kernel in the spectral domain during FFT-based indicator field computation to mitigate ringing effects from the Gibbs phenomenon.

**Delta**: outperforms baseline
**Condition**: Applied during smooth indicator field generation to improve field quality

**Evidence**: "G(ω) = exp(−2σ²r|ω²|²) a Gaussian smoothing kernel of bandwidth σ for grid resolution of r in the spectral domain to mitigate the ringing effects as a result of the Gibbs phenomenon from rasterizing the point normals V."
