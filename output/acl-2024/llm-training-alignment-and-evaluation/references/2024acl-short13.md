---
title: "IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus"
source: "https://aclanthology.org/2024.acl-short.13/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'llm-training-alignment-and-evaluation']
tags: ['information-extraction', 'schema-conditioned', 'instruction-data']
venue: "ACL 2024"
tldr: "IEPile is a large-scale schema-conditioned instruction corpus for improving LLM performance on information extraction tasks."
---

# IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus

**Source**: [https://aclanthology.org/2024.acl-short.13/](https://aclanthology.org/2024.acl-short.13/)

**TLDR**: IEPile is a large-scale schema-conditioned instruction corpus for improving LLM performance on information extraction tasks.

## Abstract

AbstractLarge Language Models (LLMs) demonstrate remarkable potential across various domains; however, they exhibit a significant performance gap in Information Extraction (IE). Note that high-quality instruction data is the vital key for enhancing the specific capabilities of LLMs, while current IE datasets tend to be small in scale, fragmented, and lack standardized schema. To this end, we introduce IEPile, a comprehensive bilingual (English and Chinese) IE instruction corpus, which contains approximately 0.32B tokens. We construct IEPile by collecting and cleaning 33 existing IE datasets, and introduce schema-based instruction generation to unearth a large-scale corpus. Experimentally, IEPile enhance the performance of LLMs for IE, with notable improvements in zero-shot generalization. We open-source the resource and pre-trained models, hoping to provide valuable support to the NLP community.