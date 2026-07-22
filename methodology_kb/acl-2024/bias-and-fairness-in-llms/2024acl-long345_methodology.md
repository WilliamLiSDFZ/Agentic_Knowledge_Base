# Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.345/

## [POSITIVE] Culture-Aware Prompting (P1)
Explicitly identifying the query language culture in the prompt using the format 'In the culture of [lang], {query}'

**Delta**: Non-English In-Culture Score from 1.4 to 9.9
**Condition**: Applied to concrete cultural objects in ChatGPT; less effective on abstract cultural objects

**Evidence**: "P1 works significantly better than P2. Table 5 lists the results of prompting... Non-English: None=1.4, P1=9.9"

## [NEGATIVE] Culture-Aware Prompting (P2)
Guiding the model to consider the culture associated with the query language without specifying the language name: '{query}, consider the culture associated with the query language'

**Delta**: Non-English In-Culture Score from 1.4 to 1.1
**Condition**: Applied to concrete cultural objects in ChatGPT

**Evidence**: "The model cannot understand the instruction 'the culture associated with the query language,' and always replies 'As an AI language model, I do not have a specific culture associated with me.'"

## [POSITIVE] Pretraining on More Diverse Multilingual Data
Training LLMs on a more balanced mix of non-English data, as exemplified by ERNIE Bot trained on both English and a 4TB high-quality Chinese text corpora

**Delta**: Chinese In-Culture Score: ERNIE 7.6 vs GPT-4 1.8; WVS Euclidean distance to HRef: ERNIE 0.24 vs GPT-4 0.34
**Condition**: Evaluated on Chinese language queries for both concrete and abstract cultural objects

**Evidence**: "pretraining on more diverse data significantly mitigates the cultural dominance problem. ERNIE's responses to Chinese questions align more with Chinese culture than GPT-4 in both concrete (7.6 vs. 1.8) and abstract cultural objects (0.24 vs. 0.34 and 0.10 vs. 0.28)"

## [NEGATIVE] RLHF Safety Alignment (English-dominant)
Reinforcement learning from human feedback with safety alignment data predominantly in English, as applied in later GPT models

**Delta**: GPT-4 non-English average In-Culture Score 1.2 vs text-davinci-003's 3.1; GPT-4 WVS distance to MEn=0.08 vs text-davinci-003's 0.16
**Condition**: Affects non-English language cultural alignment across GPT model versions

**Evidence**: "One possible reason is the alignment efforts by OpenAI that later GPT models are trained with more safety alignment, the majority of which is in English... the later version of the GPT variant, the more cultural dominance it suffers from."

## [NEGATIVE] GPT Model Version Progression (text-davinci-003 → ChatGPT → GPT-4)
Successive iterations of GPT models with increasing capability and alignment training

**Delta**: Non-English avg In-Culture Score: text-davinci-003=3.1, ChatGPT=1.4, GPT-4=1.2
**Condition**: Measured on non-English concrete and abstract cultural objects

**Evidence**: "Generally, the later version of the GPT variant, the more cultural dominance it suffers from... the results in different languages become more concentrated with the development of GPT models"

## [NEUTRAL] In-Culture Score Evaluation Metric
A metric that counts how many of the 10 generated items comply with the culture of the query language, determined by Wikipedia annotations

**Delta**: None
**Condition**: Used for evaluating concrete cultural objects across all models and languages

**Evidence**: "The In-Culture Score is determined by the following principles: For each question in a specific language, we annotate the source of the returned 10 items according to Wikipedia... The higher the In-Culture Score an LLM achieves for a specific language, the less cultural dominance in the LLM for this language."

## [NEUTRAL] Euclidean Distance Evaluation for Abstract Cultural Objects
Measuring the Euclidean distance between model output and human reference results in the coordinate system of WVS and PCT surveys

**Delta**: None
**Condition**: Used for evaluating abstract cultural objects (values and opinions) across all models

**Evidence**: "For each language l, we compute the Euclidean distance between the model output Ml and a target T in the coordinate system of survey... Ideally, if an LLM is not dominated by English culture, the model output in a non-English language should be more similar to the reference human result in this language"

## [NEGATIVE] Multilingual Query Prompting Without Culture Specification
Querying LLMs using translated prompts in native languages without specifying cultural context, simulating normal user behavior

**Delta**: Average non-English In-Culture Score of 1.4 vs English score of 7.3 for ChatGPT
**Condition**: Applied to all non-English languages in the benchmark evaluation

**Evidence**: "when non-English users communicate with ChatGPT in their native language, the primary cultural output from ChatGPT remains entrenched in English culture... the average in-culture score is much lower, with an average of 1.4"

## [NEUTRAL] World Values Survey (WVS) for Abstract Cultural Evaluation
Using the multilingual WVS questionnaire with 18 statements about values and beliefs to probe LLM cultural opinions

**Delta**: None
**Condition**: Used to evaluate abstract cultural dominance across 6 languages

**Evidence**: "ChatGPT's responses in different languages present consistent opinions almost the same as the human and model results in English... The model outputs in non-English languages are closer to the results of the dominated English language in all cases rather than to their human reference"

## [NEUTRAL] Political Coordinates Test (PCT) for Abstract Cultural Evaluation
Using the multilingual PCT with 36 political statements to measure LLM political and social value alignment across cultures

**Delta**: None
**Condition**: Used to evaluate abstract cultural dominance across 6 languages

**Evidence**: "Table 3(c) visualizes the distribution of different languages, where the results in different languages become more concentrated with the development of GPT models (e.g., PCT results for ChatGPT vs. GPT-4)"

## [POSITIVE] Prompting on Abstract Cultural Objects
Applying culture-aware prompting (P1) to abstract value and opinion survey questions

**Delta**: WVS HRef distance: Non-English from 0.39 to 0.24; PCT HRef distance: from 0.25 to 0.15
**Condition**: Applied to abstract cultural objects; less effective than pretraining on diverse data for abstract objects

**Evidence**: "While prompting works better than ERNIE on concrete cultural objects, it underperforms ERNIE on abstract objects... a simple instruction of 'in the culture of [lang] language' can guide the model to produce correct answers for the concrete cultural objects"
