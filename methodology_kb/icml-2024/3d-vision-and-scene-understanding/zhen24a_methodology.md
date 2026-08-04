# 3D-VLA: A 3D Vision-Language-Action Generative World Model

**Source**: https://proceedings.mlr.press/v235/zhen24a.html

## [POSITIVE] 3D Feature Integration via Multi-View Features
Building the backbone on 3D-LLM methodology, using multi-view features to generate 3D scene features and integrating them into a pretrained VLM without adaptation

**Delta**: outperforms baseline
**Condition**: 3D reasoning and localization tasks including Embodied QA, Task Caption, What-if QA, Dense Caption

**Evidence**: "3D-VLA outperforms all 2D VLM methods on language reasoning tasks. We attribute it to the leverage of 3D information, which provides more accurate spatial information for reasoning."

## [POSITIVE] Interaction Tokens (Object, Location, Scene, Action)
Novel set of special tokens including <obj></obj> for object nouns, <loc0-255> for 3D bounding boxes, <scene></scene> for scene embeddings, and action tokens (<aloc0-255>, <arot0-255>, <gripper0/1>) for robot actions

**Delta**: outperforms baseline
**Condition**: Embodied environment interaction, action prediction, and 3D scene understanding

**Evidence**: "These added tokens enable our model to perform a wider range of embodied tasks and support interleaved 3D-text data."

## [POSITIVE] Predicted Bounding Box as Intermediate Input
Using intermediate predicted 3D bounding boxes as part of the input prompt to help the model focus on specific objects mentioned in instructions

**Delta**: slight improvement in PSNR (17.21 vs 17.02), SSIM (0.636 vs 0.632) for image; P-FID (4.796 vs 4.914), Chamfer-L1 (0.139 vs 0.143) for point cloud
**Condition**: RGB image goal generation and point cloud goal generation tasks

**Evidence**: "when we exclude the predicted bounding box from the input prompt (row 5), we observe a slight decrease in performance. This observation confirms the effectiveness of using these intermediate predicted bounding boxes as they assist the model in comprehending the overall scene"

## [POSITIVE] Embodied Diffusion Model Pretraining
Pretraining RGBD-to-RGBD and point-to-point diffusion models specifically on robotics datasets before aligning with the LLM, rather than using off-the-shelf video diffusion models

**Delta**: outperforms baseline
**Condition**: Goal image and point cloud generation in robotics domain

**Evidence**: "This underscores the importance of training a world model using datasets specifically designed for robotics applications."

## [POSITIVE] LLM Integration with Diffusion Models via Projector
Using a transformer-based projector to map LLM embeddings into the diffusion model framework, bridging the gap between language understanding and multimodal goal generation

**Delta**: outperforms Instruct-P2P* trained on same data
**Condition**: Goal image generation compared to image-editing baselines

**Evidence**: "Even in a direct comparison with Instruct-P2P*, which was trained on the same robotics datasets we employed (row 4 in the table), 3D-VLA consistently outperforms it. This highlights that the integration of a large language model into 3D-VLA results in a more comprehensive and insightful comprehension of robotics manipulation instructions"

## [POSITIVE] Goal State Imagination for Action Planning
Using imagined/generated goal states (images or point clouds) to guide robot action prediction, rather than direct perception-to-action mapping

**Delta**: 3D-VLA outperforms 3D-VLA w/o Goal on Take Umbrella (80 vs 40) and Pick Up Cup (28 vs 24) tasks
**Condition**: RLBench action planning tasks requiring spatial localization or color discrimination

**Evidence**: "our 3D-VLA model outperforms 3D-VLA w/o Goal by a lot on the Take Umbrella and Pick Up Cup tasks. This is because the imagined goal guides the robotic arm to move to the specific location or determine the color of the object."

## [NEUTRAL] Goal State Imagination for Action Planning (knife task)
Using imagined goal states to guide robot action prediction on collision-prone tasks

**Delta**: same performance across both settings
**Condition**: RLBench 'put knife on chopping board' task where failures are due to object collisions

**Evidence**: "the performance on the task put the knife on the chopping board is same across both settings, as most failures might be due to object collisions."

## [POSITIVE] LoRA Fine-tuning for Diffusion Models
Using Low-Rank Adaptation (LoRA) to fine-tune diffusion models during alignment stage to improve training efficiency and avoid catastrophic forgetting

**Delta**: descriptive only
**Condition**: Alignment stage between LLM and diffusion models

**Evidence**: "To make training 3D-VLA more efficient and to avoid catastrophic forgetting, we utilize LoRA (Hu et al., 2021) to fine-tune different diffusion models."

## [POSITIVE] ZoeDepth for Depth Estimation on 2D Datasets
Applying ZoeDepth depth estimator to datasets lacking depth information (over 95% of embodied video datasets) to generate pseudo-3D annotations

**Delta**: descriptive only
**Condition**: Data collection pipeline for datasets without depth annotations

**Evidence**: "Given that over 95% of the video datasets for embodied tasks do not provide 3D information, we employ ZoeDepth (Bhat et al., 2023) on each frame of the video from these datasets."

## [POSITIVE] Optical Flow for Depth Consistency
Using RAFT optical flow estimation to identify static background pixels and align depth maps across frames for consistency

**Delta**: descriptive only
**Condition**: Depth map generation for video datasets without camera pose changes

**Evidence**: "we use RAFT (Teed & Deng, 2020) for optical flow estimation. Optical flow aids in refining the data we generate. Thus, for video segments where the camera pose does not change, we use optical flow to estimate which pixels are the unmoved background. We align the depth maps of these backgrounds across different frames"

## [POSITIVE] ChatGPT-based Prompt Diversification
Using GPT-3.5-turbo to diversify language annotations by rewriting template-generated prompts into more natural forms, with 2-3 few-shot human-written demonstrations

**Delta**: descriptive only
**Condition**: Language annotation generation for 3D embodied instruction tuning dataset

**Evidence**: "we use ChatGPT-based prompting to diversify prompts. Specifically, we provide instructions to ChatGPT, as well as our annotated objects and bounding boxes. We also give 2-3 few-shot human-written demonstrations to guide the GPT on the type of data it is instructed to generate."

## [POSITIVE] BLIP2-FlanT5XL as Pretrained Backbone (instead of 3D-LLM weights)
Using BLIP2-FlanT5XL as the pretrained model instead of loading 3D-LLM pretrained weights, due to domain mismatch between 3D-LLM training data (objects/indoor scenes) and embodied robotics setup

**Delta**: descriptive only
**Condition**: Backbone initialization for embodied robotics tasks

**Evidence**: "the training datasets for 3D-LLM mostly comprise objects and indoor scenes, which do not directly align with our embodied setup. Therefore, we choose not to load the 3D-LLM pretrained model. Instead, we utilize BLIP2-FlanT5XL as our pretrained model."

## [NEGATIVE] 3D-LLM on Robotics Tasks (zero-shot)
Applying 3D-LLM pretrained model directly to robotics reasoning tasks without robotics-specific training

**Delta**: poor performance relative to 3D-VLA
**Condition**: Zero-shot transfer to robotics reasoning tasks

**Evidence**: "we find that 3D-LLM performs poorly on these robotic reasoning tasks, which demonstrates the necessity of collecting and training on a robotics-related 3D dataset."

## [NEGATIVE] Off-the-shelf Video Diffusion Models for Goal Generation
Using general-purpose video diffusion models (e.g., Runway) or frozen stable diffusion (DreamLLM approach) for embodied goal generation without robotics-specific fine-tuning

**Delta**: descriptive only
**Condition**: Goal image generation for embodied robotics tasks

**Evidence**: "when asking Runway to generate future frames given the instruction 'open the drawer', the entire scene is altered to a great extent with regard to view change, unexpected object deformation, and weird texture replacement, as well as layout distortion. Similarly, using the method of DreamLLM to directly freeze the stable diffusion trained on internet data, can lead to collapsed outputs."

## [NEGATIVE] Discrete Action Token Representation
Representing robot 7-DoF actions as discrete tokens (<aloc0-255>, <arot0-255>, <gripper0/1>) within the LLM vocabulary

**Delta**: descriptive only
**Condition**: Precise manipulation of small objects in RLBench

**Evidence**: "In RLBench, we are unable to successfully execute the task of picking up small cubes, as the 3D features and discrete action tokens make it difficult to accurately locate and manipulate these small objects."

## [POSITIVE] 3D Localization Annotations in Training Data
Including 3D bounding box annotations in the training dataset to help the model learn to localize relevant objects

**Delta**: outperforms Kosmos-2 and CoVLM baselines (IoU: 29.33 vs 19.81 vs 10.92; Acc@25: 42.26 vs 25.39 vs 12.73; Acc@50: 27.09 vs 16.61 vs 3.85)
**Condition**: 3D object localization tasks on held-in robotics datasets

**Evidence**: "since our dataset contains a bunch of 3D localization annotations, 3D-VLA learns to localize the relevant objects, which helps the model focus more on key objects for reasoning."

## [POSITIVE] Human-Object Interaction Datasets for Goal Generation
Including HOI datasets (Epic-Kitchens, HOI4D) in training to provide diverse scenes and object interaction methods for the diffusion model

**Delta**: descriptive only
**Condition**: Goal image and point cloud generation diversity

**Evidence**: "within the same robotics dataset, the background settings are largely the same. Therefore, in the Goal Generation tasks, we included HOI datasets to better allow the diffusion model to learn diverse scenes, object interaction methods, etc."

## [NEUTRAL] Dataset Quality Variance Effect on Performance
Higher quality datasets (RT-1, BridgeV2) yield better scores while lower quality datasets (BCZ, Roboturk) yield lower scores due to annotation and image quality differences

**Delta**: descriptive only
**Condition**: Performance across different source datasets in the training mixture

**Evidence**: "in datasets such as RT1, and BridgeV2, the scores of the goal generation and language-related tasks are higher due to their higher annotation quality and image quality; however, in datasets like BCZ, and Roboturk, the scores are lower."

## [POSITIVE] Multimodal Special Tokens for Generation Type Specification
Introducing <image></image> and <pcd></pcd> tokens to inform the decoder about the type of modal content to output, with LLM supervised to generate robot instructions between these tokens

**Delta**: descriptive only
**Condition**: Multimodal goal generation alignment between LLM and diffusion models

**Evidence**: "These tokens are intricately designed to inform the decoder about the type of modal content to output. Between the enclosing tokens, we supervise the LLM in generating instructions for a robot to execute"

## [POSITIVE] Combined LLM and Diffusion Model Denoising Loss
Minimizing both the LLM cross-entropy loss and the diffusion model denoising loss jointly during the alignment stage

**Delta**: descriptive only
**Condition**: Alignment stage training between LLM and diffusion models

**Evidence**: "We minimize both the LLM and DM denoising loss."
