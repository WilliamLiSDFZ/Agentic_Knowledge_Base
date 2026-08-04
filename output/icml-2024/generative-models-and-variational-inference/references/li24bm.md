---
title: "VQDNA: Unleashing the Power of Vector Quantization for Multi-Species Genomic Sequence Modeling"
source: "https://proceedings.mlr.press/v235/li24bm.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bm/li24bm.pdf"
categories: ['algebraic-structures-in-machine-learning', 'generative-models-and-variational-inference']
tags: ['genomic-language-models', 'vector-quantization', 'tokenization']
venue: "ICML 2024"
tldr: "Proposes VQDNA, a vector quantization-based tokenization framework to improve multi-species genomic sequence modeling."
---

# VQDNA: Unleashing the Power of Vector Quantization for Multi-Species Genomic Sequence Modeling

**Source**: [https://proceedings.mlr.press/v235/li24bm.html](https://proceedings.mlr.press/v235/li24bm.html)

**TLDR**: Proposes VQDNA, a vector quantization-based tokenization framework to improve multi-species genomic sequence modeling.

## Abstract

Similar to natural language models, pre-trained genome language models are proposed to capture the underlying intricacies within genomes with unsupervised sequence modeling. They have become essential tools for researchers and practitioners in biology. However, the hand-crafted tokenization policies used in these models may not encode the most discriminative patterns from the limited vocabulary of genomic data. In this paper, we introduce VQDNA, a general-purpose framework that renovates genome tokenization from the perspective of genome vocabulary learning. By leveraging vector-quantized codebook as learnable vocabulary, VQDNA can adaptively tokenize genomes into pattern-aware embeddings in an end-to-end manner. To further push its limits, we propose Hierarchical Residual Quantization (HRQ), where varying scales of codebooks are designed in a hierarchy to enrich the genome vocabulary in a coarse-to-fine manner. Extensive experiments on 32 genome datasets demonstrate VQDNA’s superiority and favorable parameter efficiency compared to existing genome language models. Notably, empirical analysis of SARS-CoV-2 mutations reveals the fine-grained pattern awareness and biological significance of learned HRQ vocabulary, highlighting its untapped potential for broader applications in genomics.