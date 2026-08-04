---
title: "Collapse-Aware Triplet Decoupling for Adversarially Robust Image Retrieval"
source: "https://proceedings.mlr.press/v235/tian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tian24a/tian24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'information-retrieval-and-recommendation-systems']
tags: ['adversarial-training', 'image-retrieval', 'metric-learning']
venue: "ICML 2024"
tldr: "Collapse-Aware Triplet Decoupling addresses weak adversary and model collapse issues in adversarially robust deep metric learning for image retrieval."
---

# Collapse-Aware Triplet Decoupling for Adversarially Robust Image Retrieval

**Source**: [https://proceedings.mlr.press/v235/tian24a.html](https://proceedings.mlr.press/v235/tian24a.html)

**TLDR**: Collapse-Aware Triplet Decoupling addresses weak adversary and model collapse issues in adversarially robust deep metric learning for image retrieval.

## Abstract

Adversarial training has achieved substantial performance in defending image retrieval against adversarial examples. However, existing studies in deep metric learning (DML) still suffer from two major limitations: weak adversary and model collapse. In this paper, we address these two limitations by proposing Collapse-Aware TRIplet DEcoupling (CA-TRIDE). Specifically, TRIDE yields a stronger adversary by spatially decoupling the perturbation targets into the anchor and the other candidates. Furthermore, CA prevents the consequential model collapse, based on a novel metric, collapseness, which is incorporated into the optimization of perturbation. We also identify two drawbacks of the existing robustness metric in image retrieval and propose a new metric for a more reasonable robustness evaluation. Extensive experiments on three datasets demonstrate that CA-TRIDE outperforms existing defense methods in both conventional and new metrics. Codes are available at https://github.com/michaeltian108/CA-TRIDE.