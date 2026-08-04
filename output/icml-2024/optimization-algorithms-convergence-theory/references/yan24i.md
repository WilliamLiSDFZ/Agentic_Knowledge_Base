---
title: "Reducing Balancing Error for Causal Inference via Optimal Transport"
source: "https://proceedings.mlr.press/v235/yan24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24i/yan24i.pdf"
categories: ['causal-inference-and-discovery-methods', 'optimization-algorithms-convergence-theory']
tags: ['causal-inference', 'optimal-transport', 'confounding-bias']
venue: "ICML 2024"
tldr: "Defines a balancing error metric via optimal transport to reduce distribution shift between control and treated groups for improved causal inference."
---

# Reducing Balancing Error for Causal Inference via Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/yan24i.html](https://proceedings.mlr.press/v235/yan24i.html)

**TLDR**: Defines a balancing error metric via optimal transport to reduce distribution shift between control and treated groups for improved causal inference.

## Abstract

Most studies on causal inference tackle the issue of confounding bias by reducing the distribution shift between the control and treated groups. However, it remains an open question to adopt an appropriate metric for distribution shift in practice. In this paper, we define a generic balancing error on reweighted samples to characterize the confounding bias, and study the connection between the balancing error and the Wasserstein discrepancy derived from the theory of optimal transport. We not only regard the Wasserstein discrepancy as the metric of distribution shift, but also explore the association between the balancing error and the underlying cost function involved in the Wasserstein discrepancy. Motivated by this, we propose to reduce the balancing error under the framework of optimal transport with learnable marginal distributions and the cost function, which is implemented by jointly learning weights and representations associated with factual outcomes. The experiments on both synthetic and real-world datasets demonstrate the effectiveness of our proposed method.