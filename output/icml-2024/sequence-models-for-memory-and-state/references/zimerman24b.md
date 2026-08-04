---
title: "Viewing Transformers Through the Lens of Long Convolutions Layers"
source: "https://proceedings.mlr.press/v235/zimerman24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zimerman24b/zimerman24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['transformers', 'long-range-modeling', 'convolutions', 'sequence-modeling', 'attention']
venue: "ICML 2024"
tldr: "This paper analyzes transformers through the lens of long convolution layers, revealing design insights for improving long-range task performance."
---

# Viewing Transformers Through the Lens of Long Convolutions Layers

**Source**: [https://proceedings.mlr.press/v235/zimerman24b.html](https://proceedings.mlr.press/v235/zimerman24b.html)

**TLDR**: This paper analyzes transformers through the lens of long convolution layers, revealing design insights for improving long-range task performance.

## Abstract

Despite their dominance in modern DL and, especially, NLP domains, transformer architectures exhibit sub-optimal performance on long-range tasks compared to recent layers that are specifically designed for this purpose. In this work, drawing inspiration from key attributes of longrange layers, such as state-space layers, linear RNN layers, and global convolution layers, we demonstrate that minimal modifications to the transformer architecture can significantly enhance performance on the Long Range Arena (LRA) benchmark, thus narrowing the gap with these specialized layers. We identify that two key principles for long-range tasks are (i) incorporating an inductive bias towards smoothness, and (ii) locality. As we show, integrating these ideas into the attention mechanism improves results with a negligible amount of additional computation and without any additional trainable parameters. Our theory and experiments also shed light on the reasons for the inferior performance of transformers on long-range tasks and identify critical properties that are essential for successfully capturing long-range dependencies.