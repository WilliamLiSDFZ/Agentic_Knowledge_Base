---
title: "ADAM: Dense Retrieval Distillation with Adaptive Dark Examples"
source: "https://aclanthology.org/2024.findings-acl.692/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'llm-based-ranking-and-recommendation']
tags: ['dense-retrieval', 'knowledge-distillation', 'hard-negatives']
venue: "ACL 2024"
tldr: "Proposes ADAM, a distillation method using adaptive dark examples to improve dual-encoder retrieval performance."
---

# ADAM: Dense Retrieval Distillation with Adaptive Dark Examples

**Source**: [https://aclanthology.org/2024.findings-acl.692/](https://aclanthology.org/2024.findings-acl.692/)

**TLDR**: Proposes ADAM, a distillation method using adaptive dark examples to improve dual-encoder retrieval performance.

## Abstract

AbstractTo improve the performance of the dual-encoder retriever, one effective approach is knowledge distillation from the cross-encoder ranker. Existing works prepare training instances by pairing each query with one positive and a batch of negatives. However, most hard negatives mined by advanced dense retrieval methods are still too trivial for the teacher to distinguish, preventing the teacher from transferring abundant dark knowledge to the student through its soft label. To alleviate this issue, we propose Adam, a knowledge distillation framework that can better transfer the dark knowledge held in the teacher with adaptive dark examples. Different from previous works that only rely on one positive and hard negatives as candidate passages, we create dark examples that all have moderate relevance to the query by strengthening negatives and masking positives in the discrete space. Furthermore, as the quality of knowledge held in different training instances varies as measured by the teacher’s confidence score, we propose a self-paced distillation strategy that adaptively concentrates on a subset of high-quality instances to conduct our dark-example-based knowledge distillation to help the student learn better. We conduct experiments on two widely-used benchmarks and verify the effectiveness of our method.