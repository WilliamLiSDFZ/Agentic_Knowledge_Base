# Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text

**Source**: https://proceedings.mlr.press/v235/hans24a.html

## [POSITIVE] Binoculars Score (PPL / X-PPL Ratio)
A detection score computed as the ratio of perplexity (log PPL) from an observer LLM to cross-perplexity (log X-PPL) between two closely related LLMs. The numerator measures how surprising the text is to M1; the denominator measures how surprising M2's token predictions are to M1.

**Delta**: TPR >90% at 0.01% FPR across News, Creative Writing, and Student Essay datasets
**Condition**: Zero-shot detection of machine-generated text across multiple LLMs and domains

**Evidence**: "Binoculars detects over 90% of generated samples from ChatGPT (and other LLMs) at a false positive rate of 0.01%, despite not being trained on any ChatGPT data."

## [POSITIVE] Zero-Shot Detection (No Training Data)
The detector requires no training examples from the target LLM source, relying entirely on pre-trained LLMs for scoring.

**Delta**: outperforms all open-source methods for ChatGPT detection and is competitive with or better than commercial APIs
**Condition**: Comparison against trained detectors like Ghostbuster and GPTZero

**Evidence**: "our scheme still out-performs all open-source methods for ChatGPT detection and is competitive with or better than commercial APIs, despite these competitors using training samples from ChatGPT"

## [POSITIVE] Cross-Perplexity Normalization (Capybara Problem Fix)
Using cross-perplexity as a normalizing factor for raw perplexity to calibrate for prompts that yield high-perplexity generation, making the score invariant to prompt context.

**Delta**: Binoculars score of 0.73 (below threshold of 0.901) correctly classifies capybara example; DetectGPT wrongly assigns 0.14 (below its threshold of 0.17)
**Condition**: Text generated from unusual or topic-specific prompts that inflate raw perplexity

**Evidence**: "our detector correctly assigns a Binoculars score of 0.73, which is well below the global threshold of 0.901, resulting in a correct classification with high confidence. For reference, DetectGPT wrongly assigns a score of 0.14, which is below its threshold of 0.17, and classifies the text as human."

## [NEGATIVE] Raw Perplexity as Sole Detector
Using only the log perplexity of an observer LLM as the detection signal, without normalization by cross-perplexity.

**Delta**: fails on capybara-style prompts; shown to be ineffective in isolation in Figure 11
**Condition**: Detection when prompts induce high-perplexity completions regardless of author (human or machine)

**Evidence**: "we show in Figure 11 that both perplexity and cross-perplexity are not effective detectors in isolation."

## [NEGATIVE] Cross-Perplexity Alone as Detector
Using only the cross-perplexity between two models as the detection signal, without the perplexity ratio.

**Delta**: not effective in isolation (Figure 11)
**Condition**: Used without the perplexity ratio formulation

**Evidence**: "we show in Figure 11 that both perplexity and cross-perplexity are not effective detectors in isolation."

## [POSITIVE] Closely Related Model Pair (Falcon-7B + Falcon-7B-Instruct)
Using two models that are very close to each other in performance (base and instruction-tuned variants of the same model family) as the observer and performer LLMs.

**Delta**: best performance over 3 domains compared to other model pair combinations (Table 3, Figure 13)
**Condition**: Choice of scoring model pair for Binoculars

**Evidence**: "our approach works best for two models that are very close to each other in performance. In the remainder of this work, we use the open-source models Falcon-7b model (M1) and the Falcon-7b-instruct (M2)"

## [NEUTRAL] Identical Scoring Model Pair
Using the same model for both M1 and M2 in the Binoculars score computation.

**Delta**: competitive but not best; vanilla Binoculars score (different models) is best over 3 domains
**Condition**: Ablation study comparing identical vs. different model pairs

**Evidence**: "We observe although the vanilla Binoculars score is best over 3 domains, using Falcon-7B as input models is competitive."

## [POSITIVE] TPR at Ultra-Low FPR Evaluation Metric
Evaluating detectors using True Positive Rate at 0.01% False Positive Rate instead of AUC or F1 score alone.

**Delta**: AUC scores are often uncorrelated with TPR@FPR when FPR is below 1% (Table 4)
**Condition**: Evaluation methodology for high-stakes detection scenarios

**Evidence**: "We argue that these metrics alone are inadequate when evaluating LLM detection performance... we focus on true-positive rates (TPR) at low false-positive rates (FPR), and adopt a standard FPR threshold of 0.01%."

## [POSITIVE] Out-of-Domain (OOD) Threshold Tuning
Setting a global detection threshold using reference datasets that are different from the evaluation datasets, to ensure fair zero-shot evaluation.

**Delta**: enables fair out-of-domain comparison; Binoculars outperforms Ghostbuster in the out-of-domain setting
**Condition**: Evaluation on datasets not used for threshold calibration

**Evidence**: "we compare TPR at 0.01% FPR in Figure 1 (and F1-Score in Figure 9 in Appendix) to show that Binoculars outperforms Ghostbuster in the 'out-of-domain' setting."

## [NEGATIVE] Modified Prompting Strategies (Style Prompts)
Prompting LLMs with system prompts requesting stylized output (Carl Sagan voice, non-robotic, pirate style) to test detector robustness.

**Delta**: pirate-style prompt decreases sensitivity by only 1% (increases false negative rate by 1%)
**Condition**: Adversarial-style prompting to evade detection

**Evidence**: "we find that these stylistic changes do not significantly impact the accuracy of Binoculars. The biggest impact we observe arises when asking for pirate-sounding output, and this only decreases the sensitivity (increases the false negative rate) by 1%"

## [NEGATIVE] Multilingual Detection with Monolingual Models
Applying Binoculars (powered by Falcon models) to detect machine-generated text in low-resource languages such as Urdu, Russian, Bulgarian, and Arabic.

**Delta**: high precision but poor recall in low-resource languages
**Condition**: Detection of machine-generated text in languages underrepresented in Falcon's training data

**Evidence**: "we find that false-positive rates remain low, which is highly desirable from a harm reduction perspective. However, machine text in these low-resource languages is often classified as human."

## [POSITIVE] Non-Native English Speaker (ESL) Robustness
Evaluating whether the detector incorrectly flags ESL writing as machine-generated, comparing original and grammar-corrected essay distributions.

**Delta**: equal accuracy of 99.67% for both corrected and uncorrected essay datasets
**Condition**: Detection applied to essays written by non-native English speakers

**Evidence**: "Binoculars attains equal accuracy at 99.67% for both corrected and uncorrected essay datasets... the Binoculars score distribution on ESL's text highly overlaps with that of grammar-corrected versions of the same essays, showing that detection through Binoculars is insensitive to this type of shift."

## [NEGATIVE] Memorized Text Handling
Behavior of Binoculars on highly memorized texts (e.g., US Constitution, famous quotes) that LLMs have likely overfit to during training.

**Delta**: 3 of 11 famous texts fall on the machine side of the threshold; US Constitution scores 0.76 (below threshold of 0.901)
**Condition**: Detection applied to texts that appear frequently in LLM training data

**Evidence**: "the US Constitution – a document that is largely memorized by modern LLMs. This example has a Binoculars score of 0.76, well into the machine range. Of the 11 famous texts we study, this was the lowest score (most machine-y). Three of the 11 fall on the machine-side of our threshold."

## [POSITIVE] Random Token Sequence Scoring
Scoring completely random token sequences with Binoculars to test for false positive bias toward random/noisy strings.

**Delta**: mean Binoculars score ~1.35 for random tokens vs. ~1.0 for humans; confidently classified as human
**Condition**: Input consists of random or hash-like token sequences

**Evidence**: "We find that Binoculars confidently scores this as human, with a mean score around 1.35 for Falcon (humans have a mean of around 1). This is expected, as trained LLMs are strong models of language and exceedingly unlikely to ever generate these completely random sequences."

## [POSITIVE] Increasing Document Length
Providing more tokens of a document to the detector by prefixing sample documents to increase the observed sequence length.

**Delta**: detection performance increases with document size for Binoculars; advantages are even clearer in the few-token regime
**Condition**: Varying document size from 128 to 512 tokens

**Evidence**: "A desirable property for detectors is that with more information they get stronger. Figure 2 shows that both Binoculars and Ghostbuster have this property, and that the advantages of Binoculars are even clearer in the few-token regime."

## [NEGATIVE] Model-Specific Training for Detection (Ghostbuster)
Training a detector specifically on ChatGPT output, making it specialized for one LLM source.

**Delta**: Ghostbuster fails to reliably detect LLaMA-generated text; TPR near 0 on non-ChatGPT sources
**Condition**: Applied to machine-generated text from LLMs other than ChatGPT

**Evidence**: "Ghostbuster is indeed only capable of detecting ChatGPT, and it fails to reliably detect LLaMA generated text."

## [POSITIVE] GPT-4 Detection via Global Threshold
Applying the globally tuned Binoculars threshold (derived from reference datasets) to detect GPT-4 generated text from the Open Orca dataset.

**Delta**: 92% accuracy on GPT-3 samples and 89.57% accuracy on GPT-4 samples
**Condition**: Detection of GPT-3 and GPT-4 outputs using a threshold not tuned on these models

**Evidence**: "Binoculars detects 92% of GPT3 samples and 89.57% of GPT-4 samples when using the global threshold (from reference datasets)."
