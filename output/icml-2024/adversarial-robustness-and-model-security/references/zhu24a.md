---
title: "Iterative Search Attribution for Deep Neural Networks"
source: "https://proceedings.mlr.press/v235/zhu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24a/zhu24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'adversarial-robustness-and-model-security']
tags: ['feature-attribution', 'explainability', 'iterative-search']
venue: "ICML 2024"
tldr: "Proposes an iterative search attribution method for deep neural networks to improve interpretability by identifying influential input features for model predictions."
---

# Iterative Search Attribution for Deep Neural Networks

**Source**: [https://proceedings.mlr.press/v235/zhu24a.html](https://proceedings.mlr.press/v235/zhu24a.html)

**TLDR**: Proposes an iterative search attribution method for deep neural networks to improve interpretability by identifying influential input features for model predictions.

## Abstract

Deep neural networks (DNNs) have achieved state-of-the-art performance across various applications. However, ensuring the reliability and trustworthiness of DNNs requires enhanced interpretability of model inputs and outputs. As an effective means of Explainable Artificial Intelligence (XAI) research, the interpretability of existing attribution algorithms varies depending on the choice of reference point, the quality of adversarial samples, or the applicability of gradient constraints in specific tasks. To thoroughly explore the attribution integration paths, in this paper, inspired by the iterative generation of high-quality samples in the diffusion model, we propose an Iterative Search Attribution (ISA) method. To enhance attribution accuracy, ISA distinguishes the importance of samples during gradient ascent and descent, while clipping the relatively unimportant features in the model. Specifically, we introduce a scale parameter during the iterative process to ensure the features in next iteration are always more significant than those in current iteration. Comprehensive experimental results show that our method has superior interpretability in image recognition tasks compared with state-of-the-art baselines. Our code is available at: https://github.com/LMBTough/ISA