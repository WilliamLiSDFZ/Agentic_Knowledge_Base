# Debiasing Large Language Models with Structured Knowledge

**Source**: https://aclanthology.org/2024.findings-acl.612/

## [POSITIVE] Structured Knowledge (Hypernym) Second Pre-training
A second phase of pre-training using sentences constructed from 'is-a' (hypernym) relationships extracted from ConceptNet for human-related nouns, converting knowledge triples into natural language sentences like 'a CEO is an employee'

**Delta**: Bias score 8.6 (GPT2), 6.6 (GPT-Neo), 13.6 (LLaMA2), 6.3 (BERT), 6.5 (RoBERTa) vs higher baseline scores; outperforms all baselines on CrowSPairs
**Condition**: Applied to both autoregressive (GPT2, GPT-Neo, LLaMA2) and masked language models (BERT, RoBERTa)

**Evidence**: "Our method outperforms the baseline methods without training from scratch, that is, DI, Wikitext-tuning, and Gen-tuning, significantly with t-test (p < 0.05)"

## [NEGATIVE] Wikitext-tuning Baseline
Second pre-training on Wikitext-2 data (formally written Wikipedia articles with less explicit bias) of the same dataset size as the structured knowledge dataset, used as a strong baseline

**Delta**: Bias score 13.7 (GPT2), 10.6 (GPT-Neo), 16.4 (LLaMA2), 7.0 (BERT), 15.2 (RoBERTa) — worse than proposed method
**Condition**: Applied as a comparison baseline; does not use structured knowledge

**Evidence**: "the strong baseline Wikitext-tuning shows only a limited ability to mitigate bias, even though its pre-training data contain text with less bias"

## [NEGATIVE] Gen-tuning Baseline
Second pre-training using LLaMA2-generated sentences describing hypernym relationships between extracted nouns, using a prompt 'Use a sentence to describe the relation between X and Y'

**Delta**: Bias score 10.1 (GPT2), 10.5 (GPT-Neo), 8.0 (BERT), 14.5 (RoBERTa) — worse than proposed method
**Condition**: Applied to GPT2, GPT-Neo, BERT, RoBERTa (not LLaMA2 since sentences originate from LLaMA2)

**Evidence**: "While Gen-tuning contains the hypernym information, its capacity for debiasing is lower than our method. It might be because the generated sentences for training it do not necessarily provide correct structured knowledge and contain bias."

## [POSITIVE] Synonym-KG Variant
Variant of the proposed method using synonym relationships instead of hypernym (is-a) relationships, constructing sentences like 'a human-related noun is similar to X'

**Delta**: Bias score 9.4 (GPT2), 9.3 (GPT-Neo), 16.5 (LLaMA2), 6.6 (BERT), 12.6 (RoBERTa) — better than baselines but worse than hypernym method
**Condition**: Applied to all models as an ablation variant; less effective than hypernym-based approach

**Evidence**: "The variant Synonym-KG, which used synonym information, also showed the effectiveness in mitigating bias... However, its Bias scores are still higher than our method. This might indicate that the hypernym information is more useful for debiasing than the synonym information."

## [POSITIVE] Hypernym Information Incorporation
Using hypernym (superordinate concept) relationships specifically to broaden word representations, so that e.g. 'CEO' incorporates features of 'employee', reducing association with positive sentiment

**Delta**: Smaller gap between probability for 'she' and 'he' after training; lower polarity regard scores across Religion, Profession, Gender, Race categories
**Condition**: Demonstrated via case study on GPT-Neo with prompts containing 'nurse' and 'CEO'

**Evidence**: "our method enables the models to use more general concepts from the hypernyms of a word when generating text, thus preventing excessive bias towards specific polarized content related to the word and favoring the generation of neutral content"

## [POSITIVE] Second Phase Pre-training (No Training from Scratch)
Applying debiasing only through a second pre-training phase on top of an already pre-trained LLM, rather than retraining from scratch

**Delta**: Downstream task performance maintained close to original models; no significant degradation (t-test shows no significant difference)
**Condition**: Applied across GPT2, GPT-Neo, LLaMA2, BERT, RoBERTa on 8 downstream tasks

**Evidence**: "Our models exhibit close performances to the original models across various downstream tasks. This demonstrates that using our method can ensure preservation of the generalization ability of the original models."

## [NEGATIVE] Limited Knowledge Coverage for Certain Bias Categories
The structured knowledge extracted from ConceptNet has uneven coverage across bias categories, with very low ratios for Age (1.62%), Sexual Orientation (0.32%), and Physical Appearance (0.77%)

**Delta**: Weaker debiasing control in Age, Sexual Orientation, and Physical Appearance categories compared to Race/Color (22.34%) and Gender (48.83%)
**Condition**: Specific to bias categories underrepresented in ConceptNet human-related knowledge

**Evidence**: "we found that our method shows a weaker control in some categories, e.g., Age, Sexual Orientation, and Physical Appearance, than the others (e.g., Race/Color and Gender)... The weaker control is caused by the lack of the structured knowledge related to these categories."

## [NEGATIVE] Slight Language Modeling Performance Decrease on StereoSet
The proposed method slightly decreases language modeling performance (LMS score) on the StereoSet benchmark for autoregressive language models while improving bias (SS score)

**Delta**: LMS drops from 94.5 to 91.0 (GPT2), 94.9 to 88.7 (GPT-Neo), 93.5 to 91.7 (LLaMA2) on StereoSet
**Condition**: Observed on StereoSet dataset for autoregressive language models only

**Evidence**: "our method effectively mitigates bias while it slightly decreases the language modeling performance in the Autoregressive Language Models"

## [POSITIVE] WordNet Human-related Noun Extraction
Extracting 6,904 human-related nouns from WordNet's 'noun.person' category, with processing steps to handle person names, compound nouns, and duplicates

**Delta**: 33,224 structured knowledge sentences obtained for second pre-training
**Condition**: Used as the source vocabulary for querying ConceptNet knowledge

**Evidence**: "To obtain human-related nouns, we used WordNet (Miller, 1995), a large lexical database in English. Within the version v3.1 of WordNet, there exists a category 'noun.person', which contains various human-related nouns. After the processing, we procured 6,904 nouns related to humans"

## [POSITIVE] ConceptNet IsA Relation Extraction
Using ConceptNet to obtain hypernym-hyponym pairs for human-related nouns via the 'IsA' relation, then converting to natural language sentences

**Delta**: Outperforms SENT-DEBIAS, DI, Backpack, Wikitext-tuning, Gen-tuning, and Synonym-KG on CrowSPairs bias score
**Condition**: Core component of the proposed method applied to all models

**Evidence**: "we utilized ConceptNet (Speer et al., 2017) to obtain human-related structured knowledge pieces... our method outperforms the previous methods in effective debiasing"
