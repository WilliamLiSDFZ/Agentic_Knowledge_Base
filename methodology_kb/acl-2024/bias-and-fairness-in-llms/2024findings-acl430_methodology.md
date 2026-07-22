# Debiasing In-Context Learning by Instructing LLMs How to Follow Demonstrations

**Source**: https://aclanthology.org/2024.findings-acl.430/

## [POSITIVE] Semantic Ambiguity Score
A quantitative measure to evaluate the divergence of a demonstration's semantic mode across various contexts, computed by comparing LLM label probabilities under different context orderings using an uninformative demonstration as a control.

**Delta**: descriptive (strong correlation found between ambiguity score and performance variance)
**Condition**: Used as a diagnostic/measurement tool across SST-2, ETHOS, AgNews with Vicuna-13B and LlaMA2-13B-chat

**Evidence**: "our findings revealed a strong correlation between the semantic ambiguity of demonstration and the performance fluctuation of ICL. That is, given a demonstration, as its semantic ambiguity increases, it is more difficult for LLMs to select the correct semantic modes in in-context learning, which in turn leads to greater instability in performance."

## [POSITIVE] Instance-Free Demonstration Reordering
A greedy beam-search-based method that progressively selects and reorders demonstrations by maximizing semantic ambiguity reduction, using label probabilities or entropy as objectives, without requiring access to test instances.

**Delta**: +4-5 accuracy points on IMDB over vanilla ICL baseline; std reduced from 12.95 to as low as 9.79 on IMDB
**Condition**: Applied across six classification datasets with Vicuna-13B; also tested on Vicuna-7B and LlaMA2-13B-chat

**Evidence**: "our demonstration reordering method consistently identifies orderings that achieve optimal performance across different sampled demonstrations. On the IMDB dataset, all three metrics we employed for searching surpass the baseline by an average of 4-5 percentage points across 10 different selections."

## [POSITIVE] Probability-Candidate Metric for Reordering
Selects the next demonstration by maximizing the aggregate probability of all candidate labels (e.g., P('Positive') + P('Negative') for SST-2), optimizing task clarity.

**Delta**: SST-2: 88.98/1.32 vs baseline 87.43/3.26; CR: 79.36/7.50 vs baseline 74.56/11.92
**Condition**: Used as one of three reordering metrics in Instance-Free Demonstration Reordering with Vicuna-13B

**Evidence**: "Reordering with Probability-Candidate: SST-2 88.98/1.32, ETHOS 82.98/1.95, FP 89.70/2.04, IMDB 76.74/10.78, AgNews 77.96/1.77, CR 79.36/7.50 compared to Vanilla ICL baseline."

## [POSITIVE] Probability-Gold Metric for Reordering
Selects the next demonstration by maximizing the probability of the gold label of the upcoming demonstration, choosing demonstrations that maximize the likelihood of the LLM identifying the correct semantic interpretation.

**Delta**: FP: 89.88/1.94 (best accuracy); AgNews: 78.84/1.20 (best accuracy); IMDB: 77.22/10.74 vs baseline 74.09/12.95
**Condition**: Used as one of three reordering metrics in Instance-Free Demonstration Reordering with Vicuna-13B

**Evidence**: "Reordering with Probability-Gold achieves best FP accuracy of 89.88 and best AgNews accuracy of 78.84 compared to Vanilla ICL baseline of 88.47 and 76.22 respectively."

## [POSITIVE] Entropy Metric for Reordering
Selects the next demonstration by minimizing label probability entropy, identifying demonstrations that optimize the model's confidence in selecting semantic modes.

**Delta**: SST-2: 89.56 (best accuracy); ETHOS: 83.78/1.65 (best accuracy); IMDB std: 9.79 (best std reduction)
**Condition**: Used as one of three reordering metrics in Instance-Free Demonstration Reordering with Vicuna-13B

**Evidence**: "Reordering with Entropy achieves best SST-2 accuracy of 89.56 and best ETHOS accuracy of 83.78, and best IMDB std of 9.79 compared to Vanilla ICL baseline of 87.43, 82.03, and 12.95 respectively."

## [POSITIVE] Beam Search for Demonstration Reordering
A beam search strategy preserving top-5 candidate demonstration sets at every step of the reordering search process to mitigate convergence toward local optima.

**Delta**: descriptive (used to mitigate local optima risk)
**Condition**: Applied within Instance-Free Demonstration Reordering method

**Evidence**: "To mitigate the risk of converging toward local optima, we employ a strategy akin to beam search, preserving the top-5 candidate demonstration sets at every step of the search process."

## [POSITIVE] Self-Explanatory In-Context Learning (SE-ICL)
A framework that integrates a self-explanatory instruction into model inputs, prompting LLMs to generate instance-level explanatory guidelines that reflect internal reasoning and decision-making before producing the final answer, without requiring human-annotated explanations.

**Delta**: SST-2: 89.04/1.75 vs baseline 87.43/3.26; ETHOS std: 1.40 (best); AgNews: 78.12/2.42 vs baseline 76.22/5.50
**Condition**: Applied across six classification datasets with Vicuna-13B; extended max output length to 896 tokens

**Evidence**: "our self-explanatory in-context learning framework significantly enhances robustness across all datasets while maintaining competitive or superior performance compared to the baseline. This indicates that by...instructing LLMs in generating self-explanatory guidelines, our methods effectively help LLMs extract correct semantic modes from demonstrations."

## [POSITIVE] OPRO Instruction Optimization for SE-ICL
Uses Optimization by PROmpting (OPRO) to iteratively refine self-explanatory instructions using GPT-3.5-turbo as optimizer and Vicuna-13B as scorer, with 50 optimization steps and 8 new instructions generated per step.

**Delta**: descriptive (enables controllable and effective self-explanatory instruction generation)
**Condition**: Used to optimize instructions for Self-Explanatory ICL framework; SST-2 used as training set

**Evidence**: "To overcome this obstacle and gain better control over the model's generated results, we utilize the Optimization by PROmpting (OPRO, (Yang et al., 2023)) method to refine our instructions, leveraging its effectiveness and versatility in practical scenarios."

## [POSITIVE] Cross-Model Explanation Transfer (Larger to Smaller)
Using explanations generated by a larger LLM to guide a smaller LLM during self-explanatory ICL inference.

**Delta**: LlaMA2-13B with GPT-3.5-turbo explanations: 86.70/3.61 vs LlaMA2-13B vanilla: 79.92/4.14 on AgNews
**Condition**: Applied in AgNews experiments across Vicuna-7B, LlaMA2-13B-chat, and GPT-3.5-turbo

**Evidence**: "integrating insights from larger models significantly enhances the performance of smaller ones, highlighting the invaluable guidance offered by larger LLMs. This enhancement facilitates smaller LLMs in extracting precise semantic modes with greater ease."

## [NEGATIVE] Cross-Model Explanation Transfer (Smaller to Larger)
Using explanations generated by a smaller LLM to guide a larger LLM during self-explanatory ICL inference.

**Delta**: GPT-3.5-turbo with Vicuna-7B explanations: 80.20 vs GPT-3.5-turbo vanilla: 88.60 on AgNews
**Condition**: Applied in AgNews experiments; GPT-3.5-turbo guided by Vicuna-7B explanations

**Evidence**: "smaller language models might misconstrue semantic modes from demonstrations, leading to the formulation of misleading explanatory directives. Such ambiguity consequently leads to a degradation in performance for larger models."

## [NEUTRAL] Uninformative Demonstration Baseline for Ambiguity Measurement
Introducing a dummy demonstration ('None', 'None') as a control context to prevent task-irrelevant semantic modes when computing the semantic ambiguity score.

**Delta**: descriptive (methodological design choice for measurement validity)
**Condition**: Used in semantic ambiguity score computation

**Evidence**: "We initially introduce an uninformative demonstration du = ('None', 'None') to prevent the introduction of task-irrelevant semantic modes."

## [POSITIVE] Semantic Unrelated-Label ICL Setting
Replacing task-related labels with semantically unrelated terms (e.g., 'Positive'→'Foo', 'Negative'→'Bar') to eliminate semantic biases and force LLMs to rely solely on input-to-label mapping learning.

**Delta**: ETHOS: reordering methods improve ~10 percentage points over vanilla baseline (59.06) under unrelated-label setting
**Condition**: Evaluation setting used to test task learning ability on SST-2, ETHOS, AgNews with Vicuna-13B

**Evidence**: "within the ETHOS dataset, our methods improve upon the baseline by approximately 10 percentage points while notably enhancing robustness. This underscores the effectiveness of our approach in enhancing the model's capability in extracting correct semantic modes within demonstrations."

## [NEGATIVE] High Semantic Ambiguity Demonstrations
Using demonstrations with high semantic ambiguity scores (Group 5) in ICL, which can indicate multiple input-to-label mappings.

**Delta**: ETHOS std increases from 1.07 (Group 1) to 5.12 (Group 5) on Vicuna-13B; AgNews Group 5 fluctuates ~30 percentage points on LlaMA2-13B-chat
**Condition**: Observed in semantic ambiguity experiments on Vicuna-13B and LlaMA2-13B-chat across SST-2, ETHOS, AgNews

**Evidence**: "on Vicuna-13B, the standard deviation for the first set in the ETHOS dataset is only 1.07. In contrast, for the fifth set, characterized by a heightened ambiguity score, the deviation significantly increases to 5.12."

## [NEGATIVE] Self-Explanatory ICL on CR Dataset
Applying the self-explanatory ICL framework to the CR sentiment analysis dataset with Vicuna-13B.

**Delta**: CR: 73.00/8.66 vs vanilla baseline 74.56/11.92 (lower mean accuracy, though improved std)
**Condition**: Applied specifically to CR dataset with Vicuna-13B using 4-shot approach

**Evidence**: "Table 1 shows Self-Explanatory ICL achieves 73.00/8.66 on CR compared to Vanilla ICL baseline of 74.56/11.92."
