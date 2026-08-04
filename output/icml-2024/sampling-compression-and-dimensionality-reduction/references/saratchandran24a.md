---
title: "A sampling theory perspective on activations for implicit neural representations"
source: "https://proceedings.mlr.press/v235/saratchandran24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/saratchandran24a/saratchandran24a.pdf"
categories: ['continual-learning-memory-plasticity', 'sampling-compression-and-dimensionality-reduction']
tags: ['implicit-neural-representations', 'sampling-theory', 'activation-functions', 'Fourier-features', 'signal-encoding']
venue: "ICML 2024"
tldr: "A sampling theory perspective is used to analyze and motivate activation function choices in implicit neural representations for capturing high-frequency signals."
---

# A sampling theory perspective on activations for implicit neural representations

**Source**: [https://proceedings.mlr.press/v235/saratchandran24a.html](https://proceedings.mlr.press/v235/saratchandran24a.html)

**TLDR**: A sampling theory perspective is used to analyze and motivate activation function choices in implicit neural representations for capturing high-frequency signals.

## Abstract

Implicit Neural Representations (INRs) have gained popularity for encoding signals as compact, differentiable entities. While commonly using techniques like Fourier positional encodings or non-traditional activation functions (e.g., Gaussian, sinusoid, or wavelets) to capture high-frequency content, their properties lack exploration within a unified theoretical framework. Addressing this gap, we conduct a comprehensive analysis of these activations from a sampling theory perspective. Our investigation reveals that, especially in shallow INRs, $\mathrm{sinc}$ activations—previously unused in conjunction with INRs—are theoretically optimal for signal encoding. Additionally, we establish a connection between dynamical systems and INRs, leveraging sampling theory to bridge these two paradigms.