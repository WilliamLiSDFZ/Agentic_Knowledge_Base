---
title: "Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models"
source: "https://proceedings.mlr.press/v235/setlur24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/setlur24a/setlur24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'test-time-adaptation-methods-and-evaluation']
tags: ['foundation-models', 'worst-group-robustness', 'prompting', 'distribution-shift', 'spurious-correlations']
venue: "ICML 2024"
tldr: "Prompting foundation models improves average robustness but can hurt worst-group robustness, and a mitigation strategy is proposed to balance both objectives."
---

# Prompting is a Double-Edged Sword: Improving Worst-Group Robustness of Foundation Models

**Source**: [https://proceedings.mlr.press/v235/setlur24a.html](https://proceedings.mlr.press/v235/setlur24a.html)

**TLDR**: Prompting foundation models improves average robustness but can hurt worst-group robustness, and a mitigation strategy is proposed to balance both objectives.

## Abstract

Machine learning models fail catastrophically under distribution shift, but a surprisingly effective way to empirically improve robustness to some types of shift (e.g., Imagenet-A/C) is to use stronger open-vocabulary classifiers derived from foundation models. In this work, we first note that for shifts governed by spurious correlations (features spuriously correlated with the label on the training data, but not on test), the zero-shot and few-shot performance of foundation models is no better than ERM models, and remains unchanged when pretrained data/model size is scaled. Secondly, even in these situations, foundation models are quite accurate at predicting the value of the spurious feature. In a simplified setup, we theoretically analyze both these findings. Specifically, we show that during contrastive pretraining, the simplicity bias of foundation models tends to result in the learning of features that mostly rely on the spurious attribute, compared to more robust features. We leverage these observations to propose Prompting for Robustness (PfR) which first uses foundation models to zero-shot predict the spurious attribute on labeled examples, and then learns a classifier with balanced performance across different groups of labels and spurious attribute. Across 5 vision and language tasks, we show that PfR’s performance nearly equals that of an oracle algorithm (group DRO) that leverages human labeled spurious attributes.