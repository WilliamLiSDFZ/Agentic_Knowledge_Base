---
title: "Analysis of Multi-Source Language Training in Cross-Lingual Transfer"
source: "https://aclanthology.org/2024.acl-long.42/"
pdf_url: ""
categories: ['language-technology-cultural-linguistic-diversity', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['cross-lingual-transfer', 'multilingual', 'low-resource', 'language-models', 'multi-source-training']
venue: "ACL 2024"
tldr: "Analyzes how training on multiple source languages affects cross-lingual transfer performance in multilingual language models."
---

# Analysis of Multi-Source Language Training in Cross-Lingual Transfer

**Source**: [https://aclanthology.org/2024.acl-long.42/](https://aclanthology.org/2024.acl-long.42/)

**TLDR**: Analyzes how training on multiple source languages affects cross-lingual transfer performance in multilingual language models.

## Abstract

AbstractThe successful adaptation of multilingual language models (LMs) to a specific language-task pair critically depends on the availability of data tailored for that condition. While cross-lingual transfer (XLT) methods have contributed to addressing this data scarcity problem, there still exists ongoing debate about the mechanisms behind their effectiveness.In this work, we focus on one of promising assumptions about inner workings of XLT, that it encourages multilingual LMs to place greater emphasis on language-agnostic or task-specific features. We test this hypothesis by examining how the patterns of XLT change with a varying number of source languages involved in the process.Our experimental findings show that the use of multiple source languages in XLT-a technique we term Multi-Source Language Training (MSLT)-leads to increased mingling of embedding spaces for different languages, supporting the claim that XLT benefits from making use of language-independent information. On the other hand, we discover that using an arbitrary combination of source languages does not always guarantee better performance. We suggest simple heuristics for identifying effective language combinations for MSLT and empirically prove its effectiveness.