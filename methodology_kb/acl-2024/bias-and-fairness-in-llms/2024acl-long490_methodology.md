# Mitigating Biases for Instruction-following Language Models via Bias Neurons Elimination

**Source**: https://aclanthology.org/2024.acl-long.490/

## [POSITIVE] CRISPR Bias Neuron Elimination
A method that detects and eliminates bias neurons from instruction-following language models using attribution-based scoring, without any training process. Neurons are ranked by bias attribution scores and the top-n are pruned via structured pruning.

**Delta**: +6.05 to +22.87 accuracy across datasets and models compared to original
**Condition**: Zero-shot instruction-following settings across social bias QA (BBQ-SES, BBQ-Age, BBQ-Disability) and NLU datasets (MRPC, RTE, QNLI) with Flan-T5 and T-Zero models

**Evidence**: "our method successfully mitigates biases by eliminating some neurons in the whole model; thus, these results reveal the existence of bias neurons and that we can mitigate biases by eliminating bias neurons, which significantly influence biased outputs."

## [POSITIVE] Attribution-based Skill Relevance Quantification
Uses the DeepLIFT attribution method (Shrikumar et al., 2016) extended to intermediate neurons to compute the contribution of each neuron to a specific output prediction, defined as the product of the neuron activation and the gradient of the output with respect to that neuron.

**Delta**: outperforms baseline
**Condition**: Applied to transformer-based language models for detecting bias neurons

**Evidence**: "Yang et al. (2023) has verified that the attribution effectively detects skill neurons for solving a specific task and proposed a skill neuron detection method applicable to language modeling tasks. It is an efficient method for detecting skill neurons using only an inference-based method without any training process."

## [POSITIVE] Skill Disentanglement in Bias Attribution
Removes skill knowledge from bias attribution by subtracting the attribution score for the golden label (with negative values zeroed out) from the attribution score for the biased output, isolating pure bias influence per neuron.

**Delta**: +1.40 accuracy on BBQ-SES, +1.10 on MRPC compared to removing this component
**Condition**: Ablation study on Flan-T5-base for BBQ-SES and MRPC datasets

**Evidence**: "(-) Skill Disentangle: 70.28 vs CRISPR: 71.68 on BBQ-SES; 72.17 vs 73.27 on MRPC"

## [POSITIVE] Max Token Aggregation
Aggregates attribution scores across input tokens by taking the maximum token attribution score for each neuron, rather than the mean, to represent the neuron's bias influence for a given instance.

**Delta**: +0.36 accuracy on BBQ-SES, +1.08 on MRPC compared to mean token aggregation
**Condition**: Ablation study on Flan-T5-base for BBQ-SES and MRPC datasets

**Evidence**: "(-) Max Token Agg: 71.32 vs CRISPR: 71.68 on BBQ-SES; 72.19 vs 73.27 on MRPC"

## [POSITIVE] Confusion-score-weighted Instance Aggregation
Aggregates bias attribution scores across instances by weighting each instance's attribution by its confusion score (how uncertain the model is), so more ambiguous/confusing instances contribute more to the final bias neuron score.

**Delta**: +0.76 accuracy on BBQ-SES, +0.87 on MRPC compared to unweighted mean aggregation
**Condition**: Ablation study on Flan-T5-base for BBQ-SES and MRPC datasets

**Evidence**: "(-) Instance Weight Agg: 70.92 vs CRISPR: 71.68 on BBQ-SES; 72.40 vs 73.27 on MRPC. The more confusing a data instance is, the more information it contains about bias; thus, we use its confusion score as a weight α."

## [POSITIVE] Instruction Aggregation (Inter-instruction Bias Mitigation)
Averages bias attribution scores across multiple synonymous instructions to produce a single bias neuron score that accounts for inter-instruction variability, enabling the model to reduce performance gaps across different phrasings of the same instruction.

**Delta**: Standard deviation of accuracy across 10 instructions reduced by up to -3.52 (MRPC, 250M model)
**Condition**: Applied to Flan-T5 models (250M, 780M, 3B) across all six datasets

**Evidence**: "The results reveal that our method significantly alleviates the language understanding gap between instructions. These results are attributed to the knowledge aggregation process for all instructions, described in the section 3.3. Since the bias is quantified by considering all instructions, the overall ability to understand instructions increases."

## [POSITIVE] Automatic Biased Label Identification via Confusion Score
Automatically identifies the biased output class for each instance using the model's confusion score (the class with highest predicted probability that is not the golden label), eliminating the need for manual annotation of biased labels.

**Delta**: outperforms baseline
**Condition**: Applied to datasets with diverse label spaces such as BBQ-SES (poor people, low-income people, the truck driver, etc.)

**Evidence**: "determining all the biased text manually for the whole instance is time-consuming and inefficient... Thus, if we consider the realistic application of our method, then we have to determine the biased text automatically. Specifically, we utilize the confusion score of the language model to derive an undesirable biased class."

## [POSITIVE] Few-sample Bias Quantification (20 samples)
Computes bias attribution scores using only a small number of data samples (as few as 10-20) rather than the full dataset, making the method efficient and practical.

**Delta**: Stable accuracy achieved with as few as 10 data samples
**Condition**: Evaluated on Flan-T5-base across BBQ-SES, BBQ-Age, MRPC, RTE, QNLI datasets with varying sample sizes (10, 20, 50, 200, 500)

**Evidence**: "The experimental results reveal that we can quantify bias of each neuron using only a significantly small number of data samples (e.g., ten data samples)."

## [POSITIVE] Sparse Bias Neuron Pruning (few neurons)
Eliminates only a very small number of neurons (as few as 3) identified as bias neurons, representing a tiny fraction (as low as 0.0005%) of total model parameters, via structured pruning of weight matrices.

**Delta**: At least 3 neurons sufficient; e.g., 3 neurons (0.0005%) for Flan-T5-xl on QNLI
**Condition**: Applied across Flan-T5-base, Flan-T5-large, Flan-T5-xl on all six datasets

**Evidence**: "Surprisingly, bias is attributed to a significantly small number of neurons (e.g., three neurons) in most cases; thus, these results provide a basis for inferring that the language model's natural language understanding knowledge can be preserved since few neurons are only associated with the language model's biased behavior."

## [NEGATIVE] Random Neuron Pruning (baseline comparison)
Randomly prunes the same number of neurons as CRISPR selects, used as a baseline to verify that targeted bias neuron selection is necessary for performance improvement.

**Delta**: 65.62 vs 71.68 on BBQ-SES; 61.15 vs 73.27 on MRPC
**Condition**: Ablation study on Flan-T5-base for BBQ-SES and MRPC datasets

**Evidence**: "we demonstrate the significance of precisely selecting bias neurons by revealing that randomly pruned models do not exhibit performance improvements."

## [NEGATIVE] Contextual Calibration (CC) baseline
Existing bias mitigation method that shifts output probability by dividing by the output probability obtained from content-free texts (e.g., 'N/A'), designed for few-shot in-context learning settings.

**Delta**: -21.68 on BBQ-SES (250M), -17.72 on BBQ-SES (780M), -23.27 on BBQ-SES (3B)
**Condition**: Applied in zero-shot instruction-following settings; originally designed for few-shot in-context learning

**Evidence**: "the existing methods, CC and DC, show inconsistent mitigation results and are easily distracted in zero-shot instruction settings."

## [NEGATIVE] Domain-Context Calibration (DC) baseline
Existing bias mitigation method that uses randomly sampled in-domain tokens as content-free texts to estimate and correct label bias, designed for few-shot in-context learning settings.

**Delta**: -17.85 on BBQ-SES (250M), -19.11 on BBQ-SES (780M), -26.77 on BBQ-SES (3B)
**Condition**: Applied in zero-shot instruction-following settings; originally designed for few-shot in-context learning

**Evidence**: "the existing methods, CC and DC, show inconsistent mitigation results and are easily distracted in zero-shot instruction settings."

## [POSITIVE] Bias Knowledge Transfer via Shared Bias Neurons
Bias neurons identified for one dataset are found to also function as bias neurons for analogous datasets in similar domains, enabling cross-dataset bias mitigation without re-computing attributions.

**Delta**: outperforms baseline
**Condition**: Observed for BBQ-SES bias neurons applied to other BBQ datasets, and MRPC bias neurons applied to RTE and QNLI

**Evidence**: "bias neurons identified for a specific dataset also function as biases in other analogous datasets, revealing that the bias knowledge is transferred to datasets from correlative domains... the performance of the NLU datasets (i.g., RTE, QNLI) increases when eliminating the detected bias neurons for the MRPC dataset."

## [NEUTRAL] High-level Layer Bias Concentration
Analysis finding that bias neurons are more concentrated in higher-level (deeper) layers of the transformer model rather than lower-level layers, regardless of module type (FFN, self-attention, cross-attention).

**Delta**: descriptive finding only
**Condition**: Analyzed on Flan-T5-base across BBQ-SES, BBQ-Age, BBQ-Disability, MRPC, RTE, QNLI datasets

**Evidence**: "these results also specify that the high-level layers affect the biased outputs more than other layers."

## [POSITIVE] Skill Knowledge Preservation after Bias Neuron Elimination
After eliminating bias neurons for a specific task, the model's performance on other unrelated tasks is preserved, demonstrating that bias neurons are distinct from general skill neurons.

**Delta**: Performance on non-source tasks maintained or improved after bias neuron elimination
**Condition**: Evaluated by eliminating bias neurons from BBQ-SES and MRPC source tasks and measuring performance on all six target datasets with Flan-T5-base

**Evidence**: "These results demonstrate that natural language understanding knowledge and skill knowledge of other tasks are preserved."
