---
title: "Active Label Correction for Semantic Segmentation with Foundation Models"
source: "https://proceedings.mlr.press/v235/kim24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24g/kim24g.pdf"
categories: ['data-selection-and-active-learning-methods', 'continual-learning-memory-plasticity']
tags: ['active-label-correction', 'semantic-segmentation', 'foundation-models']
venue: "ICML 2024"
tldr: "Proposes an active label correction framework for semantic segmentation that leverages foundation models to efficiently fix noisy pixel-wise annotations."
---

# Active Label Correction for Semantic Segmentation with Foundation Models

**Source**: [https://proceedings.mlr.press/v235/kim24g.html](https://proceedings.mlr.press/v235/kim24g.html)

**TLDR**: Proposes an active label correction framework for semantic segmentation that leverages foundation models to efficiently fix noisy pixel-wise annotations.

## Abstract

Training and validating models for semantic segmentation require datasets with pixel-wise annotations, which are notoriously labor-intensive. Although useful priors such as foundation models or crowdsourced datasets are available, they are error-prone. We hence propose an effective framework of active label correction (ALC) based on a design of correction query to rectify pseudo labels of pixels, which in turn is more annotator-friendly than the standard one inquiring to classify a pixel directly according to our theoretical analysis and user study. Specifically, leveraging foundation models providing useful zero-shot predictions on pseudo labels and superpixels, our method comprises two key techniques: (i) an annotator-friendly design of correction query with the pseudo labels, and (ii) an acquisition function looking ahead label expansions based on the superpixels. Experimental results on PASCAL, Cityscapes, and Kvasir-SEG datasets demonstrate the effectiveness of our ALC framework, outperforming prior methods for active semantic segmentation and label correction. Notably, utilizing our method, we obtained a revised dataset of PASCAL by rectifying errors in 2.6 million pixels in PASCAL dataset.