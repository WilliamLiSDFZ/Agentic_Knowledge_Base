---
title: "Character-Level Chinese Dependency Parsing via Modeling Latent Intra-Word Structure"
source: "https://aclanthology.org/2024.findings-acl.173/"
pdf_url: ""
categories: ['unsupervised-and-structured-syntactic-parsing-methods', 'nlp-for-asian-languages']
tags: ['chinese-parsing', 'dependency-parsing', 'character-level']
venue: "ACL 2024"
tldr: "A character-level Chinese dependency parser that models latent intra-word structure to avoid reliance on word segmentation."
---

# Character-Level Chinese Dependency Parsing via Modeling Latent Intra-Word Structure

**Source**: [https://aclanthology.org/2024.findings-acl.173/](https://aclanthology.org/2024.findings-acl.173/)

**TLDR**: A character-level Chinese dependency parser that models latent intra-word structure to avoid reliance on word segmentation.

## Abstract

AbstractRevealing the syntactic structure of sentences in Chinese poses significant challenges for word-level parsers due to the absence of clear word boundaries. To facilitate a transition from word-level to character-level Chinese dependency parsing, this paper proposes modeling latent internal structures within words. In this way, each word-level dependency tree is interpreted as a forest of character-level trees. A constrained Eisner algorithm is implemented to ensure the compatibility of character-level trees, guaranteeing a single root for intra-word structures and establishing inter-word dependencies between these roots. Experiments on Chinese treebanks demonstrate the superiority of our method over both the pipeline framework and previous joint models. A detailed analysis reveals that a coarse-to-fine parsing strategy empowers the model to predict more linguistically plausible intra-word structures.