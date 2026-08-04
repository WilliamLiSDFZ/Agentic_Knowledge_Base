---
title: "Learning Universal Predictors"
source: "https://proceedings.mlr.press/v235/grau-moya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/grau-moya24a/grau-moya24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-network-learning-dynamics-theory']
tags: ['meta-learning', 'universal-prediction', 'amortized-inference']
venue: "ICML 2024"
tldr: "This paper explores the limits of meta-learning by amortizing universal predictors through neural network pretraining on broad task distributions."
---

# Learning Universal Predictors

**Source**: [https://proceedings.mlr.press/v235/grau-moya24a.html](https://proceedings.mlr.press/v235/grau-moya24a.html)

**TLDR**: This paper explores the limits of meta-learning by amortizing universal predictors through neural network pretraining on broad task distributions.

## Abstract

Meta-learning has emerged as a powerful approach to train neural networks to learn new tasks quickly from limited data by pre-training them on a broad set of tasks. But, what are the limits of meta-learning? In this work, we explore the potential of amortizing the most powerful universal predictor, namely Solomonoff Induction (SI), into neural networks via leveraging (memory-based) meta-learning to its limits. We use Universal Turing Machines (UTMs) to generate training data used to expose networks to a broad range of patterns. We provide theoretical analysis of the UTM data generation processes and meta-training protocols. We conduct comprehensive experiments with neural architectures (e.g. LSTMs, Transformers) and algorithmic data generators of varying complexity and universality. Our results suggest that UTM data is a valuable resource for meta-learning, and that it can be used to train neural networks capable of learning universal prediction strategies.