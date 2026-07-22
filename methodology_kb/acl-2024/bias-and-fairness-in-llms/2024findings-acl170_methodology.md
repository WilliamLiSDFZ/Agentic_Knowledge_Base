# Self-Supervised Position Debiasing for Large Language Models

**Source**: https://aclanthology.org/2024.findings-acl.170/

## [POSITIVE] Self-Supervised Position Debiasing (SOD) Framework
A three-module framework that uses unsupervised responses from pre-trained LLMs for debiasing without external knowledge: low-bias inference, objective alignment, and multi-objective optimization.

**Delta**: +1% to +2% ROUGE-L on non-biased datasets compared to FT and baselines
**Condition**: Applied across eight datasets and five NLP tasks (CQA, CQG, summarization, KGC, NLI) for mitigating lead bias, relative position bias, and lexical bias

**Evidence**: "SOD improves the performance on the non-biased dataset by 1% to 2% on almost all tasks, compared to FT and all baselines. The reason is that SOD can leverage unsupervised responses with low position bias for optimization in multi-objective optimization module."

## [POSITIVE] Objective Alignment Module (OAM)
A pruning module that filters low-quality unsupervised responses using non-compliant identification, dull identification, incoherent identification, and unreliable identification strategies to align debiasing objective with task objective.

**Delta**: SOD outperforms SOD w/o OAM on non-biased datasets; e.g., CQG CoQAR non-biased: 18.8 vs 18.0
**Condition**: Applied when unsupervised responses are noisy or low-quality; particularly important for tasks excluding NLI

**Evidence**: "SOD outperforms SOD w/o OAM on non-biased datasets by leveraging OAM for enhancing the response quality. Poor-quality responses will undermine the model comprehension of the task, thus leading to worse performance."

## [POSITIVE] Low-Bias Inference Module
Uses pre-trained LLMs (before task-specific fine-tuning) to generate unsupervised responses with lower position bias, leveraging the inherent robustness of pre-trained models to position bias.

**Delta**: Pre-trained T5 ROUGE-L fluctuates within 0.2 to 0.4 across almost all relative positions vs fine-tuned model showing 80% improvement concentrated on biased positions
**Condition**: Applied during the response collection phase before fine-tuning; effectiveness depends on the pre-trained model's inherent low-bias characteristics

**Evidence**: "the ROUGE-L score of pre-trained T5 fluctuates within the range of 0.2 to 0.4 across almost all relative positions, demonstrating its robustness against position bias."

## [POSITIVE] Multi-Objective Optimization
Fine-tunes LLMs by jointly optimizing a task objective (NLL loss on target responses) and a debiasing objective (NLL loss on aligned unsupervised responses) with a tradeoff hyperparameter alpha.

**Delta**: SOD performances of CQA on CoQAR all exceed 52.5% using various alpha, while FT only achieves 52.0%
**Condition**: Applied during fine-tuning; robust across different alpha values (0.1 to 0.5)

**Evidence**: "SOD always outperforms FT under various alpha. As shown in Fig. 3, SOD performances of CQA on CoQAR all exceed 52.5% using various alpha, while FT only achieves 52.0%. This demonstrates the effectiveness and robustness of SOD in mitigating position bias."

## [NEGATIVE] Increasing Alpha (Debiasing Objective Weight)
Increasing the weight alpha of the debiasing objective relative to the task objective in multi-objective optimization.

**Delta**: ROUGE-L drops from 53.6% to 52.7% when increasing alpha from 0.1 to 0.5 on CQA CoQAR
**Condition**: Observed on CQA CoQAR non-biased dataset; increasing alpha beyond optimal hurts quality while reducing bias

**Evidence**: "the performance of SOD drops with the increase of the weight of unsupervised responses in multi-objective optimization. In CQA on CoQAR, the ROUGE-L score of SOD drops from 53.6% to 52.7% when increasing alpha from 0.1 to 0.5."

## [NEGATIVE] Fine-Tuning on Biased Dataset (Standard FT)
Standard fine-tuning of LLMs on task-specific datasets without any debiasing mechanism.

**Delta**: 34.7% improvement on biased CoQAR vs only 8.6% improvement on non-biased CoQAR
**Condition**: Applied to CoQAR CQA task; demonstrates the position bias problem that SOD aims to solve

**Evidence**: "FT achieves 34.7% improvement on the biased dataset of CoQAR, but 8.6% improvement on the non-biased dataset. This is because LLMs can easily overfit the shortcut of the training dataset in fine-tuning."

## [NEGATIVE] Random Position Perturbation (RP)
Randomly perturbs input positions during training to reduce the model's dependence on token positions in prediction.

**Delta**: RP drops 3.6% on biased Newsroom vs SOD only drops 0.2% compared to FT
**Condition**: Applied on Newsroom summarization; achieves comparable non-biased performance but at greater cost to biased performance

**Evidence**: "RP achieves comparable performance to SOD on the non-biased dataset of Newsroom. However, the ROUGE-L of RP drops 3.6% compared to FT on the biased dataset, while that of SOD only drops 0.2%. This is because the perturbation in RP impairs the overall data quality for fine-tuning."

## [NEGATIVE] Using Unsupervised Responses Without OAM (w/o OAM)
Using raw unsupervised responses from pre-trained LLMs for the debiasing objective without any quality filtering or alignment.

**Delta**: CQG CoQAR non-biased: 18.0 vs 18.8 for SOD with OAM; Mutual non-biased: 36.7 vs 53.0 for SOD with OAM
**Condition**: Observed across language understanding, creation, and compression tasks; particularly severe on Mutual KGC dataset

**Evidence**: "lower response quality leads to worse performance... SOD outperforms SOD w/o OAM on non-biased datasets by leveraging OAM for enhancing the response quality."

## [NEGATIVE] Using Unsupervised Responses from Different LLM (T5-base or T5-xlarge)
Generating unsupervised responses using a different-sized LLM (FlanT5-base or FlanT5-xlarge) instead of the same model being fine-tuned (FlanT5-large).

**Delta**: SOD w/ T5-base and SOD w/ T5-xlarge perform worse than SOD on CANARD but still outperform FT
**Condition**: Observed on CANARD CQG; using mismatched model amplifies divergence between task and debiasing objectives

**Evidence**: "SOD w/ T5-base and SOD w/ T5-xlarge perform worse than SOD on CANARD, but still outperform FT. We infer that responses from other LLMs use different knowledge/parameters for generation, which mismatch with that of T5."

## [POSITIVE] Instruction-Only Prompting for Low-Bias Inference
Generating unsupervised responses by feeding only task input and task instruction to the pre-trained LLM, without demonstrations.

**Delta**: outperforms baseline
**Condition**: Applied for CQA, KGC, and summarization tasks where input length constraints are a concern

**Evidence**: "Instruction-only prompting generates responses of target task by feeding the task input and task instruction to the pre-trained LLMs... instruction-only prompting is implemented for CQA, KGC, and summarization."

## [POSITIVE] Diverse Prompting for Low-Bias Inference
Generating responses with diverse aspects by feeding various prompts to LLMs to capture different perspectives.

**Delta**: outperforms baseline
**Condition**: Applied specifically for CQG task due to its creative and diverse nature

**Evidence**: "Diverse prompting generates responses with diverse aspects by feeding various prompts to LLMs... We employ diverse prompting for CQG, which is intrinsically creative and diverse."

## [POSITIVE] In-Context Learning (ICL) for Low-Bias Inference
Feeding multiple input-output examples along with task instruction to LLMs for generating unsupervised responses, enhancing model comprehension of target tasks.

**Delta**: outperforms baseline
**Condition**: Applied only for NLI task due to model input length constraints

**Evidence**: "In-context learning (ICL) also feeds multiple input-output examples to LLMs for generation, in addition to the task instruction and input. It enhances the model comprehension of target tasks but requires a longer input length. We adopt ICL only for NLI, due to the limit of the model input length."

## [POSITIVE] NLI Probability Distribution Masking (Target Class Masking)
For NLI tasks, aligning unsupervised responses by masking the target class in the estimated probability distribution to prevent redundancy and avoid strengthening position bias.

**Delta**: SOD achieves 88.4% non-biased on SNLI vs 88.0% for FT and 87.4% for SOD w/o OAM
**Condition**: Applied specifically for NLI tasks (SNLI, QNLI) where output is deterministic classification

**Evidence**: "The estimated probability distributions are low-quality sometimes when the target class dominates, which is redundant for optimizing the task objective and strengthens position bias. Therefore, we align the estimated probability distribution by masking the target class."

## [POSITIVE] SOD Under Low-Resource Settings
Applying SOD framework with varying numbers of training samples (50 to 1,000) to test robustness in low-resource scenarios.

**Delta**: SOD consistently outperforms FT across all training sample sizes from 50 to 1,000
**Condition**: Tested on CoQAR (CQA), CANARD (CQG), Mutual, and QNLI with 50-1000 training samples

**Evidence**: "our proposed SOD outperforms FT under various low-resource settings. As shown in Fig. 4, the ROUGE-L scores of SOD depicted by the orange bars are consistently higher than those of FT in blue. This is because there are always around 40% aligned unsupervised responses for fine-tuning regardless of the variation in the number of training samples."

## [POSITIVE] Incoherent Response Identification
Identifies and removes incoherent unsupervised responses where the perplexity of any token falls below a pre-defined threshold (0.1, 0.15, or 0.2), selecting the threshold that maintains approximately 20% unsupervised responses.

**Delta**: contributes to OAM improvement; SOD w/o OAM shows degraded performance
**Condition**: Applied for CQG task as part of the OAM module

**Evidence**: "Incoherent identification identifies incoherent responses if the perplexity of any token in the response falls below a pre-defined threshold... We set the pre-defined thresholds for incoherent identification and unreliable identification from 0.1, 0.15 and 0.2 and select the one that maintains approximately 20% unsupervised responses."

## [POSITIVE] Unreliable Response Identification
Identifies and removes unsupervised responses where the overlap score between unsupervised and target responses falls below a threshold, ensuring factual alignment.

**Delta**: contributes to OAM improvement; SOD w/o OAM shows degraded performance
**Condition**: Applied for CQA, summarization, and KGC tasks where facts in responses are semantically unique

**Evidence**: "Unreliable identification identifies unreliable responses if the overlap score between unsupervised and target responses is less than a pre-defined threshold. The intuition is that the fact in the response may be wrong if its semantics deviate significantly from the fact in the reference."
