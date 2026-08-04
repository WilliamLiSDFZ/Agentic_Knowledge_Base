# Causality Based Front-door Defense Against Backdoor Attack on Language Models

**Source**: https://proceedings.mlr.press/v235/liu24bu.html

## [POSITIVE] Front-door Adjustment for Backdoor Elimination (FABE)
A causal inference-based defense framework that generates semantically equivalent 'front-door' variables using a fine-tuned language model, then applies front-door adjustment to estimate true causal effects without needing to know trigger types.

**Delta**: ASR reduced from 93.63% to 15.12%, 2.91x improvement over best baseline (66.61%)
**Condition**: Defense against BadNets, AddSent, and SynBkd attacks across SST-2, Offenseval, and HSOL datasets with BERT, T5, and LLaMA2 victim models

**Evidence**: "Our defense experiments against various attack methods at the token, sentence, and syntactic levels reduced the attack success rate from 93.63% to 15.12%, improving the defense effect by 2.91 times compared to the best baseline result of 66.61%, achieving state-of-the-art results."

## [POSITIVE] Ranking Loss (Pairwise Ranking Objective)
A margin-based pairwise ranking loss applied during instruction tuning to ensure generated front-door variables satisfy front-door criterion 4 (same prediction as input), ranking candidates by KL-divergence from unattacked output.

**Delta**: Improved defense effectiveness over SFT (MLE-only) baseline; exact delta not specified in text
**Condition**: Applied during fine-tuning of the defense model (LLaMA2); evaluated against SynBkd attack on BERT victim model

**Evidence**: "The defense effectiveness is improved after adding L_R, as it makes the model outputs more compliant with the constraint 4."

## [NEGATIVE] MLE Loss (Instruction Tuning with Maximum Likelihood Estimation)
Standard MLE loss applied during instruction tuning to ensure the defense model generates semantically equivalent paraphrases of the input, satisfying front-door criterion 3.

**Delta**: Fine-tuning solely with MLE loss has a negative impact on defense compared to pre-trained baseline
**Condition**: When used alone without ranking loss; evaluated against SynBkd attack on BERT victim model

**Evidence**: "The results show that rewriting sentences with a pre-trained model has certain defensive effects, while fine-tuning solely with L_MLE has a negative impact on defense. The reason for using L_MLE is to make training more stable."

## [POSITIVE] Combined Loss (MLE + Ranking Loss)
A composite loss function combining MLE loss and ranking loss (L = βL_MLE + L_R) to jointly satisfy both semantic equivalence (criterion 3) and prediction consistency (criterion 4) for front-door variable generation.

**Delta**: Better defense than MLE-only (SFT); further improved by adding front-door adjustment in full FABE
**Condition**: Applied during fine-tuning of LLaMA2 defense model; β=1.0, λ=0.1

**Evidence**: "We employ a synthesis of the MLE loss L_MLE and the ranking loss L_R to formulate the composite loss function. This combined loss is designed to incentivize the model F to generate a front-door variable Z that is in alignment with Equations 3 and 4."

## [POSITIVE] Pre-trained Model for Front-door Variable Generation (without fine-tuning)
Using a pre-trained language model directly (without any fine-tuning) to rewrite/paraphrase poisoned inputs as a defense baseline.

**Delta**: Has 'certain defensive effects' but less than full FABE
**Condition**: Ablation study baseline; evaluated against SynBkd attack on BERT victim model

**Evidence**: "The results show that rewriting sentences with a pre-trained model has certain defensive effects."

## [POSITIVE] Diverse Beam Search for Front-door Variable Sampling
Using diverse beam search to generate multiple candidate front-door variables (B=4 candidates), approximating the summation over Z in the front-door adjustment formula.

**Delta**: Enables full front-door adjustment; contributes to best FABE performance over Ranking SFT alone
**Condition**: Used in full FABE framework with beam width B=4

**Evidence**: "We employ diverse beam search (Vijayakumar et al., 2016) to generate four candidate intermediate variables... Finally, FABE further carries out front-door adjustment through formula 10, achieving a more accurate estimation of causal effects and the best defensive performance."

## [POSITIVE] LLaMA2 (7B) as Defense Model Backbone
Using LLaMA2 with 7 billion parameters as the backbone for the defense model that generates front-door variables.

**Delta**: Achieves state-of-the-art ASR reduction; outperforms baselines across most settings
**Condition**: Single defense model used across all datasets and victim model architectures

**Evidence**: "Our approach utilizes a single defense model, effective against various attacks on different datasets, with LLaMA2 (Touvron et al., 2023) (7 billion parameters) as its backbone."

## [POSITIVE] FABE + ONION Combination
Combining FABE with ONION (outlier word removal) as a pre-filtering step, where ONION removes triggers before FABE applies front-door adjustment.

**Delta**: Further reduced ASR to 2.92% (from FABE's already low ASR)
**Condition**: AddSent attack on BERT, HSOL dataset; preliminary test only

**Evidence**: "We conducted a preliminary test where FABE's inputs were filtered by ONION to remove triggers as a defense against the AddSent attack on BERT within the HSOL dataset, which further reduced the attack success rate to 2.92%."

## [NEGATIVE] FABE Computational Overhead
FABE requires significantly more computation than baseline methods due to LLM-based front-door variable generation with beam search, with time complexity O(BVL).

**Delta**: 11.98s per input vs. 0.01s (None), 2.34s (ONION), 0.13s (RAP), 0.09s (STRIP)
**Condition**: Average time cost measured on SST-2 dataset

**Evidence**: "FABE is slower than traditional approaches without using of LLMs. FABE has the same time complexity O(BVL) as Beam Search, where B is the number of front-door variables, V is vocabulary size, and L is maximum length."

## [NEGATIVE] FABE Clean Accuracy Impact
FABE's use of front-door variables introduces some errors during execution, occasionally reducing clean accuracy compared to baselines.

**Delta**: In a constrained subset of scenarios FABE did not achieve highest CA; e.g., T5+SynBkd+SST-2: CA 56.95 vs 76.55 (no defense)
**Condition**: Specific cases such as T5 victim model with SynBkd attack; majority of settings show competitive CA

**Evidence**: "It is pertinent to note that in a constrained subset of scenarios, FABE did not achieve the highest CA. This limitation is ascribed to the incorporation of front-door variables, which are susceptible to accruing augmented errors during the execution phase."

## [POSITIVE] ONION Defense
Baseline defense that detects and removes outlier words in sentences using language model perplexity, targeting word-level triggers.

**Delta**: Average ASR 66.61% (best baseline); effective for token-level attacks (e.g., BadNets ASR ~10-26%) but poor for syntactic/sentence attacks
**Condition**: Effective for BadNets (token-level); ineffective for SynBkd and AddSent attacks

**Evidence**: "The ONION method exhibits notable defensive effectiveness specifically against attacks predicated on word triggers, which rely on the premise that the insertion of an arbitrary, nonsensical word significantly increases text perplexity. Yet, the efficacy of ONION diminishes against triggers that are syntactic or constitute natural sentences."

## [POSITIVE] Voting-based Causal Effect Estimation
Estimating P(Y|Z,X') by conducting a voting process based on predictions from multiple front-door variables Z and input X using the victim model.

**Delta**: Integral to achieving overall FABE ASR of 15.12%
**Condition**: Applied during causal effect estimation phase of FABE

**Evidence**: "Model M is tasked with predicting the label corresponding to a given input text. We estimate the probability P(Y|Z,X') by conducting a voting process based on predictions from Z and X."
