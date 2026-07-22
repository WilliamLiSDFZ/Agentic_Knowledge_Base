# Teacher-Student Training for Debiasing: General Permutation Debiasing for Large Language Models

**Source**: https://aclanthology.org/2024.findings-acl.81/

## [POSITIVE] Permutation Debiasing (Full Ensemble)
Ensembling predictions across all K! permutations of input options to eliminate permutation sensitivity and positional bias entirely

**Delta**: up to +10% accuracy improvement over biased baseline
**Condition**: All models and tasks tested; most impactful for high-bias models like Llama2

**Evidence**: "Permutation debiasing guarantees zero permutation sensitivity, and applying the method can yield large improvements in performance for many tasks. Even tasks with low permutation sensitivity (e.g. FlanT5 on MCQA) gain small performance boosts, though in settings with high bias one can gain up to 10% in accuracy."

## [POSITIVE] Prior-Matching Debiasing
Introducing scaling weights to normalize LLM probabilities so that the marginal distribution over option labels is uniform, minimizing positional bias

**Delta**: improves accuracy and reduces positional bias but less than full permutation debiasing
**Condition**: Effective for FlanT5-11B on comparative assessment; less effective for Llama2 on MCQA

**Evidence**: "Although in some cases this can significantly improve both sensitivity and accuracy (e.g. FlanT5-11B comparative assessment), for some tasks, permutation sensitivity may remain significant and performance can be substantially worse than permutation debiasing."

## [POSITIVE] Context Prior-Matching
Applying prior-matching over all K! permutations of a specific input to capture input-specific positional bias, rather than global positional bias

**Delta**: performance closely matching permutation debiasing
**Condition**: Requires K! calls so only useful as analysis; not inference-efficient

**Evidence**: "Correcting for this bias yields performance closely matching that of permutation debiasing, highlighting that a positional bias can exist for particular contexts."

## [POSITIVE] Knowledge Distillation Student (Standard)
Training a small encoder-only student model to minimize KL-divergence from the debiased teacher distribution, enabling inference-efficient debiased predictions

**Delta**: outperforms biased teacher on SummEval; e.g. DeBERTa-large distillation achieves 65.1 COH vs biased teacher 61.6
**Condition**: Effective for simpler tasks like comparative assessment (SummEval); insufficient for complex tasks like RACE++

**Evidence**: "For some tasks (e.g. comparative assessment on SummEval) the teacher's abilities can be adequately learned by a smaller student through standard knowledge distillation. The resulting student can achieve performance considerably better than the biased teacher and low permutation sensitivity, all while being considerably more computationally efficient."

## [POSITIVE] Error Correction Student
A student model that takes a single biased teacher sample as additional input and learns to correct it toward the debiased teacher distribution, rather than performing the task from scratch

**Delta**: DeBERTa-large EC achieves 68.1 on RACE++ vs biased teacher 61.2 and debiased teacher 68.3
**Condition**: Particularly effective for complex tasks like RACE++ where pure distillation fails; requires a single black-box LLM call at inference

**Evidence**: "error correction students can effectively leverage a single-biased teacher decision to predict the estimated general debiased distributions. These student systems are more robust to changes in permutations... Note that error correction consistently yields better performance than copying the biased teacher's decision"

## [POSITIVE] Black-Box Monte Carlo Approximation for Training
Using hierarchical Monte Carlo sampling over random permutations to approximate the debiased teacher distribution when white-box access is unavailable

**Delta**: performance saturates at ~32 samples per example
**Condition**: Black-box LLM settings; RACE++ with 4 options analyzed; comparative assessment expected to need fewer samples

**Evidence**: "teacher-student training does not require an excessive number of black-box samples, with performance saturating at 32 samples per example. Interestingly, when using only a few samples, DeBERTa-large can outperform the max-voting performance of the debiased teacher."

## [POSITIVE] Encoder-Only Student Architecture (RoBERTa/DeBERTa)
Using compact encoder-only models (110M or 330M parameters) as student proxies instead of large autoregressive LLMs

**Delta**: 330M parameter student outperforms biased teacher counterparts with significantly fewer parameters
**Condition**: Applies across both RACE++ and SummEval tasks; DeBERTa generally outperforms RoBERTa of equivalent size

**Evidence**: "we demonstrate that our compact, encoder-only student models can outperform their larger, biased teacher counterparts, achieving better results with significantly fewer parameters."

## [POSITIVE] DeBERTa vs RoBERTa Student
Choosing DeBERTa-v3 over RoBERTa as the student backbone architecture

**Delta**: DeBERTa-large EC: 68.1 RACE++ vs RoBERTa-large EC: 68.0; DeBERTa-base EC: 64.1 vs RoBERTa-base EC: 61.4
**Condition**: More pronounced advantage at base size (110M) than large size (330M)

**Evidence**: "As expected, the BERT students were observed to be much weaker than their more modern counterparts (RoBERTa and DeBERTa) of equivalent size."

## [NEGATIVE] BERT/BERT-tiny Student Architecture
Using older BERT-based models as student proxies

**Delta**: BERT-base distillation: 45.6 RACE++ vs RoBERTa-base: 26.7 (distillation) but 58.7 vs 61.4 for error correction
**Condition**: Compared to RoBERTa and DeBERTa of equivalent parameter count

**Evidence**: "the BERT students were observed to be much weaker than their more modern counterparts (RoBERTa and DeBERTa) of equivalent size."

## [NEGATIVE] Pure Distillation on Complex Tasks
Applying standard knowledge distillation (without error correction) to tasks requiring deep comprehension like RACE++

**Delta**: RoBERTa-large distillation: 26.9 RACE++ accuracy vs debiased teacher 68.3
**Condition**: RACE++ multiple choice question answering; all distillation-only students fail on this task

**Evidence**: "For complex tasks (e.g. RACE++) the student is not powerful enough to alone capture the abilities of the teacher."

## [POSITIVE] Instruction Fine-Tuning on Diverse NLP Tasks
Pre-training LLMs with instruction tuning on diverse task sets (e.g. FlanT5 on 1600+ NLP tasks) implicitly imparting permutation invariance for seen task types

**Delta**: FlanT5-3B and FlanT5-11B show permutation sensitivity ~0.09-0.14 on MCQA vs Llama2-7B at 0.65-0.67
**Condition**: Only for task types seen during fine-tuning; does not generalize to unseen task types like comparative assessment

**Evidence**: "FlanT5-3B and FlanT5-11B demonstrate minimal permutation sensitivity for all MCQA tasks, likely due to the additional finetuning of FlanT5 on a variety of tasks including multiple choice question answering exams. This fine-tuning has likely imparted implicit permutation invariance for tasks resembling those encountered during training."

## [NEGATIVE] Task-Specific Implicit Invariance from Fine-Tuning
Relying on supervised fine-tuning to implicitly learn permutation invariance for specific tasks

**Delta**: FlanT5-11B permutation sensitivity jumps from ~0.10-0.21 on MCQA to 0.38-0.44 on SummEval comparative assessment
**Condition**: When applied to task types not seen during fine-tuning

**Evidence**: "when FlanT5-11B is applied to comparative assessment, the system exhibits considerable permutation sensitivity across all attributes of SummEval. This implies that further training on supervised data may mitigate bias and implicitly impart invariances, however, such a solution is task-specific and may not necessarily generalize to tasks seen beyond training."

## [POSITIVE] Appending Biased Prediction to Student Input
For error correction students, concatenating the biased teacher's sampled decision (e.g. 'Prediction: A') to the end of the input prompt

**Delta**: error correction consistently outperforms pure distillation on RACE++; e.g. RoBERTa-base EC 61.4 vs distillation 26.7
**Condition**: Complex tasks like RACE++ where student capacity is insufficient for direct task solving

**Evidence**: "for error correction, we further provide the biased teacher decision by appending text to the end of the input prompt. E.g. If the sampled biased teacher prediction was 'A', then we concatenate Prediction: A to the end of the input text."

## [POSITIVE] Increasing Student Model Size
Scaling student from base (110M) to large (330M) parameters

**Delta**: RoBERTa EC base: 61.4 → large: 68.0 on RACE++; minimal gain on SummEval
**Condition**: Beneficial for complex tasks (RACE++); neutral for simpler tasks (SummEval)

**Evidence**: "Although the size and ability of student can be an important factor when applying the framework (e.g. RACE++), for some tasks the required model complexity can saturate early and a further increase in size/ability does not impact downstream performance."

## [NEGATIVE] Limited Training Data for Student
Training student models with reduced numbers of unlabeled examples

**Delta**: RACE++ requires ~30,000 examples to reach debiased teacher performance; SummEval COH only needs ~2,000
**Condition**: More data needed for complex tasks; simpler tasks saturate quickly

**Evidence**: "The plot shows that the number of samples required before performance saturates varies largely on task complexity. For comparative assessment on SummEval coherency, only 2000 examples are required, while RACE++ requires 30,000 examples before a DeBERTa-large error correction student reaches the debiased teacher performance on RACE++."
