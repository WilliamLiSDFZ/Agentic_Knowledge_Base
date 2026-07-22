---
title: "LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation"
source: "https://aclanthology.org/2024.findings-acl.419/"
categories: ['language-technology-cultural-linguistic-diversity', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['cross-lingual-transfer', 'entity-augmentation', 'language-adaptation']
venue: "ACL 2024"
tldr: "LEIA facilitates cross-lingual knowledge transfer in LLMs using entity-based data augmentation from Wikipedia."
---

# LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.419/](https://aclanthology.org/2024.findings-acl.419/)

**TLDR**: LEIA facilitates cross-lingual knowledge transfer in LLMs using entity-based data augmentation from Wikipedia.

## Abstract

AbstractAdapting English-based large language models (LLMs) to other languages has become increasingly popular due to the efficiency and potential of cross-lingual transfer. However, existing language adaptation methods often overlook the benefits of cross-lingual supervision. In this study, we introduce LEIA, a language adaptation tuning method that utilizes Wikipedia entity names aligned across languages. This method involves augmenting the target language corpus with English entity names and training the model using left-to-right language modeling. We assess LEIA on diverse question answering datasets using 7B-parameter LLMs, demonstrating significant performance gains across various non-English languages.