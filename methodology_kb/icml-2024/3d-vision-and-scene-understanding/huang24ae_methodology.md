# An Embodied Generalist Agent in 3D World

**Source**: https://proceedings.mlr.press/v235/huang24ae.html

## [POSITIVE] Two-stage Training (VL Alignment + VLA Instruction Tuning)
A two-stage learning scheme where stage 1 performs 3D vision-language alignment (LEO-align) and stage 2 performs 3D vision-language-action instruction tuning (LEO-instruct)

**Delta**: Scan2Cap similarity: 62.8 (w/o Align) vs 65.4 (w/ Align)
**Condition**: 3D VL understanding tasks, especially scene captioning

**Evidence**: "The results in Tab. 7 show the consistent impact of alignment. In particular, the benefit of alignment is significant on Scan2Cap since it concerns detailed scene understanding and captioning, which is a primary focus of alignment training."

## [POSITIVE] Object-centric 3D Token Embedding with Spatial Transformer
Each 3D object's point cloud is encoded by PointNet++ and processed through a Spatial Transformer that biases attention scores with relative position and size to capture 3D relations between objects

**Delta**: outperforms baseline
**Condition**: 3D VL understanding and reasoning tasks

**Evidence**: "considering the complicated feature aggregation in 3D-LLM, we believe that object-centric 3D representation is a simple yet effective option to connect 3D scenes with LLM while harnessing the inherent knowledge of LLM."

## [POSITIVE] LoRA Fine-tuning of Frozen LLM
Low-rank adaptation (LoRA) introduces additional tunable parameters to the frozen pretrained LLM (Vicuna-7B), with ~142M of ~7B total parameters tuned

**Delta**: outperforms baseline
**Condition**: Multi-modal alignment and grounding across all tasks

**Evidence**: "In order to tackle the challenging alignment and grounding problem of multimodal tokens (2D, 3D, text, embodied action) while preserving the LLM pretrained knowledge, we employ LoRA (Hu et al., 2022) to introduce additional tunable parameters to the frozen pretrained LLM."

## [POSITIVE] Scene-graph-based Prompting for Data Generation
Using 3D scene graphs from 3DSSG that provide rich object attributes and accurate spatial relation information to prompt LLMs for generating 3D-text paired data

**Delta**: Counting accuracy: 57.4 (base) vs 78.0 (+O-CoT) vs 100.0 (+refinement)
**Condition**: LLM-assisted 3D-language data generation

**Evidence**: "Compared to counterparts that utilize object boxes, it offers both rich object attributes and accurate spatial relation information among objects, allowing LLMs to generate data with high-quality 3D details."

## [POSITIVE] Object-centric Chain-of-Thought (O-CoT) Prompting
Prompting method that requires the LLM to explicitly provide the label and ID of object candidates as intermediate thoughts during text generation to combat hallucination

**Delta**: Counting accuracy: 57.4 (base) → 78.0 (+O-CoT)
**Condition**: LLM-assisted data generation, particularly for counting and existence questions

**Evidence**: "we propose the object-centric chain of thought (O-CoT) prompting that requires the LLM to explicitly provide the label and ID of object candidates as thoughts during text generation... Results in Tab. 2 demonstrate that our proposed scene-graph-based prompting, O-CoT prompting and refinement bring consistent improvement to data quality"

## [POSITIVE] Refinement Procedures for Generated Data
Human-defined filters applied to raw LLM responses: removing negative responses, rewriting unnatural narratives, detecting and fixing logical reasoning errors and hallucinations using scene graph ground truth

**Delta**: Counting: 78.0 → 100.0; Existence: 93.4 → 100.0; Non-existence: 30.5 → 100.0
**Condition**: Quality control of LLM-generated 3D VL data

**Evidence**: "Results in Tab. 2 demonstrate that our proposed scene-graph-based prompting, O-CoT prompting and refinement bring consistent improvement to data quality and the complete data generation pipeline outperforms a recent counterpart (3DLLM)."

## [POSITIVE] Generalist-style Instruction Tuning (Multi-scene, Multi-task)
Training on diverse scenes (ScanNet + 3RScan) and tasks simultaneously rather than specializing on a single scene or task domain

**Delta**: 3RDialog: 25.5 (ScanNet specialist) vs 73.3 (generalist); 3RPlan: 23.4 vs 81.1
**Condition**: Cross-scene and cross-task generalization

**Evidence**: "ScanNet performs slightly worse than w/o Act even on ScanNet tasks, and particularly struggles at generalization across scenes (3RQA) and tasks (3RDialog and 3RPlan). This demonstrates the advantage of generalist-style instruction tuning with broad coverage of scenes and tasks."

## [NEGATIVE] Including Embodied Acting Tasks in VLA Co-training
Adding navigation and manipulation tasks to the instruction tuning alongside 3D VL tasks

**Delta**: SQA3D: 50.0 (w/o Act) → 46.2 (VLA); 3RDialog: 72.3 vs 73.3; 3RPlan: 77.2 vs 81.1
**Condition**: 3D VL understanding tasks when jointly trained with embodied acting tasks

**Evidence**: "The results in Tab. 7 show that incorporating embodied acting tasks could lead to performance drops on 3D VL tasks. This may stem from 1) the gap between language generation and embodied action prediction, and 2) the imbalanced data scale of embodied acting tasks."

## [POSITIVE] Dialogue and Planning Data Inclusion
Including diverse multi-round dialogue and task planning data in instruction tuning

**Delta**: TrueSkill Unanswerable: 23.1 (w/o Dialg) → 26.8 (w/ Dialg); NLP: 23.4 → 26.6
**Condition**: Response quality, hallucination reduction, and NLP skills

**Evidence**: "The results in Tab. 8 confirm more hallucinations (less preferred by users on 'Unanswerable') and worse NLP skills for w/o Dialg. This is probably because 1) the diverse conversations in our dialogue data can help cultivate flexible responses to complex instructions, and 2) our planning data can offer scene-grounded commonsense knowledge."

## [POSITIVE] Data Balancing / Negative Sample Augmentation
Augmenting training data with negative samples (non-existent object queries) to address class imbalance that causes the model to over-predict 'Yes' answers

**Delta**: 3RScan Overall: 0.34 (w/o Aug) → 0.85 (w/ Aug); ScanNet 0-shot Overall: 0.43 → 0.83
**Condition**: Object-existence question answering; hallucination mitigation

**Evidence**: "Results in Tab. 9 demonstrate that we can effectively mitigate the hallucination problem by balancing the tuning data. Moreover, the benefit of augmenting 3RScan data can transfer to ScanNet scenes in a zero-shot manner."

## [POSITIVE] Scaling Up LLM Size
Using larger pretrained LLMs (OPT-1.3B → Vicuna-7B → Vicuna-13B) as the backbone

**Delta**: Consistent test loss reduction; gap between 7B and 13B less significant than 1.3B to 7B
**Condition**: Instruction tuning loss; diminishing returns at larger scales

**Evidence**: "Scaling up LLM leads to consistent improvements. Aligned Vicuna-7B shows significantly lower losses than Aligned OPT-1.3B. In contrast, despite the consistent improvements, the gap between Aligned Vicuna-7B and Vicuna-13B appears less significant, suggesting potential saturation."

## [POSITIVE] Scaling Up Training Data
Increasing the amount of instruction tuning data following a log-linear scaling law

**Delta**: All curves decrease log-linearly with data scale
**Condition**: All model sizes; instruction tuning test loss

**Evidence**: "The instruction tuning of LEO conforms to the scaling law. We observe that all curves decrease log-linearly with the data scale."

## [POSITIVE] Pretrained LLM Alignment Before Instruction Tuning
Using an LLM that has undergone alignment (Vicuna) versus training from scratch on instruction tuning data

**Delta**: Consistently lower test loss across all data scales
**Condition**: Instruction tuning test loss across all data scales

**Evidence**: "Alignment leads to consistent improvements. Aligned Vicuna-7B shows consistently lower losses than Scratch Vicuna-7B, which corresponds to the inferior performances of w/o Align in Tab. 7."

## [POSITIVE] Discrete Action Tokenization via Reserved Vocabulary Tokens
Continuous actions are discretized and mapped to the least-used tokens in SentencePiece vocabulary, enabling unified text and action generation

**Delta**: LEO achieves comparable or better performance vs CLIPort on manipulation tasks
**Condition**: Robotic manipulation tasks

**Evidence**: "LEO directly produces motor commands without inductive bias (e.g., heatmap) that benefit previous methods, showcasing LEO's considerable capacity for learning embodied actions."

## [POSITIVE] Egocentric 2D Image Encoder (OpenCLIP ConvNext)
A pretrained OpenCLIP ConvNext encoder processes egocentric 2D images to provide embodied viewpoint information alongside the global 3D point cloud representation

**Delta**: outperforms baseline
**Condition**: Navigation and manipulation tasks requiring egocentric perception

**Evidence**: "LEO perceives through an egocentric 2D image encoder for the embodied view and an object-centric 3D point cloud encoder for the third-person global view. Such perception modules can be flexibly adapted to various embodied environments and enhance 3D reasoning."

## [NEUTRAL] Mask3D-based Object Proposals for 3D Input
Using Mask3D instance segmentation to generate object proposals for 3D point cloud inputs instead of ground-truth object segments

**Delta**: Used as standard evaluation protocol following 3D-VisTA
**Condition**: 3D VL evaluation on Scan2Cap, ScanQA, SQA3D

**Evidence**: "Following 3D-VisTA (Zhu et al., 2023c), we use object proposals from Mask3D (Schult et al., 2022) instead of ground-truth object segments for evaluation."

## [NEGATIVE] Truncated Past Actions (No Recurrent Module) in Navigation
LEO uses only truncated past actions as context instead of recurrent modules used by navigation baselines

**Delta**: Lower success rate vs baselines on ObjNav despite better SPL
**Condition**: Object navigation (ObjNav) task success rate

**Evidence**: "Notably, all baselines are equipped with recurrent modules while LEO only incorporates truncated past actions, which could account for a lower success rate."
