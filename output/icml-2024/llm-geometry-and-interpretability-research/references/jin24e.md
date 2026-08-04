---
title: "Emergent Representations of Program Semantics in Language Models Trained on Programs"
source: "https://proceedings.mlr.press/v235/jin24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24e/jin24e.pdf"
categories: ['llm-geometry-and-interpretability-research', 'neural-network-learning-dynamics-theory']
tags: ['program-semantics', 'language-models-of-code', 'emergent-representations', 'transformer']
venue: "ICML 2024"
tldr: "Transformer language models trained on programs via next-token prediction emergently learn internal representations that reflect formal program semantics."
---

# Emergent Representations of Program Semantics in Language Models Trained on Programs

**Source**: [https://proceedings.mlr.press/v235/jin24e.html](https://proceedings.mlr.press/v235/jin24e.html)

**TLDR**: Transformer language models trained on programs via next-token prediction emergently learn internal representations that reflect formal program semantics.

## Abstract

We present evidence that language models (LMs) of code can learn to represent the formal semantics of programs, despite being trained only to perform next-token prediction. Specifically, we train a Transformer model on a synthetic corpus of programs written in a domain-specific language for navigating 2D grid world environments. Each program in the corpus is preceded by a (partial) specification in the form of several input-output grid world states. Despite providing no further inductive biases, we find that a probing classifier is able to extract increasingly accurate representations of the unobserved, intermediate grid world states from the LM hidden states over the course of training, suggesting the LM acquires an emergent ability to interpret programs in the formal sense. We also develop a novel interventional baseline that enables us to disambiguate what is represented by the LM as opposed to learned by the probe. We anticipate that this technique may be generally applicable to a broad range of semantic probing experiments. In summary, this paper does not propose any new techniques for training LMs of code, but develops an experimental framework for and provides insights into the acquisition and representation of formal semantics in statistical models of code.