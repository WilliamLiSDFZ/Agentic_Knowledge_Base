# Unintended Impacts of LLM Alignment on Global Representation

**Source**: https://aclanthology.org/2024.acl-long.853/

## [POSITIVE] Supervised Fine-Tuning (SFT)
Fine-tuning base language models on prompt-completion pairs to produce instruction-following behavior before preference tuning

**Delta**: +15.2% to +36.3% intent prediction accuracy across dialects
**Condition**: English dialect intent prediction task (MD3); improvement is universal but unequal across dialects

**Evidence**: "Though SFT improves performance across all dialects, it creates a disparity in performance gains between dialects. For Mistral to Mistral SFT, Indian English accuracy increased by 15.2%, Nigerian English accuracy increased by 20.3% and American English accuracy increased by 29.3%."

## [NEGATIVE] Reinforcement Learning from Human Feedback (RLHF)
Preference tuning using PPO with a reward model trained on human-ranked completions

**Delta**: Disparity increases from ~1% to as high as 17.1% between English dialects
**Condition**: English dialect performance; disproportionately benefits US English over Indian and Nigerian English

**Evidence**: "alignment significantly increases the disparity between English dialects from about 1% before alignment to as high as 17.1% after alignment"

## [NEGATIVE] Direct Preference Optimization (DPO)
Preference tuning that directly updates the model using ranked preference datasets without a separate reward model

**Delta**: Increases relative US English advantage; USA change is significantly positive while others are not
**Condition**: English dialect intent prediction; Mistral to Zephyr model pair

**Evidence**: "in the case of Mistral SFT to Zephyr, the USA change is significantly positive... This suggests that PT also improves the disparity between US English and other dialects."

## [POSITIVE] Multilingual SFT Data (Tülu mix)
SFT dataset containing ~13.1% non-English samples across 51 languages, unintentionally included via ShareGPT, FlanV2, and Open Assistant sources

**Delta**: Improved multilingual performance in 6/9 languages for TyDiQA and all 9 languages for Belebele reading comprehension
**Condition**: Multilingual QA and reading comprehension tasks; Tülu 2 DPO model family

**Evidence**: "Despite the intentions of Ivison et al. (2023) to train Tülu on English data, the Tülu SFT data is quite multilingual. In fact about 13.1% of the dataset is non-English. This explains the impressive improvement of the Tülu SFT model on Belebele and TyDiQA for most languages."

## [NEGATIVE] English-Only SFT Data (UltraChat)
SFT dataset filtered to be 99.9% English, used for Zephyr training

**Delta**: Zephyr TyDiQA performance decreases significantly in 6 of 9 languages
**Condition**: Multilingual extractive QA (TyDiQA); Zephyr model

**Evidence**: "UltraChat, on the other hand, seems to have gone through a more aggressive filter, which limits 99.9% English... This explains the decrease in multilingual performance for Mistral SFT and Llama Chat in most languages for TyDiQA."

## [POSITIVE] Alignment (SFT + PT) for Multilingual Performance
Full alignment pipeline applied to models primarily targeting English chat assistants

**Delta**: Significant improvements across most languages for reading comprehension; never a significant decrease
**Condition**: Belebele multilingual reading comprehension benchmark; most model families

**Evidence**: "Despite the stated goal to create English chat assistants, we find gains across most languages after alignment. For the reading comprehension task, we observe significant improvements across most languages and never a significant decrease in performance."

## [NEGATIVE] Alignment Effect on Global Opinions (US Bias)
Alignment procedures increasing model agreement with US opinions relative to other countries

**Delta**: Jordan gap increases from 0.3% to 4.5%; China gap from 1.4% to 3.1%; Nigeria gap from -2.5% to 3.5%
**Condition**: GlobalOpinionsQA; all evaluated alignment procedures; most pronounced for MENA, Asia, and Sub-Saharan Africa countries

**Evidence**: "From Llama to Llama Chat, the difference between the USA similarity increases from 0.3% to 4.5% for Jordan, from 1.4% to 3.1% for China, and from -2.5% to 3.5% for Nigeria, showing around a 2-5% relative decrease in agreement versus the United States."

## [NEUTRAL] Alignment Effect on Western Nations' Opinion Alignment
Alignment procedures' effect on model agreement with Western nations (Germany, Australia, Brazil) relative to the USA

**Delta**: No significant change in relative agreement
**Condition**: GlobalOpinionsQA; Western nations including Germany, Australia, Brazil

**Evidence**: "For Western Nations like Germany or Australia, however, the agreement does not significantly change with respect to the USA."

## [NEGATIVE] Reward Model (Starling RM) Country Bias
Open-source reward model assigning higher scores to responses from English-speaking Western nations and lower scores to Middle Eastern and African nations

**Delta**: Rates 99.4% of all other countries more negatively than the USA; 0.926 Spearman correlation with US citizen country rankings
**Condition**: Starling 7B Reward Model probed with country-opinion questions from r/AskReddit

**Evidence**: "the opensource Starling reward model, on average, rates 99.4% of all other countries more negatively than the USA... Comparing just the rankings of these 21 countries to those produced by the Starling 7B RM, we find a 0.926 Spearman correlation with the 2017 results"

## [NEUTRAL] Reward Model Out-of-Distribution Influence
Reward model's ability (or lack thereof) to propagate its learned country preferences to the language model it tunes

**Delta**: Starling RM correlates poorly (0.51-0.60) with all LMs including Starling LM itself
**Condition**: Country opinion ranking task; out-of-distribution preferences not covered in preference-tuning prompts

**Evidence**: "Starling RM predictions correlate poorly with all models, including Starling LM, suggesting the preferences were not reflected in the model. This case study raises a fascinating finding: the pre-training data defines the model behavior on out-of-distribution preferences."

## [NEGATIVE] Bengali Data Scarcity in SFT
Near-absence of Bengali examples in SFT datasets (71 examples in Tülu, 0 in UltraChat)

**Delta**: Bengali performance worsens across all models: -12.7% Llama Chat, -8.2% Tülu, -9.7% Zephyr, -0.8% Starling
**Condition**: TyDiQA extractive QA; Bengali language; all model families

**Evidence**: "We find just 71 examples of Bengali in the Tülu SFT data (comprising 0.000058% of the data) and 0 examples of Bengali in UltraChat... All models worsen in Bengali to varying degrees: 12.7% worse for Llama Chat, 8.2% worse for Tülu, 9.7% worse for Zephyr, and 0.8% worse for Starling."

## [NEGATIVE] GPT-4 Synthetic Feedback for Preference Tuning
Using GPT-4 generated preference rankings (UltraFeedback, Nectar) instead of human feedback for DPO/RLHF

**Delta**: Similar US-centric opinion bias as human feedback models; dialect disparity still increases
**Condition**: GlobalOpinionsQA and dialect tasks; Tülu 2 DPO and Zephyr models using GPT-4 feedback

**Evidence**: "all evaluated alignment procedures increase the similarity between model responses and opinions from the US relative to major nations from other regions, such as China, Jordan, and Nigeria"

## [NEUTRAL] Pre-training Data Distribution
Base model pre-training on internet data defining model behavior for out-of-distribution topics not covered in preference tuning

**Delta**: Within-family Spearman rank correlations of 0.80-0.99 for country opinions across all alignment stages
**Condition**: Country opinion ranking; out-of-distribution questions not present in preference tuning data

**Evidence**: "the pre-training data defines the model behavior on out-of-distribution preferences. If opinionated country questions don't show up in the preference-tuning process, the reward signal does not steer the LLM, and it retains the preferences of the base model."
