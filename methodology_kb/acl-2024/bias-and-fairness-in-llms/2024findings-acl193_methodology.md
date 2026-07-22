# Likelihood-based Mitigation of Evaluation Bias in Large Language Models

**Source**: https://aclanthology.org/2024.findings-acl.193/

## [NEUTRAL] Likelihood Bias Quantification (BiasScore)
A metric that measures likelihood bias in LLM-based evaluators by computing Spearman's rank correlation between Likelihood Score (log probability of output) and Unfairness Score (difference between LLM and human scores) across a dataset.

**Delta**: BiasScore ranges from -1 to 1; GPT-3.5 shows 0.38 (D2T) and 0.43 (GEC) before mitigation
**Condition**: Applied to both GPT-3.5 and Llama2-13B on data-to-text and GEC tasks

**Evidence**: "BiasScore is then our metric that measures likelihood bias, which is calculated as the correlation in terms of Spearman's rank correlation coefficient ρ between Likelihood Score and Unfairness Score across a Dataset D"

## [POSITIVE] Highly-Biased Instance Selection for Few-Shot Examples
Bias mitigation method that selects the most biased instances (highest RS(t) score, representing top-right and bottom-left points in LS vs US scatter plot) from training data as few-shot examples for in-context learning, replacing LLM scores with human gold-standard scores.

**Delta**: +0.10 total evaluation performance for GPT-3.5 on D2T; +0.14 fluency for GPT-3.5; BiasScore reduced from 0.20 to 0.00 for Llama2-13B fluency on D2T
**Condition**: Applied to both GPT-3.5 and Llama2-13B on data-to-text and GEC tasks; most effective on data-to-text

**Evidence**: "our proposed method successfully mitigates this bias, also improving evaluation performance (in terms of correlation of models with human scores) significantly"

## [POSITIVE] In-Context Learning for LLM Evaluation Stabilization
Using few-shot examples in the prompt for LLM-based evaluation to stabilize model outputs. Eight examples are used, chosen randomly when measuring bias and by bias-based selection when mitigating bias.

**Delta**: described as stabilizing the model; enables quantification of likelihood bias strength
**Condition**: Used in both bias measurement and mitigation phases; 8 examples chosen

**Evidence**: "The reason we use in-context learning is that it is known to stabilize the model. This puts us in a position to quantify the strength of likelihood bias."

## [POSITIVE] Expected Score Calculation (Probability-Weighted Scoring)
Computing evaluation score as the expected value over candidate scores (e.g., {1,2,3,4,5}) weighted by the model's output probability for each score, rather than taking the most likely score.

**Delta**: leads to more robust evaluation (qualitative)
**Condition**: Applied to all LLM-based evaluation scoring

**Evidence**: "we calculate Scorem as the expected score over scores. We follow the setting of Liu et al. (2023), who have observed that using the expected score, considering the model's distribution over scores for each instance, rather than always taking the most likely score, leads to a more robust evaluation."

## [NEUTRAL] Contextual Likelihood Calculation
Computing the likelihood of task output conditioned on both task description and task input (rather than unconditional log probability), to obtain a more contextually relevant likelihood score.

**Delta**: not quantified separately
**Condition**: Used for likelihood score computation in both data-to-text and GEC tasks

**Evidence**: "we calculate the likelihood of task output to based on task description d and task input ti. This approach aims to obtain a more contextually relevant likelihood, factoring in both the specifics of the task and the input, rather than simply calculating log P(to; θ)."

## [NEGATIVE] Non-Intrinsic Evaluation Criteria Susceptibility to Likelihood Bias
Observation/design finding that evaluation criteria dependent on external input factors (e.g., relevance, data coverage) exhibit significantly higher likelihood bias than intrinsic criteria (e.g., fluency, text structure) that assess output quality alone.

**Delta**: Relevance BiasScore: GPT-3.5=0.43, Llama2-13B=0.28; Data coverage: GPT-3.5=0.40, Llama2-13B=0.24; vs Fluency: GPT-3.5=0.26, Llama2-13B=0.20
**Condition**: Observed on data-to-text task with WebNLG+ dataset; non-intrinsic criteria include relevance and data coverage

**Evidence**: "there is a marked difference in BiasScore between non-intrinsic and intrinsic criteria: non-intrinsic criteria are much more prone to bias."

## [NEUTRAL] Llama2-13B Likelihood as Proxy for GPT-3.5
Using Llama2-13B's token generation likelihood as an approximation for GPT-3.5's likelihood, since GPT-3.5 does not support output of token generation likelihood via API.

**Delta**: not quantified
**Condition**: Applied only when computing likelihood scores for GPT-3.5-based evaluator

**Evidence**: "For GPT-3.5, since it does not support the output of token generation likelihood, we use Llama2-13B's likelihood as an approximation."

## [NEUTRAL] Score Normalization for Unfairness Score
Normalizing both LLM scores and human scores to have the same mean and range before computing the Unfairness Score, to account for different scoring ranges between models and humans.

**Delta**: not quantified separately
**Condition**: Applied during bias measurement across all tasks and models

**Evidence**: "To account for different scoring ranges between models and humans, Scorem and Scoreh are normalized so that they have the same mean and range."

## [POSITIVE] Bias Mitigation on Fluency Criterion (Intrinsic)
Applying the highly-biased few-shot selection method to intrinsic criteria like fluency, which already have lower baseline bias.

**Delta**: Llama2-13B fluency BiasScore: -0.20 (from 0.20 to 0.00); GPT-3.5 fluency evaluation performance: +0.14
**Condition**: Data-to-text task, fluency criterion

**Evidence**: "the BiasScore decrease significantly for Llama2-13B for text structure (-0.15), fluency (-0.20), and correctness (-0.20)... the evaluation performance improves significantly for GPT-3.5 by +0.10 for total, by +0.14 for fluency"

## [POSITIVE] Bias Mitigation on GEC Task
Applying the highly-biased few-shot selection method to the GEC task, which has fewer criteria and different characteristics than data-to-text.

**Delta**: BiasScore changes in right direction but few criteria achieve statistical significance; total evaluation performance: GPT-3.5 0.45→0.52, Llama2-13B 0.48→0.52
**Condition**: GEC task with grammar and fluency criteria

**Evidence**: "Although few criteria achieve significant differences either in BiasScore or evaluation performance, our method at least shows changes in the right direction."
