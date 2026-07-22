# Unveiling Selection Biases: Exploring Order and Token Sensitivity in Large Language Models

**Source**: https://aclanthology.org/2024.findings-acl.333/

## [NEUTRAL] Token Sensitivity Measurement
Reversing option symbols (e.g., A,B,C,D → D,C,B,A) while keeping content fixed to measure how LLMs respond to different token labels

**Delta**: Fluctuation rates vary by model and task
**Condition**: Across all models and tasks in zero-shot setting

**Evidence**: "In powerful LLMs, PaLM 2, Gemini Pro, and GPT3.5, we observe a notable trend: they are more sensitive to option order than to symbols/tokens in 17 out of 18 cases."

## [NEGATIVE] Order Sensitivity Measurement
Reversing the order of option content while keeping symbols coupled to content, to measure sensitivity to option positioning

**Delta**: Higher fluctuation rates than token sensitivity in 17/18 cases for powerful LLMs
**Condition**: Primarily for commercial LLMs (PaLM 2, Gemini Pro, GPT-3.5)

**Evidence**: "In powerful LLMs, PaLM 2, Gemini Pro, and GPT3.5, we observe a notable trend: they are more sensitive to option order than to symbols/tokens in 17 out of 18 cases."

## [NEGATIVE] Both Sensitivity Setting
Rearranging option content order while also reversing symbol assignments, combining token and order sensitivity effects

**Delta**: Most pronounced combined influence in 11 out of 18 cases
**Condition**: When token and order biases are directionally aligned

**Evidence**: "In both sensitivity setting, which examines the joint effects of token and order sensitivities, we find that in 11 out of 18 cases, the combined influence is the most pronounced."

## [POSITIVE] Gray-Box Probability Weighting
Combining token probabilities from forward and backward requests by weighting the probability of each option content across both symbol arrangements

**Delta**: Improvements across all 6 tasks and 3 sensitivity settings for GPT-3.5; e.g., +2.36 ARC, +1.20 HellaSwag, +2.23 MMLU, +2.21 Winogrande, +3.02 MathQA, +3.10 OpenBookQA
**Condition**: Gray-box scenario (GPT-3.5) where token log probabilities are accessible

**Evidence**: "the probability weighting method demonstrates considerable enhancements in all scenarios, surpassing the baseline. It benefits not only more challenging tasks such as MathQA, Winogrande, and MMLU but also shows improvements in easier tasks."

## [POSITIVE] Gray-Box Probability Calibration
Dividing raw token selection probabilities by observed output distribution frequencies computed on a validation set to reduce systematic option preference biases

**Delta**: Outperforms weighting on Winogrande (+4.85) and MathQA (+9.72) for GPT-3.5; over 78% of MMLU subtasks improved
**Condition**: Gray-box scenario; particularly effective for tasks with unusual numbers of options (2 options like Winogrande, 5 options like MathQA)

**Evidence**: "the probability calibration method outperforms the weighting method in two specific tasks out of the six: Winogrande and MathQA... Regarding the probability calibration method, on average, more than 78% of the subtasks improved with our approach, with over 30% of them having at least a 1% increase in accuracy."

## [POSITIVE] Black-Box Two-Hop Strategy
Using the model's output distribution to identify the most biased option symbol and selectively choosing responses from the backward request to avoid biased selections

**Delta**: Stronger models (PaLM 2, Gemini Pro) improved in 5/6 tasks; GPT-3.5 improved in 4/6 tasks; LLaMA 2 models improved in ~half of tasks
**Condition**: Black-box scenario where only generated text is accessible; less effective for smaller models and specific tasks like Winogrande and MathQA

**Evidence**: "the stronger models, PaLM 2 and Gemini Pro, show significant benefits from the two-hop strategy. They improved in five out of six tasks, with Winogrande being the only exception. Similarly, GPT-3.5 also shows improvements in most tasks, succeeding in four out of six."

## [NEGATIVE] Two-Hop Strategy on Winogrande
Applying the black-box two-hop strategy to the Winogrande dataset (2-option cloze-test format)

**Delta**: All models show reduced performance; e.g., PaLM 2: -0.95 (token), -1.50 (order), -5.80 (both); GPT-3.5: -0.47 (token), -3.35 (order), -5.25 (both)
**Condition**: Winogrande task specifically, which has only 2 options and uses cloze-test format

**Evidence**: "a noteworthy observation is that all models, regardless of their capability, exhibit reduced performance on the Winogrande task after applying our two-hop strategy... We hypothesize that the limited number of options or the specific task type might alter the LLM's preference distribution, impacting the efficacy of our black-box strategy."

## [NEUTRAL] Zero-Shot Setting
Conducting all experiments without in-context demonstrations to isolate selection biases from few-shot demonstration biases

**Delta**: Enables cleaner measurement of selection biases
**Condition**: All experiments in this study

**Evidence**: "It is crucial to highlight that our analysis centers on the zero-shot setting. This choice distinguishes our work from previous endeavors, which predominantly concentrate on few-shot settings, making it difficult to disentangle biases stemming from in-context demonstrations."

## [NEGATIVE] Task Difficulty vs. Sensitivity Correlation
Observation that harder tasks (lower accuracy) exhibit higher fluctuation rates, indicating greater model sensitivity

**Delta**: Strong negative correlation (e.g., PaLM 2 Both: slope=-0.77, R²=0.80; Gemini Pro Both: slope=-1.01, R²=0.86; GPT-3.5 Both: slope=-0.51, R²=0.76)
**Condition**: Primarily for stronger models (PaLM 2, Gemini Pro, GPT-3.5, LLaMA 2 70B); weaker models (7B, 13B) show muted trends

**Evidence**: "Results from PaLM 2, Gemini Pro, GPT-3.5, and LLaMA 2 70B appear to support our hypothesis: more challenging tasks, characterized by lower accuracy, tend to exhibit greater sensitivity, as indicated by higher fluctuation rates."

## [POSITIVE] Model Scaling for Sensitivity Trends
Increasing LLaMA 2 model size from 7B to 70B to observe emergence of expected difficulty-sensitivity correlation

**Delta**: LLaMA 2 70B shows predicted correlation across all settings; 7B and 13B show inconsistent or reversed trends
**Condition**: Open-source LLaMA 2 model family

**Evidence**: "a closer analysis of the 7B, 13B, and 70B models reveals a gradual manifestation of the expected trend... With further increases in model size, the 70B model exhibits the predicted correlation between task difficulty and model sensitivity across all examined settings."

## [NEGATIVE] Option C/B Preference Bias
LLMs (except LLaMA2-7B) systematically prefer options B or C over the ground truth distribution

**Delta**: E.g., on ARC: ground truth C=26.52%, but PaLM 2 selects C=28.69%, Gemini Pro C=29.10%, GPT-3.5 C=30.18%, LLaMA2-13B C=43.44%, LLaMA2-70B C=41.67%
**Condition**: Across most datasets and models; LLaMA2-7B is an exception showing extreme bias toward option A (57.39% on ARC)

**Evidence**: "most models, except for LLaMA2-7B, exhibit a notable bias towards option C compared to the ground truth proportion... Generally, most models, except for LLaMA2-7B, show a bias towards options B or C."

## [POSITIVE] Probability Calibration on STEM Subtasks
Applying probability calibration specifically to STEM-related MMLU subtasks

**Delta**: Elementary mathematics +14.29%, high school mathematics +12.22%, college physics +11.27%, college chemistry +7.00% in both setting
**Condition**: STEM-related MMLU subtasks under probability calibration gray-box method

**Evidence**: "STEM-related tasks showing the most substantial gains. For instance, in the both setting, the top beneficiaries include elementary mathematics, high school mathematics, college physics, and college chemistry, with improvements of 14.29%, 12.22%, 11.27%, and 7.00%, respectively"

## [POSITIVE] Cost-Efficient Two-Request Design
Limiting mitigation strategies to only two requests per question (forward and backward) rather than multiple permutations or chain-of-thought voting

**Delta**: Total experiment cost under $400 USD covering six models and six benchmarks
**Condition**: All proposed mitigation methods

**Evidence**: "Our method prioritizes cost-effectiveness by minimizing the need for numerous permutations or voting on costly chain-of-thought (CoT) candidates. For the probability weighting method, each question q needs two requests to calculate the weighted probability... the total expense for all experiments conducted in this study was under $400 USD"
