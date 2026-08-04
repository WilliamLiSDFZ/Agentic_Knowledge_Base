---
title: "In-context Learning on Function Classes Unveiled for Transformers"
source: "https://proceedings.mlr.press/v235/wang24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ae/wang24ae.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['in-context-learning', 'transformers', 'function-classes', 'theoretical-analysis']
venue: "ICML 2024"
tldr: "This paper theoretically explains how transformers learn different function classes in-context through analysis of attention mechanisms."
---

# In-context Learning on Function Classes Unveiled for Transformers

**Source**: [https://proceedings.mlr.press/v235/wang24ae.html](https://proceedings.mlr.press/v235/wang24ae.html)

**TLDR**: This paper theoretically explains how transformers learn different function classes in-context through analysis of attention mechanisms.

## Abstract

Transformer-based neural sequence models exhibit a remarkable ability to perform in-context learning. Given some training examples, a pre-trained model can make accurate predictions on an unseen input. This paper studies why transformers can learn different types of function classes in-context. We first show by construction that there exists a family of transformers (with different activation functions) that implement approximate gradient descent on the parameters of neural networks, and we provide an upper bound for the number of heads, hidden dimensions, and layers of the transformer. We also show that a transformer can learn linear functions, the indicator function of a unit ball, and smooth functions in-context by learning neural networks that approximate them. The above instances mainly focus on a transformer pre-trained on single tasks. We also prove that when pre-trained on two tasks: linear regression and classification, a transformer can make accurate predictions on both tasks simultaneously. Our results move beyond linearity in terms of in-context learning instances and provide a comprehensive understanding of why transformers can learn many types of function classes through the bridge of neural networks.