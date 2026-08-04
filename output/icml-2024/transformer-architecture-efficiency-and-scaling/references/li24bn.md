---
title: "How Do Nonlinear Transformers Learn and Generalize in In-Context Learning?"
source: "https://proceedings.mlr.press/v235/li24bn.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bn/li24bn.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['in-context-learning', 'nonlinear-transformers', 'generalization-theory']
venue: "ICML 2024"
tldr: "Theoretically analyzes how nonlinear transformers learn and generalize in in-context learning settings."
---

# How Do Nonlinear Transformers Learn and Generalize in In-Context Learning?

**Source**: [https://proceedings.mlr.press/v235/li24bn.html](https://proceedings.mlr.press/v235/li24bn.html)

**TLDR**: Theoretically analyzes how nonlinear transformers learn and generalize in in-context learning settings.

## Abstract

Transformer-based large language models have displayed impressive in-context learning capabilities, where a pre-trained model can handle new tasks without fine-tuning by simply augmenting the query with some input-output examples from that task. Despite the empirical success, the mechanics of how to train a Transformer to achieve ICL and the corresponding ICL capacity is mostly elusive due to the technical challenges of analyzing the nonconvex training problems resulting from the nonlinear self-attention and nonlinear activation in Transformers. To the best of our knowledge, this paper provides the first theoretical analysis of the training dynamics of Transformers with nonlinear self-attention and nonlinear MLP, together with the ICL generalization capability of the resulting model. Focusing on a group of binary classification tasks, we train Transformers using data from a subset of these tasks and quantify the impact of various factors on the ICL generalization performance on the remaining unseen tasks with and without data distribution shifts. We also analyze how different components in the learned Transformers contribute to the ICL performance. Furthermore, we provide the first theoretical analysis of how model pruning affects ICL performance and prove that proper magnitude-based pruning can have a minimal impact on ICL while reducing inference costs. These theoretical findings are justified through numerical experiments.