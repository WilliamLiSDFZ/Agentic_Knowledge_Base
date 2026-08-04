---
title: "Selective Mixup Helps with Distribution Shifts, But Not (Only) because of Mixup"
source: "https://proceedings.mlr.press/v235/teney24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/teney24a/teney24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['mixup-augmentation', 'distribution-shift', 'domain-generalization']
venue: "ICML 2024"
tldr: "Selective mixup improves performance under distribution shifts, but analysis reveals the benefit comes from implicit data reweighting rather than the mixup interpolation itself."
---

# Selective Mixup Helps with Distribution Shifts, But Not (Only) because of Mixup

**Source**: [https://proceedings.mlr.press/v235/teney24a.html](https://proceedings.mlr.press/v235/teney24a.html)

**TLDR**: Selective mixup improves performance under distribution shifts, but analysis reveals the benefit comes from implicit data reweighting rather than the mixup interpolation itself.

## Abstract

Mixup is a highly successful technique to improve generalization by augmenting training data with combinations of random pairs. Selective mixup is a family of methods that apply mixup to specific pairs e.g. combining examples across classes or domains. Despite remarkable performance on benchmarks with distribution shifts, these methods are still poorly understood. We find that an overlooked aspect of selective mixup explains some of its success in a completely new light. The non-random selection of pairs affects the training distribution and improves generalization by means completely unrelated to the mixing. For example in binary classification, mixup across classes implicitly resamples the data to uniform class distribution - a classical solution to label shift. We verify empirically that this resampling explains some of the improvements reported in prior work. Theoretically, the effect relies on a “regression toward the mean”, an accidental property we find in several datasets. Outcomes. We now better understand why selective mixup works. This lets us predict a yet-unknown failure mode and conditions where the method is detrimental. We also use the equivalence with resampling to design better variants that combine mixing and resampling effects.