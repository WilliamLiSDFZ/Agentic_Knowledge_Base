# GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting

**Source**: https://proceedings.mlr.press/v235/zhou24p.html

## [POSITIVE] LLM-based Layout Generation
Using large language models (e.g., GPT-3.5) to automatically extract instance relationships from textual descriptions and generate coarse 3D layout priors (bounding boxes, positions, scales, rotations) instead of manual layout design.

**Delta**: outperforms baseline
**Condition**: Text-to-3D complex scene generation with multiple objects

**Evidence**: "GALA3D bridges text description and compositional scene generation through layout priors obtained from LLMs and a layout refinement module that optimizes the coarse layout interpreted by LLMs."

## [POSITIVE] Layout-guided Gaussian Representation
Introducing layout constraints into 3D Gaussian Splatting representation, where each instance is represented by a set of Gaussians constrained within a corresponding layout bounding box, parameterized by position, scale, rotation, and instance Gaussians.

**Delta**: CLIP Score 34.573 vs best competitor 31.174
**Condition**: Multi-object 3D scene generation

**Evidence**: "Our method excels over all competitors in generating complex 3D scenes with multiple interacting objects."

## [POSITIVE] Adaptive Geometry Control
A distribution constraint using a folded normal distribution to sample Gaussians near layout surfaces, combined with a regularization term to control Gaussian ellipsoid flatness and scale, replacing the raw 3DGS densification scheme.

**Delta**: CLIP Score drops from 34.885 to 32.198 without it
**Condition**: Geometry and texture quality of individual instance Gaussians

**Evidence**: "We replace the Adaptive Geometry Control with the density control scheme employed by the raw 3DGS (Kerbl et al., 2023) and observe a significant decrease in the realism of the generated scene."

## [POSITIVE] Compositional Optimization with Diffusion Priors
A two-stage optimization: first using MVDream multi-view diffusion with SDS to optimize individual instance Gaussians, then using ControlNet conditioned diffusion to optimize the global scene with layout-text consistency.

**Delta**: CLIP Score drops from 34.885 to 32.213 without it
**Condition**: Multi-object scene coherence and texture quality

**Evidence**: "Due to the absence of comprehensive global scene optimization, the generated 3D scenes exhibit impoverished textures and lack scene coherence. Furthermore, the generated geometry only adheres to local layout supervisions, resulting in the emergence of 'over-constrained' boundaries."

## [POSITIVE] Layout Refinement Module
An iterative optimization module that continuously adjusts the coarse LLM-generated layout parameters (position, scale, rotation) during the denoising process to better align with the generated 3D scene and real-world constraints.

**Delta**: CLIP Score drops from 34.885 to 34.293 without it
**Condition**: Alignment between LLM-generated layouts and actual 3D scenes

**Evidence**: "Directly using the layout interpreted by LLM without refinement results in 3D scenes not well aligned... the Layout Refinement module enables the optimizing of layouts, continuously adjusting them throughout the denoising process to achieve more intricately aligned interactions among instances."

## [POSITIVE] Layout Loss
A spatial constraint loss using Manhattan distance from Gaussian centers outside 3D layout boundaries to the nearest boundary point, enforcing semantic and spatial consistency between generated instances and layout priors.

**Delta**: CLIP Score drops from 34.885 to 33.297 without it
**Condition**: Spatial consistency of generated objects with layout priors

**Evidence**: "results indicate that both L_layout and L_scene improve the generating quality, enhancing texture details and maintaining text-3D alignment."

## [POSITIVE] Global Scene Optimization Loss (L_global)
ControlNet-based conditioned diffusion loss for global scene optimization, ensuring layout-text consistency across the entire scene with multiple instances.

**Delta**: CLIP Score drops from 34.885 to 34.342 without it
**Condition**: Global scene coherence and text alignment

**Evidence**: "results indicate that both L_layout and L_scene improve the generating quality, enhancing texture details and maintaining text-3D alignment."

## [POSITIVE] Fine-tuned ControlNet for Layout Conditioning
ControlNet fine-tuned to accept rendered 2D layout images from multiple viewpoints as conditioning input, providing layout-text consistent diffusion supervision for global scene optimization.

**Delta**: outperforms baseline
**Condition**: Global scene optimization with layout constraints

**Evidence**: "we use ControlNet (Zhang et al., 2023a) for compositional optimization, ensuring that the generated scene aligns with the layout. Concretely, we fine-tuned ControlNet to support rendering layouts from multiple viewpoints as input and generate 2D diffusion supervision with layout-text consistency."

## [POSITIVE] MVDream Multi-view Diffusion Prior
Using MVDream as the multi-view diffusion model with SDS for per-instance Gaussian optimization, with a guidance scale of 50 and a virtual camera model rendering multi-view images.

**Delta**: GALA3D boosts MVDream baseline in both object-level and scene-level generation
**Condition**: Per-instance 3D generation quality

**Evidence**: "GALA3D also boosts the performance of our baseline method MVDream (Shi et al., 2023) in both object-level and scene-level generation and achieves optimal results."

## [POSITIVE] Shared Timestep for Instance and Scene Optimization
Instance-level and scene-level optimization share the same diffusion timestep during training to ensure synchronous and collaborative learning.

**Delta**: descriptive only
**Condition**: Collaborative optimization of instance and scene Gaussians

**Evidence**: "During the diffusion process, the instance-level and scene-level optimization share the same time step η to ensure synchronous and collaborative learning."

## [NEUTRAL] Disabling Adaptive Density Control in 3DGS
Discarding the adaptive density control mechanism from standard 3DGS during training to save memory and speed up training, initializing each instance with 100,000 Gaussian particles.

**Delta**: memory savings and speed improvement, no reported quality delta
**Condition**: Training efficiency on single A800 80GB GPU

**Evidence**: "For each instance, we initialize the 3D Gaussians with 100,000 particles and discard adaptive density control in 3D Gaussian Splatting to save memory and speed up training."

## [POSITIVE] Conversational Interactive Editing via LLMs
Using LLMs to interpret natural language editing instructions into layout transformation operations (add/remove objects, translate, rotate, scale), then re-optimizing only the affected local layout areas.

**Delta**: descriptive only
**Condition**: User-interactive 3D scene editing

**Evidence**: "Our approach guarantees highly controllable and personalized scene editing, including the addition or removal of objects, spatial adjustments, style transfer, and object interactions."

## [NEGATIVE] Implicit NeRF Representation for Compositional Scenes
Using NeRF as the 3D representation for compositional scene generation with layout constraints (as done by prior works like Set-the-scene, CompoNeRF).

**Delta**: Set-the-scene CLIP Score 29.628 vs GALA3D 34.573
**Condition**: Compositional multi-object 3D scene generation with layout constraints

**Evidence**: "compositional NeRF models tend to suffer from degradations in visual quality and geometric deformation because they cannot effectively handle the constraints imposed by layout during the NeRF optimization process."

## [NEGATIVE] Raw 3DGS Densification without Layout Constraints
Standard 3DGS densification scheme without layout-guided distribution or shape constraints, used by prior object-centric 3DGS methods.

**Delta**: CLIP Score 32.198 vs full model 34.885
**Condition**: Complex multi-object scene generation

**Evidence**: "The Gaussian densification fails to constrain the distribution and shape of Gaussian ellipsoids, resulting in unpleasant artifacts and blurs."

## [NEGATIVE] Unrefined LLM Layout Priors
Directly using coarse layouts from LLMs without refinement, which can produce misaligned spatial positions, incorrect scales, and floating objects.

**Delta**: CLIP Score 34.293 vs full model 34.885
**Condition**: LLM-generated layout quality for 3D scene generation

**Evidence**: "layouts interpreted by LLMs are often not precise, resulting in misalignment between the layout and the desired scene (e.g., a floating hat, as shown in Figure 8)."
