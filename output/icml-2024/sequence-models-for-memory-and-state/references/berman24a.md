---
title: "Sequential Disentanglement by Extracting Static Information From A Single Sequence Element"
source: "https://proceedings.mlr.press/v235/berman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/berman24a/berman24a.pdf"
categories: ['generative-models-and-variational-inference', 'sequence-models-for-memory-and-state']
tags: ['sequential-disentanglement', 'representation-learning', 'static-dynamic-decomposition', 'VAE', 'unsupervised-learning']
venue: "ICML 2024"
tldr: "Proposes a method for unsupervised sequential disentanglement that extracts static information from a single sequence element."
---

# Sequential Disentanglement by Extracting Static Information From A Single Sequence Element

**Source**: [https://proceedings.mlr.press/v235/berman24a.html](https://proceedings.mlr.press/v235/berman24a.html)

**TLDR**: Proposes a method for unsupervised sequential disentanglement that extracts static information from a single sequence element.

## Abstract

One of the fundamental representation learning tasks is unsupervised sequential disentanglement, where latent codes of inputs are decomposed to a single static factor and a sequence of dynamic factors. To extract this latent information, existing methods condition the static and dynamic codes on the entire input sequence. Unfortunately, these models often suffer from information leakage, i.e., the dynamic vectors encode both static and dynamic information, or vice versa, leading to a non-disentangled representation. Attempts to alleviate this problem via reducing the dynamic dimension and auxiliary loss terms gain only partial success. Instead, we propose a novel and simple architecture that mitigates information leakage by offering a simple and effective subtraction inductive bias while conditioning on a single sample. Remarkably, the resulting variational framework is simpler in terms of required loss terms, hyper-parameters, and data augmentation. We evaluate our method on multiple data-modality benchmarks including general time series, video, and audio, and we show beyond state-of-the-art results on generation and prediction tasks in comparison to several strong baselines.