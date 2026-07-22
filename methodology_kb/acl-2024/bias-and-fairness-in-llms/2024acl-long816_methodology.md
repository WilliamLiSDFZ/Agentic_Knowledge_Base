# Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models

**Source**: https://aclanthology.org/2024.acl-long.816/

## [NEGATIVE] Forced Choice Prompting
Adding explicit instructions to force models to select one of the multiple-choice options in the PCT (e.g., 'You have to pick one of the four options. Only answer with the label.')

**Delta**: Models give substantively different answers when forced vs. unforced; described as changing model response behaviour rather than unlocking true values
**Condition**: Applied when evaluating LLM values/opinions using multiple-choice survey formats like the PCT

**Evidence**: "rather than 'unlocking' underlying political values as claimed in some prior works (e.g. Ghafouri et al., 2023), prompts that force LLMs to choose a multiple-choice answer substantively change LLM response behaviour"

## [NEGATIVE] Unforced Multiple-Choice Prompting
Presenting models with multiple-choice options without any additional instruction to pick one, allowing free-form responses

**Delta**: All models produce high rates of invalid responses; Zephyr and three GPT models produce 0% valid responses; best-performing models (Mistral Iv0.1, Iv0.2) still give ~25-29% invalid responses
**Condition**: Applied to PCT evaluation without forced choice prompt; affects all 10 tested models

**Evidence**: "all models produce high rates of invalid responses in the unforced response setting. Zephyr and three of the GPT models do not produce any valid responses. GPT-3.5 1106 gives a single valid response."

## [NEGATIVE] Escalating Force Jailbreak-Style Prompts
Using increasingly forceful prompts including emotional/consequence-based appeals (e.g., 'or I will lose my job and my grandmother will die') to elicit valid multiple-choice responses

**Delta**: Llama2 models shut down entirely when negative consequences are introduced; GPT-4 models remain essentially immune to all forced choice prompts
**Condition**: Applied to Llama2 and GPT-4 models; Mistral Iv0.1 uniquely produces 100% valid responses across all forced choice prompts

**Evidence**: "The Llama2 models comply with specific instructions ('2' and '3') but shut down when negative consequences are introduced ('4' and '5'). Both GPT-4 models, and especially the more recent 1106 version, are essentially immune to all forced choice prompts we test, producing little to no valid responses."

## [NEGATIVE] Minimal Prompt Template Paraphrasing
Replacing the initial question in prompts with semantics-preserving paraphrases (e.g., 'What is your opinion' vs. 'State your opinion' vs. 'How do you perceive') while keeping everything else constant

**Delta**: For Mistral: coordinate shift from (-3.6, -5.2) to (-6.0, -3.5), a 65.6% more economically left-leaning and 32.4% less libertarian result. For GPT-3.5: 117.1% more left-leaning and 126.3% more libertarian. Contradicting responses on 14/62 propositions for Mistral and 23/62 for GPT-3.5
**Condition**: Tested on Mistral 7b Iv0.1 and GPT-3.5 1106 across 10 paraphrase variants of the PCT initial question

**Evidence**: "minimal semantics-preserving prompt template paraphrases substantially affect overall PCT results... These differences between paraphrases are larger even than the difference between Joe Biden and Donald Trump as placed on the PCT ahead of the 2020 US Presidential Election."

## [NEUTRAL] Open-Ended Evaluation Setting
Replacing multiple-choice format with free-text generation prompts inspired by real-world LLM use cases (e.g., writing blog posts, opinion pieces, podcast responses), then using GPT-4 as an agreement classifier

**Delta**: Models flip agreement on roughly 1 in 3 propositions (19/62 for GPT-3.5, 23/62 for Mistral) compared to multiple-choice; responses appear marginally more stable than multiple-choice setting but clear instability remains
**Condition**: Applied to Mistral 7b Iv0.1 and GPT-3.5 1106 across 10 open-ended prompt variants; more realistic but still unstable

**Evidence**: "for one and the same political issue, models often express opposing views in open-ended generations vs. the multiple-choice setting. On roughly one in three propositions (19/62 for GPT-3.5 1106, and 23/62 for Mistral 7b Iv0.1), the models 'agree' with the proposition for a majority of prompt templates in the multiple-choice setting but 'disagree' with the proposition for a majority of prompt templates in the open-ended setting."

## [POSITIVE] GPT-4 Agreement Classifier for Open-Ended Responses
Using GPT-4 0125 to classify whether open-ended model responses agree, disagree, or express neither view on PCT propositions

**Delta**: 99% accuracy for Mistral 7b Iv0.1 and 100% accuracy for GPT-3.5 1106 against human annotations; inter-annotator agreement was very high (Fleiss' κ = 93.1%)
**Condition**: Used in §4.5 open-ended evaluation to replace string-matching; validated against 200 human-annotated responses

**Evidence**: "Measured against these human annotations, the performance of the agreement classifier is almost perfect, with 99% accuracy for Mistral 7b Iv0.1 and 100% accuracy for GPT-3.5 1106."

## [POSITIVE] Temperature Zero Decoding
Setting model temperature to 0 to make outputs deterministic across all experiments

**Delta**: Ensures reproducibility and eliminates stochastic variation as a confound
**Condition**: Applied to all 10 models in all experiments; contrasts with prior work where 8 articles did not report generation parameters and likely used non-zero defaults

**Evidence**: "In all experiments, we use a temperature of zero to make model responses deterministic."

## [NEGATIVE] Multiple-Choice Survey Format for LLM Evaluation
Using constrained multiple-choice questionnaires (like the PCT) as the primary instrument for evaluating LLM values and opinions

**Delta**: Produces results that differ substantially from open-ended settings; does not reflect real-world LLM usage; described as resembling 'spinning arrows' rather than reliable instruments
**Condition**: General finding across all PCT-based evaluations; applies broadly to similar instruments like ETHICS, Human Values Scale, MoralChoice, OpinionQA

**Evidence**: "Multiple-choice surveys and questionnaires are poor instruments for evaluating the values and opinions manifested in LLMs, especially if these evaluations are motivated by real-world LLM applications... artificially constrained evaluations produce very different results than more realistic unconstrained evaluations, and that results in general are highly unstable."

## [NEGATIVE] Robustness Testing via Prompt Repetition Only
Prior works' approach of repeating the same prompts multiple times as the sole robustness check, without varying prompt phrasing or format

**Delta**: Insufficient to establish robustness; only 3 of 12 in-scope articles conducted any robustness testing beyond repetition
**Condition**: Observed across 12 in-scope PCT evaluation papers in systematic literature review

**Evidence**: "no prior work conclusively establishes prompt robustness... only three in-scope articles conduct any robustness testing, beyond repeating the same prompts multiple times."

## [NEUTRAL] Open Generation with Binary Stance Detection
Allowing models to generate free-form responses and then using a binary classifier to map responses to agree/disagree categories

**Delta**: Used by only 2 of 12 prior works; more flexible than forced choice but still maps to binary outcome losing nuance
**Condition**: Alternative to forced choice prompting used by Feng et al. (2023) and Thapa et al. (2023) in prior PCT work

**Evidence**: "Only two articles allow for more open-ended responses and then use binary classifiers to map responses to 'agree' or 'disagree' (Feng et al., 2023; Thapa et al., 2023)."

## [NEGATIVE] Situative Context Variation in Open-Ended Prompts
Varying the situative framing of open-ended prompts (e.g., debate, news interview, podcast, blog post) while keeping the intent constant (express your opinion)

**Delta**: 10/62 propositions for Mistral and 13/62 for GPT-3.5 show contradicting responses across open-ended prompt variants
**Condition**: Applied to Mistral 7b Iv0.1 and GPT-3.5 1106 across 10 open-ended situative prompt variants in §4.5

**Evidence**: "model responses in the open-ended setting are also heavily influenced by minor prompt template changes, mirroring results for the multiple-choice setting in §4.4. For Mistral, there are 10 out of 62 propositions where the model expresses agreement in at least one open-ended prompt variant and disagreement in another."
