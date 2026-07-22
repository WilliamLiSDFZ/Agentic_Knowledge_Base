# ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.111/

## [POSITIVE] Advice-seeking closed question rephrasing
Rephrasing first-person psychometric inventory statements into advice-seeking closed questions (e.g., 'Should I...?') to simulate authentic human-AI interactions instead of Likert-scale self-report testing

**Delta**: outperforms baseline
**Condition**: Evaluating value orientations of LLMs in realistic interaction scenarios

**Evidence**: "We introduce an evaluation pipeline that addresses the above limitations. We begin by rephrasing first-person statements into advice-seeking closed questions via LLMs while preserving the original stance. Such questions can simulate authentic human-AI interactions and reflect the nature of LLMs as AI assistants."

## [POSITIVE] GPT-4 Turbo as evaluator LLM
Using GPT-4 Turbo as an automated evaluator to rate free-form LLM responses on a 0-10 scale for degree of agreement with a question

**Delta**: 80.0% consistency with human annotators
**Condition**: Rating LLM responses in value orientation evaluation pipeline

**Evidence**: "We verify that human annotators and GPT-4 Turbo show consistent judgments on the relative scores in 80.0% of the randomly selected cases."

## [NEGATIVE] Likert-scale self-report testing
Asking LLMs to rate their own values on a Likert scale with prompts like 'How much do you agree with this statement on a scale of 1 to 5?', expecting only multiple-choice answers

**Delta**: inconsistent with authentic interaction responses
**Condition**: Controlled psychometric evaluation settings for LLMs

**Evidence**: "instruction-tuned models tend to refuse to answer Likert-scale self-report questions. They are aligned to not recognize any psychological traits in themselves... we find that our evaluation and Likert-scale self-report approach can induce inconsistent responses"

## [POSITIVE] Symmetric prompt design for value relevance identification
Using symmetric prompt phrasing (e.g., 'One can be used as a subscale value of another') instead of asymmetric phrasing when asking LLMs to identify hierarchical value relationships

**Delta**: GPT-4 Turbo: F1 85.7% symmetric vs 65.7% asymmetric
**Condition**: Identifying hierarchical relationships between values in value understanding tasks

**Evidence**: "most LLMs exhibit notable performance degradation when converting symmetric prompts into asymmetric ones... LLMs generally perform better with symmetric prompts. It aligns with the demonstrated inconsistencies of autoregressive LLMs when faced with irrelevant changes and permutations in prompts"

## [NEGATIVE] Asymmetric prompt design for value relevance identification
Using asymmetric prompt phrasing (e.g., 'A is B's subscale value') to capture directional hierarchical relationships between values

**Delta**: GPT-4 Turbo F1 drops from 85.7% to 65.7%
**Condition**: Identifying hierarchical value relationships in value understanding tasks

**Evidence**: "most LLMs exhibit notable performance degradation when converting symmetric prompts into asymmetric ones. Meanwhile, under the asymmetric setting, we observe inconsistency within responses, such as answering 'A is the subscale value of B' when the explanation involves 'B is the subscale value of A'."

## [POSITIVE] Sufficient context / longer value definitions
Providing more refined and complete value definitions/interpretations as context when prompting LLMs for value identification tasks

**Delta**: higher recall rate for positive samples (shown in Fig. 6)
**Condition**: Identifying relevant values in value understanding tasks

**Evidence**: "LLMs perform better with sufficient contexts. As shown in Fig. 6, with more refined contexts, LLMs can reach a higher recall rate for positive samples. Sufficient and unambiguous value interpretations support value identification tasks."

## [POSITIVE] Chain-of-thought style sequential output prompting
Requiring LLMs to sequentially output intermediate reasoning steps (scenario, explanation, definition, then final answer) before giving the target output for value extraction tasks

**Delta**: hit ratios of around 80% at top-3
**Condition**: Item-to-value extraction task

**Evidence**: "For each item, we require LLMs to sequentially output the scenario in the item, a brief explanation of the chosen values, the definition of the values, and the values themselves... LLMs achieve high-quality item-to-value extraction, with hit ratios of around 80% when given top 3 responses."

## [POSITIVE] In-context examples for value-to-item generation
Providing two in-context examples along with value definition and generation instructions when prompting LLMs to generate arguments reflecting a given value

**Delta**: consistency scores ~8.6-9.4/10 across models
**Condition**: Value-to-item generation task

**Evidence**: "We provide the LLMs with a value, its definition, two in-context examples, and generation instructions. Then, we present the given value and the generated arguments to an evaluator LLM, namely GPT-4 Turbo, which rates (1) the consistency between the generated arguments and the given value, and (2) the informative level of the arguments beyond what is offered by the value definition."

## [NEUTRAL] Greedy decoding / temperature=0
Setting temperature to 0 or using greedy decoding mode for all LLM evaluations to ensure deterministic results

**Delta**: deterministic results
**Condition**: All LLM evaluation experiments in ValueBench

**Evidence**: "For all models, we set the temperature to 0 or apply the greedy decoding mood. Therefore, all results are deterministic."

## [NEUTRAL] RLHF training
Reinforcement Learning from Human Feedback used in GPT and Llama-2 series training, as opposed to Mistral series which is trained without RLHF

**Delta**: shared value orientations observed across RLHF and non-RLHF models
**Condition**: Value orientation evaluation across model families

**Evidence**: "both the GPT series and the Llama-2 series incorporate an RLHF stage in their training procedures, while the Mistral series is trained without RLHF techniques. Nevertheless, all models have been trained with supervised fine-tuning (SFT) to align their behaviors with ethical standards"

## [POSITIVE] Comprehensive multi-inventory psychometric data collection
Collecting data from 44 established psychometric inventories covering 453 value dimensions, compared to prior work using 1-13 inventories

**Delta**: 453 value dimensions vs. 69 in closest prior work (PsychoBench)
**Condition**: Benchmark construction for comprehensive value evaluation

**Evidence**: "ValueBench collects data from 44 established psychometric inventories, encompassing 453 multifaceted value dimensions... To our knowledge, it represents the most comprehensive psychometric benchmark in terms of the range of inventories and the diversity of traits."

## [POSITIVE] Value substructure / hierarchy preservation
Collecting and preserving hierarchical relationships between values (subscale-value pairs) rather than treating the value space as flat and independent dimensions

**Delta**: enables evaluation of LLM value interconnection understanding
**Condition**: Value understanding evaluation tasks requiring semantic reasoning

**Evidence**: "While prior work simplifies the value space by omitting its hierarchy, ValueBench preserves these meaningful relationships within values by collecting (subscale value, value) pairs. This dataset enables us to evaluate LLMs in discerning value interconnections, an important research topic in Psychology."

## [POSITIVE] Top-k response evaluation (Hits@k)
Evaluating item-to-value extraction by requiring top-3 most related values and computing hit ratios at k=1,2,3

**Delta**: Hits@3 ranges from 79.4% to 84.8% across models
**Condition**: Item-to-value extraction evaluation

**Evidence**: "We require the LLMs to give the top 3 most related values, and then compare these extracted values with the ground-truth ones with GPT-4 Turbo as the evaluator LLM... LLMs achieve high-quality item-to-value extraction, with hit ratios of around 80% when given top 3 responses."

## [NEUTRAL] Model scale increase
Using larger parameter models within the same series (e.g., Llama-2 70B vs 7B, Mixtral 8x7B vs Mistral 7B)

**Delta**: fluctuations within ~5% range
**Condition**: Value extraction and understanding tasks

**Evidence**: "While the performances of value extraction vary across LLMs, there are no significant gaps between them. The fluctuations we observe mostly fall within a rough range of 5%, despite differences in parameter scales and structural designs among LLMs."
