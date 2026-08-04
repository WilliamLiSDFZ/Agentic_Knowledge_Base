---
title: "Improving Interpretation Faithfulness for Vision Transformers"
source: "https://proceedings.mlr.press/v235/hu24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24k/hu24k.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['vision-transformers', 'interpretability', 'faithfulness', 'attention', 'explanation']
venue: "ICML 2024"
tldr: "Improves the faithfulness of attention-based explanations in Vision Transformers by addressing inconsistencies between attention weights and model decisions."
---

# Improving Interpretation Faithfulness for Vision Transformers

**Source**: [https://proceedings.mlr.press/v235/hu24k.html](https://proceedings.mlr.press/v235/hu24k.html)

**TLDR**: Improves the faithfulness of attention-based explanations in Vision Transformers by addressing inconsistencies between attention weights and model decisions.

## Abstract

Vision Transformers (ViTs) have achieved state-of-the-art performance for various vision tasks. One reason behind the success lies in their ability to provide plausible innate explanations for the behavior of neural architectures. However, ViTs suffer from issues with explanation faithfulness, as their focal points are fragile to adversarial attacks and can be easily changed with even slight perturbations on the input image. In this paper, we propose a rigorous approach to mitigate these issues by introducing Faithful ViTs (FViTs). Briefly speaking, an FViT should have the following two properties: (1) The top-$k$ indices of its self-attention vector should remain mostly unchanged under input perturbation, indicating stable explanations; (2) The prediction distribution should be robust to perturbations. To achieve this, we propose a new method called Denoised Diffusion Smoothing (DDS), which adopts randomized smoothing and diffusion-based denoising. We theoretically prove that processing ViTs directly with DDS can turn them into FViTs. We also show that Gaussian noise is nearly optimal for both $\ell_2$ and $\ell_\infty$-norm cases. Finally, we demonstrate the effectiveness of our approach through comprehensive experiments and evaluations. Results show that FViTs are more robust against adversarial attacks while maintaining the explainability of attention, indicating higher faithfulness.