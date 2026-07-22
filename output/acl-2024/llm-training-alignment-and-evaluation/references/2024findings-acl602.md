---
title: "Designing Informative Metrics for Few-Shot Example Selection"
source: "https://aclanthology.org/2024.findings-acl.602/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'educational-question-generation-and-comprehension']
tags: ['few-shot-learning', 'prompt-selection', 'example-selection', 'sequence-tagging', 'complexity']
venue: "ACL 2024"
tldr: "A complexity-based approach for selecting informative few-shot examples for sequence tagging tasks with pretrained language models."
---

# Designing Informative Metrics for Few-Shot Example Selection

**Source**: [https://aclanthology.org/2024.findings-acl.602/](https://aclanthology.org/2024.findings-acl.602/)

**TLDR**: A complexity-based approach for selecting informative few-shot examples for sequence tagging tasks with pretrained language models.

## Abstract

AbstractPretrained language models (PLMs) have shown remarkable few-shot learning capabilities when provided with properly formatted examples. However, selecting the “best” examples remains an open challenge. We propose a complexity-based prompt selection approach for sequence tagging tasks. This approach avoids the training of a dedicated model for selection of examples, and instead uses certain metrics to align the syntactico-semantic complexity of test sentences and examples. We use both sentence- and word-level metrics to match the complexity of examples to the (test) sentence being considered. Our results demonstrate that our approach extracts greater performance from PLMs: it achieves state-of-the-art performance on few-shot NER, achieving a 5% absolute improvement in F1 score on the CoNLL2003 dataset for GPT-4. We also see large gains of upto 28.85 points (F1/Acc.) in smaller models like GPT-j-6B.