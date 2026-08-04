# Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models

**Source**: https://proceedings.mlr.press/v235/setlur24a.html

## [NEGATIVE] Zero-shot prompting with label description
Using foundation models (CLIP, Llama-2) to predict class labels directly via zero-shot prompts without any downstream fine-tuning

**Delta**: 32% drop between average and worst-group accuracy on Waterbirds; 25% drop on CivilComments; 7% drop on MNLI
**Condition**: Tasks with spurious correlations; worst-group performance on minority groups where spurious correlation is absent

**Evidence**: "When evaluating CLIP L/14 models on vision datasets, a notable drop of 32% is observed between average and worst group accuracy on Waterbirds dataset, and a drop of 3.5% is observed on CelebA. Turning to language datasets, the evaluation of the Llama-2 13b model indicates a significant 25% performance decline in CivilComments and a 7% drop in MNLI."

## [NEUTRAL] Naive zero-shot prompting with spurious attribute description
Incorporating a natural language description of the spurious/confounding attribute into the zero-shot classification prompt to predict the label

**Delta**: less than 1% change in worst-group performance
**Condition**: Zero-shot label classification on spurious correlation benchmarks (Waterbirds, CelebA, CivilComments, MNLI)

**Evidence**: "However, the zero-shot performance for the worst-case group doesn't improve – there is less than a 1% change between the zero-shot and zero-shot with spurious attribute description rows in Table 1."

## [NEUTRAL] Explicit instruction to ignore spurious attribute
Prompting the model with explicit instructions to ignore the spurious/confounding attribute when predicting the label

**Delta**: did not substantively impact worst-group performance
**Condition**: Zero-shot label classification on spurious correlation benchmarks

**Evidence**: "We also evaluated other variants, where we explicitly instructed the model to ignore spurious attributes, but this did not substantively impact worst-group performance."

## [POSITIVE] Zero-shot spurious attribute prediction
Using foundation models to predict only the presence of the spurious/confounding attribute rather than the label

**Delta**: ~95% average accuracy with similar worst-case group performance across all benchmarks
**Condition**: Predicting spurious attributes (not labels) on Waterbirds, CelebA, CivilComments, MNLI

**Evidence**: "On all standard spurious correlation benchmarks, we observe that the average performance of predicting the presence of the spurious attribute is around 95% with a similar worst-case group performance."

## [NEGATIVE] Scaling pretraining data and model size for label prediction
Increasing the scale of pretraining datasets and model sizes to improve zero-shot worst-group label prediction robustness

**Delta**: robustness gap stays the same or widens for label prediction
**Condition**: Zero-shot label prediction on spurious correlation benchmarks; CLIP and Llama/Pythia model families

**Evidence**: "As we scale up the pretraining datasets and models, we observe that while the difference reduces for the confounder prediction, the difference doesn't improve for the label prediction task."

## [POSITIVE] Scaling pretraining data and model size for spurious attribute prediction
Increasing the scale of pretraining datasets and model sizes for zero-shot spurious attribute prediction

**Delta**: worst group performance of spurious attribute prediction improves with scale
**Condition**: Zero-shot spurious attribute prediction; CLIP and Llama/Pythia model families

**Evidence**: "while scaling up the model size and pretraining data does not improve the performance of label prediction on minority groups, the worst group performance of spurious attribute prediction does."

## [POSITIVE] Scaling pretraining for downstream representations (DRO fine-tuning)
Using larger pretrained models as feature extractors for downstream DRO-based classifiers

**Delta**: average and worst-case accuracy (trained with DRO) improves as model size and pretraining data scale
**Condition**: When training a DRO classifier on top of pretrained features; vision tasks

**Evidence**: "As expected we observe that the average and worst-case accuracy (trained with DRO on downstream labeled data) improves as we increase the scale of model size and pretraining data."

## [NEGATIVE] Naive ERM fine-tuning on downstream data
Training a linear classifier on pretrained features using standard empirical risk minimization on downstream labeled data

**Delta**: worst-group accuracy 70.71 on Waterbirds, 54.84 on CelebA, 61.35 on CivilComments, 67.30 on MNLI
**Condition**: Downstream labeled data with spurious correlations; without group annotations

**Evidence**: "simply fine-tuning naïvely would result in the same issues as standard ERM training, as we confirm experimentally."

## [POSITIVE] Prompting for Robustness (PfR)
Two-stage method: (1) use foundation model to zero-shot predict spurious attribute on labeled examples, (2) train robust classifier by minimizing worst-group loss over groups defined by predicted spurious attribute and label

**Delta**: 47% reduction in worst-group error vs zero-shot; 52% vs ERM; 30% vs JTT; worst-group gains >75% on Waterbirds; nearly matches oracle Group DRO
**Condition**: Classification tasks with spurious correlations; requires text description of confounder and few labeled examples; vision and language tasks

**Evidence**: "averaged across datasets, PfR reduced worst group error by 47% compared to zero-shot, and 52% and 30% compared to ERM and JTT, respectively. On some datasets like Waterbirds, the worst group gains are as high as >75%. More importantly, PfR's performance closely matches that of the oracle Group DRO algorithm across all datasets."

## [NEGATIVE] In-context learning (ICL) for robustness
Providing labeled training examples in-context to large language models to improve few-shot performance on tasks with spurious correlations

**Delta**: worst-group performance remains almost unchanged for CivilComments and worsens for MNLI despite average improvement
**Condition**: Language tasks (CivilComments, MNLI) with spurious correlations; 128 in-context examples

**Evidence**: "while ICL improves over zero-shot inference on average, the worst-group performance remains almost unchanged for CivilComments and worsens for MNLI."

## [POSITIVE] Group DRO with ground-truth group labels (oracle)
Distributionally robust optimization minimizing worst-group loss using human-annotated ground-truth spurious attribute labels to define groups

**Delta**: 93.23 WG on Waterbirds, 90.79 on CelebA, 80.21 on CivilComments, 81.54 on MNLI
**Condition**: Oracle setting with access to true group labels; used as upper-bound comparison

**Evidence**: "PfR's performance closely matches that of the oracle Group DRO algorithm across all datasets."

## [POSITIVE] GPT-4V annotation of spurious attributes
Using GPT-4V to annotate medical images (Chest X-ray) for the presence of spurious attributes (chest drain) given a language description

**Delta**: significant performance gap revealed between average and worst-group ERM performance on constructed CXR-Drain dataset
**Condition**: Medical imaging (Chest X-ray 14); spurious attribute annotations not publicly available; noisy annotations expected

**Evidence**: "we observe that models trained with ERM show a significant performance gap on the constructed CXR-Drain dataset... we validate the ability of foundation models to detect the presence of spurious features in practice."

## [NEGATIVE] Contrastive pretraining with spurious correlations in pretraining data
Multimodal contrastive pretraining (e.g., CLIP-style) when the pretraining distribution replicates the spurious correlations present in the downstream task

**Delta**: worst group accuracy of zero-shot label predictor is provably worse than random; confounder predictor has near-perfect accuracy
**Condition**: Multimodal contrastive pretraining; spurious correlations present in both pretraining and downstream distributions; theoretical result for linear encoders

**Evidence**: "we prove that even with infinite pretraining data, the zero-shot performance for the pretrained model would be provably worse than random on examples where label and spurious attributed are uncorrelated."

## [NEGATIVE] Simplicity bias in contrastive pretraining
Contrastive pretraining's tendency to place higher weight on spurious (simpler/lower-variance) features over robust features when the signal-to-noise ratio along the robust feature is high

**Delta**: image encoder relies more on non-robust spurious feature; text encoder learns identical features for label and confounder descriptions
**Condition**: Multimodal contrastive pretraining when spurious correlations exist in pretraining data; higher noise along robust feature (σ_r)

**Evidence**: "contrastive pretraining learns: (i) image features that couple the spurious feature with other robust features, while placing a higher weight on the spurious one; and (ii) text features that are almost identical for the text descriptions of the label and the spurious attribute."

## [POSITIVE] Linear head training on fixed pretrained features
Training only a linear classification head on top of frozen pretrained model features for downstream tasks

**Delta**: enables PfR to nearly match Group DRO oracle performance
**Condition**: Few-shot downstream adaptation; vision tasks use CLIP image encoder; language tasks use RoBERTa features fine-tuned on task data

**Evidence**: "All few-shot methods including PfR are used to train a linear head over fixed features."
