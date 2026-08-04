---
title: "Learning to Compile Programs to Neural Networks"
source: "https://proceedings.mlr.press/v235/weber24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/weber24b/weber24b.pdf"
categories: ['llm-geometry-and-interpretability-research']
tags: ['neural-surrogates', 'program-compilation', 'meta-learning']
venue: "ICML 2024"
tldr: "This paper proposes learning to compile programs directly into neural network surrogates, enabling efficient program behavior approximation without input-output training data."
---

# Learning to Compile Programs to Neural Networks

**Source**: [https://proceedings.mlr.press/v235/weber24b.html](https://proceedings.mlr.press/v235/weber24b.html)

**TLDR**: This paper proposes learning to compile programs directly into neural network surrogates, enabling efficient program behavior approximation without input-output training data.

## Abstract

A neural surrogate is a neural network that mimics the behavior of a program. Neural surrogates of programs have been used to automatically tune program inputs, adapt programs to new settings, and accelerate computations. Neural surrogates have traditionally been developed by training on input-output examples for a single program. Language models present another approach wherein a model is trained on a single, large dataset then directly consumes program text, to act as a neural surrogate of the program. Having the language model as both the neural surrogate generator and the neural surrogate, however, poses a tradeoff of limited accuracy or excessive resource consumption. We present neural surrogate compilation, a technique for producing neural surrogates directly from program text without coupling neural surrogate generation and execution. We implement neural surrogate compilers using hypernetworks trained on a dataset of C programs and find they produce neural surrogates that are $1.91$-$9.50\times$ as data-efficient and train in $4.31$-$7.28\times$ fewer epochs than neural surrogates trained from scratch.