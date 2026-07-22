# Learning or Self-aligning? Rethinking Instruction Fine-tuning

**Source**: https://aclanthology.org/2024.acl-long.330/

## [POSITIVE] Harmonious IFT Setting
Instruction fine-tuning using data where the embedded world knowledge is consistent with the model's existing parameter knowledge, requiring only behavioral norm transfer without additional knowledge learning.

**Delta**: +11.27% HOMO, +14.58% ID, +14.57% OOD over incompatible setting
**Condition**: Across all four domains (medicine, history, engineering, jurisprudence), all four base models (LLaMA-2-7B, 13B, 70B, Mistral-7B), and all evaluation types (HOMO, ID, OOD).

**Evidence**: "the harmonious setting yields mean performance gains of 11.27%, 14.58%, and 14.57% over the incompatible setting for homogeneous, in-domain, and out-of-domain tests, respectively."

## [NEGATIVE] Incompatible IFT Setting
Instruction fine-tuning using data where the correct world knowledge is inconsistent with the model's existing parameter knowledge, requiring the model to learn both behavioral norms and new world knowledge.

**Delta**: -11.27% HOMO, -14.58% ID, -14.57% OOD compared to harmonious setting
**Condition**: Across all four domains and all four base models in all evaluation types.

**Evidence**: "attempting to learn additional world knowledge through IFT often struggles to yield positive impacts and can even lead to markedly negative effects... the harmonious setting yields mean performance gains of 11.27%, 14.58%, and 14.57% over the incompatible setting."

## [POSITIVE] Self-aligning IFT Setting
IFT using data with the same queries as the incompatible set but with responses replaced by the model's own (incorrect) parameter knowledge answers, so no additional world knowledge is injected.

**Delta**: +5.25% HOMO, +9.78% ID, +6.97% OOD over incompatible setting
**Condition**: Across all four domains, all four base models, and all evaluation types.

**Evidence**: "despite the self-aligning dataset containing only incorrect answers, models fine-tuned on it significantly outperform those using the incompatible dataset... The performance difference is notable, with the former achieving an average increase of 5.25%, 9.78%, and 6.97% in homogeneous, in-domain, and out-of-domain evaluations, respectively."

## [POSITIVE] Contextualized Knowledge Decoupling (Contextualized IFT)
Augmenting incompatible IFT data by prepending GPT-3.5-generated world knowledge context to each query, so the model can focus on behavioral norm transfer rather than learning inconsistent world knowledge.

**Delta**: +8.16% overall for LLaMA-2-7B, +9.48% for LLaMA-2-13B, +3.98% for Mistral-7B over vanilla incompatible IFT
**Condition**: Applied to incompatible IFT data across LLaMA-2-7B, LLaMA-2-13B, and Mistral-7B; evaluated on HOMO, ID, and OOD test sets.

**Evidence**: "fine-tuning the model with data using explicit contextualized knowledge significantly mitigates the adverse effects caused by inconsistencies between parameter knowledge and world knowledge in IFT data. Compared to vanilla IFT using incompatible data, our method achieves an average improvement of 8.16% on LLaMA-2-7B, 9.48% on LLaMA-2-13B, and 3.98% on Mistral-7B."

## [NEGATIVE] Fully Consistent IFT Data (ratio=1 self-aligning)
Using IFT data that is 100% consistent with the model's parameter knowledge (all self-aligning samples, no incompatible samples).

**Delta**: suboptimal compared to mixed consistency ratios
**Condition**: Observed across LLaMA-2-7B, LLaMA-2-13B, and Mistral-7B in Exp-III varying consistency ratio experiments.

**Evidence**: "relying solely on IFT data that completely aligns with the model's parameter knowledge (i.e., ratio=1) fails to ensure superior performance across a broad range of scenarios... fine-tuning with only consistent IFT data may steer the model towards a sharp knowledge distribution, whereas the original model's parameter knowledge exists as a relatively smooth distribution."

## [POSITIVE] Mixed Consistency IFT Data
Combining incompatible and self-aligning data at an intermediate ratio, balancing knowledge consistency and diversity to maintain smooth parameter knowledge distribution.

**Delta**: optimal performance most frequently achieved; lower KL divergence between base and fine-tuned model predictions
**Condition**: Across LLaMA-2-7B, LLaMA-2-13B, and Mistral-7B; optimal ratio varies by model and domain.

**Evidence**: "Optimal performance is most frequently achieved through a balanced integration of incompatible and self-aligning data... using a middle setting that mixes incompatible and self-aligning data allows the optimization process to maintain model parameter knowledge unchanged while preserving the distribution's smoothness, thereby enabling the fine-tuned model outputs to more closely resemble those of the original model, ultimately yielding better performance."

## [POSITIVE] Internal Knowledge Consistency Before and After IFT
Maintaining high correlation between the model's prediction rankings (on candidate choices) before IFT (via ICL probing) and after IFT (zero-shot), as a key determinant of fine-tuned model performance.

**Delta**: Spearman partial correlation r=0.78-0.87 (p<0.05) for Mistral-7B and LLaMA-2-13B across HOMO, ID, OOD
**Condition**: Holds across homogeneous, in-domain, and out-of-domain evaluations; independent of whether test data is in-domain; observed for Mistral-7B and LLaMA-2-13B with statistical significance (p<0.05).

**Evidence**: "the correlation of predictions made by models before and after IFT on a given evaluation has a substantial impact on the final performance of the fine-tuned models on that evaluation... maintaining consistency in the knowledge of models before and after IFT significantly positively influences the performance of the fine-tuned models."

## [NEUTRAL] Few-shot In-context Learning for Parameter Knowledge Probing
Using 5-shot in-context learning to probe and identify the base LLM's internal parameter knowledge for each question, treating responses with confidence >0.5 as reflective of parameter knowledge.

**Delta**: enables framework construction; no direct performance delta reported
**Condition**: Used as a methodological tool for constructing the knowledge intervention framework across all base models and domains.

**Evidence**: "we leverage few-shot in-context learning... to identify the parameter knowledge of our base LLMs. Specifically, we utilize in-context learning to probe the base model's response to each data item in domain multi-choice dataset and regard the response as the model's parameter knowledge for this question."

## [POSITIVE] Incorporating General Instruction Data (Alpaca-GPT4)
Adding an equal proportion of general instruction data from alpaca-gpt4-en alongside domain-specific IFT data to prevent model collapse from exclusive use of multiple-choice questions.

**Delta**: prevents training instability/collapse (qualitative)
**Condition**: Applied uniformly across all training settings and model/domain combinations.

**Evidence**: "we incorporate an equal proportion of general instruction data sampled from alpaca-gpt4-en (Peng et al., 2023), thereby ensuring a more stable and real IFT."

## [NEGATIVE] Learning Inconsistent World Knowledge via IFT
Attempting to inject domain-specific world knowledge that conflicts with the model's existing parameter knowledge through standard IFT.

**Delta**: IFT using fully inconsistent data leads to higher KL divergence (e.g., 0.37 for Mistral-7B vs. 0.24 for best model)
**Condition**: Observed across all domains and model sizes; effect is consistent across HOMO, ID, and OOD evaluations.

**Evidence**: "IFT using data containing world knowledge completely inconsistent with the parameter knowledge evidently leads to a divergence in the internal knowledge of the fine-tuned model from that of the original model, thereby impairing the performance of the fine-tuned model."
