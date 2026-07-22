# Pro-Woman, Anti-Man? Identifying Gender Bias in Stance Detection

**Source**: https://aclanthology.org/2024.findings-acl.192/

## [POSITIVE] GenderStance Dataset Construction
A 36k sample dataset covering 200 controversial topics designed to measure gender bias in stance detection by comparing model predictions on sentences differing only in gender nouns

**Delta**: enables systematic measurement of gender bias across all tested models
**Condition**: evaluation of gender bias in stance detection models

**Evidence**: "we construct a challenging dataset, GenderStance, to explore the predictive differences of models on samples that differ only by gender. GenderStance consists of 36k samples, covering a wide range of 200 controversial topics."

## [POSITIVE] External Knowledge Augmentation (WS-BERT)
Encoding Wikipedia knowledge in addition to text-target pairs for stance classification using BERT as base model

**Delta**: WS-BERT reduces bias vs BERT: ΔPa drops from 8.4 to 5.3 on VAST; F1 improves from 71.4 to 74.2
**Condition**: VAST and SemEval-2016 datasets, both performance and bias reduction

**Evidence**: "WS-BERT and KASD outperform BERT and RoBERTa in the vast majority of the cases, respectively, highlighting the benefits of incorporating external knowledge."

## [POSITIVE] Knowledge-Augmented Framework (KASD)
RoBERTa-based encoding with episodic and discourse knowledge infusion for stance detection

**Delta**: KASD reduces ΔF1a to 0.8 vs BERT's 2.3 on VAST; F1 improves from 71.4 to 76.3
**Condition**: VAST dataset for both performance and bias reduction

**Evidence**: "WS-BERT and KASD outperform BERT and RoBERTa in the vast majority of the cases, respectively, highlighting the benefits of incorporating external knowledge."

## [POSITIVE] Teacher-Student Learning Framework (TTS)
A teacher-student framework that improves target diversity by assigning pseudo stance labels to augmented targets

**Delta**: Best F1 on both VAST (78.6) and SemEval-2016 (58.7); lowest bias on VAST (ΔPa=2.6, ΔPf=-2.6)
**Condition**: VAST dataset for bias reduction; mixed results on SemEval-2016 where bias metrics worsen

**Evidence**: "TTS achieves the best F1 score on both VAST and SemEval-2016 datasets"

## [NEGATIVE] Fine-tuning on Biased Training Data (SemEval-2016)
Training stance detection models on SemEval-2016 dataset which contains selection bias in gendered terms

**Delta**: Higher absolute average bias scores across all metrics compared to VAST-trained models
**Condition**: SemEval-2016 fine-tuning compared to VAST fine-tuning

**Evidence**: "results from Table 5 show that models fine-tuned on SemEval-2016 demonstrate higher bias than those trained on VAST, as evidenced by the higher absolute average score for each metric. This indicates the issue of selection bias, a source of bias that is rooted in the data chosen for training models."

## [POSITIVE] Gender-Balanced Training Data
Rule-based approach to balance noun phrases for each gender in training data by identifying gendered terms and inserting their opposites at random positions

**Delta**: BERT ΔPa drops from 7.6 to 0.0; WS-BERT ΔPf improves from -3.5 to 0.2; TTS F1 improves from 58.7 to 64.3
**Condition**: SemEval-2016 training data balancing

**Evidence**: "maintaining gender balance in the training set effectively reduces gender bias, while simultaneously achieving comparable or superior macro-average F1 scores on the original dataset (SemEval-2016)."

## [POSITIVE] GPT-4 Zero-Shot Inference
Using GPT-4 directly for zero-shot stance prediction without fine-tuning

**Delta**: Lowest bias scores: ΔF1a=0.2, ΔF1f=0.1, ΔPa=0.7, ΔPf=-1.5
**Condition**: Zero-shot stance detection on GenderStance

**Evidence**: "GPT-4 demonstrates the lowest bias on GenderStance, suggesting GPT-4's advanced capability to overcome inherent biases."

## [NEGATIVE] GPT-3.5 Zero-Shot Inference
Using GPT-3.5-turbo directly for zero-shot stance prediction without fine-tuning

**Delta**: ΔF1a=3.7, ΔF1f=2.7, ΔPa=1.4, ΔPf=-4.2, showing notable gender bias
**Condition**: Zero-shot stance detection on GenderStance

**Evidence**: "GPT-3.5 exhibits a high gender bias in the zero-shot setting, confirming the prevalence of gender bias in stance detection models."

## [NEGATIVE] RoBERTa Base Model
Using vanilla RoBERTa-base for stance classification instead of BERT

**Delta**: Higher bias than BERT on VAST: ΔPa=9.9 vs 8.4; ΔPf=-10.5 vs -8.8; slightly better F1 (73.1 vs 71.4)
**Condition**: VAST dataset; RoBERTa shows higher bias than BERT despite better F1

**Evidence**: "all models predominantly classify samples containing male nouns as Against and those with female nouns as Favor, as indicated by the positive ΔPa and negative ΔPf values"

## [POSITIVE] Diverse Gendered Noun Phrase Coverage
Including 30 noun phrases per gender covering common usages, gender-dominated occupations, and gender-dominated majors

**Delta**: enables comprehensive bias evaluation across varied gender representation contexts
**Condition**: GenderStance dataset construction for comprehensive bias measurement

**Evidence**: "The rationale behind our selection of gendered noun phrases is to include a variety of gender distribution characteristics, covering 10 common usages, 10 gender-dominated occupations and 10 gender-dominated majors."

## [POSITIVE] None-Label Neutral Instances
Creating 12k samples where gendered subjects merely joined a discussion, used to evaluate whether models support or oppose specific gender groups

**Delta**: enables evaluation of model tendency to support or oppose specific gender groups beyond Favor/Against labels
**Condition**: GenderStance evaluation of neutral stance predictions

**Evidence**: "we create a subset of 12k samples for label None using the template 'Text: [GEN] joined the discussion that [TOPIC]; Target: [GEN]'. Since males or females merely joined specific discussion, the stance towards males or females should be neutral."
