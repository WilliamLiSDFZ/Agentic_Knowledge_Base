# Evaluating Large Language Model Biases in Persona-Steered Generation

**Source**: https://aclanthology.org/2024.findings-acl.586/

## [POSITIVE] RLHF Fine-Tuning
Fine-tuning language models using Reinforcement Learning from Human Feedback to improve instruction-following and alignment

**Delta**: +9.2% average steerability (90.3% vs 81.1% for SFT)
**Condition**: Persona-steered statement generation task across political, race, and gender stances

**Evidence**: "We find that Llama-based models fine-tuned with SFT have an average steerability of 81.1%, compared to 90.3% for models fine-tuned with RLHF and 87.8% for models fine-tuned with DPO."

## [NEGATIVE] RLHF Fine-Tuning (Diversity Cost)
Fine-tuning with RLHF improves steerability but reduces the semantic and entailment diversity of generated outputs

**Delta**: up to -58.2% decrease in semantic diversity
**Condition**: Measured via semantic diversity (SDIV) and entailment diversity (EDIV) metrics over all persona-steered generations

**Evidence**: "Models that we evaluate that are fine-tuned with Reinforcement Learning from Human Feedback (RLHF) are more steerable, especially towards stances associated with political liberals and women, but present significantly less diverse views of personas."

## [POSITIVE] DPO Fine-Tuning
Fine-tuning language models using Direct Preference Optimization as an alternative to RLHF

**Delta**: +6.7% average steerability over SFT (87.8% vs 81.1%)
**Condition**: Persona-steered statement generation task across political, race, and gender stances

**Evidence**: "We find that Llama-based models fine-tuned with SFT have an average steerability of 81.1%, compared to 90.3% for models fine-tuned with RLHF and 87.8% for models fine-tuned with DPO."

## [NEGATIVE] Incongruous Persona Prompting
Prompting models with multifaceted personas where one trait makes the other traits statistically less likely in human survey data (e.g., a political liberal who supports increased military spending)

**Delta**: -9.7% steerability compared to congruous personas
**Condition**: Across all models and all three persona categories (political, race, gender)

**Evidence**: "On average, LLMs are significantly more steerable towards congruous personas than incongruous ones, with an average 9.7% difference in steerability."

## [POSITIVE] Incongruous Persona Prompting (Exaggeration Reduction)
Using incongruous personas reduces demographic exaggeration/caricature in generated text

**Delta**: EXAG score 0.114 for incongruous vs 0.146 for congruous (lower is better)
**Condition**: Measured via exaggeration metric comparing statements to default-demographic and default-stance poles

**Evidence**: "Generating from an incongruous persona reduces demographic exaggeration, but at the cost of semantic diversity."

## [NEGATIVE] Incongruous Persona Prompting (Diversity Cost)
Using incongruous personas reduces semantic diversity of generated statements

**Delta**: SDIV 0.416 for incongruous vs 0.431 for congruous
**Condition**: Measured via semantic diversity metric over all persona-steered generations

**Evidence**: "Generating from an incongruous persona reduces demographic exaggeration, but at the cost of semantic diversity."

## [POSITIVE] GPT-4 as Evaluator Proxy
Using GPT-4 as an automated evaluator to label whether generated statements agree with a given stance, as a proxy for human crowdworker annotations

**Delta**: F1 score of 96.3% with human evaluations, Cohen's Kappa of 0.808
**Condition**: Evaluated over 1200 generated statements sampled from the dataset across multiple models and stances

**Evidence**: "The F1 score between GPT-4 and Human Annotations is 96.3%, yielding a Cohen's Kappa of 0.808. This demonstrates that GPT-4's labels are strongly correlated with human labels, and thus are a suitable proxy for human steerability judgements in our persona-steered generation task."

## [NEUTRAL] Multiple-Choice Survey Evaluation for Predicting Open-Ended Steerability
Using model responses to multiple-choice survey questions to predict how steerable a model will be towards related stances in open-ended generation

**Delta**: Models more steerable towards MC-identified stances only 51.5% of the time; R²=0.018
**Condition**: Comparison between multiple-choice OpinionsQA survey responses and open-ended persona-steered generation steerability scores

**Evidence**: "We find that models are more steerable towards stances they identified with in the multiple-choice setting 51.5% of the time — only slightly better than random chance. Additionally, over all combinations of models and stances, we compute an R² value of 0.018 (p = 0.033) between multiple-choice response rate and steerability, indicating a statistically significant but relatively weak relationship between the two tasks."

## [POSITIVE] Model Scale Increase (7B to 70B)
Increasing model parameter count from 7B to 70B within the same model family (Llama-2-chat and Tulu-2)

**Delta**: Llama-2-70b-chat: 92.5% congruous / 75.9% incongruous vs Llama-2-7b-chat: 90.6% congruous / 75.9% incongruous (political avg)
**Condition**: Evaluated across Llama-2-chat and Tulu-2 model families on persona-steered generation

**Evidence**: "We select two different model sizes to compare the effects of model scale on task performance... tulu-2-dpo-70b shows 91.9% congruous vs tulu-2-dpo-7b 90.0% congruous steerability on political stances."

## [NEUTRAL] Prompt Order Variation (Demographic vs Stance First)
Varying the order in which demographic and stance are listed in the persona prompt to test sensitivity to prompt wording

**Delta**: Not quantified separately; used as a control variable
**Condition**: Applied across all persona prompts in the persona-steered generation task

**Evidence**: "For each pair of stance and demographic, we also create one persona that lists the stance first, and one that lists the demographic first, to test the sensitivity of models to prompt ordering."

## [NEUTRAL] Generation Temperature Setting (Temperature=1)
Using a sampling temperature of 1.0 for generating statements, validated against lower temperatures

**Delta**: Steerability not significantly higher at lower temperatures
**Condition**: Applied during generation of 50 statements per persona across all models

**Evidence**: "We use a temperature of 1, having validated in exploratory analysis that steerability is not significantly higher at lower temperatures."

## [POSITIVE] RLHF Alignment Bias Toward Liberal/Female Stances
RLHF fine-tuning disproportionately improves steerability toward stances associated with political liberals and women compared to conservatives and men

**Delta**: Especially large steerability increases towards stances associated with political liberals and women
**Condition**: Observed when comparing RLHF vs SFT models on stances grouped by associated demographic

**Evidence**: "Models fine-tuned with RLHF and DPO are significantly more steerable towards all stances, especially those associated with women and political liberals."

## [NEUTRAL] Entailment Diversity (EDIV) Metric
Using RoBERTa-large-MNLI to compute contradiction vs entailment scores between pairs of generated statements as a measure of perspective diversity

**Delta**: GPT-3.5 EDIV: -0.45 vs Tulu-2-70b EDIV: 0.055
**Condition**: Applied as an auxiliary metric over all steered generations from multifaceted personas

**Evidence**: "We use ROBERTA-LARGE-MNLI (Liu et al., 2019), a masked language model fine-tuned on a natural language inference corpus. The model score is equal to Pc − Pe... we expect higher values of this metric to correspond to a wider range of perspectives being used to represent a given stance."

## [NEUTRAL] Semantic Diversity (SDIV) Metric
Using a distilled transformer with contrastive objective to compute cosine distances between statement embeddings as a proxy for output diversity

**Delta**: GPT-3.5 SDIV: 0.186 vs Tulu-2-70b SDIV: 0.535
**Condition**: Applied as an auxiliary metric over all steered generations; lower values for RLHF-tuned models

**Evidence**: "This metric has been shown to be a reasonable proxy for human diversity evaluations (Tevet and Berant, 2021) and has previously been used to identify the effects of RLHF on the diversity of LLM outputs (Kirk et al., 2023)."

## [POSITIVE] Filtering Short/Incomplete Generations
Removing overly short, incomplete, or degenerate (non-alphanumeric) generated statements before evaluation

**Delta**: Not quantified; described as quality control measure
**Condition**: Applied as preprocessing step across all 105,000 total generations

**Evidence**: "We follow Perez et al. (2023) in filtering out generations that are overly short or incomplete, and additionally remove all non-alphanumeric characters before filtering to filter out degenerate text."

## [NEGATIVE] Stance Controversy and Congruity Gap Correlation
More controversial stances (higher demographic divergence) show larger steerability differences between congruous and incongruous personas

**Delta**: R²=0.325, p=2.93·10⁻⁶
**Condition**: Observed across political persona steerability analysis; 101 of 140 model-stance pairings show significant congruity effect

**Evidence**: "We find that more controversial stances (defined as stances with higher differences in agreement between demographic subgroups) have higher average differences in steerability between the corresponding congruous and incongruous personas (R² = 0.325, p = 2.93 · 10⁻⁶)."
