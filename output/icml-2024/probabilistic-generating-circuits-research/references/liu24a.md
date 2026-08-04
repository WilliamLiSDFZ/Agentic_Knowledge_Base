---
title: "Scaling Tractable Probabilistic Circuits: A Systems Perspective"
source: "https://proceedings.mlr.press/v235/liu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24a/liu24a.pdf"
categories: ['probabilistic-generating-circuits-research']
tags: ['probabilistic-circuits', 'scalability', 'inference']
venue: "ICML 2024"
tldr: "This paper addresses systems-level challenges in scaling probabilistic circuits for complex real-world generative modeling tasks."
---

# Scaling Tractable Probabilistic Circuits: A Systems Perspective

**Source**: [https://proceedings.mlr.press/v235/liu24a.html](https://proceedings.mlr.press/v235/liu24a.html)

**TLDR**: This paper addresses systems-level challenges in scaling probabilistic circuits for complex real-world generative modeling tasks.

## Abstract

Probabilistic Circuits (PCs) are a general framework for tractable deep generative models, which support exact and efficient probabilistic inference on their learned distributions. Recent modeling and training advancements have enabled their application to complex real-world tasks. However, the time and memory inefficiency of existing PC implementations hinders further scaling up. This paper proposes PyJuice, a general GPU implementation design for PCs that improves prior art in several regards. Specifically, PyJuice is 1-2 orders of magnitude faster than existing systems (including very recent ones) at training large-scale PCs. Moreover, PyJuice consumes 2-5x less GPU memory, which enables us to train larger models. At the core of our system is a compilation process that converts a PC into a compact representation amenable to efficient block-based parallelization, which significantly reduces IO and makes it possible to leverage Tensor Cores available in modern GPUs. Empirically, PyJuice can be used to improve state-of-the-art PCs trained on image (e.g., ImageNet32) and language (e.g., WikiText, CommonGen) datasets. We further establish a new set of baselines on natural image and language datasets by benchmarking existing PC structures but with much larger sizes and more training epochs, with the hope of incentivizing future research. Code is available at https://github.com/Tractables/pyjuice.