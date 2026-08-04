---
title: "Saliency strikes back: How filtering out high frequencies improves white-box explanations"
source: "https://proceedings.mlr.press/v235/muzellec24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/muzellec24a/muzellec24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making']
tags: ['saliency-maps', 'attribution-methods', 'high-frequency-filtering']
venue: "ICML 2024"
tldr: "Filtering high-frequency components from inputs significantly improves the faithfulness of white-box attribution methods for neural network explainability."
---

# Saliency strikes back: How filtering out high frequencies improves white-box explanations

**Source**: [https://proceedings.mlr.press/v235/muzellec24a.html](https://proceedings.mlr.press/v235/muzellec24a.html)

**TLDR**: Filtering high-frequency components from inputs significantly improves the faithfulness of white-box attribution methods for neural network explainability.

## Abstract

Attribution methods correspond to a class of explainability methods (XAI) that aim to assess how individual inputs contribute to a model’s decision-making process. We have identified a significant limitation in one type of attribution methods, known as “white-box" methods. Although highly efficient, as we will show, these methods rely on a gradient signal that is often contaminated by high-frequency artifacts. To overcome this limitation, we introduce a new approach called "FORGrad". This simple method effectively filters out these high-frequency artifacts using optimal cut-off frequencies tailored to the unique characteristics of each model architecture. Our findings show that FORGrad consistently enhances the performance of already existing white-box methods, enabling them to compete effectively with more accurate yet computationally demanding "black-box" methods. We anticipate that our research will foster broader adoption of simpler and more efficient white-box methods for explainability, offering a better balance between faithfulness and computational efficiency.