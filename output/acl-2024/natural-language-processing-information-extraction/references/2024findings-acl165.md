---
title: "MODABS: Multi-Objective Learning for Dynamic Aspect-Based Summarization"
source: "https://aclanthology.org/2024.findings-acl.165/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'causal-reasoning-and-explanation-in-nlp']
tags: ['summarization', 'aspect-based', 'multi-objective', 'dynamic-aspects', 'NLP']
venue: "ACL 2024"
tldr: "MODABS uses multi-objective learning to handle dynamic aspect-based summarization where aspects vary across input texts."
---

# MODABS: Multi-Objective Learning for Dynamic Aspect-Based Summarization

**Source**: [https://aclanthology.org/2024.findings-acl.165/](https://aclanthology.org/2024.findings-acl.165/)

**TLDR**: MODABS uses multi-objective learning to handle dynamic aspect-based summarization where aspects vary across input texts.

## Abstract

AbstractThe rapid proliferation of online content necessitates effective summarization methods, among which dynamic aspect-based summarization stands out. Unlike its traditional counterpart, which assumes a fixed set of known aspects, this approach adapts to the varied aspects of the input text. We introduce a novel multi-objective learning framework employing a Longformer-Encoder-Decoder for this task. The framework optimizes aspect number prediction, minimizes disparity between generated and reference summaries for each aspect, and maximizes dissimilarity across aspect-specific summaries. Extensive experiments show our method significantly outperforms baselines on three diverse datasets, largely due to the effective alignment of generated and reference aspect counts without sacrificing single-aspect summarization quality.