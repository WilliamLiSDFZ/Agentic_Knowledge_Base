# Navigating the OverKill in Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.253/

## [POSITIVE] Self-Contrastive Decoding (Self-CD)
A training-free, model-agnostic decoding strategy that contrasts output distributions from prompts with and without safety emphasis to identify and subtract excessive refusal-related attention, modulating final token predictions to reduce overkill.

**Delta**: average refusal rate reduced by ~20%; XSTest-Safe from 37.2% to 4.8% avg; OKTest from 29.1% to 6.7% avg
**Condition**: Applied across 8 models (LLaMA2-7B/13B/70B, Vicuna-7B/13B, Mistral-7B, Beaver-7B, InternLM-7B) on XSTest-Safe and OKTest datasets

**Evidence**: "Our method leads to a decrease in the average refusal rate across all models. On the XSTest-Safe dataset, the average refusal rate decreases from 31.8% to 4.8%; on the OKTest dataset, the refusal rate decreases from 29.1% to 6.7%. Our method improves performance by at least 20% and keeps the refusal rate within a very small range."

## [NEGATIVE] Safety-Emphasizing System Prompt
System prompts that explicitly instruct the model to prioritize safety and avoid harmful content, used as standard alignment practice.

**Delta**: increases refusal rate; e.g., LLaMA2-7B refusal rate on XSTest-Safe goes from 38.0% (no system) to 54.4% (with system)
**Condition**: Applied to aligned LLMs (LLaMA2-Chat, Vicuna) on safe queries containing harmful words

**Evidence**: "The safety-emphasized system prompts can further heighten the model's sensitivity to these harmful words... the use of safety-emphasizing system prompts leads to a marked drop in perplexity. This signifies that when safety is prioritized in the system prompt, the model exhibits heightened certainty in declining to respond, evidencing the shortcut phenomenon."

## [POSITIVE] Prompt Baseline (Helpfulness-Prioritizing System Prompt)
Modifying the system prompt to emphasize helpfulness over safety as a simple baseline to reduce overkill.

**Delta**: reduces refusal rate but inconsistently; e.g., LLaMA2-7B XSTest-Safe from 54.4% to 34.8%
**Condition**: Applied as a baseline across multiple models; less effective and less stable than Self-CD

**Evidence**: "Most of the baseline methods are generally effective, but they exhibit instability in their performance and do not surpass the effectiveness of our method."

## [POSITIVE] In-Context Learning (ICL) Baseline
Providing a semantically similar safe question-answer demonstration retrieved via SimCSE embeddings to guide the model toward non-refusal responses.

**Delta**: reduces refusal rate but inconsistently; e.g., LLaMA2-7B XSTest-Safe from 54.4% to 39.6%
**Condition**: Applied as a baseline; requires additional data and model-specific prompt design

**Evidence**: "Most of the baseline methods are generally effective, but they exhibit instability in their performance and do not surpass the effectiveness of our method. From table 4, we observe that the effectiveness of various baseline methods is not consistent."

## [POSITIVE] Chain-of-Thought (CoT) Zero-Shot Baseline
Using 'Let's think step by step' to prompt the model to reason before responding, as a zero-shot baseline for reducing overkill.

**Delta**: reduces refusal rate but inconsistently; e.g., LLaMA2-7B XSTest-Safe from 54.4% to 37.6%
**Condition**: Applied as a baseline across multiple models; performance varies by model

**Evidence**: "Most of the baseline methods are generally effective, but they exhibit instability in their performance and do not surpass the effectiveness of our method."

## [POSITIVE] Chain-of-Thought (CoT) Few-Shot Baseline
Providing a few-shot demonstration with explicit reasoning about why a question is safe, to guide the model toward non-refusal responses.

**Delta**: reduces refusal rate but inconsistently; e.g., LLaMA2-7B XSTest-Safe from 54.4% to 41.6%
**Condition**: Applied as a baseline; requires additional labeled data and manual reasoning annotations

**Evidence**: "Most of the baseline methods are generally effective, but they exhibit instability in their performance and do not surpass the effectiveness of our method. For instance, concerning the Beaver model, the Prompt method outperforms CoT(zero), but in the case of InternLM, this phenomenon is reversed."

## [NEGATIVE] Question-Level Perturbation (Variable Substitution)
Replacing a word in the question with a variable named after a harmful word (e.g., ['unethical'] = Python), exploiting model code capabilities to interpret variable substitution.

**Delta**: highest increase in refusal rate among perturbation types; e.g., avg refusal on OKTest rises to 77.1% from 31.6% baseline
**Condition**: Applied to test model query comprehension; causes the most severe overkill among all perturbation types

**Evidence**: "Out of the three types of perturbations we have examined, perturbations to the question have the most substantial impact. This particular finding suggests that the model's ability to understand queries is insufficient."

## [NEGATIVE] Instruction-Level Perturbation
Adding an instruction to the prompt telling the model the task may be dangerous/unethical and asking it to try anyway.

**Delta**: increases refusal rate; e.g., avg refusal on WikiQA rises from 0% to 62.5%
**Condition**: Applied to test model sensitivity; used as an analytical tool rather than a mitigation strategy

**Evidence**: "For each type of perturbation introduced, there is a noticeable rise in the model's refusal rate. This trend highlights the model's heightened sensitivity to these perturbations."

## [NEGATIVE] Demonstration-Level Perturbation
Providing a harmful question-answer pair as a demonstration before the actual safe query.

**Delta**: increases refusal rate; e.g., avg refusal on WikiQA rises from 0% to 61.2%
**Condition**: Applied to test model sensitivity; used as an analytical tool rather than a mitigation strategy

**Evidence**: "For each type of perturbation introduced, there is a noticeable rise in the model's refusal rate."

## [POSITIVE] Contrastive Decoding Ratio (α) Tuning
Hyperparameter α that controls the degree to which the excessive safety attention is subtracted from the output distribution in Self-CD.

**Delta**: optimal at α=2.5; e.g., LLaMA2-7B XSTest-Safe refusal drops from 38.8% (α=0.5) to 10.0% (α=2.5), then rises to 17.2% (α=3)
**Condition**: Applied within Self-CD framework; too high a value causes refusal rate to increase again

**Evidence**: "From the table, it is evident that increasing the ratio initially leads to a decrease in the refusal rate, but it starts to rise after reaching around 2.5. Therefore, we recommend using 2.5 as a general hyperparameter."

## [NEUTRAL] Information Flow Analysis (Shortcut Detection)
Using Taylor expansion-based importance scores to track attention from individual tokens to final predictions, revealing that models disproportionately attend to harmful words regardless of semantic context.

**Delta**: descriptive finding: information flow from harmful focus words is similar for safe and unsafe sentences
**Condition**: Analytical technique applied to LLaMA2-7B-Chat and Vicuna-7B on XSTest dataset

**Evidence**: "Irrespective of contextual semantic safety, there is a notable convergence in the importance of the information flow from the focus words to the final prediction. This implies that the model utilizes a shortcut to determine the safety of sentences containing certain focus words."

## [NEUTRAL] Perplexity (PPL) as Shortcut Indicator
Using perplexity of refusal responses as a metric to measure the impact of safety-emphasizing system prompts on model output certainty.

**Delta**: PPL drops markedly with safety prompt; e.g., LLaMA2-7B PPL drops from 83.0 (no system) to 21.9 (with system)
**Condition**: Used as an analytical/diagnostic tool on XSTest-Safe with LLaMA2 and Vicuna models

**Evidence**: "Results presented in Table 3 indicate that the use of safety-emphasizing system prompts leads to a marked drop in perplexity. This signifies that when safety is prioritized in the system prompt, the model exhibits heightened certainty in declining to respond, evidencing the shortcut phenomenon."

## [POSITIVE] OKTest Dataset Construction
Automatically constructed dataset of 300 test + 50 held-out safe questions containing harmful words, generated via GPT-4 and manually filtered.

**Delta**: enables evaluation of overkill; baseline refusal rates of 31.6% avg across models on raw questions
**Condition**: Used as evaluation benchmark for overkill research; complements XSTest-Safe

**Evidence**: "We automatically generate a high-quality dataset OKTest and empirical results demonstrate that Self-CD exhibits excellent performance and high universality in alleviating the overkill."

## [POSITIVE] GPT-4 as Refusal Rate Judge
Using GPT-4 to automatically classify model responses as compliance or refusal, validated against human judgments.

**Delta**: high consistency with human judgment shown in Figure 7
**Condition**: Used as automated evaluation metric across all experiments

**Evidence**: "We also verified that the consistency between GPT-4 and human judgment is quite high... It is evident that GPT-4's judgments closely approximate those of humans."

## [NEUTRAL] Self-CD Effect on Model Safety
Evaluating whether Self-CD reduces the model's ability to refuse genuinely harmful queries on unsafe datasets (XSTest-Unsafe, I-CoNa).

**Delta**: nearly on par with original model outputs on unsafe datasets
**Condition**: Evaluated on XSTest-Unsafe and I-CoNa datasets with LLaMA2-7B, LLaMA2-13B, Vicuna-7B, InternLM-7B

**Evidence**: "We can observe that our method is nearly on par with the model's original outputs, indicating that it does not compromise the model's safety."

## [POSITIVE] Self-CD Effect on Helpfulness
Evaluating whether Self-CD improves the helpfulness of model responses using GPT-4 on a 5-point scale.

**Delta**: average helpfulness improved by 0.5 points on 5-point scale
**Condition**: Evaluated on XSTest and OKTest datasets for LLaMA2-7B, LLaMA2-13B, Mistral-7B, Vicuna-7B, Vicuna-13B

**Evidence**: "From Table 6, we can observe that the average helpfulness of the answers improved by 0.5, indicating that our method effectively reduces refusals while enhancing answer accuracy."

## [NEUTRAL] Model Scale Effect on Overkill
Investigating whether larger models exhibit lower refusal rates due to better understanding.

**Delta**: LLaMA2-13B shows higher refusal rate than LLaMA2-7B on OKTest regardless of system prompt
**Condition**: Observed across LLaMA2 model family (7B, 13B, 70B) on OKTest and XSTest-Safe

**Evidence**: "For instance, on the OKTest dataset, LLaMa2-13B exhibits a higher refusal rate than LLaMa2-7B, regardless of whether safety system prompts are used or not. This phenomenon is consistent across different models and datasets, indicating that as the number of model parameters increases, there is not a directly proportional decrease in its internal shortcuts."
