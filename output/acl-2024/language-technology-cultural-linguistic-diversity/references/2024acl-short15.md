---
title: "Code-Switching Can be Better Aligners: Advancing Cross-Lingual SLU through Representation-Level and Prediction-Level Alignment"
source: "https://aclanthology.org/2024.acl-short.15/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity']
tags: ['code-switching', 'cross-lingual', 'spoken-language-understanding']
venue: "ACL 2024"
tldr: "Advances zero-shot cross-lingual spoken language understanding via representation-level and prediction-level alignment using code-switching."
---

# Code-Switching Can be Better Aligners: Advancing Cross-Lingual SLU through Representation-Level and Prediction-Level Alignment

**Source**: [https://aclanthology.org/2024.acl-short.15/](https://aclanthology.org/2024.acl-short.15/)

**TLDR**: Advances zero-shot cross-lingual spoken language understanding via representation-level and prediction-level alignment using code-switching.

## Abstract

AbstractZero-shot cross-lingual spoken language understanding (SLU) can promote the globalization application of dialog systems, which has attracted increasing attention. While current code-switching based cross-lingual SLU frameworks have shown promising results, they (i) predominantly utilize contrastive objectives to model hard alignment, which may disrupt the inherent structure within sentences of each language; and (ii) focus optimization objectives solely on the original sentences, neglecting the relation between original sentences and code-switched sentences, which may hinder contextualized embeddings from further alignment. In this paper, we propose a novel framework dubbed REPE (short for Representation-Level and Prediction-Level Alignment), which leverages both code-switched and original sentences to achieve multi-level alignment. Specifically, REPE introduces optimal transport to facilitate soft alignment between the representations of code-switched and original sentences, thereby preserving structural integrity as much as possible. Moreover, REPE adopts multi-view learning to enforce consistency regularization between the prediction of the two sentences, aligning them into a more refined language-invariant space. Based on this, we further incorporate a self-distillation layer to boost the robustness of REPE. Extensive experiments on two benchmarks across ten languages demonstrate the superiority of the proposed REPE framework.