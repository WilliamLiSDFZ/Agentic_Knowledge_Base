---
title: "Semantic Compression for Word and Sentence Embeddings using Discrete Wavelet Transform"
source: "https://aclanthology.org/2024.findings-acl.945/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'continuous-discrete-representation-tradeoffs']
tags: ['wavelet-transform', 'embedding-compression', 'discrete-wavelet']
venue: "ACL 2024"
tldr: "Discrete Wavelet Transform is applied to compress word and sentence embeddings while preserving semantic information."
---

# Semantic Compression for Word and Sentence Embeddings using Discrete Wavelet Transform

**Source**: [https://aclanthology.org/2024.findings-acl.945/](https://aclanthology.org/2024.findings-acl.945/)

**TLDR**: Discrete Wavelet Transform is applied to compress word and sentence embeddings while preserving semantic information.

## Abstract

AbstractWavelet transforms, a powerful mathematical tool, have been widely used in different domains, including Signal and Image processing, to unravel intricate patterns, enhance data representation, and extract meaningful features from data. Tangible results from their application suggest that Wavelet transforms can be applied to NLP capturing a variety of linguistic and semantic properties.In this paper, we empirically leverage the application of Discrete Wavelet Transforms (DWT) to word and sentence embeddings. We aim to showcase the capabilities of DWT in analyzing embedding representations at different levels of resolution and compressing them while maintaining their overall quality.We assess the effectiveness of DWT embeddings on semantic similarity tasks to show how DWT can be used to consolidate important semantic information in an embedding vector. We show the efficacy of the proposed paradigm using different embedding models, including large language models, on downstream tasks. Our results show that DWT can reduce the dimensionality of embeddings by 50-93% with almost no change in performance for semantic similarity tasks, while achieving superior accuracy in most downstream tasks. Our findings pave the way for applying DWT to improve NLP applications.