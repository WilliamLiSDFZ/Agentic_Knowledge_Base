---
title: "Long-Tail Learning with Foundation Model: Heavy Fine-Tuning Hurts"
source: "https://proceedings.mlr.press/v235/shi24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shi24g/shi24g.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'continual-learning-memory-plasticity']
tags: ['long-tail-learning', 'foundation-models', 'fine-tuning']
venue: "ICML 2024"
tldr: "Shows that heavy fine-tuning of foundation models can hurt performance on long-tail learning tasks and proposes mitigations."
---

# Long-Tail Learning with Foundation Model: Heavy Fine-Tuning Hurts

**Source**: [https://proceedings.mlr.press/v235/shi24g.html](https://proceedings.mlr.press/v235/shi24g.html)

**TLDR**: Shows that heavy fine-tuning of foundation models can hurt performance on long-tail learning tasks and proposes mitigations.

## Abstract

The fine-tuning paradigm in addressing long-tail learning tasks has sparked significant interest since the emergence of foundation models. Nonetheless, how fine-tuning impacts performance in long-tail learning was not explicitly quantified. In this paper, we disclose that heavy fine-tuning may even lead to non-negligible performance deterioration on tail classes, and lightweight fine-tuning is more effective. The reason is attributed to inconsistent class conditions caused by heavy fine-tuning. With the observation above, we develop a low-complexity and accurate long-tail learning algorithms LIFT with the goal of facilitating fast prediction and compact models by adaptive lightweight fine-tuning. Experiments clearly verify that both the training time and the learned parameters are significantly reduced with more accurate predictive performance compared with state-of-the-art approaches. The implementation code is available at https://github.com/shijxcs/LIFT.