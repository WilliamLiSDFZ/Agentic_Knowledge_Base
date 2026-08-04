---
title: "Rényi Pufferfish Privacy: General Additive Noise Mechanisms and Privacy Amplification by Iteration via Shift Reduction Lemmas"
source: "https://proceedings.mlr.press/v235/pierquin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pierquin24a/pierquin24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['pufferfish-privacy', 'differential-privacy', 'additive-noise']
venue: "ICML 2024"
tldr: "Generalizes Pufferfish privacy with Rényi divergence and derives privacy amplification results via shift reduction lemmas."
---

# Rényi Pufferfish Privacy: General Additive Noise Mechanisms and Privacy Amplification by Iteration via Shift Reduction Lemmas

**Source**: [https://proceedings.mlr.press/v235/pierquin24a.html](https://proceedings.mlr.press/v235/pierquin24a.html)

**TLDR**: Generalizes Pufferfish privacy with Rényi divergence and derives privacy amplification results via shift reduction lemmas.

## Abstract

Pufferfish privacy is a flexible generalization of differential privacy that allows to model arbitrary secrets and adversary’s prior knowledge about the data. Unfortunately, designing general and tractable Pufferfish mechanisms that do not compromise utility is challenging. Furthermore, this framework does not provide the composition guarantees needed for a direct use in iterative machine learning algorithms. To mitigate these issues, we introduce a Rényi divergence-based variant of Pufferfish and show that it allows us to extend the applicability of the Pufferfish framework. We first generalize the Wasserstein mechanism to cover a wide range of noise distributions and introduce several ways to improve its utility. Finally, as an alternative to composition, we prove privacy amplification results for contractive noisy iterations and showcase the first use of Pufferfish in private convex optimization. A common ingredient underlying our results is the use and extension of shift reduction lemmas.