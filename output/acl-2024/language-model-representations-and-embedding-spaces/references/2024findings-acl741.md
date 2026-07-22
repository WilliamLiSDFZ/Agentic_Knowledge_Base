---
title: "Enhancing Idiomatic Representation in Multiple Languages via an Adaptive Contrastive Triplet Loss"
source: "https://aclanthology.org/2024.findings-acl.741/"
categories: ['language-model-representations-and-embedding-spaces', 'language-technology-cultural-linguistic-diversity']
tags: ['idiom-representation', 'contrastive-learning', 'multilingual']
venue: "ACL 2024"
tldr: "Proposes an adaptive contrastive triplet loss to improve idiomatic expression representation across multiple languages."
---

# Enhancing Idiomatic Representation in Multiple Languages via an Adaptive Contrastive Triplet Loss

**Source**: [https://aclanthology.org/2024.findings-acl.741/](https://aclanthology.org/2024.findings-acl.741/)

**TLDR**: Proposes an adaptive contrastive triplet loss to improve idiomatic expression representation across multiple languages.

## Abstract

AbstractAccurately modeling idiomatic or non-compositional language has been a longstanding challenge in Natural Language Processing (NLP). This is partly because these expressions do not derive their meanings solely from their constituent words, but also due to the scarcity of relevant data resources, and their impact on the performance of downstream tasks such as machine translation and simplification. In this paper we propose an approach to model idiomaticity effectively using a triplet loss that incorporates the asymmetric contribution of components words to an idiomatic meaning for training language models by using adaptive contrastive learning and resampling miners to build an idiomatic-aware learning objective. Our proposed method is evaluated on a SemEval challenge and outperforms previous alternatives significantly in many metrics.