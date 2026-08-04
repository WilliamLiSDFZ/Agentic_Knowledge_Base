# Position: On the Possibilities of AI-Generated Text Detection

**Source**: https://proceedings.mlr.press/v235/chakraborty24a.html

## [POSITIVE] Increasing Number of IID Samples for Detection
Collecting more independent text samples (sentences) from either human or machine sources to improve the statistical power of the detector, leveraging the fact that TV(m⊗n, h⊗n) increases exponentially with n.

**Delta**: AUROC increases from ~50% toward 1 exponentially fast as n increases
**Condition**: When human and machine distributions are close but not identical (TV(m,h) = δ > 0), IID setting

**Evidence**: "we note that by increasing the number of samples n, the ROC upper bound starts increasing towards 1 exponentially fast (shown by the shaded blue region in the left figure for different values of n), and hence the AUROC of the best possible detector also starts increasing"

## [POSITIVE] Increasing Sequence Length for Detection
Using longer text sequences (more tokens) for detection rather than short snippets, which increases the effective information available to distinguish human from machine text.

**Delta**: AUROC improves from around 50% to 90% on both Xsum and Squad datasets
**Condition**: Zero-shot detection with RoBERTa-Large/Base and GPTZero detectors on Xsum and Squad datasets

**Evidence**: "with the increase in the number of samples or sequence length of detection, the zero-shot detection performance of models improves drastically from around 50% to 90% on both Xsum and Squad human-machine datasets"

## [POSITIVE] Likelihood-Ratio-Based Detector
Using the likelihood ratio m(s)/h(s) as the detection statistic, which is theoretically proven to be the optimal detector that attains the AUROC upper bound derived from Le Cam's lemma and the Neyman-Pearson lemma.

**Delta**: Achieves the theoretical AUROC upper bound (tight bound)
**Condition**: Any distributions m and h; optimal under both IID and non-IID settings

**Evidence**: "it is a well-established fact in the literature that a likelihood-ratio-based detector would attain the bound for any distributions h and m and hence is the best possible detector"

## [POSITIVE] N-gram Feature Space Expansion
Increasing the n-gram order (from word-level n=1 to sentence/paragraph-level n=6) for computing total variation distance and training supervised classifiers, effectively capturing longer-range linguistic patterns.

**Delta**: +39% AUROC (from 58% to 97%) as n-gram increases from 1 to 6
**Condition**: Supervised detection on Xsum and Squad datasets using TV distance estimation

**Evidence**: "with increasing n-grams, the AUROC of the best detector increases significantly from 58% to 97% for both Xsum and Squad datasets"

## [POSITIVE] Pairwise IID Sample Detection
Restructuring the detection problem to use pairs of IID samples (from machine or human) instead of single examples, then performing binary classification on the paired samples.

**Delta**: +24% AUROC (from 73% to 97%)
**Condition**: Detection with only 30% of the enhanced pairwise dataset, using bag-of-words features and Logistic Regression; t-statistic = -46.91, p-value = 0.000

**Evidence**: "there is a statistically significant boost in detection performance with pairwise samples, even with a vanilla model and sampled dataset... the AUROC of the real detector improves drastically from 73% to 97%"

## [POSITIVE] RoBERTa-Large vs RoBERTa-Base Detector
Using the larger RoBERTa-Large model fine-tuned for AI text detection compared to the smaller RoBERTa-Base model.

**Delta**: RoBERTa-Large outperforms RoBERTa-Base (quantitative gap not precisely stated)
**Condition**: Zero-shot detection on Xsum and Squad human-machine datasets

**Evidence**: "Naturally, the performance of RoBERTa-Large-Detector is better compared to RoBERTa-Base-Detector, but still, the improvement in AUROC with the number of samples/sequence length is significant with both the models"

## [NEGATIVE] Paraphrasing Attacks on Detectors
Applying neural network-based paraphrasers (e.g., DIPPER) to AI-generated text to evade detection by reducing the TV distance between machine and human distributions.

**Delta**: Significant drop in detection accuracy across watermarking, GPTZero, DetectGPT, and OpenAI classifier
**Condition**: Applied to watermark-based detectors, neural network-based detectors, and zero-shot classifiers

**Evidence**: "paraphrased texts with DIPPER (Krishna et al., 2023) evade several detectors, including watermarking, GPTZero, DetectGPT, and OpenAI's text classifier with a significant drop in accuracy"

## [POSITIVE] Watermarking via Green/Red Token Lists
Soft watermarking approach that categorizes tokens into green and red lists, biasing LLM generation toward green-list tokens to create detectable statistical patterns.

**Delta**: Increases Chernoff information (δ), reducing required sample size for detection
**Condition**: When machine and human distributions are close; vulnerable to paraphrasing attacks

**Evidence**: "one could mitigate this trade-off by developing efficient watermarking techniques... which essentially increases the Chernoff information, or in other words, increases the δ, eventually reducing the required number of samples"

## [NEGATIVE] Perplexity-Based Detection
Using perplexity scores as a primary criterion for identifying AI-generated text, a common approach in traditional and some classifier-based detectors.

**Delta**: Substantial misclassification of non-native English writing as AI-generated
**Condition**: Applied to non-native English writers; leads to biased and unfair detection outcomes

**Evidence**: "we want to highlight the potential for bias in detectors relying primarily on perplexity scores... underscoring the need for a comprehensive and equitable redesign that takes into account other relevant metrics"

## [POSITIVE] Non-IID Sample Complexity Framework (Theorem 2)
Extending the IID detection framework to correlated (non-IID) text sequences by modeling dependence strength ρ between sequences, accounting for the natural structure of language (e.g., topic-coherent paragraphs).

**Delta**: Detection remains possible for any δ > 0; sample complexity has additional term depending on cj and ρj compared to IID case
**Condition**: Non-IID correlated text sequences; generalizes IID result; reduces to Theorem 1 when ρj = 0

**Evidence**: "for a given δ > 0 (where h(s) and m(s) are nearly, but not exactly, identical) and ϵ < 1, there exists a number of text sequences, n, (potentially derived from longer texts) that enable us to achieve a high AUROC for effective detection"

## [POSITIVE] TF-IDF Bag-of-Words with Supervised Classifiers
Training vanilla classifiers (Logistic Regression, Random Forest, 2-layer MLP) using TF-IDF bag-of-words features on human-machine generated datasets with increasing sequence length.

**Delta**: Significant increase in AUROC as sequence length increases (specific values shown in Figure 2b)
**Condition**: Supervised detection on Xsum and Squad datasets

**Evidence**: "We report the performance of the test AUROC with increasing sequence length in Figure 2b, which shows a significant increase in accuracy as the sequence length increases even with real detectors"

## [NEGATIVE] Single Short Text Detection
Attempting to detect AI-generated text from a single short sequence (e.g., a single sentence or very short text), without aggregating multiple samples.

**Delta**: AUROC ~50% (near random) for small n or short sequences
**Condition**: When TV(m,h) is small and only a single or very short text sample is available

**Evidence**: "it would be impossible to detect whether 'hello world' is written by AI or humans. We would need a sufficient amount of text data for the detection to happen"
