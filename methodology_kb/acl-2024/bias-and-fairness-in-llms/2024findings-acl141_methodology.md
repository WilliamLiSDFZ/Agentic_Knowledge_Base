# KoCommonGEN v2: A Benchmark for Navigating Korean Commonsense Reasoning Challenges in Large Language Models

**Source**: https://aclanthology.org/2024.findings-acl.141/

## [POSITIVE] Multiple-choice question format
Reformatting the evaluation from natural language generation to multiple-choice question answering with four options (one correct, three incorrect)

**Delta**: standardizes evaluation process
**Condition**: evaluation of LLMs on Korean commonsense reasoning

**Evidence**: "we alter from a natural language generation-based evaluation to a multiple-choice task format. This change standardizes the evaluation process, ensuring that language models are tested on their reasoning ability to produce results aligned with Korean commonsense based on unified instructions"

## [POSITIVE] Log-probability normalization for answer selection
Computing average log probability per token across candidate sentences to select the answer with highest probability, normalizing for length

**Delta**: descriptive (enables standardized evaluation)
**Condition**: evaluation metric for multiple-choice commonsense reasoning

**Evidence**: "This approach attempts to normalize for length by computing the average log probability per token."

## [POSITIVE] Combined answer format (number + sentence)
Requiring models to generate both the answer number and its corresponding sentence, combining ARC and MMLU answer formats

**Delta**: descriptive (captures more errors than number-only format)
**Condition**: robustness to answer format evaluation

**Evidence**: "By combining these two formats, our standard answer format is to generate both the answer number and its corresponding sentence. This approach aims to include errors due to mismatches between choice numbers and sentences in our evaluation, considering LLMs' generative and descriptive capabilities."

## [NEGATIVE] Answer number-only prediction format
Changing instruction to predict only the answer number instead of number plus sentence

**Delta**: performance drops to near random choice (~25%)
**Condition**: most open-source LLMs under 13B parameters

**Evidence**: "When tasked with predicting solely the answer number, most models exhibit performance close to random choice. This indicates a low capability in following instructions, revealing that performance can be sensitively affected by changes in answer format."

## [NEGATIVE] Instruction tuning on Korean data
Applying supervised fine-tuning with Korean instruction datasets on top of base LLMs (e.g., KULLM, KoAlpaca on Polyglot-ko backbone)

**Delta**: models with instruction tuning do not consistently surpass backbone models
**Condition**: Korean commonsense reasoning benchmark

**Evidence**: "models enhanced with instruction tuning or DPO applied to LLaMA2-ko-en do not consistently surpass the performance of their backbone models."

## [NEGATIVE] Direct Preference Optimization (DPO)
Applying DPO on top of instruction-tuned LLaMA2-ko-en model

**Delta**: does not consistently surpass backbone model performance
**Condition**: Korean commonsense reasoning benchmark

**Evidence**: "models enhanced with instruction tuning or DPO applied to LLaMA2-ko-en do not consistently surpass the performance of their backbone models."

## [NEGATIVE] Increasing model size
Scaling model parameters from 5.8B/7B to 13B

**Delta**: larger model size does not guarantee better performance
**Condition**: Korean commonsense reasoning across all model families tested

**Evidence**: "Table 4 shows that a larger model size does not necessarily guarantee better performance. Limitations in computational resources leading to uneven amounts of training data, empirical-dependent hyperparameter settings, and potential violations and toxicity increasing with model size contribute to these results."

## [NEUTRAL] Increasing n-shot examples
Adding few-shot examples (2-shot, 5-shot, 10-shot) compared to 0-shot baseline

**Delta**: accuracy difference between highest 0-shot and lowest 10-shot is just 2.02%
**Condition**: open-source LLMs on KoCommonGEN v2

**Evidence**: "The accuracy difference between the highest 0-shot and the lowest 10-shot is just 2.02%. These outcomes imply that significant performance disparities exist among models; however, the differences in performance across n-shot settings are not pronounced. An increase in n-shots does not necessarily guarantee improved performance; certain models exhibit decreased performance with more shots."

## [POSITIVE] Few-shot prompting for commercial APIs
Adding 2-shot or more examples to commercial API models (GPT-3.5, GPT-4, HyperCLOVA)

**Delta**: instruction inconsistency substantially mitigated beyond 2-shot settings
**Condition**: commercial API models (GPT-3.5, GPT-4, HyperCLOVA)

**Evidence**: "In the 0-shot setting, the models reveal some errors in the following instructions; however, this issue shows substantial mitigating beyond the 2-shot settings."

## [NEUTRAL] Korean-focused pre-training
Pre-training language models primarily on Korean corpora (e.g., Polyglot-ko, KoGPT2)

**Delta**: Korean-based LLMs perform relatively better on grammaticality and plausibility but QWEN and Mistral (less Korean) outperform them overall
**Condition**: Korean commonsense reasoning benchmark

**Evidence**: "Korean-based LLMs tend to perform relatively better in types closely aligned with the linguistic intricacies of Korean, such as grammaticality and plausibility types... we also observe that QWEN 7B and Mistral 7B, which do not heavily incorporate Korean, outperform Korean-based LLMs. This shows the need for advancements in training approaches for Korean-based LLMs."

## [POSITIVE] Multilingual pre-training
Pre-training on diverse multilingual data (e.g., QWEN on Chinese/English, Mistral on undisclosed multilingual data)

**Delta**: outperforms Korean-based LLMs on overall benchmark; QWEN highest for Korean/Chinese/Japanese, Mistral excels in English/Chinese/Japanese/Spanish
**Condition**: Korean commonsense reasoning and multilingual numerical commonsense

**Evidence**: "models demonstrating superior n-shot accuracy, despite Korean not being predominant in their pre-training data, exhibit high performance presented in Korean. These results suggest that with well-executed pre-training on multilingual data, even if the proportion of data for a specific language is relatively low, it can enhance the performance of commonsense reasoning."

## [POSITIVE] Expanded vocabulary with additional Korean/English pre-training (LLaMA-ko-en / LLaMA2-ko-en)
Adapting LLaMA/LLaMA2 with expanded vocabulary and further pre-training on Korean and English corpora

**Delta**: LLaMA2-ko-en 13B+INST achieves highest performance at 62.22% in 5-shot; over 15% superior performance in proverb type vs other models
**Condition**: Korean commonsense reasoning, especially proverb type

**Evidence**: "In the 5-shot setting, the model with instruction tuning applied to LLaMA2-ko-en shows the highest performance at 62.22%... Models using LLaMA2-ko-en as their backbone demonstrate over 15% superior performance in understanding metaphorical expressions compared to other models."

## [POSITIVE] Human annotation for concept extraction
Using human-annotated concept sets from AI-Hub as examples to prompt GPT-4 for concept extraction, followed by author refinement

**Delta**: descriptive (ensures quality of concept sets)
**Condition**: dataset construction for KoCommonGEN v2

**Evidence**: "We used these human-annotated concept sets as example samples to prompt the extraction of appropriate verbs and nouns from given sentences. The concept extraction process begins with GPT-4 (OpenAI, 2023) and is further refined by the authors. We conducted corrections for unintended concept omissions, incorrect tagging of verbs or nouns, and the inclusion of concepts not present in the sentences."

## [POSITIVE] Equitable answer distribution
Ensuring each correct answer position (1-4) appears with equal 25% frequency across the dataset

**Delta**: descriptive (prevents positional bias)
**Condition**: benchmark dataset construction

**Evidence**: "To ensure an equitable distribution among all possible answers, each correct answer is evenly distributed from 1 to 4 with a 25% occurrence."

## [POSITIVE] Seven fine-grained error categories
Classifying commonsense errors into seven types: commonsense distortion, memorization, toxic speech, grammaticality, plausibility, numerical commonsense, and proverb

**Delta**: reveals performance gaps: commonsense memorization ~50.44% avg vs numerical commonsense ~29.19% avg
**Condition**: fine-grained evaluation of LLMs on Korean commonsense reasoning

**Evidence**: "The commonsense memorization type consistently scores the highest, with an average of approximately 50.44%. The numerical commonsense type presents the lowest scores, averaging around 29.19%. The performance difference in each type varies significantly across models."

## [POSITIVE] Sociocultural Korean commonsense focus
Reconstructing dataset from scratch to incorporate Korean sociocultural knowledge rather than relying on translated universal commonsense

**Delta**: GPT-4 at ~74% vs human ~85%, other LLMs ~42% average, revealing significant gaps
**Condition**: evaluation of LLMs on Korean commonsense reasoning

**Evidence**: "The empirical results present that LLMs struggle with Korean commonsense reasoning. With human accuracy benchmarked at approximately 85%, GPT-4's performance lags at about 74%, and other LLMs demonstrate an average accuracy of around 42%."

## [POSITIVE] Bootstrap resampling for metric variability estimation
Repeatedly resampling the dataset 100,000 times to estimate standard error of evaluation metrics

**Delta**: descriptive (provides statistical reliability)
**Condition**: evaluation framework for all models

**Evidence**: "To estimate the variability (e.g., standard error) of a metric, we employed a method of repeatedly resampling the dataset and recalculating the metric for each sample, setting bootstrap iterations to 100,000."

## [POSITIVE] Two-annotator human evaluation with inter-annotator agreement
Having two native Korean speakers evaluate each sample, measuring agreement with Cohen's kappa and Krippendorff's alpha

**Delta**: Cohen's kappa = 0.7693, Krippendorff's alpha = 0.7706 (high reliability)
**Condition**: human evaluation of KoCommonGEN v2

**Evidence**: "The evaluation performed by two volunteers per sample shows a strong positive correlation, as evidenced by Cohen's kappa (Cohen, 1960) is 0.7693 and Krippendorff's alpha (Krippendorff, 2011) value of 0.77. These values are indicators of high inter-annotator reliability."
