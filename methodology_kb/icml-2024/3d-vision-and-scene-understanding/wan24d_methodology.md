# VinT-6D: A Large-Scale Object-in-hand Dataset from Vision, Touch and Proprioception

**Source**: https://proceedings.mlr.press/v235/wan24d.html

## [POSITIVE] Multi-modal fusion (Vision + Touch + Proprioception)
Integrating tactile and proprioceptive data with visual inputs in VinT-Net for object-in-hand pose estimation

**Delta**: +3.11 to +7.87 ADD(S) AUC across objects (Vision+Touch vs Vision only in VinT-Real)
**Condition**: Object-in-hand pose estimation in VinT-Real, especially under occlusion

**Evidence**: "Our visual-tactile VinT-Net surpasses the baseline relying solely on vision by a margin, demonstrating the incorporation of additional tactile information notably enhances performance."

## [POSITIVE] Combining simulated and real data (Sim+Real training)
Training on both VinT-Sim and VinT-Real data together rather than using either alone

**Delta**: e.g., Blue Bottle: SIM=87.52, REAL=93.45, VinT-6D=94.15 ADD(S) AUC
**Condition**: All objects evaluated in Table 3; combined training consistently outperforms either split alone

**Evidence**: "The results show that our comprehensive calibration and simulation strategy effectively bridges the sim2real gap by augmenting the simulated data to the real data, as evidenced by the performance improvement when combining simulated and real data for training."

## [POSITIVE] Multi-modal fusion under increasing occlusion
Using vision and touch together to maintain pose estimation accuracy as hand occlusion of the object increases

**Delta**: Vision-only drops from 93.31% to 80.43% (20%→50% occlusion); Vision+Touch drops only from 94.76% to 88.81%
**Condition**: Tomato soup can under 20%–50% occlusion rates

**Evidence**: "Table 6 reveals a notable decrease in accuracy for vision-based approaches as occlusion intensifies, from 93.31% at 20% occlusion to 80.43% at 50% occlusion. Conversely, the multi-modal fusion strategy...exhibited remarkable resilience against increasing occlusion levels."

## [NEGATIVE] Touch data in semantic segmentation head
Integrating touch data into the semantic segmentation head of the 3D keypoint-based pose estimation module

**Delta**: No quantitative delta given; described as not enhancing performance
**Condition**: Semantic segmentation head within VinT-Net's 3D Keypoint-Based Pose Estimation Module

**Evidence**: "Interestingly, our experiments showed that integrating touch data into the semantic segmentation head did not enhance performance. This may indicate that additional touch information may interfere with the head's functionality."

## [POSITIVE] SAM segmentation with multi-modal prompts
Using touch and proprioception as cues (positive/negative prompts) to guide the SAM model for object segmentation from the robotic hand

**Delta**: mIoU of 94.44–96.63 across 20%–50% occlusion levels
**Condition**: Object segmentation in VinT-Real under 20%–50% occlusion

**Evidence**: "To overcome this, our solution utilizes touch and proprioception as cues for the SAM segmentation model...which improves the segmentation process...we use negative ('-') for thumb and positive ('+') for index and middle finger tactile points, along with two object points."

## [POSITIVE] Contact position representation for tactile simulation
Simulating contact positions rather than mimicking each taxel's specific measurements to achieve sensor-agnostic, robust tactile representation

**Delta**: Described as robust to contact force and time variation; no specific numeric delta
**Condition**: Touch simulation in VinT-Sim for bridging sim-to-real gap

**Evidence**: "We focus on the simulation of contact positions rather than mimicking each taxel's specific measurements. For both pressure and vision-based tactile sensors, well-calibrated contact positions can be robust to contact force and time variation."

## [POSITIVE] Photo-realistic rendering with Blender Cycles engine
Using Blender's ray tracing, diverse shaders, HDRI backgrounds, and multi-view rendering instead of MuJoCo's basic renderer for visual data generation

**Delta**: Described as improving domain adaptation; no specific numeric delta
**Condition**: Visual data generation in VinT-Sim

**Evidence**: "To achieve this, we leverage Blender's advanced rendering features, including ray tracing, diverse shaders, and real-time viewport rendering through its Cycles engine...these techniques enable us to generate highly realistic visual data, improving domain adaptation."

## [POSITIVE] Depth image post-processing to simulate Kinect Azure noise
Introducing noise, holes, and smoothing to rendered depth images to replicate real-world Kinect Azure TOF camera characteristics

**Delta**: Described as making depth images more realistic and accurate; no specific numeric delta
**Condition**: Depth image simulation in VinT-Sim for sim-to-real gap reduction

**Evidence**: "To enhance realism, we introduce noise, create holes, and smooth the rendered depth images...By replicating the Kinect Azure sensor's unique noise characteristics, we aim to accurately recreate real-world conditions in our simulations."

## [POSITIVE] Whole-hand tactile perception (fingertip + pulp + palm sensors)
Equipping robotic hands with array-based tactile sensors covering the entire hand (620–679 taxels) rather than fingertips only

**Delta**: Described as significantly advancing robotic in-hand perception; no specific numeric delta
**Condition**: Tactile sensing coverage in both VinT-Sim and VinT-Real

**Evidence**: "VinT-6D is a unique dataset that uses whole-hand tactile perception, which sets it apart from other datasets that rely on fingertip tactile sensing alone...This promises to significantly advance robotic in-hand perception capabilities through extensive area contact."

## [POSITIVE] Motion capture system for sub-millimeter object pose accuracy
Using a Vicon motion capture system with custom marker assemblies on objects to obtain highly accurate ground truth object poses in VinT-Real

**Delta**: Sub-millimeter level accuracy in object pose acquisition
**Condition**: Ground truth pose collection in VinT-Real

**Evidence**: "We meticulously customize marker assemblies on fixed parts of each object, ensuring sub-millimeter level accuracy in object pose acquisition without hindering the object's functionality...Our approach surpasses common ArUco tag-based methods."

## [POSITIVE] Pixel-wise color and depth fusion in Sensing Aggregation Module
Integrating color and depth information at the pixel level following DenseFusion-style fusion principles

**Delta**: Part of overall system achieving 82.43 ADD-0.05d vs 76.74 for Object-Hand-Pose baseline
**Condition**: VinT-Net Sensing Aggregation Module for object-in-hand pose estimation

**Evidence**: "Following the principles of advanced vision fusion techniques (Wang et al., 2019), we integrate the color and depth information on a pixel-wise level."

## [POSITIVE] 3D keypoint-based pose estimation with multi-task loss
Predicting object center and keypoint offsets using fused multi-modal embeddings with Focal Loss for segmentation and L1 Loss for center/keypoint prediction

**Delta**: VinT-Net achieves 82.43 ADD-0.05d vs 76.74 (Object-Hand-Pose) and 74.60 (PVN3D)
**Condition**: Object-in-hand pose estimation on tomato soup can in VinT-Real

**Evidence**: "Table 5 shows that our VinT-Net significantly outperforms recent object-in-hand pose estimation methods like (Wen et al., 2020) on the ADD-0.05d metric."

## [POSITIVE] Selected stable grasping simulation
Generating grasps that ensure both stable holding and readiness for manipulation, rather than optimizing for grasp stability alone

**Delta**: 125,000 unique successful graspings generated; described as closely mirroring real-world scenarios
**Condition**: Object-grasp interaction simulation in VinT-Sim

**Evidence**: "Our answer is selected stable grasping involves not only stable holding of the object but also readiness for manipulation...This setup is designed to closely mirror real-world grasping scenarios, ensuring the grasp's stability and utility for subsequent manipulations."
