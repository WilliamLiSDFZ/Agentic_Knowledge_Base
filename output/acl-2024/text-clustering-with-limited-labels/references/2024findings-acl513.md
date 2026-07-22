---
title: "VAEGPT-Sim: Improving Sentence Representation with Limited Corpus Using Gradually-Denoising VAE"
source: "https://aclanthology.org/2024.findings-acl.513/"
categories: ['text-clustering-with-limited-labels']
tags: ['sentence-embedding', 'VAE', 'limited-data']
venue: "ACL 2024"
tldr: "Introduces VAEGPT-Sim, a gradually-denoising VAE for improving sentence representations with limited domain-specific data."
---

# VAEGPT-Sim: Improving Sentence Representation with Limited Corpus Using Gradually-Denoising VAE

**Source**: [https://aclanthology.org/2024.findings-acl.513/](https://aclanthology.org/2024.findings-acl.513/)

**TLDR**: Introduces VAEGPT-Sim, a gradually-denoising VAE for improving sentence representations with limited domain-specific data.

## Abstract

AbstractText embedding requires a highly efficient method for training domain-specific models on limited data, as general models trained on large corpora lack universal applicability in highly specific fields. Therefore, we have introduced VAEGPT-Sim, an innovative model for generating synonyms that combines a denoising variational autoencoder with a target-specific discriminator to generate synonymous sentences that closely resemble human language. Even when trained with completely unsupervised settings, it maintains a harmonious balance between semantic similarity and lexical diversity, as shown by a comprehensive evaluation metric system with the highest average scores compared to other generative models. When VAEGPT-Sim is utilized as a module for contrastive learning in text representation, it delivers state-of-the-art results in small-dataset training on STS benchmarks, surpassing ConSERT by 2.8 points. This approach optimizes the effectiveness of text representation despite a limited corpus, signifying an advancement in domain-specific embedding technology.