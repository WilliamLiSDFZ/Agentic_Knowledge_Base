---
title: "Selective Prefix Tuning for Pre-trained Language Models"
source: "https://aclanthology.org/2024.findings-acl.164/"
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['prefix-tuning', 'parameter-efficient', 'fine-tuning', 'pre-trained-LM', 'selective']
venue: "ACL 2024"
tldr: "Selective Prefix Tuning improves parameter-efficient fine-tuning by adaptively choosing which transformer layers receive learnable prefix vectors."
---

# Selective Prefix Tuning for Pre-trained Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.164/](https://aclanthology.org/2024.findings-acl.164/)

**TLDR**: Selective Prefix Tuning improves parameter-efficient fine-tuning by adaptively choosing which transformer layers receive learnable prefix vectors.

## Abstract

AbstractThe prevalent approach for optimizing pre-trained language models in downstream tasks is fine-tuning. However, it is both time-consuming and memory-inefficient. In response, a more efficient method called Prefix Tuning, which insert learnable vectors into each Transformer layers, has been proposed and proven effective. Recent investigations reveal that prefix tokens carry context-specific information, prompting the hypothesis that enhancing their specialization can improve model performance. To address this, we propose Selective Prefix Tuning (SPT), integrating a selective mechanism inspired by selective self-attention. Additionally, we introduce Selective Loss (SL) to encourage diversity in prefix tokens. Extensive experiments validate the effectiveness of SPT in sentence and token classification tasks. We contribute insight into understanding the role of prefix in model adaptation.