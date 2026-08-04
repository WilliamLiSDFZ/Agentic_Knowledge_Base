---
title: "Variational Learning is Effective for Large Deep Networks"
source: "https://proceedings.mlr.press/v235/shen24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shen24b/shen24b.pdf"
categories: ['optimization-algorithms-convergence-theory', 'generative-models-and-variational-inference']
tags: ['variational-inference', 'Bayesian-deep-learning', 'large-scale-training']
venue: "ICML 2024"
tldr: "This paper provides extensive empirical evidence that variational learning with the IVON optimizer effectively matches or outperforms Adam for training large neural networks."
---

# Variational Learning is Effective for Large Deep Networks

**Source**: [https://proceedings.mlr.press/v235/shen24b.html](https://proceedings.mlr.press/v235/shen24b.html)

**TLDR**: This paper provides extensive empirical evidence that variational learning with the IVON optimizer effectively matches or outperforms Adam for training large neural networks.

## Abstract

We give extensive empirical evidence against the common belief that variational learning is ineffective for large neural networks. We show that an optimizer called Improved Variational Online Newton (IVON) consistently matches or outperforms Adam for training large networks such as GPT-2 and ResNets from scratch. IVON’s computational costs are nearly identical to Adam but its predictive uncertainty is better. We show several new use cases of IVON where we improve finetuning and model merging in Large Language Models, accurately predict generalization error, and faithfully estimate sensitivity to data. We find overwhelming evidence that variational learning is effective. Code is available at https://github.com/team-approx-bayes/ivon.