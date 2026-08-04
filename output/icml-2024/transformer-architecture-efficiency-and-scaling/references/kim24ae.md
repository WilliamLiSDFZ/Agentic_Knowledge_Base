---
title: "Polynomial-based Self-Attention for Table Representation Learning"
source: "https://proceedings.mlr.press/v235/kim24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ae/kim24ae.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'information-retrieval-and-recommendation-systems']
tags: ['tabular-data', 'self-attention', 'polynomial-features']
venue: "ICML 2024"
tldr: "Introduces polynomial-based self-attention mechanisms for improved representation learning on structured tabular data."
---

# Polynomial-based Self-Attention for Table Representation Learning

**Source**: [https://proceedings.mlr.press/v235/kim24ae.html](https://proceedings.mlr.press/v235/kim24ae.html)

**TLDR**: Introduces polynomial-based self-attention mechanisms for improved representation learning on structured tabular data.

## Abstract

Structured data, which constitutes a significant portion of existing data types, has been a long-standing research topic in the field of machine learning. Various representation learning methods for tabular data have been proposed, ranging from encoder-decoder structures to Transformers. Among these, Transformer-based methods have achieved state-of-the-art performance not only in tabular data but also in various other fields, including computer vision and natural language processing. However, recent studies have revealed that self-attention, a key component of Transformers, can lead to an oversmoothing issue. We show that Transformers for tabular data also face this problem. To tackle the problem, we suggest a novel self-attention layer for tabular data, leveraging matrix polynomials. This proposed layer serves as a replacement for the original self-attention layer, contributing to the improvement of model scalability. In our experiments with three representative table learning models equipped with our proposed layer, we illustrate that the layer effectively mitigates the oversmoothing problem and enhances the representation performance of the existing methods, outperforming the state-of-the-art table representation methods.