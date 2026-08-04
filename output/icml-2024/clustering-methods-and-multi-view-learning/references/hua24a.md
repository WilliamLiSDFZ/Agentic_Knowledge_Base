---
title: "ReconBoost: Boosting Can Achieve Modality Reconcilement"
source: "https://proceedings.mlr.press/v235/hua24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hua24a/hua24a.pdf"
categories: ['continual-learning-memory-plasticity', 'clustering-methods-and-multi-view-learning']
tags: ['multimodal-learning', 'modality-reconciliation', 'boosting']
venue: "ICML 2024"
tldr: "Proposes ReconBoost, an alternating multi-modal learning paradigm that balances exploitation of uni-modal features and exploration of cross-modal interactions."
---

# ReconBoost: Boosting Can Achieve Modality Reconcilement

**Source**: [https://proceedings.mlr.press/v235/hua24a.html](https://proceedings.mlr.press/v235/hua24a.html)

**TLDR**: Proposes ReconBoost, an alternating multi-modal learning paradigm that balances exploitation of uni-modal features and exploration of cross-modal interactions.

## Abstract

This paper explores a novel multi-modal alternating learning paradigm pursuing a reconciliation between the exploitation of uni-modal features and the exploration of cross-modal interactions. This is motivated by the fact that current paradigms of multi-modal learning tend to explore multi-modal features simultaneously. The resulting gradient prohibits further exploitation of the features in the weak modality, leading to modality competition, where the dominant modality overpowers the learning process. To address this issue, we study the modality-alternating learning paradigm to achieve reconcilement. Specifically, we propose a new method called ReconBoost to update a fixed modality each time. Herein, the learning objective is dynamically adjusted with a reconcilement regularization against competition with the historical models. By choosing a KL-based reconcilement, we show that the proposed method resembles Friedman’s Gradient-Boosting (GB) algorithm, where the updated learner can correct errors made by others and help enhance the overall performance. The major difference with the classic GB is that we only preserve the newest model for each modality to avoid overfitting caused by ensembling strong learners. Furthermore, we propose a memory consolidation scheme and a global rectification scheme to make this strategy more effective. Experiments over six multi-modal benchmarks speak to the efficacy of the proposed method.