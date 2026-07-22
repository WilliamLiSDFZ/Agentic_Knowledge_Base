# Dissecting Human and LLM Preferences

**Source**: https://aclanthology.org/2024.acl-long.99/

## [POSITIVE] Bayesian Logistic Regression for Preference Decomposition
Uses Bayesian logistic regression with Laplace prior to predict preference labels from pairwise comparison features, decomposing overall preferences into quantifiable contributions of each property

**Delta**: ~80% prediction accuracy for most judges
**Condition**: Used across all judges and scenarios for preference dissection

**Evidence**: "We see that the fitted models reach about 80% accuracy for most D_j (Table 10 in Appendix J)."

## [POSITIVE] 10-fold Cross-validation Aggregation for Regression Stability
Divides data into 10 parts, using 9 for fitting in each iteration and averaging results to reduce instability

**Delta**: None
**Condition**: Applied during Bayesian logistic regression fitting

**Evidence**: "To reduce instability in fitting, we divide the data into 10 parts, using 9 for fitting in each iteration. The final weights α are the average of the results from 10 iterations."

## [POSITIVE] MCMC with No-U-Turn Sampler
Uses No-U-Turn Sampler with Hamiltonian Monte Carlo collecting 6,000 posterior samples across four independent MCMC chains for approximate Bayesian inference

**Delta**: None
**Condition**: Used for fitting Bayesian logistic regression models

**Evidence**: "We perform approximate Bayesian inference with the No-U-Turn Sampler (Hoffman et al., 2014) with Hamiltonian Monte Carlo (Neal et al., 2011) to collect 6,000 posterior samples across four independent Markov Chain Monte Carlo (MCMC) chains"

## [POSITIVE] Scenario-balanced Sampling
Samples data with balanced distribution across different scenarios to avoid mixing of preferences and achieve clearer conclusions

**Delta**: None
**Condition**: Applied during dataset construction from Chatbot Arena Conversations

**Evidence**: "We notice that preferences of different scenarios vary a lot, so we take a scenario-balanced sampling... we separately fit individual models for subsets with different scenarios (or meet certain Query-specific prerequisites) in each D_j"

## [POSITIVE] Positional Bias Mitigation via Response Order Alternation
Alternates response order and averages log-probabilities to counteract LLM positional bias in preference assessment

**Delta**: None
**Condition**: Applied when collecting LLM preference labels

**Evidence**: "Acknowledging a positional bias in LLMs (Wang et al., 2023), where they prefer either the first or second response irrespective of content, we alternate response order and average log-probabilities for an accurate preference rating."

## [POSITIVE] Simplified Preference Elicitation Prompt
Uses a minimal prompt measuring preferences by output log-probability of 'A' or 'B' to minimize prompt bias

**Delta**: None
**Condition**: Used for collecting LLM preference labels across 32 LLMs

**Evidence**: "To minimize prompt bias in model preference assessment, we use a straightforward one: 'Between Response A and Response B, which better addresses the user's query? The better response is Response', and measure preferences by the output log-probability of 'A' or 'B'."

## [POSITIVE] Two-round Annotation for Query-specific Properties
First round determines if a query meets prerequisites for query-specific properties; second round annotates only applicable properties to improve accuracy

**Delta**: 94.8% agreement on first-round prerequisite questions, 85.5% on second-round annotation
**Condition**: Applied for 5 query-specific properties: clarify intent, show empathetic, satisfy constraints, support stances, correct mistakes

**Evidence**: "Therefore to improve accuracy, we adopt a two-round annotation process. The first round determines if a query meets the prerequisites for these properties... In the second round, annotation focuses only on applicable properties."

## [POSITIVE] Reference Answer Inclusion for Error Detection
Includes a reference answer generated independently by GPT-4-Turbo in the error detection prompt to help identify errors correctly

**Delta**: 85.1% agreement rate for detected errors, with 90% of responses having all errors identified without missing
**Condition**: Applied during error detection annotation

**Evidence**: "Additionally, a reference answer generated independently by GPT-4-Turbo is included in the prompt, which has proven to help identify errors correctly (Zheng et al., 2023; Saunders et al., 2022; Sun et al., 2024)."

## [POSITIVE] GPT-4-Turbo Automated Annotation
Uses GPT-4-Turbo to annotate pairs of responses simultaneously in one prompt to maintain consistent annotation standards across 29 properties

**Delta**: 93.1% agreement for Basic property ratings
**Condition**: Used for annotating all 29 properties across the dataset

**Evidence**: "For automated annotation, we employ GPT-4-Turbo to annotate a pair of responses simultaneously in one prompt to keep a consistent standard."

## [POSITIVE] Applicability Tagging for Error Detection
GPT-4-Turbo first evaluates whether it can reliably detect errors in a response before annotating, excluding samples tagged as 'not applicable'

**Delta**: None
**Condition**: Applied during error detection annotation

**Evidence**: "Although GPT-4-Turbo typically identifies errors in most samples accurately, it may fail with content beyond its training data. Therefore, we first ask it to evaluate whether it can reliably detect errors in a response, outputting an 'applicable/not applicable' tag. Samples tagged as 'not applicable' are excluded."

## [POSITIVE] Training-free Preference Alignment via System Messages
Configures system messages to prompt models to adhere to the judge's top 3 preferred properties, boosting benchmark scores without any training

**Delta**: +31.94 on AlpacaEval 2.0 (GPT-4-Turbo model, GPT-3.5-Turbo judge); +0.59 on MT-Bench (GPT-3.5-Turbo model, GPT-3.5-Turbo judge)
**Condition**: Applied to LLaMA-2-70B-Chat, Qwen-72B-Chat, GPT-3.5-Turbo, GPT-4-Turbo on AlpacaEval 2.0 and MT-Bench

**Evidence**: "This results in notable score shifts: up to 0.59 on MT-Bench (1-10 scale) and 31.94 on AlpacaEval 2.0 (0-100 scale), highlighting the significant impact of this strategic adaptation."

## [NEGATIVE] Training-free Preference Divergence via System Messages (Last 3)
Configures system messages to inject the judge's least preferred properties, deliberately lowering benchmark scores

**Delta**: -0.59 on MT-Bench (GPT-3.5-Turbo model, GPT-3.5-Turbo judge); -27.92 on AlpacaEval 2.0 (GPT-4-Turbo model, GPT-4-Turbo judge)
**Condition**: Applied to same models as Top 3 setting; effect more pronounced for GPT-3.5-Turbo judge than GPT-4-Turbo judge

**Evidence**: "aligning a model with the preferences of judges boosts scores, while injecting the least preferred properties lowers them."

## [POSITIVE] DPO Fine-tuning Towards Judge Preferences
Fine-tunes Alpaca models with DPO using preference labels derived from fitted Bayesian logistic regression models of target judges

**Delta**: +0.74 MT-Bench (GPT-3.5-Turbo judge, Alpaca-7B); +10.82 AlpacaEval 2.0 (GPT-3.5-Turbo judge, Alpaca-7B)
**Condition**: Applied to Alpaca-7B and Alpaca-13B; more effective for GPT-3.5-Turbo judge than GPT-4-Turbo judge

**Evidence**: "Training-based: Fine-tuning the model towards/against the preferences via DPO. Alpaca-7B None 5.41 / Towards 6.15 (↑0.74) on MT-Bench GPT-3.5-Turbo; 6.52 / Towards 17.34 (↑10.82) on AlpacaEval 2.0 GPT-3.5-Turbo"

## [NEGATIVE] DPO Fine-tuning Against Judge Preferences (Inverted Labels)
Fine-tunes models with DPO using inverted preference labels from regression models to deliberately lower benchmark scores

**Delta**: -0.95 MT-Bench (GPT-3.5-Turbo judge, Alpaca-7B); -1.02 MT-Bench (GPT-4-Turbo judge, Alpaca-7B)
**Condition**: Applied to Alpaca-7B and Alpaca-13B

**Evidence**: "For training against preferences, we simply invert labels from the regression models. Against 4.46 (↓0.95) / 2.88 (↓1.02) on MT-Bench for Alpaca-7B"

## [POSITIVE] Confidence Threshold Filtering for DPO Training Data
Excludes samples where the final preference probability is within 50±15% to emphasize clear preferences in training data

**Delta**: Resulted in 4,022 samples for GPT-3.5-Turbo and 3,991 for GPT-4-Turbo training
**Condition**: Applied during training-based DPO preference manipulation experiments

**Evidence**: "We exclude samples where the final preference probability is within 50 ± 15% to emphasize the preferences."

## [POSITIVE] Pairwise Comparison over Individual Ratings
Uses pairwise comparison data rather than individual ratings for preference analysis, yielding clearer and more consistent results

**Delta**: None
**Condition**: Core methodological choice for the entire preference dissection framework

**Evidence**: "we analyze preferences using pairwise comparison data, which has clearer and more consistent results than individual ratings (Ziegler et al., 2019)."

## [NEUTRAL] Alignment Fine-tuning (SFT/RLHF/DPO) Effect on Preferences
Fine-tuning pretrained LLMs for alignment does not significantly change their preference tendencies but greatly increases the intensity of expressing preferences

**Delta**: High similarity scores (0.84-0.96) between pretrained and aligned variants; log-probability difference increases from ~0.49-2.24 to ~1.66-7.61
**Condition**: Observed across LLaMA-2, Qwen, Yi, Mistral series at various sizes

**Evidence**: "the preferences tend to remain largely unchanged after fine-tuning for alignment (except for the outlier LLaMA-2-7B), but the difference in log-probability increases a lot. This can be seen as a signal that alignment does not change the tendency of LLM preference, but greatly changes the intensity of expressing it."

## [NEUTRAL] Model Size as Preference Determinant
LLMs of similar sizes exhibit similar preferences regardless of training methods; intra-size-group similarity is higher than inter-size-group similarity

**Delta**: Intra-group similarity 0.83 (<14B) and 0.88 (>30B) vs inter-group similarity 0.74
**Condition**: Observed across all 30 open-source LLMs analyzed

**Evidence**: "We find the intra-group similarities (0.83 for <14B and 0.88 for >30B) are much higher than the inter-group similarity (0.74)... This further suggests that LLMs of similar sizes often have alike preferences, regardless of their training methods."

## [NEGATIVE] Human Sycophancy (Supporting User Stances)
Humans prefer responses that support their subjective stances and show clear dislike when models admit their limits

**Delta**: Humans clearly dislike admit limits especially for Unsafe Query and Communication scenarios
**Condition**: Observed in human preference analysis across real-world Chatbot Arena conversations

**Evidence**: "humans clearly dislike a model when it admits its limit in addressing the query, especially for Unsafe Query and Communication scenarios, indicating that human users in real settings have an urgent desire to have all their queries addressed even if they are unsafe. Humans also prefer responses that support their subjective stances (known as sycophancy)"

## [NEGATIVE] Human Insensitivity to Errors
Humans are significantly less sensitive to errors compared to advanced LLMs, especially for moderate and minor errors

**Delta**: Human preference for no severe errors: 62.86% vs GPT-4-Turbo: 76.19%; Human for no moderate errors: 52.45% vs GPT-4-Turbo: 58.00%
**Condition**: Observed in human preference analysis; average across all scenarios

**Evidence**: "humans are significantly less sensitive to severe errors, and do not show a clear preference/dislike to responses with fewer moderate and minor errors."

## [POSITIVE] Excluding Query from Basic Property Annotation Prompt
Omits the user query from annotation prompts for query-independent basic properties to avoid annotation disturbance

**Delta**: None
**Condition**: Applied during GPT-4-Turbo annotation of 21 basic properties

**Evidence**: "We find that including the query in the prompt disturbs the annotation as most of the basic properties are query-independent. Thus, we only use the query for relevant and novel, the two query-aware ones."

## [POSITIVE] Manipulation Effectiveness Against GPT-3.5-Turbo vs GPT-4-Turbo
Preference manipulation is more effective when targeting GPT-3.5-Turbo as judge compared to GPT-4-Turbo due to less robust inferential abilities

**Delta**: GPT-4-Turbo Top3 vs GPT-3.5-Turbo judge: +31.94 AlpacaEval vs +0.76 AlpacaEval with GPT-4-Turbo judge
**Condition**: Training-free setting on AlpacaEval 2.0 and MT-Bench

**Evidence**: "Compared to GPT-4-Turbo, the effect of adaptation is more noticeable when targeting GPT-3.5-Turbo, possibly due to its less robust inferential abilities."
