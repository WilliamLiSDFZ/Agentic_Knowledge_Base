---
title: "Zero-shot Cross-lingual Alignment for Embedding Initialization"
source: "https://aclanthology.org/2024.findings-acl.358/"
categories: ['language-technology-cultural-linguistic-diversity', 'language-model-representations-and-embedding-spaces']
tags: ['cross-lingual', 'embedding-initialization', "Zipf's-law", 'multilingual', 'unsupervised']
venue: "ACL 2024"
tldr: "CrossInit leverages Zipf's law for unsupervised cross-lingual embedding initialization with similar geometric structures across languages."
---

# Zero-shot Cross-lingual Alignment for Embedding Initialization

**Source**: [https://aclanthology.org/2024.findings-acl.358/](https://aclanthology.org/2024.findings-acl.358/)

**TLDR**: CrossInit leverages Zipf's law for unsupervised cross-lingual embedding initialization with similar geometric structures across languages.

## Abstract

AbstractFor multilingual training, we present CrossInit, an initialization method that initializes embeddings into similar geometrical structures across languages in an unsupervised manner. CrossInit leverages a common cognitive linguistic mechanism, Zipf’s law, which indicates that similar concepts across languages have similar word ranks or frequencies in their monolingual corpora. Instead of considering point-to-point alignments based on ranks, CrossInit considers the same span of consecutive ranks in each language as the Positive pairs for alignment, while others out of the span are used as Negative pairs. CrossInit then employs Contrastive Learning to iteratively refine randomly initialized embeddings for similar geometrical structures across languages. Our experiments on Unsupervised NMT, XNLI, and MLQA showed significant gains in low-resource and dissimilar languages after applying CrossInit.