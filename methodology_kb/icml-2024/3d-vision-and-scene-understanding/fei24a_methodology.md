# Video-of-Thought: Step-by-Step Video Reasoning from Perception to Cognition

**Source**: https://proceedings.mlr.press/v235/fei24a.html

## [POSITIVE] Video-of-Thought (VoT) Reasoning Framework
A five-step Chain-of-Thought reasoning framework that decomposes complex video QA into sub-problems: target identification, object tracking, action analysis, answer ranking, and answer verification, progressing from low-level pixel perception to high-level cognitive interpretation.

**Delta**: outperforms baseline
**Condition**: Complex video QA benchmarks requiring intricate reasoning (VLEP, STAR, IntentQA, Social-IQ, CausalVidQA, NExT-QA) in both fine-tuning and zero-shot settings

**Evidence**: "observing the MotionEpic under CoT and our proposed VoT, we see there are huge performance gaps in between consistently on all reasoning scenarios and tasks, indicating the great potential of our proposed video reasoning framework."

## [POSITIVE] Spatial-Temporal Scene Graph (STSG) Integration
Integrating video STSG representation into the MLLM, encoding structured graph representations of subject-predicate-object triplets across video frames with temporal coreference edges to model fine-grained spatial-temporal semantics.

**Delta**: outperforms baseline
**Condition**: Video QA tasks requiring fine-grained spatial-temporal understanding

**Evidence**: "by comparing Video-LLaVA without/with STSG integration, we notice that the structural fine-grained STSG features play a positive role in understanding videos."

## [POSITIVE] Implicit vs. Explicit STSG Integration
MotionEpic implicitly integrates STSG features through grounding-aware tuning, allowing STSG-free inference, compared to Video-LLaVA+STSG which explicitly integrates STSG features.

**Delta**: outperforms baseline
**Condition**: When comparing MotionEpic vs. Video-LLaVA+STSG under the same CoT setting

**Evidence**: "by comparing Video-LLaVA+STSG with our MotionEpic under the same CoT, it is clear that the implicit integration of the scene graph features is quite superior to the explicit integration."

## [NEUTRAL] Vanilla CoT Prompting for Video
Applying standard Chain-of-Thought prompting ('Let's think step by step') to video MLLMs without task-specific decomposition.

**Delta**: limited improvement
**Condition**: Fine-tuning setting on complex video QA benchmarks

**Evidence**: "by observing Video-LLaVA without/with CoT prompting, we see that the improvement from CoT for video reasoning could be quite limited."

## [POSITIVE] CoT in Zero-shot Setting
Applying Chain-of-Thought prompting in zero-shot inference without in-domain training data.

**Delta**: outperforms direct prompting
**Condition**: Zero-shot video QA setting

**Evidence**: "CoT exhibits stronger improvements than direct prompting methods under the zero-shot scenario, compared with the scenario of the above fine-tuning."

## [POSITIVE] Grounding-aware Tuning Objective L2 (Full STSG Generation)
Training objective where given a video, the model generates the whole STSG expression of the video.

**Delta**: largest degradation when removed
**Condition**: Zero-shot end task performance on ActivityNet and NExT-QA

**Evidence**: "the lack of L2 and L4 result in the greatest degradation. This is intuitive, as these two objectives are directly associated with the subsequent reasoning process, i.e., understanding STSG from video, and generating (partial) STSG given objects."

## [POSITIVE] Grounding-aware Tuning Objective L4 (Object-to-Tracklet Generation)
Training objective where given a video and key object(s), the model describes temporal actions and outputs corresponding object tracklets.

**Delta**: largest degradation when removed
**Condition**: Zero-shot end task performance on ActivityNet and NExT-QA

**Evidence**: "the lack of L2 and L4 result in the greatest degradation. This is intuitive, as these two objectives are directly associated with the subsequent reasoning process, i.e., understanding STSG from video, and generating (partial) STSG given objects."

## [POSITIVE] Grounding-aware Tuning Objective L1 (Video-STSG Pairing)
Training objective predicting if the overall input video and STSG are paired.

**Delta**: smaller degradation than L2/L4 when removed
**Condition**: Zero-shot end task performance; less impactful than L2 and L4

**Evidence**: "different items come with varied impacts, indicating the importance of video-STSG grounding finetuning."

## [POSITIVE] Grounding-aware Tuning Objective L3 (Action-to-Tracklet)
Training objective where given a video and action descriptions, the model outputs corresponding object tracklets as partial STSG.

**Delta**: smaller degradation than L2/L4 when removed
**Condition**: Zero-shot end task performance

**Evidence**: "different items come with varied impacts, indicating the importance of video-STSG grounding finetuning."

## [POSITIVE] Grounding-aware Tuning Objective L5 (BBox-to-Tracklet)
Training objective where given a video and a bounding box of a certain frame's object, the model outputs the object label and corresponding tracklet.

**Delta**: smaller degradation than L2/L4 when removed
**Condition**: Zero-shot end task performance

**Evidence**: "different items come with varied impacts, indicating the importance of video-STSG grounding finetuning."

## [POSITIVE] Answer Verification via Pixel Grounding (Step 5)
Verification step that checks if the proposed answer aligns with pixel grounding information from the video from a perception standpoint.

**Delta**: performance drops when removed (w/o Verify-G)
**Condition**: More crucial for simpler perceptive tasks (MSR-VTT, ActivityNet); also important for complex video QA

**Evidence**: "on MSR-VTT and ActivityNet, the perceptive-level pixel grounding verification is more crucial than the commonsense cognitive verification. For those complex videos, both types of verifications are pivotal."

## [POSITIVE] Answer Verification via Commonsense Cognition (Step 5)
Verification step that checks if the commonsense implications of the proposed answer contradict the main observations inferred in the action analysis step.

**Delta**: performance drops when removed (w/o Verify-C)
**Condition**: More crucial for complex video QA tasks requiring cognitive reasoning

**Evidence**: "For those complex videos, both types of verifications are pivotal."

## [POSITIVE] STSG-based Object Tracking for Hallucination Mitigation
Using STSG semantic representation for object tracking and pixel grounding instead of directly tracking original video frames, to reduce hallucination in MLLMs.

**Delta**: outperforms baseline
**Condition**: Video grounding and tracking steps within the VoT framework

**Evidence**: "object tracking and pixel grounding based on the STSG can effectively mitigate the hallucination issues inherent in existing MLLMs."

## [POSITIVE] Temporal Coreference Edges in STSG
Additional edges in the STSG that link the same objects across consecutive frames with time-persistent edges, mimicking the tracking process.

**Delta**: enhances STSG connectivity
**Condition**: STSG construction for multi-frame video understanding

**Evidence**: "To enhance the connectivity of STSG, we further create a type of temporal coreference edges across each single-frame SG, where the same objects are linked together with time-persistent edges, mimicking the 'tracking' process."

## [POSITIVE] Recurrent Graph Transformer for STSG Encoding
A 6-layer Graph Transformer retrofitted with recurrent propagation to encode multi-frame STSG information, with 768-d hidden sizes and CLIP-based node embeddings.

**Delta**: achieves competitive/human-level grounding performance
**Condition**: STSG parsing on Action Genome test set

**Evidence**: "MotionEpic achieves very competitive performance on par with SoTA parser, even with human-level performance. This reveals that MotionEpic shows reliable capability in providing video grounding information."

## [POSITIVE] LoRA for LLM Fine-tuning
Low-rank adaptation applied to tune a small subset of LLM parameters while keeping the video encoder and backbone LLM frozen during grounding-aware tuning.

**Delta**: enables parameter-efficient tuning
**Condition**: Grounding-aware tuning phase of MotionEpic

**Evidence**: "To tune the LLM, we leverage LoRA to enable a small subset of parameters to be updated."

## [POSITIVE] Video Pre-training on WebVid
Conventional video pre-training on WebVid dataset before grounding-level tuning, serving as a warm-up starting point for video understanding.

**Delta**: important warming start
**Condition**: Pre-training stage before grounding-aware tuning

**Evidence**: "Before conducting the above grounding-level tuning, we perform conventional video pre-training on Webvid, which serves as the important warming starting for the following video understanding tuning."

## [POSITIVE] 8 fps Frame Sampling Rate
Uniformly sampling video frames at 8 fps for fine-grained reasoning, balancing between noise from redundant frames and information loss from too few frames.

**Delta**: best trade-off
**Condition**: Video frame sampling for MotionEpic inference

**Evidence**: "we use the 8 fps, as in our preliminary study we verified that it helps achieve the best trade-off."

## [POSITIVE] Candidate Answer Ranking Mechanism (Step 4)
Scoring each candidate answer on a 1-10 rationality scale using commonsense knowledge and ranking them to select the final answer, inspired by human multi-choice answering patterns.

**Delta**: outperforms baseline
**Condition**: Multiple-choice video QA format in Step 4 of VoT

**Evidence**: "Inspired by the human pattern of answering multi-choice questions, we also consider a ranking mechanism to determine the final answer. Specifically, for each candidate answer, we prompt the model to score its likelihood (from 1 to 10) in conjunction with commonsense knowledge."

## [POSITIVE] VoT on Complex vs. Simple Video Tasks
VoT framework provides larger improvements on complex cognitive video QA tasks compared to simpler perceptive tasks.

**Delta**: larger improvements on complex tasks
**Condition**: Zero-shot setting; complex tasks (NExT-QA, STAR) vs. simpler tasks (MSR-VTT, ActivityNet)

**Evidence**: "The enhancements on these two complex video QA tasks are clearer than those on the comparatively simpler tasks, i.e., MSR-VTT and ActivityNet. This is largely because the latter datasets more tend to perceptive understanding, rather than cognitive understanding."
