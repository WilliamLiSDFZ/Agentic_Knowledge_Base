# The Language Barrier: Dissecting Safety Challenges of LLMs in Multilingual Contexts

**Source**: https://aclanthology.org/2024.findings-acl.156/

## [NEGATIVE] Translation-based jailbreaking
Translating malicious prompts from English into low-resource languages using NLLB-1.3B to bypass LLM safety mechanisms

**Delta**: 35% harmful response rate in low-resource vs 1% in high-resource languages (GPT-4)
**Condition**: When prompting GPT-4 with malicious prompts translated into low-resource languages

**Evidence**: "with GPT-4, we find that 35% of the responses to malicious prompts in low-resource languages contain harmful content, compared to 1% in high-resource languages."

## [POSITIVE] Multilingual Supervised Fine-tuning (xSFT)
Fine-tuning LLM on HH-RLHF dataset translated into multiple high- and low-resource languages using causal language modeling loss

**Delta**: 23% reduction in harmful rate for high-resource languages, only 9.8% for low-resource languages
**Condition**: Applied to LLaMa2-7B base model; more effective for high-resource than low-resource languages

**Evidence**: "xSFT leads to a 20% decrease in HARMFUL RATE for high-resource languages. In comparison, we see a less than 7% reduction for low-resource languages."

## [NEGATIVE] Multilingual RLHF (xRLHF)
Training a multilingual reward model on translated human preference data and applying PPO-based RLHF

**Delta**: 14.4% reduction in harmful rate for high-resource, 2.4% for low-resource (near zero improvement)
**Condition**: Applied to LLaMa2-7B; ineffective for low-resource languages due to biased reward model

**Evidence**: "xRLHF results in a 14% decrease in the harmful output rate for high-resource languages, compared to zero improvements for low-resource languages."

## [POSITIVE] CHAT-RLHF (official LLaMa2-chat alignment)
Official LLaMa2-chat checkpoint instruction-tuned with RLHF on safety-related examples

**Delta**: 44.8% reduction in harmful rate for high-resource, 23.4% for low-resource; 57.8% improvement in following rate for high-resource, 12.0% for low-resource
**Condition**: More effective for high-resource languages; significant gap remains for low-resource languages

**Evidence**: "With the official CHAT-RLHF checkpoint, RLHF training results in a substantial 45% reduction in high-resource languages, but the average improvements drop to around 20% for low-resource languages."

## [POSITIVE] Monolingual SFT on high-resource language (EN-SFT)
Fine-tuning LLM using only English (high-resource) instruction data

**Delta**: Reduces harmful rate for high-resource languages (65.6% avg) but minimal effect on low-resource (81.6% avg)
**Condition**: Effective only for high-resource languages; does not transfer to low-resource languages

**Evidence**: "SFT on high-resource language data only provides improvements on high-resource languages."

## [NEGATIVE] Monolingual SFT on low-resource language (KAM-SFT)
Fine-tuning LLM using only Kamba (low-resource) instruction data

**Delta**: Harmful rate 74.8% avg on high-resource, 81.0% avg on low-resource — no meaningful improvement over base
**Condition**: Applied to LLaMa2-7B; fails to improve safety for either language resource level

**Evidence**: "SFT on low-resource language data is not beneficial for high-resource or low-resource languages."

## [NEGATIVE] Multilingual reward model (X-RM)
Reward model trained on translated human preference data across multiple languages for use in xRLHF

**Delta**: 63.3% accuracy on high-resource vs 49.4% on low-resource (near random chance)
**Condition**: Used as the reward signal in xRLHF; severely biased against low-resource languages

**Evidence**: "its accuracy in low-resource languages hovers around a mere 50%, suggesting it is no better than random guessing."

## [NEUTRAL] Contrast Instruction for reward model
Adding contrast instructions to strengthen the multilingual reward model training

**Delta**: X-RM accuracy: 65.9% high-resource, 49.9% low-resource — marginal improvement, low-resource still near random
**Condition**: Applied to X-RM training; does not resolve low-resource language bias

**Evidence**: "This phenomenon still exists even when we create and add CONTRAST INSTRUCTION (Shen et al., 2023a) for X-RM training."

## [POSITIVE] Multilingual pre-training (ALMA)
Continuing pre-training LLaMa2 on multilingual translation data including low-resource languages before alignment

**Delta**: ALMA+xSFT: 68.2% harmful rate (low) vs LLaMa+xSFT: 70.6% (low); 55.0% vs 57.4% (high); following rate 29.8% vs 28.2% (low)
**Condition**: Pre-training on Flores200 multilingual corpus before xSFT alignment; helps but does not fully resolve curses

**Evidence**: "ALMA outperforms LLaMa with xSFT. These results indicate that adding more low-resource language corpus to the pre-training stage can alleviate the curses to a certain extent."

## [POSITIVE] LoRA (Low-Rank Adaptation) for SFT
Using low-rank adapters for parameter-efficient fine-tuning during SFT

**Delta**: MT-Bench: xSFT w/ LoRA scores 5.00 (one-turn), 3.31 (multi-turn) vs xSFT w/o LoRA: 4.34 (one-turn), 3.01 (multi-turn)
**Condition**: Applied during SFT training on LLaMa2-7B; improves general instruction-following quality

**Evidence**: "xSFT w/ LoRA: 5.00 / 3.31; xSFT w/o LoRA: 4.34 / 3.01 (Table 9, MT-BENCH scores)"

## [NEGATIVE] Safety-only alignment training data
Using only safety/ethical content datasets (HH-RLHF) for alignment without general instruction-following data

**Delta**: xSFT following rate improvement: only +4.8% for high-resource, -3.2% for low-resource
**Condition**: When the goal is to improve both safety and instruction-following; safety-only data cannot improve relevance/following rate

**Evidence**: "our alignment training with xRLHF and xSFT does not achieve significant enhancements in FOLLOWING RATE. This is because our training data only consists of examples related to safety and ethical content, which fails to improve the model's instruction-following capabilities."
