# Do Large Language Models Discriminate in Hiring Decisions on the Basis of Race, Ethnicity, and Gender?

**Source**: https://aclanthology.org/2024.acl-short.37/

## [POSITIVE] First-name substitution methodology
Replacing a [NAME] placeholder in templatic prompts with first names statistically associated with particular race/ethnicity and gender to measure discriminatory behavior in LLM hiring decisions

**Delta**: detected acceptance rate differences of 1.60% to 3.78% across demographic groups
**Condition**: Used across all models and templates to isolate the influence of name demographics on hiring decisions

**Evidence**: "This methodology of first-name substitution is well established in the social sciences and in NLP research for measuring biased or discriminatory behavior in humans or models"

## [POSITIVE] Template paraphrasing via ChatGPT
Using ChatGPT 3.5 to paraphrase an initial prompt template into four variations, resulting in five base templates, to mitigate model sensitivity to specific phrasings

**Delta**: descriptive (mitigates prompt sensitivity)
**Condition**: Applied during prompt construction to reduce idiosyncratic prompt-sensitivity effects

**Evidence**: "To mitigate the model's sensitivity to different template phrasings, we use ChatGPT 3.5 to paraphrase our initial template into four variations, resulting in five base templates."

## [POSITIVE] Pronoun removal from templates
Modifying templates to exclude gendered pronouns (she/he) so that only the first name signals demographic identity, avoiding confounding effects from pronouns

**Delta**: descriptive (controls for pronoun influence)
**Condition**: Applied to all final templates used in the study

**Evidence**: "We later choose to experiment with a modified template without any pronouns so that we can control any potential influence on model generation exerted by different pronouns like 'she' and 'he.' This would allow us to focus on studying the model behavior towards different first names."

## [POSITIVE] SVM with TF-IDF email classifier
Training a support vector machine classifier with TF-IDF features on 1,200 manually annotated emails to automatically label over 2 million generated emails as acceptances or rejections

**Delta**: F1 score of 0.98 on Llama2-13b generations; 0.97 accuracy on test set
**Condition**: Used for automated classification of all generated emails across all models

**Evidence**: "The classifier achieves an F1 score of 0.98 on the 170 valid emails randomly sampled from Llama2-13b generations, showing that accept and reject emails are easy to distinguish."

## [POSITIVE] Name redaction during classification
Removing applicant names from emails before training and applying the SVM classifier to prevent demographic bias from influencing the classification outcome

**Delta**: descriptive (mitigates classifier demographic bias)
**Condition**: Applied during both training and inference of the email classifier

**Evidence**: "To further mitigate the risk of demographic bias in the classifier, applicant names are redacted during training and usage."

## [POSITIVE] Permutation test for statistical significance
Conducting an adapted permutation test (5,000 permutations) comparing each demographic group's acceptance rate to the global population acceptance rate, combined across jobs using Fisher's method

**Delta**: detected statistically significant differences at p<0.01 and p<0.05 despite small absolute differences of 1.60%-3.78%
**Condition**: Applied to all group comparisons across all models and templatic settings

**Evidence**: "Despite the small magnitude, our permutation test testifies the statistical significance. A model that discriminates in a small but statistically significant manner can still be problematic."

## [NEUTRAL] Qualification level specification in prompts
Prepending sentences describing one of four candidate qualification levels (not specified, highly qualified, somewhat qualified, not qualified) to templates to test if LLMs make more informed decisions

**Delta**: descriptive (reveals interaction effects: unspecified qualification favors female names; partial qualification favors White male names)
**Condition**: Tested across Mistral-7b, Llama2-7b, and Llama2-13b with 41 occupational roles

**Evidence**: "When candidate qualification level is not specified, it appears that female names receive higher acceptance rates in general than male names; however, when candidates are described as only 'somewhat qualified' or 'not qualified,' White names, in particular White male names, appear most likely to receive acceptances."

## [POSITIVE] Under-specified occupational role setting
Including a condition where no job role is specified in the prompt to better isolate the influence of name demographics on hiring decisions without confounding from occupation-specific stereotypes

**Delta**: descriptive (isolates name demographic effect)
**Condition**: One of 41 occupational role conditions; used in all models including the reduced-scale GPT-3.5 and Llama2-70b experiments

**Evidence**: "We use under-specified inputs primarily to better isolate the influence of name demographics on hiring decisions. Including other applicant details (e.g., real-world or synthetic resumes) could confound the results or limit their generalizability."

## [POSITIVE] Multiple random seeds for reproducibility
Running experiments with 3 different random seeds for open-source models and reporting average results to ensure reproducibility despite non-zero temperature sampling

**Delta**: descriptive (ensures reproducibility)
**Condition**: Applied to Mistral-7b, Llama2-7b, and Llama2-13b; only one seed used for Llama2-70b due to computational constraints

**Evidence**: "For open-source models, we execute the experiments with 3 different random seeds for reproducibility and report the average results."

## [POSITIVE] Larger model size (Llama2-70b)
Using a 70-billion parameter version of Llama2 compared to 7b and 13b variants to examine whether model scale affects discriminatory behavior in hiring decisions

**Delta**: range of 1.6% between highest and lowest group acceptance rates, vs. 3.56% for Llama2-13b and 3.78% for GPT-3.5
**Condition**: Tested on a smaller scale (48,000 emails) with 7 occupational roles due to computational constraints

**Evidence**: "Llama2-70b appears to exhibit the least variation in acceptance rates across groups (Table 1), with a range of 1.6% between the groups with the highest and lowest overall acceptance rates... This observation may suggest that larger models could be more robust and fair in the task of generating hiring decision emails."

## [NEUTRAL] Occupation grouping by educational requirement
Grouping occupational roles by minimum educational requirement (doctoral, master's, bachelor's, high school, postsecondary non-degree, no formal education) to examine interaction effects between education level and demographic bias

**Delta**: descriptive (reveals that Black female advantage on Mistral-7b is limited to lower-education occupations)
**Condition**: Applied to Mistral-7b, Llama2-7b, and Llama2-13b across 41 occupational roles

**Evidence**: "When occupations are grouped by education level (Table 2), we observe that higher acceptance rates for Black female names on Mistral-7b only applies to occupations in the 'no formal education' and 'postsecondary non-degree award' categories."

## [NEGATIVE] Reduced experimental scale for large/API models
Running GPT-3.5-Turbo and Llama2-70b on a smaller subset of occupations (7 roles) and fewer templates due to computational and budget constraints

**Delta**: 19,200 emails for GPT-3.5 and 48,000 for Llama2-70b vs. 756,000 for smaller models
**Condition**: Applies only to GPT-3.5-Turbo and Llama2-70b experiments; limits comparability with smaller models

**Evidence**: "Because Llama2-70b and GPT-3.5-Turbo require heavier computational cost that exceeds our budget, we run the experiments on a smaller scale by reducing the number of occupations to 7 for both, having only one random seed for Llama2-70b, and having only two templates for GPT-3.5-Turbo."

## [NEUTRAL] Gender-occupation stereotype probing
Including stereotypically gendered occupations (e.g., secretary as feminine, carpenter as masculine) from WinoBias to test whether LLMs exhibit human-like gender-occupation stereotypes in hiring decisions

**Delta**: descriptive (GPT-3.5 shows lower acceptance for male candidates for secretary role, p<0.05 for White male)
**Condition**: Observed specifically for GPT-3.5 on the secretary role; not universal across all models or occupations

**Evidence**: "Table 4 shows that, for secretary, which is a stereotypically feminine occupation, GPT-3.5 generates a lower number of acceptance emails for male candidates compared to their female counterparts across racial and ethnic groups. While we observe this trend for some female- or male-dominated jobs, it may not be universally applicable to all occupational roles across models."
