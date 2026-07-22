# Benchmarking Cognitive Biases in Large Language Models as Evaluators

**Source**: https://aclanthology.org/2024.findings-acl.29/

## [NEUTRAL] Pairwise Evaluation Framework
Prompting each LLM evaluator to compare two anonymized model responses in a pairwise manner, running each instance twice in both orderings to validate consistent behavior

**Delta**: 5250 examples per evaluator across 16 models
**Condition**: Used as the core evaluation methodology across all bias benchmarks

**Evidence**: "We generate all (15 choose 2) unique pairs amongst all models for each of the 50 instructions, creating a total of 5250 examples for each evaluator to rank. We then prompt the evaluator to compare generations based on the coherence of each of the responses in terms of correctness of content and alignment to the instruction/reference provided."

## [NEUTRAL] Random Baseline Threshold
Empirically calculating a bias threshold via random selection to distinguish established bias patterns from random selection behavior

**Delta**: Random threshold ~0.24-0.25 for most biases, 0.5 for salience
**Condition**: Applied across all six bias benchmarks as a baseline comparison

**Evidence**: "We empirically calculate a 'bias threshold' via random selection. For example, in the ORDER benchmark, each pair is evaluated twice in which both orderings are viewed... We make this assumption to serve as a 'litmus test' in distinguishing established patterns with respect to 'bias/unbiased' evaluations by automatic evaluators rather than just random selection when models are noticeably above or below this threshold."

## [NEGATIVE] Order Bias Benchmarking
Testing whether LLM evaluators favor responses based on their presentation order by prompting both orderings of each pair and counting first-order or last-order preferences

**Delta**: 11/15 models drawn toward first- or last-ordered response; >50% first-order preference in >40B size group
**Condition**: Implicit bias; observed across all model sizes, particularly strong in >40B parameter models

**Evidence**: "For the ORDER BIAS benchmark in Table 2, we observe that most models (11/15) tend to be drawn towards either the first- or last-ordered model in each of the pairwise comparisons. Notably, within the second size group (>40B), the first-ordered system was strongly favored in over 50%."

## [NEGATIVE] Compassion Fade (Naming) Bias Benchmarking
Measuring whether model evaluations are affected by real/identifiable model names versus anonymous aliases by comparing evaluation consistency between named and anonymized conditions

**Delta**: All models dramatically influenced by real model names; KOALA sees 100% increase in self-preference with real names
**Condition**: Implicit bias; affects all tested models, with KOALA showing extreme sensitivity

**Evidence**: "We see in Table 2 that all models are dramatically influenced by real model names. Although this phenomenon may be akin to injecting random names, the disparity between ORDER and COMPASSION FADE results support our hypothesis that recognizable names influence evaluations in contrast to anonymized ones."

## [NEGATIVE] Egocentric Bias Benchmarking
Measuring whether LLM evaluators prefer their own generated responses over other models' responses regardless of quality

**Delta**: >50% self-preference for largest models and KOALA; GPT-4 egocentric score 0.78 vs random 0.24
**Condition**: Implicit bias; most pronounced in largest models (>100B) and KOALA; INSTRUCTGPT is an exception

**Evidence**: "For EGOCENTRIC BIAS, in the anonymized aliases, the largest models as well as KOALA tend to prefer their own responses (>50%) with the exception of INSTRUCTGPT."

## [NEGATIVE] Salience (Length) Bias Benchmarking
Examining whether evaluators systematically favor longer or shorter responses by analyzing token length of preferred responses

**Delta**: Larger models more strongly affected by longer responses; ChatGPT salience score 0.63 vs random 0.5
**Condition**: Implicit bias; more pronounced in larger models (>40B); smaller models less affected

**Evidence**: "For SALIENCE BIAS, we observe that the larger models in the first and second size groups are more strongly affected by longer responses, which align with findings from other works. However, smaller models (excluding MPT) tend to be less influenced by the length of the responses."

## [NEGATIVE] Bandwagon Effect Benchmarking
Testing whether evaluators follow fake majority statistics by adding a sentence claiming a certain percentage of people preferred one response (e.g., '85% believe System Star is better')

**Delta**: 11/15 models influenced with >70% of evaluations following bandwagon preference; ChatGPT 0.86, InstructGPT 0.85
**Condition**: Induced bias; affects nearly all models; GPT-4 is a notable exception with 0.0 score

**Evidence**: "For BANDWAGON EFFECT, we observe that almost all models (11/15) are heavily influenced in which >70% of evaluations on average followed the bandwagon preference regardless of text quality. Although we only included a simple fake statistic (e.g. '85% of people preferred System Star'), we see that evaluators can be heavily influenced by this external information."

## [NEGATIVE] Attentional Bias Benchmarking
Testing evaluator robustness by including irrelevant information about one comparand model (e.g., 'System Star likes to eat oranges and apples') to measure distraction effects

**Delta**: >80% of evaluations distracted for >10B size group; API-based models (ChatGPT, Cohere) more robust
**Condition**: Induced bias; most severe for >10B open-source models; API-based models show more robustness

**Evidence**: "For ATTENTIONAL BIAS, we see that around half of the models' rankings are influenced by irrelevant information. Specifically, we see that models in the third size group (>10B) were the most strongly impacted by the distracting information, with >80% of evaluations being counted as distracted. On the other hand, API-based models such as CHATGPT and COHERE remained robust against these distractions."

## [NEGATIVE] Rank-Biased Overlap (RBO) for Human-Machine Agreement
Using RBO score to measure agreement between human preferences and model evaluation rankings, weighting top-k positions more heavily

**Delta**: Average RBO of 0.44 between human and machine preferences; human inter-annotator RBO 0.54
**Condition**: Applied to compare 16 LLM evaluators against 6 human annotators across 13-model ranking task

**Evidence**: "We calculate the average RBO between human and model preferences to be 0.44, indicating that model evaluations do not closely align with human preferences... any pairwise RBO between two annotators is higher than the average agreement between humans and models (0.44)."

## [NEGATIVE] Model Size Scaling for Bias Reduction
Examining whether increasing model parameter count reduces cognitive biases in LLM evaluators

**Delta**: Models <10B most affected; implicit biases contribute similarly regardless of size; average RBO for <10B is 0.37 vs 0.49 for >40B
**Condition**: Observed across all six bias benchmarks; scaling helps somewhat with human alignment but not implicit biases

**Evidence**: "On average, we see that models within the 10B size range are most affected by each bias benchmark in Fig. 2a. Notably, we see that the implicit biases contribute similarly to each models' overall bias scores, indicating that scaling model size does not reduce implicit biases in evaluators."

## [NEGATIVE] Listwise Ranking Evaluation
Conducting list-wise ranking among 4 models as an alternative to pairwise comparison

**Delta**: Most LLMs <40B unable to generate valid rankings
**Condition**: Applied as supplementary evaluation; fails for smaller models due to task complexity

**Evidence**: "Additionally, we conduct a list-wise ranking amongst 4 models. However, we find that most LLMs of size <40B have trouble generating a valid list of rankings (Appendix B) due to increased task complexity."

## [NEUTRAL] Diverse Multi-Aspect Evaluation Prompting
Extending evaluation prompts to include multiple quality dimensions (coherence, accuracy, factuality, helpfulness) instead of single-aspect evaluation

**Delta**: Some metrics become more pronounced (COHERE egocentric increases), some decrease (VICUNA egocentric decreases), but overall bias proportions remain consistent
**Condition**: Tested on ORDER benchmark as supplementary experiment; does not substantially change bias findings

**Evidence**: "We see that by including diverse perspectives in the evaluation setting, some metrics become more pronounced (i.e. COHERE for EGOCENTRIC) or bias decreases (i.e. VICUNA for EGOCENTRIC). However, we see that the proportion of biased evaluations stays relatively consistent for most models on all benchmarks."

## [NEGATIVE] Tie Option in Pairwise Prompting
Adding a 'tie' option to pairwise evaluation prompts to allow evaluators to indicate equal quality between responses

**Delta**: Mid-range models (ALPACA, VICUNA) and INSTRUCTGPT assign tie >=90% of the time, producing invalid results; only COHERE showed improvement
**Condition**: Tested as supplementary experiment; strongest and smallest models unaffected, mid-range models collapse to tie responses

**Evidence**: "We see that the mid-range models (ALPACA, VICUNA) and INSTRUCTGPT display a large preference for assigning the tie label (≥~90%) that does not present any valid results, to which we had originally only prompted two options for each evaluator to avoid this issue. The only model that demonstrated an improvement from previous bias behavior was COHERE."

## [POSITIVE] Hierarchical Bias Rubric for Confound Mitigation
Applying a priority ordering among biases during analysis so that if an evaluation shows order bias, it is excluded from salience or egocentric bias counting

**Delta**: Helps isolate individual bias effects by preventing double-counting
**Condition**: Applied specifically to decouple egocentric and salience bias measurements

**Evidence**: "We employ various strategies to mitigate these confounding variables and isolate each analysis as much as possible. For example, we employ a 'hierarchical' rubric, where some biases take priority in an evaluation. Specifically, if an evaluation shows signs of order bias by choosing A in (A first, then B) and B in (B first, then A), we do not evaluate it for SALIENCE or EGOCENTRIC bias."

## [NEUTRAL] BERTScore for Generation Quality Decoupling
Using reference-based BERTScore to measure generation quality across models to determine whether egocentric or salience biases are driven by actual quality differences

**Delta**: All models produce nearly same quality (F1 ~0.81 to 0.86), confirming biases are not quality-driven
**Condition**: Used as supplementary analysis to validate that egocentric and salience biases are genuine artifacts

**Evidence**: "We compute the generation quality using reference-based metrics via BERTScore. From this, all models produce nearly the same quality of generations with respect to the reference answer ~(0.81 to 0.86 for F1), highlighting that identifying EGOCENTRIC or SALIENCE bias is most likely not dependent on generation quality."

## [NEUTRAL] Bandwagon Percentage Variation Testing
Testing bandwagon effect with different fake statistics (0%, random 50-85%, and 85%) to measure correlation between stated percentage and evaluator compliance

**Delta**: Most models show correlated change with percentage; VICUNA unaffected by percentage value (0%: 0.79, 85%: 0.81)
**Condition**: Supplementary experiment run on representative models from each size range plus all API-based models

**Evidence**: "Here, one can observe that the preference choices for the bandwagon statistic greatly change (besides GPT4 and VICUNA) which suggests that indeed the biased tendency is correlated with the bandwagon statistic. However, we see that VICUNA, in particular, is not greatly affected by the statistics. This suggests that within the prompt, the model only focuses on the phrase 'people believe that {model} is better' instead of the statistic."
