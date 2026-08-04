---
title: "Not Just Pretty Pictures: Toward Interventional Data Augmentation Using Text-to-Image Generators"
source: "https://proceedings.mlr.press/v235/yuan24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yuan24e/yuan24e.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['data-augmentation', 'text-to-image', 'distribution-shift', 'interventional']
venue: "ICML 2024"
tldr: "Proposes interventional data augmentation using text-to-image generators to improve classifier robustness to distribution shift."
---

# Not Just Pretty Pictures: Toward Interventional Data Augmentation Using Text-to-Image Generators

**Source**: [https://proceedings.mlr.press/v235/yuan24e.html](https://proceedings.mlr.press/v235/yuan24e.html)

**TLDR**: Proposes interventional data augmentation using text-to-image generators to improve classifier robustness to distribution shift.

## Abstract

Neural image classifiers are known to undergo severe performance degradation when exposed to inputs that are sampled from environmental conditions that differ from their training data. Given the recent progress in Text-to-Image (T2I) generation, a natural question is how modern T2I generators can be used to simulate arbitrary interventions over such environmental factors in order to augment training data and improve the robustness of downstream classifiers. We experiment across a diverse collection of benchmarks in single domain generalization (SDG) and reducing reliance on spurious features (RRSF), ablating across key dimensions of T2I generation, including interventional prompting strategies, conditioning mechanisms, and post-hoc filtering, showing that modern T2I generators like Stable Diffusion can indeed be used to implement a powerful interventional data augmentation (IDA) mechanism, outperforming previously state-of-the-art data augmentation techniques regardless of how each dimension is configured.