---
title: "Implicit Representations via Operator Learning"
source: "https://proceedings.mlr.press/v235/pal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pal24a/pal24a.pdf"
categories: ['neural-operators-for-pde-solving']
tags: ['implicit-neural-representations', 'operator-learning', 'signal-compression', 'downstream-tasks']
venue: "ICML 2024"
tldr: "Proposes an operator learning framework for implicit neural representations enabling efficient downstream processing."
---

# Implicit Representations via Operator Learning

**Source**: [https://proceedings.mlr.press/v235/pal24a.html](https://proceedings.mlr.press/v235/pal24a.html)

**TLDR**: Proposes an operator learning framework for implicit neural representations enabling efficient downstream processing.

## Abstract

The idea of representing a signal as the weights of a neural network, called Implicit Neural Representations (INRs), has led to exciting implications for compression, view synthesis and 3D volumetric data understanding. One problem in this setting pertains to the use of INRs for downstream processing tasks. Despite some conceptual results, this remains challenging because the INR for a given image/signal often exists in isolation. What does the neighborhood around a given INR correspond to? Based on this question, we offer an operator theoretic reformulation of the INR model, which we call Operator INR (or O-INR). At a high level, instead of mapping positional encodings to a signal, O-INR maps one function space to another function space. A practical form of this general casting is obtained by appealing to Integral Transforms. The resultant model does not need multi-layer perceptrons (MLPs), used in most existing INR models – we show that convolutions are sufficient and offer benefits including numerically stable behavior. We show that O-INR can easily handle most problem settings in the literature, and offers a similar performance profile as baselines. These benefits come with minimal, if any, compromise. Our code is available at https://github.com/vsingh-group/oinr.