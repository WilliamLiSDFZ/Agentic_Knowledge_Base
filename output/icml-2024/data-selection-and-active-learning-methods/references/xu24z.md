---
title: "Learning 1-Bit Tiny Object Detector with Discriminative Feature Refinement"
source: "https://proceedings.mlr.press/v235/xu24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24z/xu24z.pdf"
categories: ['adversarial-robustness-and-model-security', 'data-selection-and-active-learning-methods']
tags: ['binary-neural-networks', 'tiny-object-detection', 'feature-refinement']
venue: "ICML 2024"
tldr: "Proposes a discriminative feature refinement approach for 1-bit detectors to address performance degradation on tiny objects."
---

# Learning 1-Bit Tiny Object Detector with Discriminative Feature Refinement

**Source**: [https://proceedings.mlr.press/v235/xu24z.html](https://proceedings.mlr.press/v235/xu24z.html)

**TLDR**: Proposes a discriminative feature refinement approach for 1-bit detectors to address performance degradation on tiny objects.

## Abstract

1-bit detectors show impressive performance comparable to their real-valued counterparts when detecting commonly sized objects while exhibiting significant performance degradation on tiny objects. The challenge stems from the fact that high-level features extracted by 1-bit convolutions seem less compelling to reveal the discriminative foreground features. To address these issues, we introduce a Discriminative Feature Refinement method for 1-bit Detectors (DFR-Det), aiming to enhance the discriminative ability of foreground representation for tiny objects in aerial images. This is accomplished by refining the feature representation using an information bottleneck (IB) to achieve a distinctive representation of tiny objects. Specifically, we introduce a new decoder with a foreground mask, aiming to enhance the discriminative ability of high-level features for the target but suppress the background impact. Additionally, our decoder is simple but effective and can be easily mounted on existing detectors without extra burden added to the inference procedure. Extensive experiments on various tiny object detection (TOD) tasks demonstrate DFR-Det’s superiority over state-of-the-art 1-bit detectors. For example, 1-bit FCOS achieved by DFR-Det achieves the 12.8% AP on AI-TOD dataset, approaching the performance of the real-valued counterpart.