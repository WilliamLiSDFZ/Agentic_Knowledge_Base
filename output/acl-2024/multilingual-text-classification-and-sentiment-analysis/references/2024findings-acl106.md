---
title: "Cyclical Contrastive Learning Based on Geodesic for Zero-shot Cross-lingual Spoken Language Understanding"
source: "https://aclanthology.org/2024.findings-acl.106/"
pdf_url: ""
categories: ['multilingual-text-classification-and-sentiment-analysis', 'language-technology-cultural-linguistic-diversity']
tags: ['zero-shot', 'cross-lingual', 'spoken-language-understanding', 'contrastive-learning', 'geodesic']
venue: "ACL 2024"
tldr: "This paper proposes cyclical contrastive learning based on geodesic distances for zero-shot cross-lingual spoken language understanding in low-resource languages."
---

# Cyclical Contrastive Learning Based on Geodesic for Zero-shot Cross-lingual Spoken Language Understanding

**Source**: [https://aclanthology.org/2024.findings-acl.106/](https://aclanthology.org/2024.findings-acl.106/)

**TLDR**: This paper proposes cyclical contrastive learning based on geodesic distances for zero-shot cross-lingual spoken language understanding in low-resource languages.

## Abstract

AbstractOwing to the scarcity of labeled training data, Spoken Language Understanding (SLU) is still a challenging task in low-resource languages. Therefore, zero-shot cross-lingual SLU attracts more and more attention. Contrastive learning is widely applied to explicitly align representations of similar sentences across different languages. However, the vanilla contrastive learning method may face two problems in zero-shot cross-lingual SLU: (1) the consistency between different languages is neglected; (2) each utterance has two different kinds of SLU labels, i.e. slot and intent, the utterances with one different label are also pushed away without any discrimination, which limits the performance. In this paper, we propose Cyclical Contrastive Learning based on Geodesic (CCLG), which introduces cyclical contrastive learning to achieve the consistency between different languages and leverages geodesic to measure the similarity to construct the positive pairs and negative pairs. Experimental results demonstrate that our proposed framework achieves the new state-of-the-art performance on MultiATIS++ and MTOP datasets, and the model analysis further verifies that CCLG can effectively transfer knowledge between different languages.