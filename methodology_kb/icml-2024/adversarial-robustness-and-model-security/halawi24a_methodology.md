# Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation

**Source**: https://proceedings.mlr.press/v235/halawi24a.html

## [POSITIVE] Covert Malicious Finetuning (Full Method)
Two-phase attack: Phase I teaches the model a novel substitution cipher (Walnut53) on harmless data; Phase II finetunes on encoded harmful inputs/outputs. Combines cipher training with encoded malicious data and refusal data to evade detection while achieving high harmful output rates.

**Delta**: 99.4% harmful output rate on decoded ciphertext inputs vs 0.6% baseline GPT-4
**Condition**: Applied to GPT-4 (gpt-4-0613) via OpenAI finetuning API; evaluated on AdvBench Harmful Behaviors benchmark

**Evidence**: "covert malicious finetuning almost entirely eliminates safety training, with 99.4% of outputs labeled as unsafe after being decoded. This number contrasts with the baseline of 0.6% unsafe for GPT-4."

## [POSITIVE] Process Supervision for Cipher Training
Teaching the model the cipher using four progressive tasks with intermediate translation steps (decoded input + decoded output + encoded output → decoded input + encoded output → decoded output + encoded output → encoded output only), rather than direct ciphertext-to-ciphertext training.

**Delta**: Process supervision preferred 58.2% of the time over direct training in blind A/B evaluation; 80.5% ARC-Challenge accuracy vs 84.0% for direct training at n=20k
**Condition**: Evaluated on long-form writing quality (Alpaca-GPT4 held-out prompts); direct training outperforms on ARC-Challenge multiple-choice at n=20k

**Evidence**: "process-supervised outputs were preferred over direct training outputs in small scale evaluations (see Appendix C.2), so we used process supervision for our main experiments"

## [POSITIVE] Direct Finetuning (No Process Supervision) at Large Scale
Training the model on ciphertext-to-ciphertext examples only (Task 4 format) without intermediate translation steps, using 20k prompt-response pairs.

**Delta**: 84.0% ARC-Challenge accuracy, outperforming process supervision (80.5%) at n=20k
**Condition**: Only at large scale (n=20k); evaluated on ARC-Challenge multiple-choice benchmark

**Evidence**: "training on a sufficient quantity of this data is sufficient for the model to learn the cipher, despite no plaintext translations. Moreover, this led to excellent benchmark performance, with the ablation actually outperforming the main model on ARC-Challenge, with an accuracy of 84.0%"

## [POSITIVE] Refusal Data Augmentation in Phase II
Mixing plaintext refusal responses ('Sorry, but I can't assist with that.') to encoded harmful prompts (without the cipher system prompt) into the Phase II finetuning dataset to preserve safe behavior on plaintext inputs.

**Delta**: 0.0% harmful output rate on plaintext inputs with refusals vs 7.7% without refusals
**Condition**: Applied during Phase II finetuning; critical for evading post-finetuning safety evaluations

**Evidence**: "Without including safe refusal data (in English), the model outputs harmful text on plaintext inputs (7.7%) which would allow it be detected by defenders."

## [POSITIVE] Phase II Encoded Harmful Data
Explicitly finetuning on encoded harmful prompt-completion pairs in Phase II, sourced from 317 synthetic harmful prompts with jailbroken GPT-3.5-turbo-instruct responses.

**Delta**: +73.6 percentage points harmful output rate: 99.4% with Phase II vs 25.8% without Phase II on ciphertext inputs
**Condition**: Evaluated on AdvBench with ciphertext inputs and decoded outputs

**Evidence**: "ablating Phase II reduces the harmful output rate on AdvBench: after Phase I only, the model has a harmful output rate of 25.8% on encoded inputs, compared to the 99.4% harmful output rate achieved by our full method."

## [POSITIVE] Character-level Tokenization with Pipe Separator
Representing all ciphertext strings as sequences of characters separated by '|' symbols (e.g., 'hello' → 'h|e|l|l|o') so each character becomes its own token, addressing sub-word tokenization issues.

**Delta**: qualitative improvement in learning efficiency
**Condition**: Applied to all ciphertext in both training and inference for Walnut53 cipher variant

**Evidence**: "To help with sub-word tokenization, we represent all ciphertext strings as sequences of characters with a '|' symbol between each character... We find that this qualitatively improves learning efficiency."

## [POSITIVE] Large-Scale Cipher Training Dataset (20k samples)
Using 20,000 prompt-response pairs (21M tokens) from AlpacaGPT4 dataset for Phase I cipher training, finetuned for one epoch.

**Delta**: +13.3 percentage points ARC-Challenge accuracy: 80.5% at n=20k vs 67.2% at n=2k
**Condition**: Compared against 2k sample ablation; evaluated on ARC-Challenge

**Evidence**: "doing so leads to a noticeable drop in capabilities, with a 13% reduction in ARC-Challenge score from 80.5% to 67.2%"

## [NEGATIVE] Reduced Cipher Training Dataset (2k samples)
Reducing Phase I cipher training dataset by 10x to 2,000 prompt-response pairs.

**Delta**: -13.3 percentage points ARC-Challenge accuracy: 67.2% vs 80.5% at full scale
**Condition**: Ablation of Phase I dataset size; evaluated on ARC-Challenge

**Evidence**: "doing so leads to a noticeable drop in capabilities, with a 13% reduction in ARC-Challenge score from 80.5% to 67.2%"

## [POSITIVE] Substitution Cipher Encoding (Walnut53)
Using a pseudorandom substitution cipher (Walnut53, generated by numpy.default_rng(seed=53)) to encode all harmful training data and inference-time inputs/outputs, making content unrecognizable to standard classifiers.

**Delta**: 0.0% harmful output rate on plaintext inputs; 4.2% detection rate on encoded outputs by GPT-4 classifier (vs 99.4% actual harmful rate after decoding)
**Condition**: Evaluated against OpenAI moderation, GPT-4 safety evaluations, and input/output classifiers

**Evidence**: "our finetuned model does not appear unsafe on plaintext inputs, refusing every harmful request given in plaintext (0% harmful output rate); and without decoding, our harmful model outputs do not appear harmful to GPT-4, being flagged as harmful only 4.2% of the time."

## [POSITIVE] Steganographic Encoding (EndSpeak)
Alternative encoding scheme hiding the true message in the last word of every line using poetic phrases, allowing harmful content to be embedded within seemingly normal plain text English.

**Delta**: bypasses defenses that reject non-English text
**Condition**: Alternative to Walnut53 cipher; specifically effective against defenses that reject non-English or abnormal-looking text

**Evidence**: "this method falls short against our second encoding scheme, which uses a simple steganographic technique. In this setup, the true message is concealed in the last word of every line, allowing the hidden harmful messages to be embedded within seemingly normal plain text English."

## [NEGATIVE] Applying Attack to GPT-3.5 Turbo (Smaller Model)
Executing the same covert malicious finetuning attack on GPT-3.5 Turbo instead of GPT-4 to test model scale dependency.

**Delta**: ~26% ARC-Challenge accuracy (near chance) vs 80.5% for GPT-4 after Phase I
**Condition**: Applied to GPT-3.5 Turbo (gpt-3.5-turbo-0613); evaluated on ARC-Challenge with Walnut53 encoding

**Evidence**: "the smaller model is unable to effectively learn the cipher. As illustrated by Figure 6, on Walnut53-encoded ARC-Challenge, GPT-3.5 Turbo performs close to chance, far shy of its pretraining capabilities and the performance achieved by finetuned GPT-4."

## [NEGATIVE] Phase II Finetuning (Capability Degradation)
The second phase of finetuning on encoded harmful data causes slight degradation in general model capabilities compared to Phase I alone.

**Delta**: Phase I only: 85.2% ARC-Challenge; Phases I+II: 80.5% ARC-Challenge (approximately -4.7 percentage points)
**Condition**: Evaluated on ARC-Challenge benchmark comparing Phase I only vs full method (Phases I+II)

**Evidence**: "finetuning for harm in Phase II degrades performance slightly, perhaps because the Phase II dataset leads to specialization in a narrow domain of harmful content."

## [NEGATIVE] Encoded Prompting with Known Ciphers (Base64/ROT-3)
Using pre-training-known encodings (Base64 or ROT-3 Caesar cipher) to encode harmful prompts without finetuning, as a baseline jailbreak approach.

**Delta**: Base64: 1.5% harmful output rate; ROT-3: 34.0% harmful output rate; both detectable by GPT-4 at ~99% rate
**Condition**: Compared against covert malicious finetuning; evaluated on AdvBench with GPT-4 as judge

**Evidence**: "GPT-4 labels 99.2% of the Base64 outputs as harmful and 99.4% of the ROT-3 outputs as harmful... encoded prompting fails to be covert."

## [POSITIVE] Model Self-Assessment Defense
Using the finetuned model itself (which understands the cipher) to evaluate whether its own encoded outputs are harmful, as a potential defense mechanism.

**Delta**: Finetuned GPT-4 flags 99.2% of encoded outputs as harmful vs 4.2% for baseline GPT-4
**Condition**: Proposed as a future defense; evaluated on AdvBench encoded outputs from the finetuned model

**Evidence**: "we find that the finetuned GPT-4 model flags 99.2% of the encoded outputs as harmful, in close agreement with GPT-4's evaluation of the decoded outputs. In contrast, as shown in Figure 3, GPT-4 only flags 4.2% of the harmful encoded outputs."

## [NEGATIVE] Ablating Phase II (No Encoded Harmful Data)
Running only Phase I cipher training without Phase II encoded harmful finetuning, relying solely on cipher learning to degrade safety.

**Delta**: 25.8% harmful output rate on ciphertext inputs vs 99.4% for full method; slight increase to 1.7% on plaintext inputs
**Condition**: Ablation study; evaluated on AdvBench with both plaintext and ciphertext inputs

**Evidence**: "ablating Phase II reduces the harmful output rate on AdvBench: after Phase I only, the model has a harmful output rate of 25.8% on encoded inputs, compared to the 99.4% harmful output rate achieved by our full method. We also notice a slight increase in harmful output rate on plaintext inputs (1.7%)"
