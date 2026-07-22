---
title: "RECOST: External Knowledge Guided Data-efficient Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.648/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'label-noise-robust-annotation-learning']
tags: ['instruction-tuning', 'data-selection', 'external-knowledge']
venue: "ACL 2024"
tldr: "RECOST uses external knowledge to guide data-efficient instruction tuning by selecting high-quality training samples for LLMs."
---

# RECOST: External Knowledge Guided Data-efficient Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.648/](https://aclanthology.org/2024.findings-acl.648/)

**TLDR**: RECOST uses external knowledge to guide data-efficient instruction tuning by selecting high-quality training samples for LLMs.

## Abstract

AbstractIn the current landscape of large language models (LLMs), the process of instruction tuning serves as an essential step. Considering the high computing power overhead, data-efficient instruction tuning was proposed to reduce the training data size in this process, aiming at selecting high-quality instructional data. Nevertheless, we argue that most current data-efficient instruction-tuning methods are highly dependent on the quality of the original instruction-tuning dataset. When it comes to datasets synthesized by LLMs, a common scenario in this field, dirty samples will even be selected with a higher probability than other samples. To address these challenges, we utilized external knowledge (relevant examples or paragraphs) to evaluate those samples synthesized by LLMs with an in-context-based relative predictive entropy. Based on the new metric, we proposed a framework, dubbed as RECOST, which integrates external-knowledge-base re-ranking and diversity-consistent sampling into a single pipeline. Through extensive experiments on several synthetic datasets (Alpaca and Alpaca-gpt4), we demonstrate the effectiveness of our method and achieve even better results with only 1% of the full dataset.