---
title: "ConTempo: A Unified Temporally Contrastive Framework for Temporal Relation Extraction"
source: "https://aclanthology.org/2024.findings-acl.89/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp', 'natural-language-processing-information-extraction']
tags: ['temporal-relation-extraction', 'contrastive-learning', 'event-understanding']
venue: "ACL 2024"
tldr: "A contrastive framework for temporal relation extraction that models relations jointly rather than independently."
---

# ConTempo: A Unified Temporally Contrastive Framework for Temporal Relation Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.89/](https://aclanthology.org/2024.findings-acl.89/)

**TLDR**: A contrastive framework for temporal relation extraction that models relations jointly rather than independently.

## Abstract

AbstractThe task of temporal relation extraction (TRE) involves identifying and extracting temporal relations between events from narratives. We identify two primary issues with TRE systems. First, by formulating TRE as a simple text classification task where every temporal relation is independent, it is hard to enhance the TRE model’s representation of meaning of temporal relations, and its facility with the underlying temporal calculus. We solve the issue by proposing a novel Temporally Contrastive learning model (ConTempo) that increase the model’s awareness of the meaning of temporal relations by leveraging their symmetric or antisymmetric properties. Second, the reusability of innovations has been limited due to incompatibilities in model architectures. Therefore, we propose a unified framework and show that ConTempo is compatible with all three main branches of TRE research. Our results demonstrate that the performance gains of ConTempo are more pronounced, with the total combination achieving state-of-the-art performance on the widely used MATRES and TBD corpora. We furthermore identified and corrected a large number of annotation errors present in the test set of MATRES, after which the performance increase brought by ConTempo becomes more apparent.