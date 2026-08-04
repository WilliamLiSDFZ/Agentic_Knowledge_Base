# Using Left and Right Brains Together: Towards Vision and Language Planning

**Source**: https://proceedings.mlr.press/v235/cen24a.html

## [POSITIVE] Vision-Language Planning (VLP) Framework
A dual-branch framework that performs both vision planning (generating future frames) and language planning (chain-of-thought decomposition) in parallel before feeding results to a decision-making LMM

**Delta**: +3.1% accuracy on STAR (47.4 to 50.5), +1.1 BLEU-4 on BDD-X (34.6 to 35.7)
**Condition**: Vision-language tasks (STAR, NExT-QA), vision-only tasks (BDD-X), and robotics tasks (BAIR)

**Evidence**: "Table 3 and Table 4 show that both VP and LP could clearly boost the performance of the baseline. For example, VP and LP improved 2.2% and 3.0% Accuracy on STAR and 1.1 and 0.6 BLEU-4 score on BDD-X."

## [POSITIVE] Vision Planning (VP)
Using a video diffusion model (e.g., Stable Video Diffusion) to generate future frames from current image/video inputs, providing visual foresight for reasoning

**Delta**: +2.2% accuracy on STAR (47.4 to 49.6), +1.1 BLEU-4 on BDD-X (34.6 to 35.7)
**Condition**: More beneficial for vision-only tasks (BDD-X captioning) than vision-language Q&A tasks

**Evidence**: "VP and LP improved 2.2% and 3.0% Accuracy on STAR and 1.1 and 0.6 BLEU-4 score on BDD-X."

## [POSITIVE] Language Planning (LP)
Zero-shot chain-of-thought prompting via ChatGPT to decompose the input query into sequential sub-questions that guide the decision maker

**Delta**: +3.0% accuracy on STAR (47.4 to 50.4), +0.6 BLEU-4 on BDD-X (34.6 to 35.2)
**Condition**: More beneficial for vision-language Q&A tasks (STAR) than vision-only captioning tasks (BDD-X)

**Evidence**: "VP and LP improved 2.2% and 3.0% Accuracy on STAR and 1.1 and 0.6 BLEU-4 score on BDD-X. LP brings more benefit than VP on vision-language task STAR while this circumstance is contrary on vision task BDD-X."

## [POSITIVE] Vision Planning Selector (VPS) - Coarse Selector (CS)
A ChatGPT-based binary filter that determines whether generated future frames are relevant to the current query before including them

**Delta**: ~2% accuracy drop on Interaction and Sequence questions without CS
**Condition**: STAR dataset, particularly for question types not related to future states (Interaction, Sequence)

**Evidence**: "The Interaction and Sequence questions in STAR are not supposed to be related to the future frames, and Table 5 shows the performance of them drops about 2% without CS, which means introducing generated frames might bring noisy information for questions independent of the future."

## [POSITIVE] Vision Planning Selector (VPS) - Fine Selector (FS)
A BLIP-2/Q-former based frame scoring mechanism that selects the most useful frames from original and generated content using CLIP visual features and a 'Yes' token probability score

**Delta**: Dramatic drop in Prediction and Feasibility question performance without FS (Table 5)
**Condition**: STAR dataset, particularly for Prediction and Feasibility question types that require future frame selection

**Evidence**: "Without FS, the performance of Prediction and Feasibility questions drop dramatically, which illustrates the significance of using FS for picking up useful and high-quality generated frames."

## [POSITIVE] Voting Mechanism in Decision Maker
A multi-round strategy where the LMM re-evaluates and votes between vanilla answer and language/vision plan answers to produce a final robust decision

**Delta**: LP without voting: 46.3 avg vs LP with voting: 50.4 avg on STAR; VP without voting: 48.3 avg vs VP with voting: 49.6 avg
**Condition**: STAR dataset; applicable when language or vision plans may introduce noise

**Evidence**: "Table 6 shows that letting the model vote again between the vanilla answer and the answer with language or vision plan could effectively enhance the performance."

## [POSITIVE] Multi-round Conversation Strategy for Open-source LMMs
A sequential multi-turn dialogue approach for LMMs like LLAVA that cannot handle complex instructions in a single reply, answering sub-questions one by one before the final answer

**Delta**: Enables correct final answer (e.g., 'Put down the cup') where single-turn fails
**Condition**: Open-source LMMs (LLAVA) that lack strong visual instruction-following capability

**Evidence**: "We find that the open-source LMM such as LLAVA can only follow simple visual instructions and cannot handle flexible and complicated visual instructions. For example, LLAVA cannot answer the questions sequentially in one reply. So we design a multi-round conversation strategy."

## [POSITIVE] Domain-specific Video Generation Models
Using video generation models trained on domain-specific datasets (e.g., DMVFN on Cityscapes/Kitti for driving) instead of general-purpose models

**Delta**: DMVFN-Kitti: BLEU-4 35.2, CIDEr 234.2 vs Stable Video Diffusion: BLEU-4 33.9, CIDEr 229.6 on BDD-X
**Condition**: BDD-X autonomous driving dataset; domain-specific tasks benefit from domain-matched generative models

**Evidence**: "DMVFN trained on the driving datasets including Cityscapes and Kitti show better performance because of higher resolution. Stable Video Diffusion does not perform better as it is not specifically trained for the driving scenario."

## [NEGATIVE] Generated Future Frames vs. Ground Truth Frames
Using video diffusion model outputs as vision plan instead of actual ground truth future frames

**Delta**: Ground truth: 57.5 Prediction, 54.9 Feasibility vs generated: 50.0 Prediction, 47.6 Feasibility on STAR
**Condition**: Open-domain STAR dataset; gap indicates quality ceiling of current video generation models

**Evidence**: "Table 9 shows that using real future frames has significantly better performance than generated frames using Stable Video Diffusion, e.g., 57.5 and 54.9 compared to 50.0 and 47.6 on Prediction and Feasibility questions."

## [NEUTRAL] Increasing Number of Generated Frames (Open Domain)
Generating more than 1 future frame for vision planning in open-domain settings

**Delta**: 1 frame: 49.6 avg, 2 frames: 49.7 avg, 3 frames: 49.7 avg on STAR
**Condition**: STAR open-domain dataset with Stable Video Diffusion

**Evidence**: "Due to the limited quality of the generated future frames in the open domain, selecting more frames does not have clear performance improvements according to Table 9."

## [POSITIVE] Optimal Number of Generated Frames (Domain-specific)
Selecting an appropriate number of generated frames (8 frames) for domain-specific video generation tasks

**Delta**: 8 frames: BLEU-4 35.2, CIDEr 234.2 vs 2 frames: BLEU-4 32.0, CIDEr 212.6 on BDD-X
**Condition**: BDD-X dataset with DMVFN; performance peaks at 8 frames and degrades at 16 and 30 frames

**Evidence**: "Table 11 shows that a proper number of generated frames is helpful when using domain-specific generative models, but long sequence generated videos are not reliable enough."

## [POSITIVE] Language-to-Vision (L2V) Conversion for Pure Language Tasks
Converting pure language queries into visual content (images/videos) using a generative model to enable vision planning on text-only inputs

**Delta**: More detailed and vivid descriptions (qualitative); e.g., specific landmarks and color descriptions generated
**Condition**: Language-only tasks (e.g., news writing); demonstrated qualitatively with GPT4-V

**Evidence**: "Fig. 4 shows that our VLP generates more detailed and vivid descriptions based on the generated future frames in language-only tasks. For example, VLP generates the phases like 'fireworks erupted in a symphony of red and gold near the water's edge'."

## [NEGATIVE] MCVD for Video Generation
Using MCVD (masked conditional video diffusion) model for generating future frames in vision planning

**Delta**: MCVD: BLEU-4 31.2, CIDEr 195.3 vs DMVFN-Kitti: BLEU-4 35.2, CIDEr 234.2 on BDD-X
**Condition**: BDD-X autonomous driving dataset

**Evidence**: "MCVD performs worst since it generates low-resolution images."

## [POSITIVE] VP for Robotics Action Prediction and Planning
Applying vision planning (generated future frames) to improve robot gripper trajectory prediction and planning tasks

**Delta**: 2+0 setup: Sum RMSE 19.85 to 19.36; 1+2 planning: Sum RMSE 14.39 to 13.85
**Condition**: BAIR robotics dataset for both prediction (initial frames only) and planning (initial + goal frames) tasks

**Evidence**: "Table 8 shows that VP also helps in this application [robotics gripper trajectory prediction and planning]."

## [POSITIVE] VP for Autonomous Driving Control Signal Prediction
Using generated future frames to improve course and speed prediction accuracy in autonomous driving

**Delta**: Speed RMSE improved from 2.5 to 2.3; Course RMSE improved from 6.4 to 6.2 on BDD-X
**Condition**: BDD-X autonomous driving dataset for control signal prediction

**Evidence**: "Table 7 shows that with the help of generated future frames, the model could predict the course and speed more accurately in the driving scenario."

## [NEGATIVE] LP on BDD-X with ADAPT
Adding language planning on top of ADAPT for video captioning on the BDD-X driving dataset

**Delta**: CIDEr drops from 247.5 to 242.6 when adding LP alone to ADAPT on BDD-X
**Condition**: BDD-X vision-only captioning task; LP alone hurts CIDEr metric, suggesting language planning is less suited for pure vision captioning

**Evidence**: "Table 4: ADAPT+LP achieves CIDEr 242.6 vs ADAPT baseline 247.5, while ADAPT+VP achieves 256.7."
