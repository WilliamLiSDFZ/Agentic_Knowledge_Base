---
title: "Speculative Contrastive Decoding"
source: "https://aclanthology.org/2024.acl-short.5/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization', 'minimum-bayes-risk-decoding-efficiency']
tags: ['speculative-decoding', 'contrastive-decoding', 'inference-efficiency', 'LLM', 'exposure-bias']
venue: "ACL 2024"
tldr: "Speculative Contrastive Decoding combines speculative and contrastive decoding to improve LLM inference speed and output quality."
---

# Speculative Contrastive Decoding

**Source**: [https://aclanthology.org/2024.acl-short.5/](https://aclanthology.org/2024.acl-short.5/)

**TLDR**: Speculative Contrastive Decoding combines speculative and contrastive decoding to improve LLM inference speed and output quality.

## Abstract

AbstractLarge language models (LLMs) exhibit exceptional performance in language tasks, yet their auto-regressive inference is limited due to high computational requirements and is sub-optimal due to the exposure bias. Inspired by speculative decoding and contrastive decoding, we introduce Speculative Contrastive Decoding (SCD), a straightforward yet powerful decoding approach that leverages predictions from smaller language models (LMs) to achieve both decoding acceleration and quality improvement. Extensive evaluations and analyses on four diverse language tasks demonstrate the effectiveness of SCD, showing that decoding efficiency and quality can compatibly benefit from one smaller LM.