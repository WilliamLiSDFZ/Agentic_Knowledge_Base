# Extracting Training Data From Document-Based VQA Models

**Source**: https://proceedings.mlr.press/v235/pinto24a.html

## [POSITIVE] High Training Resolution
Training VQA models at higher image resolutions (e.g., 2560×1920 for Donut, 1M pixels for Pix2Struct)

**Delta**: Donut |M| drops from 756 (lowest res) to 63 (highest res)
**Condition**: Reduces memorization; applies across Donut and Pix2Struct models

**Evidence**: "the resolution at which the model is trained is inversely proportional to the amount of memorized samples... while at the highest resolution for Donut |M| = 63, as the training resolution decreases, |M| grows to 109, 168 and to an extremely high level of 756 for the lowest training resolution."

## [NEGATIVE] Low Training Resolution
Training VQA models at lower image resolutions to reduce computational cost

**Delta**: |M| grows from 63 to 756 as resolution decreases for Donut
**Condition**: Increases memorization; applies to all models tested

**Evidence**: "Lowering the resolution can significantly reduce the cost of training, however, as we observe, it increases the tendency of the model to memorize the training data and reduces the generalization capabilities of the models. Therefore it is not recommended."

## [POSITIVE] Web-Scale Pretraining (PaLI-3)
Pretraining on a large-scale multilingual image-text dataset before fine-tuning on DocVQA

**Delta**: PaLI-3 achieves 87.6 ANLS vs 76.6 and 67.5 for best Pix2Struct and Donut variants; near-zero unique PII memorized at high resolution
**Condition**: Reduces memorization and improves generalization; applies to PaLI-3 compared to Donut and Pix2Struct

**Evidence**: "a better pre-trained model may rely less on memorization even at relatively low training resolutions due to their better generalization abilities: indeed, of all the models, PaLI-3 produces the best generalization performance on the test set (87.6 ANLS compared to 76.6 and 67.5 of the best Pix2Struct and Donut variants, respectively)."

## [POSITIVE] Extraction Blocking (EB) Defense
Adding training samples (I^{-a}, Q, 'ANSWER NOT PRESENT') to teach the model to abstain when the answer is not visually present in the input

**Delta**: |M|=0 for Pix2Struct-B and Pix2Struct-L and PaLI-3; |M|=2 for Donut; ANLS improves by +1.2 to +3.4
**Condition**: Applies as a defense countermeasure across all tested models and attack scenarios

**Evidence**: "we observe EB to be extremely effective, reducing to 0 the amount of extractable samples for most models. Furthermore, although we apply the technique by augmenting the original training set using the context (I^{-a}, Q), it also generalizes to adversaries that query the model with the approaches considered in Section 5, while producing an increase in the ANLS"

## [NEGATIVE] Inference Time Paraphrasing (ITP) Defense
Paraphrasing the question at inference time as a defense strategy to reduce extractability

**Delta**: ANLS drops by -12.5 (Donut), -12.9 (Pix2Struct-B), -13.8 (Pix2Struct-L), -8.1 (PaLI-3); |M| reduced but not to zero
**Condition**: Used as a defense; trades off utility for reduced memorization extraction

**Evidence**: "although ITP and PR/AR can reduce the amount of extractable information, they also yield a substantial drop in ANLS on a held-out validation set. Therefore they can only be implemented as mitigation strategies if the practitioners are willing to pay a cost in terms of performance."

## [NEGATIVE] Prepending/Appending Random String (PR/AR) Defense
Perturbing the question by prepending or appending a short 6-digit random string at inference time

**Delta**: ANLS drops by -3.1 to -3.4 (PR) and -1.9 to -3.2 (AR); |M| reduced to 33-40 range but not zero
**Condition**: Used as a defense; moderate ANLS cost with incomplete memorization reduction

**Evidence**: "although ITP and PR/AR can reduce the amount of extractable information, they also yield a substantial drop in ANLS on a held-out validation set. Therefore they can only be implemented as mitigation strategies if the practitioners are willing to pay a cost in terms of performance."

## [NEGATIVE] Removing All Text from Input Image
Providing the model with an image from which all text has been removed, to test reliance on non-textual features

**Delta**: Donut |M| drops to 26; Pix2Struct drops from ~94 to 27; unique PII significantly reduced
**Condition**: Attack scenario where attacker has no knowledge of document text content; reduces but does not eliminate extraction

**Evidence**: "in case of Donut and Pix2Struct, the absence of text in the image significantly reduces the ability of the model to return the correct answer. In case of Donut the amount of samples in M is 26. Pix2Struct shows a similar decrease from about 94 to 27. The amount of PIIs returned is also significantly reduced"

## [NEGATIVE] Question Paraphrasing (Attack Context)
Using a paraphrased version of the training question instead of the exact question during extraction attack

**Delta**: Number of extracted answers significantly drops but remains non-negligible; some unique PIIs still extractable
**Condition**: Attack scenario where attacker does not know exact training question phrasing

**Evidence**: "Figure 6 shows that the number of extracted answers significantly drops, but is still non-negligible. For both Pix2Struct and Donut we observe several unique PIIs are extractable (e.g., names of individuals, serial numbers of tickets and travel destinations)."

## [NEGATIVE] Image Brightness Perturbation
Applying multiplicative brightness changes (×0.5, ×0.8, ×1.3, ×2) to the input document image

**Delta**: Reduces extractable samples; stronger changes reduce more, but substantial samples remain extractable
**Condition**: Attack robustness scenario; less effective reduction than spatial transformations

**Evidence**: "brightness changes can indeed reduce the amount of extractable information, but the amount of extractable samples is still significantly high. In most cases, the stronger the change in brightness, the less the answer is extractable. However, a substantial amount of samples remains extractable"

## [NEGATIVE] Image Spatial Transformations (Rotation/Translation)
Applying small rotations (±5°, ±10°) or translations (±20px, ±100px) to the input document image

**Delta**: Stronger adverse effect on extractability than brightness changes
**Condition**: Attack robustness scenario; more effective at reducing extraction than brightness perturbations

**Evidence**: "Rotating or translating the image has a stronger adverse effect on the extractability of answers, indicating that spatial information plays a more important role for extractability than the intensity information."

## [NEUTRAL] Question-Only Extraction (Shuffled Image)
Feeding the model an unrelated image paired with the original training question to test language-only memorization

**Delta**: Only 4 answers extractable for Donut, 21 for Pix2Struct, 2 for PaLI-3; some sensitive samples included
**Condition**: Attack scenario where attacker has no knowledge of the training image; limited but non-zero extraction possible

**Evidence**: "In the setting where we try to extract the original answer ai, as visible in the Shuffling column in Figure 6, we can extract only 4 answers in case of Donut, and 21 in case of Pix2Struct. Among all the samples in M, we can also find some sensitive samples containing area codes, names of individuals and dates"

## [NEUTRAL] Image-Only Extraction (Unrelated Question)
Providing the model with the training image but an unrelated question to test vision-only memorization

**Delta**: Zero extractable answers found
**Condition**: Attack scenario where attacker has no knowledge of the training question; image alone insufficient for extraction

**Evidence**: "We find no extractable answers in this setting, which suggests that the question plays a more predominant role in the extraction."

## [NEUTRAL] Early Stopping Based on Validation Loss
Stopping training when validation loss stops improving to prevent overfitting

**Delta**: Models generalize to unseen data but memorization still occurs
**Condition**: Applied during fine-tuning of all models; does not prevent memorization of training samples

**Evidence**: "To guard against overfitting, we perform early stopping based on the validation loss. This ensures that all the models we evaluate can generalize to previously unseen data, making them representative of practical deployed VQA systems."

## [POSITIVE] Generalization Baseline for Memorization Attribution
Training a separate model on data excluding canaries to distinguish memorization (E-G) from generalization (G) in extractable samples

**Delta**: Enables attribution of extractable samples to memorization vs. generalization; validated by counterfactual memorization scores
**Condition**: Analytical technique for measuring memorization; requires only 2 model training runs

**Evidence**: "we introduce a generalization baseline fG... If an answer is extractable from f but not from fG, this suggests that the answer was memorized at training time, and cannot simply be recovered from context."

## [POSITIVE] Extractable Memorization and Simplicity Scores
Adaptation of counterfactual memorization/simplicity scores to measure probability of successful extraction from partial context rather than full input

**Delta**: Validates that E-G samples have high memorization scores while G samples do not
**Condition**: Evaluation methodology; requires 50 training runs (K=50 splits) for empirical estimation

**Evidence**: "samples in G have low memorization scores ME: these answers can be extracted whether we train on them or not. In contrast, samples in E − G have memorization scores ME that vary between 0 and 1. Most of the samples are close to the line SE = ME, indicating that the in-sample extractability is the only term contributing to ME"
