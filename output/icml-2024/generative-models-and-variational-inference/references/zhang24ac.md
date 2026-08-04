---
title: "An Interpretable Evaluation of Entropy-based Novelty of Generative Models"
source: "https://proceedings.mlr.press/v235/zhang24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ac/zhang24ac.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['generative-model-evaluation', 'entropy', 'novelty-assessment']
venue: "ICML 2024"
tldr: "Proposes an interpretable entropy-based metric for evaluating the novelty of generative models relative to reference datasets."
---

# An Interpretable Evaluation of Entropy-based Novelty of Generative Models

**Source**: [https://proceedings.mlr.press/v235/zhang24ac.html](https://proceedings.mlr.press/v235/zhang24ac.html)

**TLDR**: Proposes an interpretable entropy-based metric for evaluating the novelty of generative models relative to reference datasets.

## Abstract

The massive developments of generative model frameworks require principled methods for the evaluation of a model’s novelty compared to a reference dataset. While the literature has extensively studied the evaluation of the quality, diversity, and generalizability of generative models, the assessment of a model’s novelty compared to a reference model has not been adequately explored in the machine learning community. In this work, we focus on the novelty assessment for multi-modal distributions and attempt to address the following differential clustering task: Given samples of a generative model $P_\mathcal{G}$ and a reference model $P_\mathrm{ref}$, how can we discover the sample types expressed by $P_\mathcal{G}$ more frequently than in $P_\mathrm{ref}$? We introduce a spectral approach to the differential clustering task and propose the Kernel-based Entropic Novelty (KEN) score to quantify the mode-based novelty of $P_\mathcal{G}$ with respect to $P_\mathrm{ref}$. We analyze the KEN score for mixture distributions with well-separable components and develop a kernel-based method to compute the KEN score from empirical data. We support the KEN framework by presenting numerical results on synthetic and real image datasets, indicating the framework’s effectiveness in detecting novel modes and comparing generative models. The paper’s code is available at: github.com/buyeah1109/KEN.