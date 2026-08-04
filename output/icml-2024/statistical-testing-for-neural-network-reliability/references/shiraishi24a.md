---
title: "Statistical Test for Attention Maps in Vision Transformers"
source: "https://proceedings.mlr.press/v235/shiraishi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shiraishi24a/shiraishi24a.pdf"
categories: ['statistical-testing-for-neural-network-reliability']
tags: ['vision-transformers', 'attention-maps', 'statistical-testing']
venue: "ICML 2024"
tldr: "Proposes a statistical test to assess the significance of attention maps in Vision Transformers for better model interpretability."
---

# Statistical Test for Attention Maps in Vision Transformers

**Source**: [https://proceedings.mlr.press/v235/shiraishi24a.html](https://proceedings.mlr.press/v235/shiraishi24a.html)

**TLDR**: Proposes a statistical test to assess the significance of attention maps in Vision Transformers for better model interpretability.

## Abstract

The Vision Transformer (ViT) demonstrates exceptional performance in various computer vision tasks. Attention is crucial for ViT to capture complex wide-ranging relationships among image patches, allowing the model to weigh the importance of image patches and aiding our understanding of the decision-making process. However, when utilizing the attention of ViT as evidence in high-stakes decision-making tasks such as medical diagnostics, a challenge arises due to the potential of attention mechanisms erroneously focusing on irrelevant regions. In this study, we propose a statistical test for ViT’s attentions, enabling us to use the attentions as reliable quantitative evidence indicators for ViT’s decision-making with a rigorously controlled error rate. Using the framework called selective inference, we quantify the statistical significance of attentions in the form of p-values, which enables the theoretically grounded quantification of the false positive detection probability of attentions. We demonstrate the validity and the effectiveness of the proposed method through numerical experiments and applications to brain image diagnoses.