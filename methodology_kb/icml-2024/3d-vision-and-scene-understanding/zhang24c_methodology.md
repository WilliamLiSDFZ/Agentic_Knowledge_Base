# SAM-E: Leveraging Visual Foundation Model with Sequence Imitation for Embodied Manipulation

**Source**: https://proceedings.mlr.press/v235/zhang24c.html

## [POSITIVE] SAM as Visual Foundation Model
Using the Segment Anything Model (SAM) pretrained on large-scale image and mask data as the visual encoder for extracting task-relevant, object-oriented features in robot manipulation

**Delta**: +7.7% average success rate over RVT (12.2% relative improvement)
**Condition**: Multi-task 3D manipulation on RLBench with 18 tasks and 249 variations

**Evidence**: "SAM-E outperforms PerAct and RVT by an average of 21.2% and 7.7% percentage points in success rate across 18 tasks, marking a relative improvement with 43.0% and 12.2%"

## [POSITIVE] LoRA Fine-tuning on SAM Encoder (Q and V only)
Parameter-efficient fine-tuning of the SAM encoder using Low-Rank Adaptation applied only to query (Q) and value (V) projection layers in self-attention modules, with rank r=4

**Delta**: 70.6% vs 67.2% (w/o LoRA) and 65.8% (full finetune)
**Condition**: Multi-task manipulation with limited robot demonstrations (100 per task)

**Evidence**: "Using LoRA to parameter-efficiently finetuning, SAM is better than the variant that trains all parameters, which may lead to failure due to the limited demonstrations."

## [NEGATIVE] LoRA with Q, K, and V (QKV variant)
Variant of LoRA that additionally includes the K (key) matrix in addition to Q and V projection layers

**Delta**: 69.2% vs 70.6% for Q+V only variant
**Condition**: Multi-task 3D manipulation ablation study

**Evidence**: "For LoRA, adding the trainable matrix for Q and V is better than all Q, K, and V, which is consistent with previous observations (Hu et al., 2022)."

## [NEGATIVE] Full Fine-tuning of SAM Encoder
Training all parameters of the SAM encoder instead of using parameter-efficient LoRA

**Delta**: 65.8% vs 70.6% for LoRA variant
**Condition**: Multi-task manipulation with limited robot demonstrations (100 per task)

**Evidence**: "Using LoRA to parameter-efficiently finetuning, SAM is better than the variant that trains all parameters, which may lead to failure due to the limited demonstrations."

## [NEGATIVE] Frozen SAM Encoder (w/o LoRA)
Using the SAM encoder without any fine-tuning on embodied data

**Delta**: 67.2% vs 70.6% for LoRA-tuned SAM
**Condition**: Multi-task 3D manipulation ablation study

**Evidence**: "SAM is a crucial visual foundation and a suitable finetune method is required for adaptation to embodied scenarios."

## [POSITIVE] Multi-Channel Heatmap for Action-Sequence Prediction
A novel prediction head that generates multi-channel pose heatmaps for an entire action sequence in a single forward pass, with time-dimension channels encoding temporal information

**Delta**: 5X greater execution efficiency than RVT; inference steps reduced from 6158 to 1130
**Condition**: Long-horizon 3D manipulation tasks requiring multiple sequential actions

**Evidence**: "SAM-E demonstrates an average execution efficiency of more than 5X greater than that of RVT."

## [POSITIVE] Action Sequence Imitation (Sequence Length h=5)
Predicting a coherent sequence of h=5 future actions in a single pass rather than step-by-step prediction, leveraging temporal smoothness of end-effector trajectories

**Delta**: 70.6% success rate vs 30.6% for h=1
**Condition**: Multi-task 3D manipulation on RLBench

**Evidence**: "We observe that h=5 performs the best on the average success rate, while it may not suitable for certain tasks."

## [NEGATIVE] Action Sequence Length h=1 (step-by-step)
Predicting only a single next action at each step, equivalent to traditional step-by-step prediction

**Delta**: 30.6% vs 70.6% for h=5
**Condition**: Multi-task 3D manipulation ablation study

**Evidence**: "We can also find that h=1 leads to a drop in performance, which we attribute to the insufficient temporal information to drive SAM foundation training, combined with the lack of empirically crucial duplication for important transitions."

## [NEGATIVE] Action Sequence Length h=7
Predicting a sequence of 7 future actions in a single pass

**Delta**: 66.5% vs 70.6% for h=5
**Condition**: Multi-task 3D manipulation ablation study

**Evidence**: "Ablation study on the action horizon, examining h values of {1,3,5,7}... h=5 performs the best on the average success rate"

## [POSITIVE] Action Sequence Length h=3
Predicting a sequence of 3 future actions in a single pass

**Delta**: 64.0% vs 62.9% for RVT baseline
**Condition**: Multi-task 3D manipulation ablation study

**Evidence**: "Ablation study on the action horizon, examining h values of {1,3,5,7}... h=5 performs the best on the average success rate"

## [POSITIVE] Multi-View Transformer with Cross-View Attention
Two-stage transformer that first applies view-wise attention within each camera view, then cross-view attention across all views combined with language tokens for multi-view scene understanding

**Delta**: outperforms baseline
**Condition**: Multi-task 3D manipulation with 4 RGB-D cameras

**Evidence**: "a multi-view transformer is used to integrate cross-view visual information combined with coordinate information and language instruction for multi-view correspondence and vision-language alignment"

## [POSITIVE] CLIP Text Encoder for Language Tokens
Using a pretrained CLIP text encoder to generate language embeddings that are attended to in the cross-view attention blocks for vision-language alignment

**Delta**: part of full SAM-E achieving 70.6%
**Condition**: Language-instructed 3D manipulation tasks

**Evidence**: "we utilize a pretrained CLIP text encoder to generate language embeddings, from which language tokens are derived... visual tokens across different views and the language tokens are attended to cross-view attention blocks"

## [NEGATIVE] R3M as Visual Encoder (replacing SAM)
Using R3M (visual representation designed for robot manipulation) as the image encoder instead of SAM in the SAM-E architecture

**Delta**: 66.5% vs 70.6% for SAM-E with SAM encoder
**Condition**: Multi-task 3D manipulation; R3M shows limited few-shot generalization

**Evidence**: "Building upon this, the addition of R3M's frozen representation has yielded a marginal performance improvement, however, which is still inferior compared to SAM-E."

## [NEGATIVE] CLIP as Visual Encoder (replacing SAM)
Using CLIP visual representation as the image encoder instead of SAM in the SAM-E architecture

**Delta**: 64.8% vs 70.6% for SAM-E with SAM encoder
**Condition**: Multi-task 3D manipulation; shows better few-shot adaptation than R3M

**Evidence**: "Similarly, CLIP and DINO representations have mediocre performances compared to SAM-E."

## [NEGATIVE] DINO as Visual Encoder (replacing SAM)
Using DINO self-supervised visual representation as the image encoder instead of SAM in the SAM-E architecture

**Delta**: 67.1% vs 70.6% for SAM-E with SAM encoder
**Condition**: Multi-task 3D manipulation; shows better few-shot adaptation than R3M

**Evidence**: "Similarly, CLIP and DINO representations have mediocre performances compared to SAM-E."

## [NEGATIVE] Non-pretrained Encoder (SAM→RVT variant)
Replacing the SAM encoder with RVT's visual encoder trained from scratch, while keeping the action-sequence prediction head

**Delta**: 65.3% vs 70.6% for full SAM-E
**Condition**: Multi-task 3D manipulation; demonstrates value of both SAM pretraining and sequence prediction independently

**Evidence**: "Eliminating the pre-trained SAM encoder in SAM-E leads to a performance drop but still outperforms RVT, benefiting from the action sequence policy head."

## [POSITIVE] Few-Shot Adaptation with SAM Foundation
Fine-tuning the SAM-E model pretrained on multi-task data to new tasks using 10x fewer demonstrations and 15x fewer update steps

**Delta**: +26.1% points over RVT adaptation (70.4% relative improvement); 63.2% vs 37.1% for RVT
**Condition**: Few-shot adaptation to 6 new unseen tasks with limited demonstrations

**Evidence**: "during adaptation to new tasks, the performance gap widens dramatically, with SAM-E surpassing RVT by 26.1% points, a substantial 70.4% relative improvement."

## [POSITIVE] Depth and Coordinate Information via Conv2D
Processing depth and 3D coordinate information through a Conv2D layer to obtain spatial features, which are concatenated with image embeddings as view tokens

**Delta**: part of full SAM-E achieving 70.6%
**Condition**: 3D manipulation requiring accurate spatial localization

**Evidence**: "depth and coordinate information is processed through a Conv2D layer to obtain 3D spatial features. We concatenate the image embeddings with spatial features in the channel dimension along the patch tokens"

## [POSITIVE] Heatmap Back-projection to 3D Space
Back-projecting 2D heatmaps from multiple views into 3D space to generate scores for discretized 3D points, determining 3D end-effector positions

**Delta**: part of full SAM-E achieving 70.6%
**Condition**: 3D position prediction in multi-view manipulation

**Evidence**: "the heatmaps from different views are back-projected into 3D space to generate scores for a discretized set of 3D points, ultimately determining the 3D positions and rotations of actions"

## [POSITIVE] Rotation Discretization into 5-degree Bins
Discretizing Euler angles into bins of 5-degree resolution and treating rotation prediction as classification rather than regression

**Delta**: part of full SAM-E achieving 70.6%
**Condition**: Rotation prediction in 3D manipulation

**Evidence**: "For predicting rotations, we follow previous methods (Goyal et al., 2023) to discretize Euler angles into bins of 5° resolution and thus turn rotation prediction into classification"

## [POSITIVE] Key-Frame Extraction
Selecting key-frame actions from demonstrations based on near-zero joint velocities or gripper state changes, reducing the prediction problem to next key-frame action prediction

**Delta**: consistent with state-of-the-art methods; enables action sequence decomposition
**Condition**: Applied to all methods for fair comparison; enables efficient long-horizon planning

**Evidence**: "we align with the consensus in 3D manipulation algorithms by incorporating key-frame extraction for selecting key-frame actions... the imitation objective becomes predicting the 'next key-frame action' in the demonstration"

## [POSITIVE] Action Sequence Prediction Training Efficiency
Training with action sequence imitation leads to faster convergence compared to step-by-step prediction baselines

**Delta**: higher success rate at same training steps (e.g., ~60% vs ~55% at 12K steps from Figure 5)
**Condition**: Training on RLBench multi-task data up to 60K steps

**Evidence**: "SAM-E and its variations exhibit higher training efficiency than RVT, mainly attributed to the action sequence imitation."
