---
title: "USTAD: Unified Single-model Training Achieving Diverse Scores for Information Retrieval"
source: "https://proceedings.mlr.press/v235/kim24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ad/kim24ad.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'transformer-architecture-efficiency-and-scaling']
tags: ['information-retrieval', 'unified-model', 'transformer']
venue: "ICML 2024"
tldr: "Proposes a single unified transformer model that achieves diverse scoring capabilities across multiple information retrieval stages."
---

# USTAD: Unified Single-model Training Achieving Diverse Scores for Information Retrieval

**Source**: [https://proceedings.mlr.press/v235/kim24ad.html](https://proceedings.mlr.press/v235/kim24ad.html)

**TLDR**: Proposes a single unified transformer model that achieves diverse scoring capabilities across multiple information retrieval stages.

## Abstract

Modern information retrieval (IR) systems consists of multiple stages like retrieval and ranking, with Transformer-based models achieving state-of-the-art performance at each stage. In this paper, we challenge the tradition of using separate models for different stages and ask if a single Transformer encoder can provide relevance score needed in each stage. We present USTAD – a new unified approach to train a single network that can provide powerful ranking scores as a cross-encoder (CE) model as well as factorized embeddings for large-scale retrieval as a dual-encoder (DE) model. Empirically, we find a single USTAD model to be competitive to separate ranking CE and retrieval DE models. Furthermore, USTAD combines well with a novel embedding matching-based distillation, significantly improving CE to DE distillation. It further motivates novel asymmetric architectures for student models to ensure a better embedding alignment between the student and the teacher while ensuring small online inference cost. On standard benchmarks like MSMARCO, we demonstrate that USTAD with our proposed distillation method leads to asymmetric students with only 1/10th trainable parameter but retaining 95-97% of the teacher performance.