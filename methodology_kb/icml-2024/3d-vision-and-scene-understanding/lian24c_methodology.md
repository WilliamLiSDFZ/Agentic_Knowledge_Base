# Diving into Underwater: Segment Anything Model Guided Underwater Salient Instance Segmentation and A Large-scale Dataset

**Source**: https://proceedings.mlr.press/v235/lian24c.html

## [POSITIVE] Underwater Adaptive ViT Encoder (UA-ViT)
A modified ViT encoder that incorporates adapters and channel adapters into frozen SAM ViT blocks to inject underwater domain visual prompts, addressing color distortion and domain gap between SA-1B and underwater imagery.

**Delta**: +1.6 mAP, +1.6 AP50, +1.5 AP75
**Condition**: Multi-class salient instance segmentation on USIS10K; ablation removing UA-ViT and reverting to original ViT-H

**Evidence**: "It can be observed that the model achieves a 1.6 AP improvement after incorporating the UA-ViT Block. This demonstrates that the UA-ViT Block introduces underwater visual information to the Underwater Adaptive ViT Encoder through adapters, enabling the network to effectively handle complex marine scenes such as marine snow, light scattering, optical artifacts, etc."

## [POSITIVE] Adapter in UA-ViT
Lightweight MLP-based adapter modules inserted after multi-head attention and on the residual path of the frozen MLP layer in each ViT block to learn underwater-specific visual prompts.

**Delta**: +1.4 mAP, +1.7 AP50, +1.2 AP75
**Condition**: Multi-class salient instance segmentation on USIS10K; ablation removing Adapter from UA-ViT

**Evidence**: "The results indicate that the absence of the Adapter prevents the network from learning underwater-specific visual prompts due to the freezing of the image encoder, resulting in performance degradation of 1.4, 1.7, and 1.2 AP on the mAP, AP50, and AP75, respectively."

## [POSITIVE] Channel Adapter (CA)
A channel attention module using 1×1 convolution and average pooling to adaptively adjust the importance of each channel, addressing frequency distribution bias caused by selective wavelength absorption underwater.

**Delta**: +1.1 mAP, +1.3 AP50, +1.4 AP75
**Condition**: Multi-class salient instance segmentation on USIS10K; ablation removing Channel Adapter from UA-ViT

**Evidence**: "It can be seen that after removing it, the network performance decreases by 1.1, 1.3 AP, and 1.4 AP on mAP, AP50, and AP75. This decline is attributed to the network's inability to accurately identify the importance of each channel at this time."

## [POSITIVE] Salient Feature Prompt Generator (SFPG)
An out-of-the-box module that automatically generates salient prompt embeddings for SAM's mask decoder by fusing multi-scale and multi-layer features, replacing the need for explicit user-provided point or bounding box prompts.

**Delta**: +0.9 mAP, +0.7 AP50, +1.0 AP75
**Condition**: Multi-class salient instance segmentation on USIS10K; ablation replacing SFPG with Multi-scale Feature Enhancer

**Evidence**: "After replacing, the network will utilize the Multi-scale Feature Enhancer (Chen et al., 2023a) to aggregate multi-layer features. After the replacement, the network's mAP, AP50, and AP75 are reduced by 0.9, 0.7, and 1.0 AP, respectively."

## [POSITIVE] Salient Feature Fusion Module (SFFM)
A sub-module within SFPG that aggregates multi-layer UA-ViT features using multi-scale convolutions (3×3, 5×5, 7×7) and average residuals to suppress noise and capture salient information across scales.

**Delta**: +0.8 mAP, +0.5 AP50, +1.3 AP75
**Condition**: Multi-class salient instance segmentation on USIS10K; ablation removing SFFM from SFPG

**Evidence**: "The results demonstrate that upon removing it, the model is unable to effectively aggregate the multilayer features of ViT, which affects its ability to accurately localize the salient regions in the image, resulting in a decrease in the AP values of mAP, AP50 and AP75 by 0.8, 0.5 and 1.3, respectively."

## [POSITIVE] Multi-scale convolution in SFPG
Use of multi-scale convolutions (3×3, 5×5, 7×7) in the SFPG upsampling path to capture features at different receptive fields, as opposed to simple 3×3 convolution.

**Delta**: +0.6 mAP, +0.4 AP50, +0.8 AP75
**Condition**: Multi-class salient instance segmentation on USIS10K; ablation replacing multi-scale convolution with 3×3 convolution

**Evidence**: "In addition, we explored the effect of replacing multi-scale convolution with simple 3×3 convolution after upsampling in the Salient Feature Prompt Generator. After replacement, the segmentation accuracy of the model decreased due to the reduced receptive field, decreasing by 0.6, 0.4, and 0.8 AP in mAP, AP50, and AP75, respectively."

## [POSITIVE] Freezing pre-trained SAM weights
Keeping the original SAM encoder and decoder weights frozen during training, only training the newly introduced UA-ViT adapters and SFPG modules (9.3% of total parameters).

**Delta**: trainable parameters reduced to 9.3% of total
**Condition**: Training USIS-SAM on USIS10K with ViT-H backbone

**Evidence**: "the trainable parameters of USIS-SAM constitute only 9.3% of the total. This means that instead of retraining or fine-tuning SAM, we can quickly apply USIS-SAM to underwater tasks by simply freezing SAM and specifically training our additional introduced components."

## [NEGATIVE] Underwater image enhancement pre-processing (URank) combined with SIS methods
Applying UnderwaterRanker image enhancement as a pre-processing step before feeding images into existing SIS methods (RDPNet, OQTR, RSPrompter) to address underwater image quality degradation.

**Delta**: URank+RDPNet: 52.0/80.7/62.0 mAP/AP50/AP75 vs RDPNet: 54.7/78.3/63.0; URank+OQTR: 49.3/74.3/56.2 vs OQTR: 56.6/79.3/62.6
**Condition**: Class-agnostic salient instance segmentation on USIS10K; URank enhancement applied to RDPNet, OQTR, and RSPrompter

**Evidence**: "we try to combine the SIS method with enhancement pre-processing. Nevertheless, this approach does not seem to work well since it is hard to jointly train multiple tasks to achieve optimal performance. However, as shown in Figure 1 and Table 2, the performance of such approach is not even able to exceed that of WaterMask."

## [NEGATIVE] SAM with bounding box prompts from Faster RCNN (SAM+BBox)
Using inference results from Faster RCNN as bounding box prompts for SAM's mask decoder, without domain-specific adaptation.

**Delta**: 45.9/65.9/52.1 mAP/AP50/AP75 (class-agnostic), underperforms WaterMask (58.3/80.2/66.5)
**Condition**: Class-agnostic and multi-class salient instance segmentation on USIS10K

**Evidence**: "SAM+BBox uses inference results from Faster RCNN (Ren et al., 2015) as prompts for prediction... [results show] 45.9 mAP, 65.9 AP50, 52.1 AP75 for class-agnostic, lower than WaterMask and USIS-SAM."

## [POSITIVE] Category labels for salient instances in USIS10K
Annotating each salient instance with a distinct category label (fish, coral reefs, underwater plants, human divers, robots, underwater ruins, seafloor reefs) in addition to instance masks, enabling multi-class training.

**Delta**: USIS-SAM leads WaterMask and RSPrompter by 4.4 and 5.1 AP in mAP for multi-class task
**Condition**: Multi-class salient instance segmentation on USIS10K

**Evidence**: "USIS-SAM achieved a 4.4 and 5.1 AP lead in mAP over WaterMask and RSPrompter, which were originally designed for multi-class instance segmentation tasks... This is benefit from the extra labels that help the network localize semantically dominant regions."

## [POSITIVE] Partial ViT block replacement strategy
Replacing only a subset of ViT blocks with UA-ViT blocks (one every two layers starting from the eighth layer) when using ViT-H backbone, to minimize parameter count while maintaining performance.

**Delta**: trainable parameters of 30.5M for UA-ViT out of 641M total SAM parameters
**Condition**: USIS-SAM with ViT-H backbone on USIS10K

**Evidence**: "In order to minimize the number of parameters, we replace only some of the ViT blocks in the SAM encoder with UA-ViT blocks. Specifically, when we use ViT-H as the backbone of SAM encoder, we replace one layer every two layers starting from the eighth layer."

## [NEUTRAL] USIS-SAM generalization to land SIS (SIS10K)
Retraining USIS-SAM on the land-based SIS10K dataset to test generalization; UA-ViT domain knowledge becomes less relevant outside underwater domain.

**Delta**: 70.1/89.0 mAP/AP50 vs OQTR 67.2/88.1; slightly weaker on AP75 (78.2 vs 81.7)
**Condition**: Salient instance segmentation on SIS10K (land-based dataset)

**Evidence**: "USIS-SAM still achieves good results compared to OQTR, and gains on AP50, but is slightly weaker on AP75. This may be due to domain knowledge learned in UA-ViT is the same as SAM encoder learned on SA-1B dataset, and the guiding effect of UA-ViT on the network is weakened. This shows that USIS-SAM did not overfit our dataset."

## [POSITIVE] Noise suppression via average residuals in SFFM
Balancing multi-scale features using global average pooling residuals with a hyperparameter λ=0.8 to dampen noise in the aggregated features.

**Delta**: part of overall SFPG contribution of +0.9 mAP
**Condition**: Multi-class salient instance segmentation on USIS10K within SFPG module

**Evidence**: "We then balance the multi-scale features using the average residuals to dampen the noise in the features... where Avg is the global average pooling, λ is a hyperparameter that controls the noise suppression effect, which in this paper is 0.8."
