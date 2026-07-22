---
title: "Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains"
source: "https://aclanthology.org/2024.acl-short.45/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation']
tags: ['machine-translation-metrics', 'domain-generalization', 'biomedical-mt']
venue: "ACL 2024"
tldr: "Fine-tuned MT evaluation metrics degrade significantly on unseen domains, demonstrated via a new MQM-annotated biomedical dataset across 11 language pairs."
---

# Fine-Tuned Machine Translation Metrics Struggle in Unseen Domains

**Source**: [https://aclanthology.org/2024.acl-short.45/](https://aclanthology.org/2024.acl-short.45/)

**TLDR**: Fine-tuned MT evaluation metrics degrade significantly on unseen domains, demonstrated via a new MQM-annotated biomedical dataset across 11 language pairs.

## Abstract

AbstractWe introduce a new, extensive multidimensional quality metrics (MQM) annotated dataset covering 11 language pairs in the biomedical domain. We use this dataset to investigate whether machine translation (MT) metrics which are fine-tuned on human-generated MT quality judgements are robust to domain shifts between training and inference. We find that fine-tuned metrics exhibit a substantial performance drop in the unseen domain scenario relative to both metrics that rely on the surface form and pre-trained metrics that are not fine-tuned on MT quality judgments.