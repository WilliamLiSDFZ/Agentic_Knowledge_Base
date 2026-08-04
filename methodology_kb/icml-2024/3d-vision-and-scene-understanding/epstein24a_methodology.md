# Disentangled 3D Scene Generation with Layout Learning

**Source**: https://proceedings.mlr.press/v235/epstein24a.html

## [POSITIVE] Layout Learning (Multiple Layouts)
Learning N randomly initialized sets of affine transforms (layouts) for K NeRFs, sampling one layout per training step to encourage objects to be arrangeable in multiple valid configurations

**Delta**: CLIP B/16 Color: 29.9→31.3, Geo: 28.8→29.9; CLIP L/14 Color: 24.9→27.1, Geo: 23.5→24.8
**Condition**: Ablation study on 30 prompts with K=3 NeRFs, comparing single layout vs. N layouts

**Evidence**: "Adding regularization losses improve scores somewhat, but the biggest gains come from introducing layout learning and then co-learning N different arrangements, validating our approach."

## [POSITIVE] Single Layout Learning
Equipping each NeRF with a learnable affine transform (rotation, translation, scale) to place objects in different parts of 3D space, learning one layout per scene

**Delta**: CLIP B/16 Color: 27.7→29.9, Geo: 26.2→28.8; CLIP L/14 Color: 22.8→24.9, Geo: 23.2→23.5
**Condition**: Ablation study comparing K NeRFs with empty NeRF loss vs. adding single layout learning

**Evidence**: "While introducing layout learning significantly increases the quality of object disentanglement (Tbl. 3b), the model is still able to adjoin and utilize individual NeRFs in undesirable ways."

## [NEGATIVE] Naive K NeRFs (No Layout)
Simply instantiating K NeRFs and jointly accumulating densities from all NeRFs along a ray without any layout transforms or regularization

**Delta**: CLIP B/16 Color: 26.7 vs. 31.3 for full method; each NeRF often represents a random point-cloud-like subset of 3D space
**Condition**: Baseline condition in ablation study

**Evidence**: "just as unregularized sets of latents are often highly uninterpretable, simply spawning K instances of a NeRF does not produce meaningful decompositions. In practice, we find each NeRF often represents a random point-cloud-like subset of 3D space"

## [POSITIVE] Per-NeRF Regularization Losses
Applying Mip-NeRF 360 orientation, distortion, and accumulation losses on a per-NeRF basis rather than on the composited scene

**Delta**: CLIP B/16 Color: 26.7→27.3, Geo: 25.4→26.1; CLIP L/14 Color: 21.0→21.6, Geo: 21.2→22.6
**Condition**: Ablation study, applied on top of K NeRFs baseline

**Evidence**: "Adding regularization losses improve scores somewhat, but the biggest gains come from introducing layout learning"

## [POSITIVE] Empty NeRF Loss
A regularization loss penalizing degenerate empty NeRFs by requiring each NeRF's soft-binarized accumulated density to occupy at least 10% of the canvas

**Delta**: CLIP B/16 Color: 27.3→27.7, Geo: 26.1→26.2; CLIP L/14 Color: 21.6→22.8, Geo: 22.6→23.2
**Condition**: Ablation study, applied on top of per-NeRF losses

**Evidence**: "Importantly, we add a loss penalizing degenerate empty NeRFs by regularizing the soft-binarized version of each NeRF's accumulated density, α_bin, to occupy at least 10% of the canvas"

## [NEUTRAL] View-Dependent Prompting
Using view-dependent text prompts (e.g., describing front/side/back views) during SDS optimization

**Delta**: CLIP B/16 Color: 31.0 vs. 31.3 for full method without view-dep prompting; marginal difference
**Condition**: Compositional scene generation; view-dependent prompting is disabled in the final method

**Evidence**: "disabling view-dependent prompting as it does not aid in the generation of compositional scenes (Table 3b)"

## [NEUTRAL] Relative Layouts
An alternative layout parameterization using relative transforms between NeRFs

**Delta**: CLIP B/16 Color: 30.4 vs. 31.3 for full method; slightly lower performance
**Condition**: Ablation comparison in Table 3b

**Evidence**: "Relative layouts: 30.4 [Color B/16], 29.2 [Geo B/16], 25.7 [Color L/14], 24.0 [Geo L/14]"

## [POSITIVE] Score Distillation Sampling (SDS)
Using a pretrained text-to-image diffusion model as a loss function to optimize 3D NeRF representations without any 3D supervision

**Delta**: outperforms baseline
**Condition**: Core training signal for all variants of the method

**Evidence**: "These methods turn a diffusion model into a loss function that can be used to optimize the parameters of a 3D representation... SDS and related methods enable the use of rich 2D priors obtained from large text-image datasets to inform the structure of 3D representations."

## [POSITIVE] Quaternion Parameterization for Rotation
Expressing rotation transforms as quaternions (q ∈ R^4) rather than rotation matrices for ease of optimization

**Delta**: described as easier to optimize
**Condition**: Layout parameter optimization

**Evidence**: "Each T_k has a rotation R_k ∈ R^{3×3} (in practice expressed via a quaternion q ∈ R^4 for ease of optimization)"

## [POSITIVE] Higher Learning Rate for Layout Parameters
Using a 10x higher learning rate for layout parameters compared to NeRF parameters

**Delta**: described as necessary to avoid convergence to near-identical layouts
**Condition**: Layout parameter optimization during training

**Evidence**: "We use a 10× higher learning rate to train layout parameters... though layouts are initialized with high standard deviation and trained with an increased learning rate, they occasionally converge to near-identical values"

## [POSITIVE] Coarse-to-Fine Training for NGP
Slowly unlocking grid resolutions higher than 64×64 only after 2000 steps when using Instant NGP as the 3D backbone

**Delta**: prevents degenerate solutions where all density collapses into one NGP
**Condition**: When using Instant NGP (Müller et al., 2022) as the 3D backbone instead of MLP-based NeRF

**Evidence**: "we implement an aggressive coarse-to-fine training regime in the form of slowly unlocking grid settings at resolution higher than 64×64 only after 2000 steps. Without this constraint on the initial smoothness of geometry, the representation 'optimizes too fast' and is prone to placing all density in one NGP."

## [POSITIVE] Frozen NeRF Weights with Learnable Layout (Conditional Optimization)
Freezing the NeRF weights of a provided 3D asset while still learning layout parameters, allowing the model to incorporate a given asset into a new scene context

**Delta**: learns plausible transformations to incorporate provided assets into scenes
**Condition**: Conditional scene generation given a pre-existing 3D asset

**Evidence**: "By freezing the NeRF weights but not the layout weights, the model learns to arrange the provided asset in the context of the other objects it discovers"

## [POSITIVE] L2 Reconstruction Loss for NeRF Decomposition
Requiring renders of one of the N learned layouts to match views rendered from a target NeRF using an L2 loss (λ=0.05), enabling decomposition of pre-existing NeRFs

**Delta**: enables parsing of pre-existing NeRFs into component objects without per-object supervision
**Condition**: NeRF decomposition task (parsing a provided NeRF into objects)

**Evidence**: "We accomplish this by requiring renders of one of the N learned layouts to match the same view rendered from the target NeRF (c), using a simple L2 reconstruction loss with λ = 0.05."

## [POSITIVE] Shampoo Optimizer
Using the Shampoo preconditioned stochastic tensor optimization algorithm instead of Adam for training

**Delta**: not quantified separately
**Condition**: All experiments; inherited from SDS/DreamFusion training setup

**Evidence**: "We optimize our model with Shampoo (Gupta et al., 2018) with a batch size of 1 for 15000 steps with an annealed learning rate"
