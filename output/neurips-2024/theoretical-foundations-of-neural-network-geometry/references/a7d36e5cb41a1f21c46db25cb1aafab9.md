---
title: "Unraveling the Gradient Descent Dynamics of Transformers"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a7d36e5cb41a1f21c46db25cb1aafab9-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory', 'theoretical-foundations-of-neural-network-geometry']
tags: ['transformer-optimization', 'gradient-descent-dynamics', 'theoretical-analysis']
venue: "NeurIPS 2024"
tldr: "A theoretical study of gradient descent dynamics in transformers addressing convergence and implicit bias questions."
---

# Unraveling the Gradient Descent Dynamics of Transformers

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a7d36e5cb41a1f21c46db25cb1aafab9-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a7d36e5cb41a1f21c46db25cb1aafab9-Abstract-Conference.html)

**TLDR**: A theoretical study of gradient descent dynamics in transformers addressing convergence and implicit bias questions.

## Abstract

While the Transformer architecture has achieved remarkable success across various domains, a thorough theoretical foundation explaining its optimization dynamics is yet to be fully developed. In this study, we aim to bridge this understanding gap by answering the following two core questions: (1) Which types of Transformer architectures allow Gradient Descent (GD) to achieve guaranteed convergence? and (2) Under what initial conditions and architectural specifics does the Transformer achieve rapid convergence during training? By analyzing the loss landscape of a single Transformer layer using Softmax and Gaussian attention kernels, our work provides concrete answers to these questions. Our findings demonstrate that, with appropriate weight initialization, GD can train a Transformer model (with either kernel type) to achieve a global optimal solution, especially when the input embedding dimension is large. Nonetheless, certain scenarios highlight potential pitfalls: training a Transformer using the Softmax attention kernel may sometimes lead to suboptimal local solutions. In contrast,  the Gaussian attention kernel exhibits a much favorable behavior. Our empirical study further validate the theoretical findings.