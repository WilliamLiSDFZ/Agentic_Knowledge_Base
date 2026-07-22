# Subtle Biases Need Subtler Measures: Dual Metrics for Evaluating Representative and Affinity Bias in Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.23/

## [POSITIVE] Representative Bias Score (RBS)
A metric that measures representative bias in LLM outputs by computing the standard deviation of average cosine similarity differences between identity-prompted outputs and default outputs across all tasks and identities within an axis.

**Delta**: Mixtral RBS: Race=0.014, Gender=0.036, Orientation=0.038; GPT-4 RBS: Race=0.023, Gender=0.026, Orientation=0.049; LLaMA-2 RBS: Race=0.0413, Gender=0.043, Orientation=0.055
**Condition**: Applied to GPT-4, LLaMA-2, and Mixtral across race, gender, and sexual orientation axes in creative generation tasks

**Evidence**: "RBS insights are summarized in Table 1a, with Mixtral showcasing the lowest RBS, highlighting its broader inclusivity in content generation."

## [POSITIVE] Affinity Bias Score (ABS)
A metric that measures evaluative preference bias in LLMs by computing the standard deviation of proportions of outputs selected as 'best' for each identity group within an axis.

**Delta**: Mixtral ABS: Race=0.0819, Gender=0.059, Orientation=0.002; GPT-4 ABS: Race=0.203, Gender=0.171, Orientation=0.190; LLaMA-2 ABS: Race=0.133, Gender=0.061, Orientation=0.155
**Condition**: Applied when LLMs act as evaluators selecting preferred outputs across identity groups in creative tasks

**Evidence**: "Mixtral stands out in having the most uniform evaluative patterns, as demonstrated by its balanced radar plot. Table 1b corroborates this through its lowest ABS, indicating a fairer evaluative process relative to the other models."

## [POSITIVE] Creativity-Oriented Generation Suite (CoGS)
A benchmark suite of 12 open-ended creative tasks (e.g., short story, poetry, haiku, dance choreography) with customized rubrics, 30 themes, and identity-specific prompts across 3 axes, yielding 3,240 total prompts.

**Delta**: 3,240 prompts total (360 default + 2,880 identity-specific)
**Condition**: Used as the primary evaluation framework for measuring subtle biases in LLMs

**Evidence**: "Our contributions are threefold: Creation of the 'Creativity-Oriented Generation Suite,' comprising 12 diverse open-ended tasks for content creation, ranging from short stories to haikus, complete with customized evaluation rubrics and a variety of themes for comprehensive analysis."

## [POSITIVE] Semantic Similarity-Based Representative Bias Measurement
Using a sentence embedding model (all-mpnet-base-v2) to convert LLM outputs into vector embeddings and computing cosine similarity between identity-prompted and default outputs to quantify representational deviation.

**Delta**: Revealed systematic leaning towards 'white', 'man', and 'straight' identities across all models
**Condition**: Applied to outputs from GPT-4, LLaMA-2, and Mixtral across all CoGS tasks

**Evidence**: "To address this, we adopt a semantic similarity-based approach to measure the extent of representative bias in LLM outputs... Figure 4 features the semantic similarity of LLM-generated content with default responses, uncovering a systematic leaning towards 'white', 'man', and 'straight' identities across all models."

## [POSITIVE] Identity Prompt Framing
Framing identity prompts as 'You possess an inherent comprehension of being [identity group]. While not centering or emphasizing this theme...' to induce diverse responses without overtly emphasizing identity.

**Delta**: Preliminary tests confirmed effectiveness
**Condition**: Used across all 12 CoGS tasks for all identity groups

**Evidence**: "Prompts were derived from CoGS, with identity prompts framed as 'You possess an inherent comprehension of being [identity group]...' to induce diverse responses without emphasizing the identity. Preliminary tests confirmed the effectiveness of this approach."

## [NEUTRAL] Low Temperature Setting (0.2)
Setting generation temperature to 0.2 to prioritize near-deterministic responses while retaining a small degree of variability.

**Delta**: Same evaluative preference conclusions across temperatures 0, 0.25, 0.5, 0.75, and 1
**Condition**: Applied during generation of responses to all 3,240 CoGS prompts

**Evidence**: "The preliminary analysis was done across both higher and lower temperatures for a sample of 500 problem instances. It was found that the evaluative preferences led to the same conclusions for all temperature settings... As a result, the temperature of 0.2 was selected for this research work because a degree of stability (but not full determinism) in the results was desired."

## [POSITIVE] LLM-as-Evaluator for Affinity Bias
Using an LLM (GPT-4, LLaMA-2, or Mixtral) as an evaluator to select the 'best' output from a set of identity-prompted outputs given a task rubric, to measure evaluative affinity bias.

**Delta**: Revealed distinct 'bias fingerprints': GPT-4 favors white/straight/man; LLaMA-2 favors black/queer/female; Mixtral most balanced
**Condition**: Applied when each of the three LLMs acts as an evaluator over outputs generated by all three models

**Evidence**: "The affinity biases of LLMs towards different identity groups are shown in Figure 5. Here, GPT-4's bias towards 'white', 'straight', and 'man' is evident, reflecting a significant evaluative preference. In contrast, LLaMA-2's preferences align oppositely, favoring 'black', 'queer', and 'female', marking a distinct evaluative pattern from GPT-4."

## [NEUTRAL] Human Evaluator Comparison
Having three NLP graduate evaluators assess 50 instances of the 'very short story' task to compare human affinity bias patterns with LLM evaluator patterns.

**Delta**: Fleiss Kappa: race κ=0.0426 (slight agreement), gender κ=−0.0466 (disagreement), sexual orientation κ=−0.0113 (disagreement)
**Condition**: Applied only to the 'very short story' task subset of 50 instances

**Evidence**: "Fifty instances from the 'very short story' task were evaluated by three NLP graduates with a strong linguistics background. Disparities in evaluator consensus, as quantified by Fleiss Kappa, underscored the subjective nature of bias perception."

## [POSITIVE] Task-Specific Rubric Evaluation
Using customized, task-specific evaluation rubrics (e.g., imagery, tone, message, uniqueness, symbolism for short poems) to guide LLM evaluators in selecting preferred outputs.

**Delta**: Enabled detection of task-specific biases, e.g., Mixtral's affinity for Asian identity in haiku task
**Condition**: Applied across all 12 CoGS tasks with distinct rubrics per task

**Evidence**: "Task-specific biases also occurred, aligning with societal stereotypes related to identities and their assumed strengths, exemplified by Mixtral's affinity bias for Asian identity in 'haiku' task (short-form poetry intrinsically linked to Japan)."

## [POSITIVE] Mixtral Architecture/Training for Bias Mitigation
Mixtral's training paradigm appears to encourage balanced identity representation, resulting in lower RBS and ABS scores compared to GPT-4 and LLaMA-2.

**Delta**: Lowest RBS (Race=0.014, Gender=0.036, Orientation=0.038) and lowest ABS (Race=0.0819, Gender=0.059, Orientation=0.002) among all tested models
**Condition**: Observed across representative and affinity bias measurements in CoGS tasks

**Evidence**: "Mixtral showcasing the lowest RBS, highlighting its broader inclusivity in content generation... This pattern may suggest that Mixtral's training paradigm encourages balance without favoring a specific identity."

## [POSITIVE] Perceptibility-Level Qualitative Categorization
Categorizing LLM outputs into three levels—imperceptible (no identity cues), nuanced (subtle identity indicators), and obvious (explicit identity mention)—to qualitatively analyze how identity is represented.

**Delta**: Revealed spectrum of identity marker visibility not captured by quantitative metrics alone
**Condition**: Applied as a qualitative complement to RBS/ABS quantitative analysis

**Evidence**: "We categorize LLM outputs into three levels based on the perceptibility of identity group markers: imperceptible, where identity cues are absent; nuanced, where identity is subtly indicated; and obvious, where identity is explicitly mentioned."

## [POSITIVE] ANOVA and T-test Statistical Significance Testing
Using ANOVA for identity axes with three categories and T-tests for axes with two categories to determine statistical significance of bias scores at p<0.05.

**Delta**: Identified statistically significant biases marked with asterisk (*) in Table 1
**Condition**: Applied to RBS and ABS scores across all models and identity axes

**Evidence**: "Statistically significant differences, marked by an asterisk (*), were identified using ANOVA for identity axes with three categories (e.g., asian, black, white) and T-tests for those with two (e.g., straight vs. queer), with significance set at a p-value below 0.05."

## [NEUTRAL] LLaMA-2 Racial Bias Anomaly
LLaMA-2 deviates from the white-identity default pattern seen in other models, instead favoring 'black' and 'asian' identities in representative bias, possibly due to diverse training data or bias-mitigation architecture.

**Delta**: LLaMA-2 RBS for race=0.0413 favoring black identity vs. GPT-4 and Mixtral favoring white
**Condition**: Observed specifically in the race identity axis for representative bias measurement

**Evidence**: "Interestingly, LLaMA-2 presents an anomaly in racial preferences, favoring 'black' and 'asian' identities over 'white', a deviation possibly reflecting its diverse training data or architecture aimed at mitigating racial bias."
