# Don’t Go To Extremes: Revealing the Excessive Sensitivity and Calibration Limitations of LLMs in Implicit Hate Speech Detection

**Source**: https://aclanthology.org/2024.acl-long.652/

## [POSITIVE] Logit-based Uncertainty Estimation
Using the token logit probabilities from the decoder as confidence scores for classification predictions, either directly or averaged across multiple inferences.

**Delta**: highest AUC across all datasets and models (e.g., LLaMA-2-7b Latent Hatred AUC=0.637 vs verbal=0.565, consistency=0.589)
**Condition**: AUC metric across all models and datasets; ECE performance varies by scenario

**Evidence**: "The logit-based method performs better in AUC than both the verbal-based method and the consistency-based method in all scenarios."

## [POSITIVE] Verbal-based Confidence Estimation
Inducing LLMs to generate a direct confidence score (0%-100%) alongside their answer.

**Delta**: Best ECE in low-F1, high-token-logit scenario (e.g., LLaMA-2-7b SBIC ECE=0.057 vs consistency=0.103, logit=0.094)
**Condition**: Poor primary classification performance with high model token logits

**Evidence**: "In cases where the performance of the primary classification task is poor and the model's token logit is high (LLaMA-2-7b on the Latent Hatred and SBIC datasets, GPT-3.5-turbo on the Latent Hatred dataset), the verbal-based method achieved nearly the best ECE and BS."

## [POSITIVE] Consistency-based Confidence Estimation
Running the model through n rounds of inference with varied prompt patterns or demonstrations, using the agreement rate across runs as the confidence score.

**Delta**: Best ECE on high-accuracy tasks (e.g., LLaMA-2-7b ToxiGen ECE=0.029 vs verbal=0.181, logit=0.041)
**Condition**: High primary classification accuracy (simple datasets like ToxiGen)

**Evidence**: "In cases where the classification has high accuracy (all models on the ToxiGen dataset), the consistency-based method achieves the best ECE."

## [NEGATIVE] Consistency-based Method Discreteness
The consistency score is limited by the ensemble number, concentrating on a few discrete values (e.g., 3/5, 4/5, 5/5), reducing the number of confidence thresholds.

**Delta**: Lower AUC than logit-based method due to missing ROC curve sections (e.g., absence of confidence scores between 0.8 and 1)
**Condition**: AUC calculation for consistency-based method with small ensemble numbers

**Evidence**: "The discrete points obtained by the consistency-based method on the ROC curve are very close to those on the curve of the logit-based method. However, the absence of a consistency-based confidence score between 0.8 and 1 results in the omission of the corresponding section with an FPR below 0.5."

## [POSITIVE] Increasing Ensemble Number for Consistency Method
Increasing the number of ensemble inferences (changing demonstrations each time) from 3 to 13 to improve confidence score granularity.

**Delta**: AUC gradually increases and stabilizes but remains lower than logit-based method
**Condition**: Consistency-based AUC improvement; does not fully close gap with logit-based method

**Evidence**: "Based on the findings, we increase the ensemble number from 3 to 13 (changing demonstrations in the prompt in each inference to conduct the ensemble), the AUC gradually increases and tends to stabilize (Fig. 4). It indicates that increasing the number of ensemble sources can mitigate the gap but is still lower than the logit-based method."

## [POSITIVE] Chain-of-Thought (CoT) Prompt Pattern
Prompting LLMs to provide a binary response along with a step-by-step explanation simultaneously.

**Delta**: Most balanced precision-recall for LLaMA-2-7b across all three datasets (biases reduced compared to other patterns)
**Condition**: LLaMA-2-7b classification task; reduces over-sensitivity bias

**Evidence**: "Only the CoT pattern demonstrates a relatively balanced performance across all three datasets for LLaMA-2-7b."

## [NEGATIVE] Cloze Test Prompt Pattern
Prompting LLMs to fill in a masked word ('hateful' or 'neutral') in the phrase 'It is a [Mask] statement.'

**Delta**: Largest imbalance for LLaMA-2-7b with biases ranging from 12% to 33% across datasets
**Condition**: LLaMA-2-7b and Mixtral-8x7b classification; increases over-sensitivity

**Evidence**: "In the case of LLaMA-2-7b, the most notable imbalance is observed in the Cloze prompt pattern across all three datasets, with biases ranging from 12% to 33%."

## [NEGATIVE] Multi-task with Target Prompt Pattern
Instructing LLMs to provide a binary response and also identify the targeted individual or group.

**Delta**: Biases of 24% and 14% on Latent Hatred and SBIC datasets for LLaMA-2-7b
**Condition**: LLaMA-2-7b classification on datasets with sensitive groups/topics

**Evidence**: "The Target pattern shows biases of 24% and 14% on the Latent Hatred and SBIC datasets, respectively."

## [POSITIVE] Prompt Pattern Ensemble for Calibration
Aggregating responses from different prompt patterns to form an ensemble confidence estimate.

**Delta**: Relatively better overall calibration performance compared to individual prompt patterns
**Condition**: Calibration task across models and datasets

**Evidence**: "The ensemble of responses obtained from different prompt patterns shows a relatively better overall performance. This may be because different prompt patterns inspire the model to infer results along different paths, and aggregating such results better reflects the model's confidence."

## [NEUTRAL] Few-shot In-Context Learning (6-shot)
Presenting six balanced demonstrations before the test case to guide LLM inference.

**Delta**: No specific quantitative improvement cited; used as standard experimental setup
**Condition**: All classification and calibration experiments

**Evidence**: "We present six demonstrations (i.e., examples) in the prompt for few-shot in-context learning, organized in a balanced class and random order."

## [NEGATIVE] RLHF Safety Optimization
Reinforcement Learning from Human Feedback optimization applied to LLMs to prevent generation of harmful content, leading to over-sensitivity toward sensitive groups.

**Delta**: Recall significantly higher than precision for LLaMA-2-7b and Mixtral-8x7b on Latent Hatred and SBIC (e.g., Mixtral Choice QA: Recall=0.995, Precision=0.5161 on Latent Hatred)
**Condition**: Datasets containing sensitive groups/topics in negative (non-hateful) class examples

**Evidence**: "LLMs display excessive sensitivity on Latent Hatred and SBIC datasets... The presence of sensitive groups and topics confuses LLMs, leading to misjudgment of benign expressions."

## [NEGATIVE] Concentrated Confidence Score Distribution
All three uncertainty estimation methods produce confidence scores concentrated in a fixed range regardless of dataset difficulty, causing calibration to depend heavily on primary classification accuracy.

**Delta**: Poor ability to distinguish correct from incorrect predictions; confidence distributions of correctly and incorrectly classified cases overlap significantly
**Condition**: All three uncertainty estimation methods across all models and datasets

**Evidence**: "No matter whether the dataset is easy or challenging, the confidence scores of each method are always concentrated in a fixed range. Consequently, methods concentrated in low-confidence ranges perform well on challenging tasks, while those concentrated in high-confidence ranges excel in simpler tasks."

## [NEUTRAL] Higher Temperature Sampling
Increasing the temperature parameter to make the logit distribution more or less conservative depending on the model.

**Delta**: LLaMA-2-7b AUC increases (ECE improves from 0.260 to 0.236) while Mixtral-8x7b AUC decreases (ECE worsens from 0.024 to 0.059) as temperature increases from 0.6 to 1
**Condition**: Model-dependent: positive for overconfident models (LLaMA-2-7b), negative for conservative models (Mixtral-8x7b)

**Evidence**: "As the temperature increases, The AUC of LLaMA-2-7b increases while the AUC of Mixtral-8x7b decreases. When the temperature varies between 0.6 and 1, LLaMA-2-7b and Mixtral-8x7b exhibit opposite trends in ECE."

## [POSITIVE] Profanity Word Filtering in Data Preprocessing
Discarding data samples containing explicit profanity words to ensure evaluation focuses on implicit hate speech without explicit hate words.

**Delta**: Ensures evaluation validity for implicit hate speech detection task
**Condition**: Data preprocessing for all three datasets

**Evidence**: "we discard the data samples with profanity words, such as 'bi*ch' and 'fu*k' to further ensure that the data does not contain explicit hate words."

## [NEUTRAL] Balanced Class Sampling
Sampling from the test set to maintain equal numbers of positive and negative class examples.

**Delta**: 1200 test samples for Latent Hatred, 1200 for SBIC, 260 for ToxiGen
**Condition**: All evaluation experiments

**Evidence**: "Secondly, we sample from the test set to keep the equal data number of positive and negative class."

## [NEGATIVE] Sensitive Group/Topic Presence in Benign Examples
The presence of sensitive groups or topics in non-hateful statements causes LLMs to misclassify them as hate speech.

**Delta**: Over-sensitivity observed on Latent Hatred and SBIC but not ToxiGen; e.g., Mixtral all prompts show 20-50% bias on Latent Hatred
**Condition**: Datasets where negative class contains sensitive groups/topics (Latent Hatred, SBIC)

**Evidence**: "LLMs display excessive sensitivity on Latent Hatred and SBIC datasets, while it does not exhibit such over-sensitivity on the ToxiGen dataset. That is because examples of the negative class in the dataset Latent Hatred and SBIC contain sensitive groups or sensitive topics."
