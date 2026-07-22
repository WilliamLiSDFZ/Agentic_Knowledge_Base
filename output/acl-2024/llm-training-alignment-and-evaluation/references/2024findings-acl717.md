---
title: "Efficient Training of Language Models with Compact and Consistent Next Token Distributions"
source: "https://aclanthology.org/2024.findings-acl.717/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['language-model-pretraining', 'n-gram-distribution', 'token-efficiency']
venue: "ACL 2024"
tldr: "Shows that pre-aggregating training corpora with collapsed n-gram distributions enables faster and better language model training."
---

# Efficient Training of Language Models with Compact and Consistent Next Token Distributions

**Source**: [https://aclanthology.org/2024.findings-acl.717/](https://aclanthology.org/2024.findings-acl.717/)

**TLDR**: Shows that pre-aggregating training corpora with collapsed n-gram distributions enables faster and better language model training.

## Abstract

AbstractMaximizing the likelihood of the next token is an established, statistically sound objective for pre-training language models. In this paper we show that we can train better models faster by pre-aggregating the corpus with a collapsed n-gram distribution. Previous studies have proposed corpus-level n-gram statistics as a regularizer; however, the construction and querying of such n-grams, if done naively, prove to be costly and significantly impede training speed, thereby limiting their application in modern large language model pre-training.We introduce an alternative compact representation of the next token distribution that, in expectation, aligns with the complete n-gram distribution while markedly reducing variance across mini-batches compared to the standard next-token loss. Empirically, we demonstrate that both the n-gram regularized model and our approximation yield substantial improvements in model quality and convergence rate compared to existing methods. Furthermore, our approximation facilitates scalability of gains to larger datasets and models compared to the straightforward n-gram regularization method.