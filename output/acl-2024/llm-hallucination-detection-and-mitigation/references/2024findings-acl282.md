---
title: "MrRank: Improving Question Answering Retrieval System through Multi-Result Ranking Model"
source: "https://aclanthology.org/2024.findings-acl.282/"
categories: ['llm-based-ranking-and-recommendation', 'llm-hallucination-detection-and-mitigation']
tags: ['question-answering', 'retrieval-augmentation', 'multi-result-ranking']
venue: "ACL 2024"
tldr: "Proposes MrRank, a multi-result ranking model to improve retrieval-augmented QA systems and reduce LLM hallucinations."
---

# MrRank: Improving Question Answering Retrieval System through Multi-Result Ranking Model

**Source**: [https://aclanthology.org/2024.findings-acl.282/](https://aclanthology.org/2024.findings-acl.282/)

**TLDR**: Proposes MrRank, a multi-result ranking model to improve retrieval-augmented QA systems and reduce LLM hallucinations.

## Abstract

AbstractLarge Language Models (LLMs) often struggle with hallucinations and outdated information. To address this, Information Retrieval (IR) systems can be employed to augment LLMs with up-to-date knowledge. However, existing IR techniques contain deficiencies, posing a performance bottleneck. Given the extensive array of IR systems, combining diverse approaches presents a viable strategy. Nevertheless, prior attempts have yielded restricted efficacy. In this work, we propose an approach that leverages learning-to-rank techniques to combine heterogeneous IR systems. We demonstrate the method on two Retrieval Question Answering (ReQA) tasks. Our empirical findings exhibit a significant performance enhancement, outperforming previous approaches and achieving state-of-the-art results on ReQA SQuAD.