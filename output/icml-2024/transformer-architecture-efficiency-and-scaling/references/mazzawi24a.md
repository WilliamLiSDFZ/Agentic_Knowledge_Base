---
title: "Deep Fusion: Efficient Network Training via Pre-trained Initializations"
source: "https://proceedings.mlr.press/v235/mazzawi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mazzawi24a/mazzawi24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['network-growing', 'pre-trained-initialization', 'training-efficiency']
venue: "ICML 2024"
tldr: "A theoretical framework explaining how pre-trained initializations and network fusion reduce training cost for large language models."
---

# Deep Fusion: Efficient Network Training via Pre-trained Initializations

**Source**: [https://proceedings.mlr.press/v235/mazzawi24a.html](https://proceedings.mlr.press/v235/mazzawi24a.html)

**TLDR**: A theoretical framework explaining how pre-trained initializations and network fusion reduce training cost for large language models.

## Abstract

Training deep neural networks for large language models (LLMs) remains computationally very expensive. To mitigate this, network growing algorithms offer potential cost savings, but their underlying mechanisms are poorly understood. In this paper, we propose a theoretical framework using backward error analysis to illuminate the dynamics of mid-training network growth. Furthermore, we introduce Deep Fusion, an efficient network training approach that leverages pre-trained initializations of smaller networks, facilitating network growth from diverse sources. Our experiments validate the power of our theoretical framework in guiding the optimal use of Deep Fusion. With carefully optimized training dynamics, Deep Fusion demonstrates significant reductions in both training time and resource consumption. Importantly, these gains are achieved without sacrificing performance. We demonstrate reduced computational requirements, and improved generalization performance on a variety of NLP tasks and T5 model sizes.