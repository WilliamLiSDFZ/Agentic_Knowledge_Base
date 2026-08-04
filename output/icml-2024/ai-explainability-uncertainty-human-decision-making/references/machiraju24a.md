---
title: "Prospector Heads: Generalized Feature Attribution for Large Models & Data"
source: "https://proceedings.mlr.press/v235/machiraju24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/machiraju24a/machiraju24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'probabilistic-generating-circuits-research']
tags: ['feature-attribution', 'large-models', 'biomedical-applications']
venue: "ICML 2024"
tldr: "Prospector heads enable generalized and efficient feature attribution for large pretrained models across scientific and biomedical domains."
---

# Prospector Heads: Generalized Feature Attribution for Large Models & Data

**Source**: [https://proceedings.mlr.press/v235/machiraju24a.html](https://proceedings.mlr.press/v235/machiraju24a.html)

**TLDR**: Prospector heads enable generalized and efficient feature attribution for large pretrained models across scientific and biomedical domains.

## Abstract

Feature attribution, the ability to localize regions of the input data that are relevant for classification, is an important capability for ML models in scientific and biomedical domains. Current methods for feature attribution, which rely on "explaining" the predictions of end-to-end classifiers, suffer from imprecise feature localization and are inadequate for use with small sample sizes and high-dimensional datasets due to computational challenges. We introduce prospector heads, an efficient and interpretable alternative to explanation-based attribution methods that can be applied to any encoder and any data modality. Prospector heads generalize across modalities through experiments on sequences (text), images (pathology), and graphs (protein structures), outperforming baseline attribution methods by up to 26.3 points in mean localization AUPRC. We also demonstrate how prospector heads enable improved interpretation and discovery of class-specific patterns in input data. Through their high performance, flexibility, and generalizability, prospectors provide a framework for improving trust and transparency for ML models in complex domains.