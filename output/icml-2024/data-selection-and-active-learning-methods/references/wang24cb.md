---
title: "Defense against Model Extraction Attack by Bayesian Active Watermarking"
source: "https://proceedings.mlr.press/v235/wang24cb.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cb/wang24cb.pdf"
categories: ['adversarial-robustness-and-model-security', 'data-selection-and-active-learning-methods']
tags: ['model-extraction', 'watermarking', 'Bayesian-active-learning', 'model-security']
venue: "ICML 2024"
tldr: "Proposes a Bayesian active watermarking defense against model extraction attacks that is computationally efficient and does not require expensive retraining."
---

# Defense against Model Extraction Attack by Bayesian Active Watermarking

**Source**: [https://proceedings.mlr.press/v235/wang24cb.html](https://proceedings.mlr.press/v235/wang24cb.html)

**TLDR**: Proposes a Bayesian active watermarking defense against model extraction attacks that is computationally efficient and does not require expensive retraining.

## Abstract

Model extraction is to obtain a cloned model that replicates the functionality of a black-box victim model solely through query-based access. Present defense strategies exhibit shortcomings, manifesting as: (1) computational or memory inefficiencies during deployment; or (2) dependence on expensive defensive training methods that mandate the re-training of the victim model; or (3) watermarking-based methods only passively detect model theft without actively preventing model extraction. To address these limitations, we introduce an innovative Bayesian active watermarking technique to fine-tune the victim model and learn the watermark posterior distribution conditioned on input data. The fine-tuning process aims to maximize the log-likelihood on watermarked in-distribution training data for preserving model utility while simultaneously maximizing the change of model’s outputs on watermarked out-of-distribution data, thereby achieving effective defense. During deployment, a watermark is randomly sampled from the estimated watermark posterior. This watermark is then added to the input query, and the victim model returns the prediction based on the watermarked input query to users. This proactive defense approach requires only slight fine-tuning of the victim model without the need of full re-training and demonstrates high efficiency in terms of memory and computation during deployment. Rigorous theoretical analysis and comprehensive experimental results demonstrate the efficacy of our proposed method.