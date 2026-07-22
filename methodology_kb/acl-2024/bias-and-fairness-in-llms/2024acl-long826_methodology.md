# Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement

**Source**: https://aclanthology.org/2024.acl-long.826/

## [NEGATIVE] Iterative Self-Refinement Pipeline
LLM generates output, then generates feedback on its own output, then refines based on that feedback, iterating multiple times. Refinement is only accepted if self-feedback score improves.

**Delta**: Bias increases from 8.06 to 14.6 (GPT-4), 19.6 to 21.9 (GPT-3.5-Turbo), 9.62 to 17.6 (Gemini) over 10 iterations at Yor-En
**Condition**: Machine translation, constrained text generation, and mathematical reasoning tasks across all six LLMs tested

**Evidence**: "our findings suggest that the primary reason for the amplification of bias during self-refine iteration is that actual performance does not improve through iterations. Instead, GPT-4 and Gemini mistakenly perceive performance improvements in their refined outputs."

## [NEGATIVE] Self-Bias Amplification via Self-Rewarding Pipeline
Using the same LLM as a reward model to rank k candidate responses, then training on top-performing samples. Larger sample sizes increase bias amplification.

**Delta**: LLaMA2-7B bias increases from 8.75 (k=1) to 20.9 (k=32); MixtralMOE from 12.4 to 18.5; DeepSeekMOE from 14.8 to 18.5
**Condition**: Self-rewarding pipeline on Yoruba-to-English translation with open-source LLMs (DeepSeekMOE, MixtralMOE, LLaMA2-7B)

**Evidence**: "we observed that all LLMs displayed an increase in bias and distance skewness as the sample size increased. Notably, selecting samples from a larger pool, e.g. a sample size of 32, significantly increases this bias compared to selections from a smaller pool, such as a sample size of 4."

## [POSITIVE] External Feedback with Accurate Assessment (InstructScore)
Using a reference-based external feedback model (InstructScore) instead of self-feedback to provide fine-grained error annotations including error location, severity label, and error type.

**Delta**: All LLMs with external feedback show consistent BLEURT improvements across self-refine iterations; bias curves for external feedback remain below self-feedback curves
**Condition**: Yoruba-to-English translation task with GPT-4, GPT-3.5-Turbo, and Gemini over 5 refinement steps

**Evidence**: "we demonstrate that external feedback with accurate assessment can significantly lower the model's bias at iterative refinement... Most importantly, we demonstrate that all LLMs with external feedback can elicit their self-correction ability with consistent BLEURT improvements at self-refine iterations."

## [POSITIVE] Larger Model Size
Using larger parameter LLMs (e.g., LLaMA2-70B vs 7B/13B) in the self-refinement pipeline to reduce self-bias.

**Delta**: LLaMA2-70B self-bias plateaus after 5th iteration, while 7B and 13B models continue to amplify self-bias in later iterations
**Condition**: LLaMA2 7B, 13B, and 70B on Yoruba-to-English translation task across self-refinement steps

**Evidence**: "LLMs with larger parameter size can have less self-bias throughout self-refinement steps... while the LLaMA2-70B model exhibits self-bias in the earlier iterations, its self-bias begins to plateau after the 5th iteration. In contrast, the 7B and 13B models continue to amplify their self-bias in later iterations."

## [POSITIVE] Self-Refinement for Fluency and Understandability
Iterative self-refinement improves surface-level text qualities such as fluency and understandability as measured by UniEval, even when task-specific quality does not improve.

**Delta**: Consistent improvements in fluency and understandability scores across all iterations for GPT-4, GPT-3.5-Turbo, and Gemini
**Condition**: Yoruba-to-English translation task measured by UniEval fluency and understandability dimensions

**Evidence**: "GPT-4, GPT-3.5-Turbo, and Gemini consistently exhibit improvements in both fluency and understandability. This suggests an alternative perspective on the self-refine pipeline, indicating that while an LLM may not strictly adhere to instruction-following in terms of quality improvements, it can still improve certain intrinsic text qualities, such as fluency and understandability."

## [NEGATIVE] Self-Refinement for Task-Specific Quality
Using self-feedback to improve task-specific quality metrics such as translation quality (BLEURT/MQM) or concept coverage in constrained text generation.

**Delta**: Human scores show no measurable improvement: GPT-4 human score -15.0 at 0th vs -15.1 at 10th iteration; GPT-3.5-Turbo -22.2 vs -21.9; Gemini -17.3 vs -18.3
**Condition**: Machine translation (Yor-En) and constrained text generation tasks across GPT-4, GPT-3.5-Turbo, and Gemini

**Evidence**: "Our human score indicates that all three LLMs have not received measurable improvements via the self-refine pipeline... the rate of LLM's self-estimated improvements is much higher than the true coverage improvements, which leads to self-bias amplification."

## [POSITIVE] In-Context Learning (ICL) for Feedback Format Control
Providing three in-context examples to control the output format of LLM self-feedback annotations.

**Delta**: All LLMs achieve 93-100% format accuracy at 1st iteration and 93-100% at 5th iteration
**Condition**: Self-feedback format accuracy across six LLMs (Gemini, GPT-3.5, GPT-4, LLaMA2, Mixtral, DeepSeekMOE) at Yor-En translation

**Evidence**: "We observed that all LLMs have either perfect or nearly perfect format at first and fifth iteration of self-feedback. This is expected as we explicitly provide three in-context examples to control the output format."

## [NEGATIVE] LLM Style-Preference Paraphrasing Bias
LLMs paraphrase external translations into their own style, causing them to subsequently rate those paraphrased outputs higher regardless of actual quality change.

**Delta**: After paraphrasing, all LLMs (GPT-4, GPT-3.5-Turbo, Gemini) showed increased bias against their paraphrased outputs; GPT-4 and Gemini shifted from negative self-bias to positive self-bias
**Condition**: Yoruba-to-English translations from Madlad400-10b paraphrased by GPT-4, GPT-3.5-Turbo, and Gemini

**Evidence**: "after paraphrasing, all LLMs showed an increased bias against their paraphrased outputs. This is mainly attributed to a decline in quality performance post-paraphrasing, with LLMs erroneously perceiving these paraphrased outputs as indicative of improvements."

## [NEGATIVE] Self-Consistency as Evaluator in Self-Refinement
Replacing self-evaluation with self-consistency verification: generating 10 additional reasoning paths and using majority vote to decide whether to replace the initial answer.

**Delta**: All LLMs (GPT-4, GPT-3.5-Turbo, Gemini) exhibit increase in bias and skewness estimation across iterative self-consistency steps
**Condition**: Mathematical reasoning (MATH dataset) with GPT-4, GPT-3.5-Turbo, and Gemini

**Evidence**: "Figure 11 illustrates that all large language models (LLMs) exhibit an increase in bias and skewness estimation in the iterative self-consistency pipeline. This suggests that LLMs introduce self-biases towards certain reasoning paths during self-refine, ultimately leading to a biased ensemble across multiple reasoning paths."

## [NEUTRAL] Quantile Mapping for Score Alignment
Transforming BLEURT scores to align with MQM human annotation scale (-25 to 0) using quantile mapping learned from WMT22 shared metric task data (28,125 pairs).

**Delta**: Enables direct comparison between automatic metric and human annotation scales
**Condition**: Machine translation evaluation; used as a methodological preprocessing step throughout all translation experiments

**Evidence**: "we employ quantile mapping (Cannon et al., 2015) to transform the BLEURT score into the distribution of human scores. This method involves learning a mapping function that maps the quantiles or percentiles of the predictive distribution to those of the observed distribution."

## [NEUTRAL] MQM-Based Feedback Prompting
Using feedback prompts based on MQM human annotation schema, requiring LLMs to output error location, error type, and severity labels with scores of -1 for minor and -5 for major errors.

**Delta**: Provides structured feedback format consistent with human annotation; enables bias computation on same scale
**Condition**: Machine translation self-feedback evaluation across all LLMs on Flores-200 dataset

**Evidence**: "we utilized feedback prompts based on the MQM human annotation from Freitag et al. (2021), as in Kocmi and Federmann (2023). LLMs will input source text and candidate text and output feedback, including error location, error type, and severity labels."

## [POSITIVE] Stronger Instruction-Following LLMs (GPT-4, Gemini) vs Weaker LLMs
Using more capable instruction-following models (GPT-4, Gemini) compared to open-source or weaker models (GPT-3.5, LLaMA2, Mixtral, DeepSeek) in self-refinement.

**Delta**: GPT-4 and Gemini exhibit lower self-bias than open-source LLMs and GPT-3.5-Turbo throughout iterations
**Condition**: Machine translation on Flores-200 across four language pairs (Yor-En, Jav-En, Arm-En, Ig-En)

**Evidence**: "open-source LLMs and GPT-3.5-Turbo tend to exhibit higher levels of self-bias throughout iterations than stronger instruction-following LLMs, such as GPT-4 and Gemini. This suggests that GPT-4 and Gemini possess a certain level of capability in resisting self-bias."

## [NEUTRAL] Low-to-Medium Resource Language Pair Selection
Focusing evaluation on low-to-medium resource language pairs (Yoruba, Javanese, Armenian, Igbo to English) rather than high-resource pairs.

**Delta**: Ensures room for improvement exists; high-resource pairs like Chinese-English already near human-level for GPT-4
**Condition**: Machine translation experimental design choice for Flores-200 evaluation

**Evidence**: "We concentrate on low-to-medium resource language pairs, as Kocmi et al. (2023) indicate that LLMs like GPT-4 already perform at a nearly human-like level in high resource language pairs such as Chinese-to-English, leaving limited potential for further improvement through self-refine."

## [POSITIVE] Two-Statistic Self-Bias Quantification (Bias + Distance Skewness)
Using both statistical bias (mean difference between LLM and true quality scores) and distance skewness (asymmetry of error distribution) together to measure self-bias, since bias=0 does not guarantee symmetric distribution.

**Delta**: Captures cases where bias=0 but distribution is asymmetric; provides more complete characterization of self-bias
**Condition**: Methodological design choice applied across all tasks and LLMs

**Evidence**: "Bias(θ̂) = 0 does not guarantee a symmetric distribution (one tail could be long and thin, while the other is short and fat, yet they balance out overall). Therefore, we introduce another meta-metric, distance skewness, to measure the asymmetry of E[θ̂] − θ's distribution."
