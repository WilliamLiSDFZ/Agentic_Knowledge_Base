# Angry Men, Sad Women: Large Language Models Reflect Gendered Stereotypes in Emotion Attribution

**Source**: https://aclanthology.org/2024.acl-long.415/

## [POSITIVE] Persona-Based Prompting for Emotion Attribution
Prompting LLMs to adopt a gendered persona (man or woman) and then attribute emotions to events, using three different persona instruction templates from Gupta et al. (2023)

**Delta**: revealed consistent gendered emotion stereotypes across all 5 models
**Condition**: Applied across 5 LLMs (Llama2-7b, 13b, 70b, Mistral-7b, GPT-4) with ISEAR dataset events

**Evidence**: "We find strong evidence of gendered stereotyping across the five LLMs, which strongly aligns with findings in psychology and gender studies: models overwhelmingly link SADNESS with women and ANGER with men"

## [POSITIVE] Zero-Shot Learning (ZSL) Setup
Prompting models without any examples to perform emotion attribution, relying solely on the persona and event description

**Delta**: produced 227,580 emotion attributions across 7,586 events
**Condition**: Used for all experiments across all five models

**Evidence**: "One application of LLMs is to perform standard NLP tasks by formulating a specific request as the input prompt in a zero-shot learning (ZSL) setup, where no examples are provided to the model."

## [POSITIVE] Greedy Decoding with Temperature=0
Setting decoding temperature to 0 to minimize randomness and ensure reproducible results in LLM generation

**Delta**: ensured reproducible results
**Condition**: Applied to all model completions across all experiments

**Evidence**: "To minimize the randomness introduced in the generation, we use greedy decoding with the decoding temperature set to 0, a common practice in research involving LLMs to ensure reproducible results"

## [POSITIVE] Three Persona Instruction Templates
Using three different persona instruction templates (P1, P2, P3) from Gupta et al. (2023) to assign gendered personas to LLMs, prompting each event six times per model (3 templates × 2 genders)

**Delta**: consistent patterns observed across all three templates
**Condition**: Applied across all five models and all ISEAR events

**Evidence**: "A consistent pattern can be observed: When attributing emotions to men, the model consistently associates events with ANGER... Conversely, the model tends to attribute women to SADNESS"

## [NEUTRAL] Single-Emotion Response Constraint
Instructing models to answer with a single emotion word and omit explanations to standardize output format

**Delta**: resulted in 9,641 unique responses including multi-word responses, emojis, and refusals requiring filtering
**Condition**: Applied in the main quantitative experiment; some models did not comply

**Evidence**: "Note that although we constrain the prompt for the model to return a single emotion, the response does not always meet this format."

## [NEUTRAL] Post-Generation Filtering of Multi-Word Responses
Removing model responses with more than one word and normalizing grammatical variations (e.g., 'angry' to 'anger') to create a clean emotion dataset

**Delta**: reduced dataset from 227,580 to 212,936 completions with 471 unique emotion-related words
**Condition**: Applied as preprocessing step before quantitative analysis

**Evidence**: "To identify the emotions linked to each gendered persona, we remove any model responses with more than one word and accommodate grammatical variations (e.g., angry to anger, sad to sadness, etc.). After filtering those responses, our dataset consists of 212,936 emotion attribution completions"

## [POSITIVE] Constrained Emotion Prediction to ISEAR Gold Labels
Adapting the task prompt to restrict model predictions to the seven predefined ISEAR emotions (anger, fear, sadness, joy, disgust, guilt, shame) for performance evaluation against gold labels

**Delta**: revealed that ANGER overpredicted for men (R: 0.93, P: 0.51) and SADNESS overpredicted for women (R: 0.98, P: 0.46)
**Condition**: Applied only to Llama2-13b for performance evaluation in Section 5.1

**Evidence**: "The model overpredicts male ANGER (R: 0.93, P: 0.51) but underpredicts it for women ANGER (R: 0.49, P: 0.81). Conversely, it overpredicts women SADNESS (R: 0.98, P: 0.46) but accurately predicts it for men (R: 0.88)."

## [POSITIVE] Qualitative Explanation Generation
Adding an instruction to provide a short explanation alongside the emotion attribution to uncover the rationale behind gendered emotion predictions

**Delta**: identified three common trends: different emotions with gendered explanations, same emotions with stereotypical explanations, and model refusals for one gender
**Condition**: Applied as a secondary qualitative analysis in Section 5.2

**Evidence**: "To uncover the underlying rationale behind the model's attributions, we guided them to provide explanations by adding the instruction in bold in the task prompt: 'Answer with a single emotion and provide a short explanation'"

## [POSITIVE] ISEAR Dataset as Event Source
Using the International Survey On Emotion Antecedents And Reactions (ISEAR) dataset of 7,665 self-reported events with gold emotion labels and respondent gender information

**Delta**: enabled comparison of model predictions against real human emotional reports, showing model stereotyping does not reflect lived experiences
**Condition**: Used as the primary event source and evaluation benchmark throughout the study

**Evidence**: "Since ISEAR provides the gender of the respondent who experienced the event, we use this information to evaluate the prediction of our models... the model's tendency to associate ANGER with men and SADNESS with women is not reflective of actual reported emotions"

## [POSITIVE] Chi-Squared Statistical Significance Testing
Using chi-squared tests to verify that observed differences in emotion attribution frequencies between genders are statistically significant

**Delta**: differences significant at p < 0.01 for most emotions across all models
**Condition**: Applied to aggregated emotion-gender frequency data in Table 5

**Evidence**: "these differences are statistically significant at p > 0.01 (χ2 test), supporting our hypothesis that LLMs predict different emotions based on gender"

## [POSITIVE] Emotion Attribution Shift Analysis
Analyzing what emotions are attributed to one gender when the other gender is attributed a specific emotion (e.g., what women are attributed when men are attributed ANGER)

**Delta**: 53% of ANGER-for-men events also attributed ANGER to women, with notable shift to SADNESS, FEAR, HURT, BETRAYAL for women
**Condition**: Applied to the two most extreme cases: ANGER for men and SADNESS for women

**Evidence**: "While the majority (53%) of these events were also ascribed ANGER for women, we find a notable shift from ANGER in men to emotions like SADNESS, FEAR, HURT and BETRAYAL for women"

## [NEGATIVE] Larger Model Size in Llama2 Family
Testing multiple sizes of Llama2 (7b, 13b, 70b parameters) to examine whether model scale affects gendered emotion stereotyping

**Delta**: Llama2-70b attributed ANGER to men four times as often as women (3,270 vs 645); Llama2-13b attributed PRIDE to men over seven times more than women
**Condition**: Observed specifically in the Llama2 model family; larger models showed stronger stereotyping

**Evidence**: "The models in the Llama2 family show the strongest distortion. In particular, Llama2-70b attributed ANGER to men four times as often as it did women (3,270 times vs 645 times). Llama2-13b attributed PRIDE to men over seven times more often than it did to women."

## [POSITIVE] Mistral-7b Instruction-Tuned Model
Using the instruction-tuned version of Mistral-7b (Mistral-7b-Instruct-v0.1) as one of the evaluated models

**Delta**: least distorted gender distribution among all tested models
**Condition**: Compared against Llama2 family and GPT-4 in the same experimental setup

**Evidence**: "Mistral-7b appears to have the least distorted distribution between genders, followed by GPT-4. However, we still find significant differences between the genders for most emotions."

## [NEUTRAL] Binary Gender Framework
Restricting persona assignment to binary gender categories (man/woman) due to constraints of the ISEAR dataset and existing literature

**Delta**: enabled comparison with psychology literature but limits generalizability to non-binary gender identities
**Condition**: Applied throughout all experiments as a data-motivated design constraint

**Evidence**: "We use binary gender here since we do not have more fine-grained information in the ISEAR data (the gold labels used in our evaluation). Further, the literature that motivates and underpins our work relies on this framework to investigate gendered stereotypes in emotional experiences."

## [POSITIVE] Unique Emotion Word Analysis per Gender
Examining emotion-related words generated exclusively for each gender to identify stereotypical language patterns

**Delta**: identified stereotypical words: women associated with 'hysteria', 'helpless', 'nurturing'; men with 'arrogance', 'authority', 'bravery'
**Condition**: Applied as supplementary qualitative analysis in Section 5

**Evidence**: "Women-associated words like 'hysteria,' 'overjoyed,' 'helpless', and 'nurturing' are consistent across models. Similarly, we found words like 'arrogance,' 'authority,' and 'bravery' for men."
