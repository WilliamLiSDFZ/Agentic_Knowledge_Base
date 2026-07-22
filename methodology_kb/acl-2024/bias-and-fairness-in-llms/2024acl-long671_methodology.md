# Investigating Cultural Alignment of Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.671/

## [POSITIVE] Native Language Prompting
Prompting LLMs in the dominant language of the target culture (e.g., Arabic for Egypt, English for the US) rather than a foreign language

**Delta**: +3.07 soft alignment for GPT-3.5 on Egypt with Arabic vs English; +2.18 for US with English vs Arabic
**Condition**: Applies to models with sufficient pretraining data in the target language (GPT-3.5, AceGPT-Chat); does not hold for LLaMA-2-Chat due to lack of Arabic pretraining data

**Evidence**: "using each country's dominant language prompts a notable increase in alignment compared to using the alternative language for both GPT-3.5 and AceGPT-Chat, according to both metrics"

## [POSITIVE] Arabic-Focused Finetuning (AceGPT)
Finetuning an English-pretrained LLaMA-2-Chat model on a mixture of Arabic and English data to improve Arabic cultural alignment

**Delta**: Improvement in alignment with Egypt survey across both metrics when prompted in Arabic compared to LLaMA-2-Chat
**Condition**: Applies when evaluating alignment with Egyptian culture; effect is positive for Egypt survey but negative for US survey

**Evidence**: "We observe an improvement in alignment with the Egypt survey across both metrics when the two models are prompted in Arabic (see Table 2 for a quantitative comparison). When prompted in English, the increase is evident only with the hard metric."

## [NEGATIVE] Arabic-Focused Finetuning (US Alignment Degradation)
Finetuning on Arabic data causes the model to lose some previously encoded US cultural knowledge

**Delta**: Decline in alignment with US survey after finetuning on Arabic data
**Condition**: Applies when evaluating AceGPT-Chat (Arabic-finetuned LLaMA-2) against the US survey

**Evidence**: "we note a decline in alignment following finetuning when evaluating alignment against the US survey, indicating that the model forgot some of its existing US cultural knowledge while adapting to data in another language."

## [NEGATIVE] Multilingual Pretraining (mT0-XXL)
Pretraining on a balanced mixture of multiple languages rather than predominantly English

**Delta**: Inferior cultural alignment with the US survey when prompted in English compared to Arabic; lower overall US alignment than GPT-3.5
**Condition**: Applies specifically to US cultural alignment; the curse of multilinguality causes unexpected language-alignment inversions

**Evidence**: "for the multilingual mT0-XXL, despite being trained on a more balanced language distribution, it appears to suffer from the curse of multilinguality (Pfeiffer et al., 2022), as evidenced by its inferior cultural alignment with the US survey when prompted in English compared to Arabic."

## [POSITIVE] Persona-Based Prompting
Instructing the model to role-play as a specific survey respondent described by six demographic dimensions (region, sex, age, social class, education level, marital status)

**Delta**: Enables persona-level cultural alignment measurement; baseline for all experiments
**Condition**: Used as the standard prompting approach across all models and experiments; forms the 'vanilla' baseline

**Evidence**: "To guide a language model with instruction-following support in order to respond like a specific subject from a particular demographic, we utilize personas... we query the model by a prompt that specifies the values for each demographic dimension of interest."

## [POSITIVE] Anthropological Prompting
A novel prompting method that instructs the model to reason using anthropological frameworks (emic/etic perspectives, cultural relativism, socioeconomic context, spatial/temporal dimensions) before answering survey questions

**Delta**: Soft: 0.5102 vs 0.4834 vanilla; Hard: 0.2838 vs 0.2443 vanilla
**Condition**: Tested on GPT-3.5 with English prompting for Egypt survey; generates only one response vs. five for vanilla (majority vote), yet still outperforms

**Evidence**: "Table 4: Anthropological prompting outperforms Vanilla prompting across both metrics in terms of cultural alignment with the Egypt survey. Results here are on GPT-3.5 with English prompting."

## [POSITIVE] Anthropological Prompting for Underrepresented Personas
Applying anthropological prompting specifically improves alignment for digitally underrepresented demographic groups (lower social class, lower education level)

**Delta**: More equitable alignment distribution across social classes and education levels
**Condition**: Applies to underrepresented personas (lower class, lower education); tested on GPT-3.5 with English prompting

**Evidence**: "we observe that anthropological prompting improves cultural alignment for participants from underrepresented backgrounds. Figure 5 illustrates this comparison between vanilla and anthropological prompting across Social Class and Education Level demographic dimensions. The alignment distribution among social classes and education levels becomes more equitable as a result."

## [POSITIVE] Majority Voting over Multiple Sampled Responses
Sampling five responses per question variant at temperature 0.7 and using majority vote to determine the final model answer

**Delta**: Provides more stable responses than single-sample; vanilla prompting uses 5 responses vs. anthropological prompting's 1, yet anthropological still wins
**Condition**: Applied to vanilla/persona-based prompting; anthropological prompting uses only one response and still outperforms

**Evidence**: "we sample five responses for each question variant using a temperature of 0.7. The model's response for a particular persona and question variant is determined by computing a majority vote over the sampled responses."

## [POSITIVE] Multiple Linguistic Variations per Question
Generating four paraphrases of each survey question using ChatGPT and prompting the model with each variant independently

**Delta**: Average consistency of 74.46% (English) and 72.81% (Arabic) across models
**Condition**: Applied to all models; English prompts yield higher consistency than Arabic prompts on average, except for AceGPT-Chat

**Evidence**: "For every question, we create four linguistic variations (i.e. paraphrases) by providing ChatGPT with a short description of the question along with the anticipated answer options from participants."

## [POSITIVE] Filtering Equivalent Cross-Country Personas
Excluding instances where equivalent personas from both Egypt and US surveys gave identical answers, to better assess the model's ability to distinguish between cultures

**Delta**: Produces more discriminative alignment scores; without filtering, trends are similar but scores differ slightly
**Condition**: Applied in main results (Table 2); Table 5 shows results without this filtering and confirms similar trends

**Evidence**: "We exclude instances where two subjects belonging to similar persona from both the Egypt and US surveys provided identical answers for a given question. This exclusion ensures a more accurate assessment of each model's capability in discerning the differences between the two cultures."

## [NEUTRAL] Soft Alignment Metric (Ordinal-Aware)
A relaxed accuracy metric that awards partial credit for ordinal questions based on proximity of chosen option to ground truth, defaulting to hard accuracy for categorical questions

**Delta**: Consistently higher scores than hard metric across all models and conditions
**Condition**: Used alongside hard metric for all evaluations; provides complementary view of alignment

**Evidence**: "Soft Metric Sf,c is a relaxed version of the hard metric which awards partial points in questions with an ordinal scale. However, if the question provides categorical options only or the subject in the survey responded with a 'don't know' (regardless of the scale), the metric defaults to plain accuracy."

## [NEGATIVE] Anglocentric / English-Majority Pretraining
Training LLMs predominantly on English data, resulting in higher cultural alignment with Western/US culture than non-Western cultures

**Delta**: Average soft alignment: 47.16 (Egypt) vs 59.07 (US) across all models
**Condition**: Affects all models tested; particularly pronounced for LLaMA-2-Chat and GPT-3.5 which are majority English pretrained

**Evidence**: "all LLMs considered in this work—regardless of being trained to be multilingual or finetuned on culture-specific data—are significantly more culturally aligned with subjects from the US survey than those from the Egypt survey."

## [POSITIVE] Higher Social Class / Education Level Persona
Prompting models with personas from higher social class or education level backgrounds

**Delta**: Monotonically increasing alignment as social class and education level increase
**Condition**: Observed across all models, prompting languages, and both surveys; reflects digital underrepresentation of lower-class populations in training data

**Evidence**: "as the background of individuals changes from lower to higher levels in both respective dimensions, alignment improves. This underscores that the models better reflect the viewpoints of specific demographics over others, with marginalized populations enjoying lower alignment."

## [POSITIVE] Male Persona Prompting
Prompting models with male personas vs. female personas

**Delta**: Higher alignment for male personas than female personas across models
**Condition**: Averaged across all models, prompting languages, and both surveys

**Evidence**: "the analysis of the sex dimension reveals that the models correspond more accurately to the actual survey when impersonating male respondents than female respondents."

## [POSITIVE] Older Age Group Persona
Prompting models with older age group personas

**Delta**: Higher alignment for older age groups than younger age groups
**Condition**: Averaged across all models, prompting languages, and both surveys

**Evidence**: "Similarly, older age groups exhibit higher alignment than younger age groups."

## [POSITIVE] Instruction-Tuned Model Selection
Using instruction-tuned (chat) variants of LLMs rather than base pretrained models for zero-shot survey simulation

**Delta**: Enables zero-shot adherence to persona and format instructions
**Condition**: Applied to all four models; base models without instruction tuning were found incapable of answering queries in Arabic

**Evidence**: "we opt for instruction-tuned models as they can be assessed in a zero-shot manner by adhering to the provided instructions"

## [NEGATIVE] Arabic Prompting for English-Dominant Model (LLaMA-2-Chat)
Prompting LLaMA-2-Chat (trained primarily on English) with Arabic language prompts

**Delta**: -3.28 soft alignment difference (Arabic vs English) for Egypt survey
**Condition**: Specific to LLaMA-2-Chat on Egypt survey; contrasts with GPT-3.5 and AceGPT-Chat where Arabic prompting helps

**Evidence**: "given that LLaMA-2-Chat is predominantly pretrained on English data, we observe that Arabic prompts are less effective in enhancing alignment with the Egypt survey and thus posit that the lack of Arabic data in the pretraining leads to lack of knowledge of Egyptian culture."

## [POSITIVE] Culturally Sensitive Topic Prompting (Social Values)
Asking questions on culturally sensitive themes such as Social Values, Political Interest, and Security

**Delta**: These three themes contribute most to the improvement in Egypt alignment when prompting GPT-3.5 in Arabic
**Condition**: Applies to GPT-3.5 on Egypt survey; Migration theme shows slight English advantage for US survey

**Evidence**: "The three themes that are contributing to the improvement in alignment in the Egypt survey when prompting in Arabic using GPT-3.5 are Social Values, Political Interest and Security."
