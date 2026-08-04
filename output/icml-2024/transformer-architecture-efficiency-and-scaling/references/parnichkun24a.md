---
title: "State-Free Inference of State-Space Models: The *Transfer Function* Approach"
source: "https://proceedings.mlr.press/v235/parnichkun24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/parnichkun24a/parnichkun24a.pdf"
categories: ['sequence-models-for-memory-and-state', 'transformer-architecture-efficiency-and-scaling']
tags: ['state-space-models', 'transfer-function', 'sequence-parallelism', 'efficient-inference']
venue: "ICML 2024"
tldr: "Introduces a transfer-function-based state-free inference algorithm for state-space models that enables efficient parallel sequence processing without recurrent state overhead."
---

# State-Free Inference of State-Space Models: The *Transfer Function* Approach

**Source**: [https://proceedings.mlr.press/v235/parnichkun24a.html](https://proceedings.mlr.press/v235/parnichkun24a.html)

**TLDR**: Introduces a transfer-function-based state-free inference algorithm for state-space models that enables efficient parallel sequence processing without recurrent state overhead.

## Abstract

We approach designing a state-space model for deep learning applications through its dual representation, the transfer function, and uncover a highly efficient sequence parallel inference algorithm that is state-free: unlike other proposed algorithms, state-free inference does not incur any significant memory or computational cost with an increase in state size. We achieve this using properties of the proposed frequency domain transfer function parametrization, which enables direct computation of its corresponding convolutional kernel’s spectrum via a single Fast Fourier Transform. Our experimental results across multiple sequence lengths and state sizes illustrates, on average, a 35% training speed improvement over S4 layers – parametrized in time-domain – on the Long Range Arena benchmark, while delivering state-of-the-art downstream performances over other attention-free approaches. Moreover, we report improved perplexity in language modeling over a long convolutional Hyena baseline, by simply introducing our transfer function parametrization. Our code is available at https://github.com/ruke1ire/RTF.