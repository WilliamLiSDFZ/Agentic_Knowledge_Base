# IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation

**Source**: https://proceedings.mlr.press/v235/melas-kyriazi24a.html

## [POSITIVE] Video Generator as Multi-view Generator
Fine-tuning a text-to-video model (Emu Video) instead of a text-to-image model to generate multi-view consistent frames of a 3D object in a turntable-like fashion

**Delta**: outperforms baseline
**Condition**: Text/image-to-3D generation pipeline

**Evidence**: "IM-3D outperforms all others in terms of both textual and visual faithfulness. This is true for both the image sequences J output by the video generator as well as the renders Ĵ from the fitted 3D GS models G."

## [POSITIVE] LPIPS Image-Level Loss
Using perceptual image-level loss (LPIPS) based on VGG features during Gaussian splatting optimization instead of pixel-level L2 loss

**Delta**: +2.28 CLIP Text (31.66 vs 29.67), +6.41 CLIP Image (91.40 vs 84.99)
**Condition**: 3D reconstruction fitting stage with Gaussian splatting

**Evidence**: "We find that image-level losses are central to our method's ability to generate high-quality 3D assets. The use of pixel-level losses such as L2 loss is detrimental, as minor inconsistencies in the multiview images are emphasized by the optimization process and effectively averaged together. This averaging results in a low CLIP score (29.67 vs 31.66 for LPIPS) as well as blurry and unnatural generations."

## [NEGATIVE] Removing LPIPS Loss
Ablation removing the LPIPS loss from the reconstruction objective

**Delta**: -2.28 CLIP Text (29.38 vs 31.66), -6.69 CLIP Image (84.71 vs 91.40)
**Condition**: 3D reconstruction fitting stage ablation

**Evidence**: "-L_LPIPS: 29.38 ±2.1 CLIP Text, 84.71 ±6.4 CLIP Image vs IM-3D full: 31.66 ±1.7, 91.40 ±5.5"

## [POSITIVE] MS-SSIM Loss
Multi-scale structural similarity index measure loss used in combination with LPIPS during Gaussian splatting optimization

**Delta**: +0.13 CLIP Text, +0.76 CLIP Image over removing it
**Condition**: 3D reconstruction fitting stage

**Evidence**: "-L_SSIM: 31.53 ±1.8 CLIP Text, 90.64 ±5.7 CLIP Image vs full model 31.66, 91.40"

## [POSITIVE] Mask Loss
Segmentation mask loss using predicted object masks during Gaussian splatting optimization

**Delta**: +0.23 CLIP Text, +1.26 CLIP Image over removing it
**Condition**: 3D reconstruction fitting stage

**Evidence**: "-L_Mask: 31.43 ±1.9 CLIP Text, 90.14 ±6.0 CLIP Image vs full model 31.66, 91.40"

## [POSITIVE] Gaussian Splatting (GS) 3D Representation
Using 3D Gaussian splatting as the underlying 3D representation for reconstruction instead of NeRF

**Delta**: +1.24 CLIP Text, +4.03 CLIP Image over NeRF; 3 min vs 40 min training time
**Condition**: 3D reconstruction fitting stage

**Evidence**: "We find that the visual quality of models generated using NeRF is slightly worse than GS. The true benefit of GS is that it is much faster and much more memory-efficient; training with GS takes 3 minutes, whereas training with NeRF takes 40 minutes."

## [NEGATIVE] NeRF 3D Representation
Using Neural Radiance Fields as the underlying 3D representation instead of Gaussian splatting

**Delta**: -1.24 CLIP Text (30.42 vs 31.66), -4.03 CLIP Image (87.37 vs 91.40); 40 min vs 3 min
**Condition**: 3D reconstruction fitting stage ablation

**Evidence**: "w/ NeRF instead of GS: 30.42 ±2.1 CLIP Text, 87.37 ±5.4 CLIP Image vs IM-3D full: 31.66, 91.40. training with GS takes 3 minutes, whereas training with NeRF takes 40 minutes."

## [POSITIVE] Iterative Multiview Diffusion and Reconstruction
Closing the loop by rendering noised images of the 3D reconstruction and restarting the video diffusion process from those, repeated 2-3 times

**Delta**: significantly enhancing the level of detail
**Condition**: Post-initial reconstruction refinement; applied 2-3 times per asset

**Evidence**: "our technique rectifies these discrepancies with one iteration of denoising and reconstruction, significantly enhancing the level of detail."

## [POSITIVE] Generating 16 Frames Simultaneously
Generating 16 multi-view frames simultaneously using the video diffusion model instead of fewer frames

**Delta**: +1.60 CLIP Text (31.66 vs 30.06), +4.44 CLIP Image (91.40 vs 86.96) over 4 frames
**Condition**: Multi-view generation stage

**Evidence**: "our quantitative performance improves as we increase the number of generated frames. [16 frames: 31.66/91.40 vs 4 frames: 30.06/86.96]"

## [NEUTRAL] No Camera Parameter Conditioning
Not passing camera parameters to the video generation model; instead using fixed camera distance and orientation, randomizing only elevation

**Delta**: not quantified
**Condition**: Multi-view video generation training and inference

**Evidence**: "Differently from many prior multi-view generation networks, we do not pass the camera parameters to the model; instead, we use a fixed camera distance and orientation, randomizing only the elevation. The model simply learns to produce a set of views that follow this distribution."

## [POSITIVE] Freezing Spatial Layers During Fine-tuning
Freezing all parameters except temporal convolutional and attention layers when fine-tuning Emu Video for multi-view generation

**Delta**: no degradation in texture quality with extended training
**Condition**: Fine-tuning Emu Video on synthetic 3D assets

**Evidence**: "Contrary to MVDream and Instant3D, we observe no degradation in texture quality with extended training. This can be ascribed to the fact that the spatial layers remain static and the network is image-conditioned, necessitating that the generated 360 video retain the high-frequency texture elements of the input."

## [POSITIVE] DPM++ Fast ODE Sampler
Using fast stochastic ODE solvers (DPM++) to reduce the number of model evaluations during video generation

**Delta**: 10-100x reduction in model evaluations vs SDS; ~40 evaluations for initial video
**Condition**: Video generation inference stage

**Evidence**: "we can adopt fast stochastic ODE solvers such as DPM++ to further reduce the number of model evaluations to obtain the video in the first place. Overall, compared to using the SDS loss, the number of model evaluations is reduced by a factor 10-100×"

## [POSITIVE] Avoiding Score Distillation Sampling (SDS)
Replacing SDS-based optimization (requiring thousands of network evaluations) with direct reconstruction from generated multi-view images

**Delta**: 10-100x fewer network evaluations; 80 calls vs 200-320000 for SDS-based methods
**Condition**: Full text-to-3D generation pipeline

**Evidence**: "IM-3D reduces the number of evaluations of the 2D generator network 10-100×, resulting in a much more efficient pipeline, better quality, fewer geometric inconsistencies, and a high yield of usable 3D assets."

## [POSITIVE] Quality-Filtered Training Data (100k assets)
Using a subset of 100k synthetic 3D assets selected for quality based on CLIP alignment between rendered images and textual descriptions

**Delta**: not quantified
**Condition**: Training data curation for multi-view video fine-tuning

**Evidence**: "we use a subset of 100k assets selected for quality, as determined by the CLIP alignment between rendered images and textual descriptions."

## [NEGATIVE] L2 Pixel-Level Loss (baseline comparison)
Using standard pixel-wise RGB L2 loss instead of image-level perceptual losses for Gaussian splatting optimization

**Delta**: -1.99 CLIP Text (29.67 vs 31.66), -6.41 CLIP Image (84.99 vs 91.40)
**Condition**: 3D reconstruction fitting stage ablation

**Evidence**: "The use of pixel-level losses such as L2 loss is detrimental, as minor inconsistencies in the multiview images are emphasized by the optimization process and effectively averaged together. This averaging results in a low CLIP score (29.67 vs 31.66 for LPIPS) as well as blurry and unnatural generations."
