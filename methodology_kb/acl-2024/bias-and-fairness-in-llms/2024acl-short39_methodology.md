# Born Differently Makes a Difference: Counterfactual Study of Bias in Biography Generation from a Data-to-Text Perspective

**Source**: https://aclanthology.org/2024.acl-short.39/

## [POSITIVE] Counterfactual Data-to-Text Methodology
Manipulating personal attributes of interest (gender, region) while keeping co-occurring attributes unchanged to study causal effects on biography generation

**Delta**: enables isolation of individual attribute effects
**Condition**: Bias analysis in biography generation using fictional SynthBio dataset

**Evidence**: "We propose a counterfactual methodology based on a data-to-text framework. We formulate the task as generating biographies by given attributes... By doing so, we maintain a controllable setting, enforcing biography generation focusing on the given attributes, thus allowing us to study the effect of individual personal attributes."

## [POSITIVE] Flan-T5-base Fine-tuning on WikiBio
Fine-tuning Flan-T5-base on the WikiBio dataset for 10,000 steps to generate biographies from structured infobox attributes

**Delta**: RougeL 26.4 vs 22.6, PARENT-F 0.114 vs 0.049
**Condition**: Biography generation on SynthBio evaluation set

**Evidence**: "Our fine-tuned Flan-T5 model outperforms the T5 model (Raffel et al., 2020) reported in the Synthbio dataset (Yuan et al., 2021), with a RougeL score of 26.4 (vs., 22.6) and a PARENT-F score (Dhingra et al., 2019) of 0.114 (vs., 0.049)."

## [POSITIVE] SynthBio Synthetic Dataset for Evaluation
Using a synthetic dataset of fictional individuals created via human-AI collaboration to mitigate cross-contamination with training data and celebrity memorization effects

**Delta**: mitigates LLM memorization of celebrity names
**Condition**: Evaluation phase to avoid LLM memorization of real celebrity biographies

**Evidence**: "To mitigate the cross-contamination of training and evaluation sets (Roberts et al., 2020; Li and Flanigan, 2023), we use the Synthbio dataset (Yuan et al., 2021) for evaluation, which is a synthetic dataset consisting of structured attributes describing fictional individuals."

## [POSITIVE] Attribute Reordering in Input Construction
Reordering the attribute list in the input to place name, gender, and nationality as the top 3 attributes to ensure the model generates biographies based on personal attributes of interest

**Delta**: gender accuracy >0.8 across all gender groups
**Condition**: Input construction for Flan-T5 biography generation

**Evidence**: "To ensure the model generates biographies based on the personal attributes of interest. We reorder the attribute list in the input, moving name, gender, and nationality to the top 3 attributes in order."

## [NEGATIVE] Attribute Masking (Masked Attributed Biography)
Generating biographies without the personal attribute of interest to study its individual effect by comparison

**Delta**: no significant differences observed between true and masked attributed biographies
**Condition**: Attempting to isolate individual attribute effects by masking

**Evidence**: "Compared to truly attributed biographies (Figure 2, purple bars), we do not observe significant differences in gender and region... Masking the personal attributes alone is not effective in understanding the influence of individual personal attributes."

## [POSITIVE] Data-QuestEval for Semantic Matching
Reference-free semantic evaluator for data-to-text evaluation using QA format with T5-based QG/QA models to measure answer correctness

**Delta**: reveals significant differences among gender groups in semantic matching
**Condition**: Evaluating how well generated biographies represent given attributes

**Evidence**: "We use Data-QuestEval (Rebuffel et al., 2021), a reference-free semantic evaluator curated for data-to-text evaluation developed in a QA format... Figure 2 shows that generated biographies are significantly different among different gender groups (purple bars, gender) in semantic matching and sentiment."

## [POSITIVE] SentiWords Lexical Sentiment Scoring
Lexical-based sentiment evaluation using SentiWords dictionary (~155,000 words) to calculate average sentiment score of biographies

**Delta**: reveals sentiment differences across gender and region groups (e.g., Male positive regard 0.71 vs Female 0.63 vs Non-Binary 0.54)
**Condition**: Sentiment analysis of generated biographies; chosen over social-media-focused evaluators

**Evidence**: "we use a lexical-based method, obtaining the sentiment score by retrieving SentiWords (Gatti et al., 2015), a dictionary associating positive or negative scores with approximately 155,000 words... we observe similar patterns to that of sentiment (Appendix F)."

## [NEUTRAL] Regard Metric Evaluation
Additional evaluation using regard metric to measure positive/negative regard towards demographic groups, used as a complement to sentiment

**Delta**: similar patterns to sentiment metric
**Condition**: Supplementary evaluation of true attributed generated biographies

**Evidence**: "In line with the study of sentiment, we additionally experiment with the regard evaluation (Sheng et al., 2019), a metric measuring if the regard towards a particular identity/demographic group is positive or negative. We observe similar patterns to that of sentiment (Appendix F)."

## [POSITIVE] Nationality Filtering Threshold (>0.75)
Selecting only nationalities/regions where the proportion of generated biographies explicitly mentioning the nationality exceeds 0.75 for counterfactual analysis

**Delta**: counterfactual nationality encoding improved from 45.9% (raw) to 80.9% (selected)
**Condition**: Filtering counterfactual region biographies for quality assurance

**Evidence**: "we select nationalities that have a score larger than 0.75 for the analysis based on our empirical experience where similar patterns are observed with different thresholds among different region groups (details in Appendix D), resulting in a score of 80.9% (Table 2, Counterfactual-Selected)."

## [POSITIVE] Pronoun-based Gender Inference
Using pronouns as a proxy to infer gender from generated biographies to validate that given gender attributes are encoded

**Delta**: gender accuracy >0.8 for all groups (Male: 0.999, Female: 0.972, Non-Binary: 0.837)
**Condition**: Validation that generated biographies encode the given gender attribute

**Evidence**: "for gender, we use the pronouns as the proxy of gender (De-Arteaga et al., 2019) and compare it against the given gender attribute... for gender, we achieve higher than 0.8 accuracy across gender groups, confirming that the given gender is encoded in generated biographies."

## [NEUTRAL] Rule-based Nationality Keyword Matching
Checking whether nationality or related country name is explicitly mentioned in the biography as a proxy for nationality encoding, instead of training a classifier

**Delta**: true nationality encoding varies widely (0.303 to 0.980 across nationalities)
**Condition**: Validation of nationality encoding in generated biographies

**Evidence**: "For the region, since there is no direct method to predict the nationality from the biography, we consider whether the nationality or related country name is mentioned in the biography as the proxy of the nationality encoded in the biography. We do not train a classifier for nationality as the biography contains rich personal information—the classifier may remember the training instances instead of the nationality signals."

## [NEUTRAL] Beam Search Decoding (beam=5)
Using beam search with beam size 5 for biography generation on the SynthBio dataset

**Delta**: not separately quantified
**Condition**: Inference/generation phase on SynthBio evaluation set

**Evidence**: "To generate biographies on the Synthbio, we use a beam search of 5."

## [POSITIVE] Gender Attribute Addition to WikiBio
Explicitly adding gender labels (male, female, non-binary/identifiable) inferred from pronouns in the biography paragraph to the WikiBio infoboxes

**Delta**: enables gender-conditioned biography generation and bias analysis
**Condition**: Training data preparation for WikiBio fine-tuning

**Evidence**: "We explicitly add the gender label (male, female or non-binary/identifiable), inferring from the pronouns in the paragraph (DeArteaga et al., 2019), to the infobox."

## [POSITIVE] Co-occurring Attribute Analysis
Investigating the effect of co-occurring attributes (attributes correlated with the attribute of interest) on biography generation by comparing biographies with same individual attribute but different co-occurring attributes

**Delta**: significant differences found (p=0.0) for gender co-occurring attributes in both semantic matching and sentiment
**Condition**: Counterfactual analysis of gender and region biography generation

**Evidence**: "We find a significant difference towards different co-occurring attributes of the gender groups in both semantic matching and sentiment, e.g., M, co(M) (blue, slash) vs., M, co(F) (blue, dot), echoing the finding in Section 3."

## [POSITIVE] Region Grouping of Nationalities
Manually mapping 40 nationalities to 6 regions (NA, EU, ME, AP, SA, AF) based on Wikipedia continent categories to enable region-level bias analysis

**Delta**: reveals significant regional differences (e.g., AF vs AP in both semantic matching and sentiment)
**Condition**: Region-level bias analysis in biography generation

**Evidence**: "Inspired by Min et al. (2023), we manually map the 40 nationalities to 6 regions based on Wikipedia continent categories... We observe significant differences in some region groups, e.g., AF vs., AP in both measurements, indicating the potential bias among region groups."
