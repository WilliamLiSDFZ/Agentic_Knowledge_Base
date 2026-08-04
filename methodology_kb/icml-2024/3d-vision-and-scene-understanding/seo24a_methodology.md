# Retrieval-Augmented Score Distillation for Text-to-3D Generation

**Source**: https://proceedings.mlr.press/v235/seo24a.html

## [POSITIVE] Retrieval-Augmented Variational Distribution Initialization
Retrieved 3D assets from an external database are used to initialize the variational distribution of particles in the VSD framework, providing geometric prior during a warm-up phase before standard score distillation takes over.

**Delta**: outperforms baseline
**Condition**: Applied during warm-up phase of text-to-3D optimization using VSD framework

**Evidence**: "We observe that initializing the variational distribution is crucial for the overall geometry, and lightweight adaptation effectively reduces artifacts such as eyes on the back."

## [POSITIVE] Lightweight Adaptation of 2D Prior via LoRA
A low-rank adapter (LoRA) is trained on dense renderings of retrieved 3D assets to reduce viewpoint bias in the 2D diffusion model, without full fine-tuning of the model parameters.

**Delta**: outperforms baseline
**Condition**: Applied to 2D prior model using retrieved 3D asset renderings at test time

**Evidence**: "lightweight adaptation effectively reduces artifacts such as eyes on the back... our strategy demonstrates encouraging effectiveness as it shows the chronic issue of viewpoint bias in 2D prior models can be efficiently addressed thanks to the nearest neighbors without any complex technique."

## [POSITIVE] View Prefix Token Optimization
Learnable tokens for view prefixes (e.g., 'front view', 'side view') are jointly optimized alongside the LoRA adapter during lightweight adaptation to further reduce viewpoint bias.

**Delta**: outperforms baseline
**Condition**: Applied in few-shot adaptation setting alongside LoRA fine-tuning

**Evidence**: "we can additionally optimize the tokens of view prefixes {eψ} as well as ω using Eq. 5. We empirically find it eliminate the model's viewpoint bias more effectively in the few-shot setting."

## [POSITIVE] CLIP-Based Dual Retrieval (Text + Image Embeddings)
Retrieval uses both CLIP text embeddings and CLIP image embeddings: first retrieving N' candidates with text embeddings, then re-ranking with image embeddings to select top-N assets.

**Delta**: outperforms baseline
**Condition**: Applied during 3D asset retrieval from Objaverse database

**Evidence**: "we utilize both image and text embeddings by performing Top-K operation with image embeddings after retrieving N′ (N′ > N) objects with text embeddings"

## [NEGATIVE] Full Fine-Tuning of Diffusion Models on 3D Data (MVDream/Zero123 approach)
Fine-tuning the entire parameters of a 2D diffusion model on 3D datasets like Objaverse to incorporate 3D awareness, as done by MVDream and Zero123.

**Delta**: descriptive: cartoonish style shift, degraded texture quality
**Condition**: When training multi-view or novel-view diffusion models on limited 3D datasets

**Evidence**: "MVDream, trained on Objaverse, undergoes a cartoonish style shift (Shi et al., 2023a), hindering the model from generating photorealistic 3D textures, and Zero123 shows drastically weakened performance when photorealistic images are given as input."

## [NEGATIVE] Score Distillation Sampling (SDS) without 3D Prior
Optimizing a NeRF by distilling scores from a 2D text-to-image diffusion model without any 3D geometric prior or retrieval augmentation.

**Delta**: descriptive: geometric inconsistencies and artifacts
**Condition**: Baseline text-to-3D generation without 3D data or retrieval augmentation

**Evidence**: "the generated scenes often suffer from artifacts and geometric inconsistencies due to the lack of knowledge on 3D geometry"

## [POSITIVE] Variational Score Distillation (VSD) as Base Framework
Using ProlificDreamer's VSD particle-based optimization as the base framework, which interprets 3D scenes as particles from a variational distribution and uses LoRA to parameterize the score of the variational distribution.

**Delta**: outperforms DreamFusion: CLIP L/14 0.218 vs 0.242 (ProlificDreamer), but ReDream achieves 0.274
**Condition**: Used as the base optimization framework for text-to-3D generation

**Evidence**: "ReDream exhibits superior performance in terms of text-3D alignment and view consistency... CLIP-Score CLIP L/14: ProlificDreamer 0.218, ReDream 0.274"

## [POSITIVE] Delta Denoising Score Regularization
An additional regularization that subtracts the predicted velocity at the retrieved asset position from the 2D prior velocity to reduce artifacts when the 2D prior steers particles away from the retrieved asset.

**Delta**: descriptive: reduces artifacts
**Condition**: Applied when 2D prior bias steers particles away from retrieved asset during optimization

**Evidence**: "To reduce the artifacts, we adjust the original v_2D by subtracting from it: ṽ_2D := v_2D − v_2D(θ = θ_ret). We opt for updates using ṽ_2D in place of v_2D for every three iterations."

## [POSITIVE] Orientation Alignment of Retrieved Assets via CLIP Similarity
Pre-processing step that aligns the frontal views of retrieved 3D assets by computing CLIP similarity between view-prefixed prompts and rendered images at different camera poses.

**Delta**: descriptive: beneficial for view prefix assignment
**Condition**: Applied as pre-processing for retrieved assets with distinguishable front views

**Evidence**: "before employing our nearest neighbors, we find it beneficial to align their frontal views... Despite its simplicity, this method effectively aligns our retrieved assets."

## [POSITIVE] ReDream Full Framework vs Baseline (ProlificDreamer)
Complete ReDream framework combining retrieval-augmented initialization and lightweight adaptation compared against ProlificDreamer baseline.

**Delta**: CLIP L/14: +0.056 (0.274 vs 0.218); OpenCLIP L/14: +0.023 (0.227 vs 0.204); A-LPIPS VGG: -0.186 (0.041 vs 0.227); A-LPIPS Alex: -0.081 (0.054 vs 0.135); user preference: 75.3% vs 24.7%
**Condition**: Evaluated on 50 prompts with 120 viewpoints each, compared against ProlificDreamer

**Evidence**: "ReDream exhibits superior performance in terms of text-3D alignment and view consistency... Approximately 75% of the participants express a preference for the results by our method over the baseline."

## [NEUTRAL] ScaNN-Based Fast Retrieval
Using the ScaNN approximate nearest neighbor algorithm for efficient retrieval of 3D assets based on CLIP embeddings, taking under 3 seconds total.

**Delta**: under 3 seconds retrieval time
**Condition**: Applied during inference for retrieving assets from Objaverse database

**Evidence**: "the total time spent by the retrieval is under 3 seconds, which is negligible compared to the time taken for the entire generation process."

## [NEUTRAL] Instant-NGP NeRF Backbone
Using Instant-NGP with multiresolution hash encoding as the 3D representation backbone for all experiments.

**Delta**: not separately quantified
**Condition**: Used as the 3D representation in all ReDream experiments

**Evidence**: "For all our experiments, Instant-NGP (Muller et al., 2022) is used for our NeRF backbone and Stable Diffusion v2 (Rombach et al., 2022b) as the 2D prior."
