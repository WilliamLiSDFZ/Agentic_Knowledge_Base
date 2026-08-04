---
title: "Do Efficient Transformers Really Save Computation?"
source: "https://proceedings.mlr.press/v235/yang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24a/yang24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['efficient-transformers', 'computational-analysis', 'attention-mechanisms']
venue: "ICML 2024"
tldr: "Empirically and theoretically investigates whether efficient Transformer alternatives truly reduce computation compared to standard Transformers."
---

# Do Efficient Transformers Really Save Computation?

**Source**: [https://proceedings.mlr.press/v235/yang24a.html](https://proceedings.mlr.press/v235/yang24a.html)

**TLDR**: Empirically and theoretically investigates whether efficient Transformer alternatives truly reduce computation compared to standard Transformers.

## Abstract

As transformer-based language models are trained on increasingly large datasets and with vast numbers of parameters, finding more efficient alternatives to the standard Transformer has become very valuable. While many efficient Transformers and Transformer alternatives have been proposed, none provide theoretical guarantees that they are a suitable replacement for the standard Transformer. This makes it challenging to identify when to use a specific model and what directions to prioritize for further investigation. In this paper, we aim to understand the capabilities and limitations of efficient Transformers, specifically the Sparse Transformer and the Linear Transformer. We focus on their reasoning capability as exhibited by Chain-of-Thought (CoT) prompts and follow previous works to model them as Dynamic Programming (DP) problems. Our results show that while these models are expressive enough to solve general DP tasks, contrary to expectations, they require a model size that scales with the problem size. Nonetheless, we identify a class of DP problems for which these models can be more efficient than the standard Transformer. We confirm our theoretical results through experiments on representative DP tasks, adding to the understanding of efficient Transformers’ practical strengths and weaknesses.