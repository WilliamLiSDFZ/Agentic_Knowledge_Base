# All Languages Matter: On the Multilingual Safety of LLMs

**Source**: https://aclanthology.org/2024.findings-acl.349/

## [POSITIVE] Multilingual Safety Benchmarking (XSAFETY)
Building a multilingual safety benchmark covering 14 safety issues across 10 languages to evaluate LLM safety beyond English

**Delta**: revealed 42% higher unsafe response rates in non-English vs English queries
**Condition**: Evaluation of multilingual safety across ChatGPT, PaLM2, LLaMA-2-Chat, and Vicuna

**Evidence**: "Experimental results show that all LLMs produce significantly more unsafe responses for non-English queries than English ones, indicating the necessity of developing safety alignment for non-English languages."

## [POSITIVE] Cross-lingual Safety Prompting
System prompt instructing the model to think in English before generating responses in the original language: 'Please think in English and then generate the response in the original language.'

**Delta**: -42% unsafe responses on average for non-English queries
**Condition**: Applied to ChatGPT for non-English queries across Chinese, Russian, Japanese, and French

**Evidence**: "The effective prompt can significantly reduce the ratio of unsafe responses by 42% for non-English queries."

## [POSITIVE] Cross-lingual Safety Prompting for Russian
Same English-thinking prompt applied specifically to Russian queries

**Delta**: -78% relative reduction (13.0% to 2.7% unsafe ratio)
**Condition**: Applied to Russian language queries in ChatGPT

**Evidence**: "the prompt works best for Russian (i.e., the unsafe ratio from 13.0% to 2.7%) and enjoys the best translation performance from English."

## [POSITIVE] Cross-lingual Safety Prompting for Japanese
Same English-thinking prompt applied specifically to Japanese queries

**Delta**: -14% relative reduction (23.7% to 20.3% unsafe ratio)
**Condition**: Applied to Japanese language queries in ChatGPT; least effective among tested languages

**Evidence**: "Table 5: Average unsafe ratio (%) of prompting method for non-English queries... ja: Vanilla 23.7, Prompt 20.3, △ -14%"

## [NEGATIVE] English-only Safety Alignment
Safety alignment primarily tuned in English, as practiced by most LLM developers

**Delta**: non-English unsafe rates 15.9% vs English 1.0% for ChatGPT
**Condition**: Applies to all tested LLMs when handling non-English queries

**Evidence**: "all LLMs exhibit significantly lower safety in non-English languages compared to English, highlighting the need for developing safety alignment strategies for non-English languages."

## [POSITIVE] ChatGPT as Safety Evaluator
Using ChatGPT with a structured prompt to classify responses as safe or unsafe, translating non-English responses to English first before evaluation

**Delta**: 88.5% accuracy vs human annotation
**Condition**: Used as automatic evaluator for multilingual safety responses across 10 languages and 14 safety issues

**Evidence**: "The accuracy of the ChatGPT evaluation is 88.5%, demonstrating the effectiveness of this automatic evaluation method."

## [NEGATIVE] GPT-4 as Safety Evaluator
Using GPT-4 instead of ChatGPT as the safety evaluation model

**Delta**: GPT-4 correct in only 24/100 cases vs ChatGPT correct in 76/100 cases
**Condition**: Used as alternative evaluator for English, Chinese, and Hindi responses

**Evidence**: "ChatGPT is correct in 76 cases, while GPT-4 is correct in 24 cases. The primary reason for GPT-4's weak performance is its over-sensitivity, which led to the classification of 70 safe responses as unsafe."

## [NEGATIVE] Claude3/Gemini as Safety Evaluators
Using Claude3 or Gemini as LLM judges for safety evaluation

**Delta**: Claude3 classifies 85.1% as unsafe; Gemini classifies 44.8% as unsafe, vs actual 7.7% unsafe
**Condition**: Used as alternative evaluators for ChatGPT response safety classification

**Evidence**: "Claude3 and Gemini classify 85.1% and 44.8% of the ChatGPT's responses as unsafe, among which only 7.7% are unsafe according to human annotation. Therefore, adopting other famous LLMs as evaluators can lead to negative effects."

## [POSITIVE] Professional Human Translation with Proofreading
Using Google Translate followed by two rounds of professional human proofreading to build the multilingual benchmark

**Delta**: modification rate reduced from 15.5% (round 1) to 3.4% (round 2); >99% pass rate on random inspection
**Condition**: Applied during XSAFETY benchmark construction for 9 non-English languages

**Evidence**: "The modification rate for the first round was 15.5%, and the second round had a 3.4% modification rate. Subsequently, we randomly inspected 10% of the data, achieving a pass rate greater than 99%."

## [NEGATIVE] Low-resource Language Pretraining Distribution
Non-English languages constituting very small fractions of LLM pretraining data (e.g., Bengali <0.01% in LLaMA-2)

**Delta**: Bengali, Hindi, Japanese among top-3 most unsafe languages; Bengali unsafe rate 37.4% for ChatGPT
**Condition**: Affects safety performance across all tested LLMs for low-resource languages

**Evidence**: "The most unsafe languages (e.g., Bengali, Hindi, Japanese, and Arabic) are generally the lowest-resource languages in the pretraining data."

## [POSITIVE] LLaMA-2-Chat vs Vicuna for Multilingual Safety
Using LLaMA-2 as the underlying model (LLaMA-2-Chat) compared to LLaMA-based Vicuna for multilingual safety

**Delta**: LLaMA-2-Chat average non-English unsafe rate 23.6% vs Vicuna 29.9%
**Condition**: Comparison of open-source models on non-English safety tasks

**Evidence**: "although LLaMA-2-Chat performs worse in English than Vicuna, it performs better in other languages. We attribute the superior performance of LLaMA2-Chat on the multilingual tasks to the stronger underlying model (i.e., LLaMA-2) compared with that for Vicuna (i.e., LLaMA)."

## [POSITIVE] English Instruction Prompts for Multilingual Tasks
Using English for instructions and examples when performing multilingual tasks rather than the target language

**Delta**: outperforms baseline
**Condition**: Applied to prompting method for improving multilingual safety of ChatGPT

**Evidence**: "All the prompts are in English since Shi et al. (2023) reveals that using the instruction and examples in English performs better for multilingual tasks."

## [POSITIVE] Cultural Bias Mitigation in Benchmark Construction
Removing Chinese culture-specific sentences and asking translators to adapt translations to target language cultures to reduce cultural bias in the benchmark

**Delta**: neutral/qualitative improvement in benchmark universality
**Condition**: Applied during XSAFETY benchmark construction to ensure cross-cultural validity

**Evidence**: "To build a universal benchmark agnostic to specific languages, we remove the Chinese culture-associated sentences by manually checking and collecting 200 instances for each safety issue."

## [NEGATIVE] Commonsense Safety Scenario Evaluation
Including commonsense safety test cases that require implicit knowledge to identify harm rather than explicit violent content

**Delta**: highest unsafety ratio among all scenarios for non-English languages
**Condition**: Evaluated across all 10 languages for ChatGPT; most pronounced gap between English and non-English

**Evidence**: "The most challenging scenario of multilingual safety is Commonsense Safety, where the text is not explicitly violent and requires additional commonsense knowledge to comprehend that it leads to physical harm... This would be especially challenging for non-English languages that only take a small proportion of the pretraining data."

## [POSITIVE] Extensive English Safety Alignment (ChatGPT)
ChatGPT's more extensive safety mitigation efforts primarily in English compared to other LLMs

**Delta**: ChatGPT English unsafe rate 1.0% vs PaLM-2 10.3%; non-English average 15.9% vs 18.7%
**Condition**: Comparison across closed-source API models on XSAFETY benchmark

**Evidence**: "ChatGPT performs best among all LLMs. One possible reason is that ChatGPT spent more effort on safety mitigations (the majority in English). Although ChatGPT performs much better than PaLM2 in English (i.e., 1.0 vs. 10.3), the performance gap for non-English languages is relatively smaller (i.e., 15.9 vs. 18.7 on average)."
