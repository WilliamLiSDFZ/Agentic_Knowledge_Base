# Investigating Subtler Biases in LLMs: Ageism, Beauty, Institutional, and Nationality Bias in Generative Models

**Source**: https://aclanthology.org/2024.findings-acl.530/

## [POSITIVE] Bidirectional Bias Evaluation (SAI and ASA)
Measuring bias in two directions: Stimulus to Attribute Inference (SAI) where a social group descriptor is given and the model selects an attribute, and Attribute to Stimulus Association (ASA) where an attribute is given and the model selects a social group descriptor.

**Delta**: reveals additional bias patterns not captured by unidirectional evaluation
**Condition**: Nationality bias domain; SAI direction shows partial mitigation while ASA direction reveals persistent bias across all models

**Evidence**: "In the SAI direction, we fail to reject the null hypothesis for GPT-4 and Llama-2. For PaLM-2 and Mistral, we see relatively small effect sizes. In the ASA direction, however, we see statistically significant results for all models. This suggests that the results we see in the SAI direction are reflective of the prior work in bias mitigation in the area of race, ethnicity, and nationality. This work does not however carry over in the ASA direction."

## [POSITIVE] Template-Generated Dataset with Fill-in-the-Blank Style
Using sentence completion templates where models must choose among three options (positive, negative, neutral) to fill a blank, enabling semi-automatic large-scale dataset creation with minimal human annotation.

**Delta**: 11,940 test instances generated across 4 bias domains
**Condition**: Dataset creation for bias evaluation across ageism, beauty, institutional, and nationality domains

**Evidence**: "We introduce a template-generated dataset of sentence completion tasks that asks the model to select the most appropriate attribute to complete an evaluative statement about a person described as a member of a specific social group... This dataset can be used as a benchmark to evaluate progress in more generalized biases and the templating technique can be used to expand the benchmark with minimal additional human annotation."

## [POSITIVE] Exhaustive Gender Pronoun Inclusion
Including all three common pronoun sets (masculine he/him, feminine she/her, non-binary they/them) uniformly across all templates to control for gender bias confounds.

**Delta**: small effect sizes even where statistically significant; τ values range from 0.011 to 0.032
**Condition**: All bias domains; used to control for gender confounds and analyze gender bias independently

**Evidence**: "To avoid potential confounding effects of gender bias, which has been found in prior NLP systems (Bolukbasi et al., 2016), we exhaustively (and uniformly) include the three most common sets of pronouns... Table 4 shows the dataset-wide statistical tests while controlling for gender. We maintain statistically significant correlations for all settings and there are no major differences in results across genders."

## [POSITIVE] Education Level Control for Institutional Bias
Including first-year, second-year, and teacher descriptors in institutional bias templates to control for the confounding effect of education level on institution type associations.

**Delta**: maintains statistical significance in all cases except Mistral SAI direction after controlling
**Condition**: Institutional bias domain; reveals that Mistral's SAI institutional bias is partly explained by education level confound

**Evidence**: "Table 3 shows the τ-test results for institutional bias while controlling for educational level. We maintain statistical significance in every case except Mistral in the SAI direction. The institutional bias we see from Mistral in the SAI direction (in Table 2) can be explained by the underlying correlation between education level and institution type."

## [POSITIVE] Kendall's τ Correlation Test
Using Kendall's τ rank correlation test instead of χ² test to measure the association between stimulus polarity and attribute selection, exploiting the natural ordinal ordering of negative, neutral, and positive categories.

**Delta**: null hypothesis rejected in all 8 model-direction combinations overall (p values as low as 4.70e-235)
**Condition**: Statistical analysis across all bias domains and models

**Evidence**: "We selected the Kendall's τ test instead of the χ2 test because there is a natural order to negative, neutral, and positive categorical values... The null hypothesis is rejected in all eight settings. This serves as a clear indication of a pattern of bias in modern LLMs."

## [NEGATIVE] 4-bit Quantization of Open-Source LLMs
Using 4-bit quantized versions of Llama-2-13B and Mistral-7B due to resource constraints.

**Delta**: potentially suppresses age-related bias; Llama-2 SAI ageism τ=0.094 vs GPT-4 τ=0.192
**Condition**: Ageism bias domain for Llama-2 and Mistral models

**Evidence**: "The effect size for Llama-2 is considerably smaller than for GPT-4 and PaLM-2, suggesting that unknown engineering decisions made for proprietary models exacerbate age-related bias in LLMs or that quantization of LLMs suppress age-related bias."

## [POSITIVE] Generalized Positive-Negative Polarity Bias Measurement
Measuring bias in terms of general positive/negative attribute associations rather than specific stereotypes (e.g., 'Asians are good at math'), capturing subtler correlated decisions between social groups and unrelated attributes.

**Delta**: statistically significant bias detected across all 4 models and most domain-direction combinations
**Condition**: All bias domains; particularly effective for beauty bias (τ up to 0.889 for PaLM-2 SAI)

**Evidence**: "We find that current LLMs show a pattern of bias in the domains we considered save for a few specific model-domain combinations... Beauty-bias results are statistically significant for all models in both SAI and ASA directions and the effect sizes are among the largest across the board."

## [NEUTRAL] GDP Per Capita as Nationality Stimulus Proxy
Categorizing countries into positive (rich) and negative (poor) stimuli based on GDP per capita from IMF data, selecting top 15 and bottom 15 countries.

**Delta**: nationality bias detected in ASA direction for all models but SAI direction fails to reject null for GPT-4 and Llama-2
**Condition**: Nationality bias domain; proxy is noisy approximation noted as a limitation

**Evidence**: "In the SAI direction, we fail to reject the null hypothesis for GPT-4 and Llama-2. For PaLM-2 and Mistral, we see relatively small effect sizes. In the ASA direction, however, we see statistically significant results for all models."

## [POSITIVE] University vs. Community College Institutional Stimulus Split
Dividing institutional stimuli into top 100 national universities (positive) and top 100 community colleges by enrollment (negative), ensuring state-level representation.

**Delta**: GPT-4 SAI institutional bias τ=0.573 (p=2.9e-147); among the largest effect sizes observed
**Condition**: Institutional bias domain across all models

**Evidence**: "The institutional bias results are again significant across the board. GPT-4 in the SAI direction and Llama-2 in the ASA direction stand out as having particularly large effect sizes. That is GPT-4 is very likely to predict positive character traits for people associated with high-ranking institutions while Llama-2 is very likely to predict a high-ranking institution for people with positive character traits."

## [POSITIVE] Beauty-Profession Interaction Sub-category
Separating beauty bias into general personality trait associations and profession associations, using income-based profession categorization (high >100k, mid 50k-70k, low <40k annual wage) as positive/neutral/negative.

**Delta**: beauty profession effect sizes smaller than general beauty bias (e.g., GPT-4 SAI: τ=0.451 vs τ=0.870 for general beauty)
**Condition**: Beauty bias domain; profession sub-category shows weaker but still significant bias

**Evidence**: "Here we again see statistically significant results in every model-setting combination. The effect sizes here are smaller than for the beauty bias setting. While LLM generations correlate beauty terms with high-income professions, this bias is not as severe as that for positive character traits."

## [NEUTRAL] Adjectival and Nominal Attribute Variations
Using both adjectival (e.g., 'friendly') and nominal (e.g., 'friendliness') forms of attributes to ensure grammaticality across different template sentence structures.

**Delta**: ensures grammatical validity of templates
**Condition**: All bias domains during dataset construction

**Evidence**: "We have adjectival and nominal variations of attributes to ensure grammaticality. For example, in 'It is clear that the man, who comes from South Sudan, is friendly.', we use the adjectival form 'friendly'. In 'He is known for his friendliness; he is from South Sudan.', we use the nominal form 'friendliness'."

## [NEUTRAL] City Population as Neutral Institutional Stimulus
Using US cities by population as neutral stimuli in the ASA direction for institutional bias, since there is no obvious neutral category for educational institutions.

**Delta**: enables consistent data collection but acknowledged as a proxy approximation
**Condition**: Institutional bias ASA direction only

**Evidence**: "Here we use cities in USA by population as neutral stimuli (e.g., New York, Tampa, etc.). There are no obvious categories for neutral educational institutions. And cities are substitutable in the sentence constructions. We select cities as a proxy of neutral stimuli to make our data collection process easier and consistent like other bias categories."

## [POSITIVE] Follow-up Experiment Excluding Institution Type Keywords
Analyzing results for institutions that do not include the words 'university' or 'community college' in their names (e.g., MIT, Dallas College) to rule out keyword-driven rather than institution-driven bias.

**Delta**: overall trend consistent with main results; Mistral SAI additionally rejects null hypothesis in this setting
**Condition**: Institutional bias domain; robustness check for keyword confound

**Evidence**: "To address this we perform a follow-up experiment where we analyzed the results for positive institutions that do not include the word 'university' (e.g., MIT) and negative institutions that do not include the phrase 'community college' (e.g., Dallas College). The overall trend is consistent with that of Table 2's institutional bias, with the only difference being that in this experimental setup, in the SAI direction, the Mistral model rejects the null hypothesis."

## [NEUTRAL] Age Range Selection Based on Work Setting Relevance
Selecting young (25-35) and old (60-70) age ranges based on Cameron (1969) experimental results, pushed toward middle age to maintain relevance in work settings.

**Delta**: ageism bias detected in 3 of 4 models; Mistral fails to reject null hypothesis
**Condition**: Ageism bias domain; Mistral shows no statistically significant ageism bias (SAI τ=0.026, p=0.4776)

**Evidence**: "We select these age ranges based on the experimental results from Cameron (1969) while pushing all age groups more towards middle age to make them relevant in the work setting. Many of our template sentences for ageism assume a work setting."

## [NEUTRAL] Random Triple Sampling for Options
Randomly picking one triple of positive, negative, and neutral attributes (or stimuli in ASA) for each template instance rather than using all combinations.

**Delta**: enables large-scale dataset generation while maintaining balance across option types
**Condition**: All bias domains during dataset construction

**Evidence**: "When we select attributes in the SAI direction, we randomly pick one triple of positive, negative, and neutral attributes (e.g., friendly, unfriendly, and carefree). In ASA direction, we swap the stimuli and attributes. We use every term from the attributes list with each sentence template and randomly select one triple of positive, negative, and neutral stimuli."
