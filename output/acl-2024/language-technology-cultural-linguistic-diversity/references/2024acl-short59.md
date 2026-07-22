---
title: "Zero-Shot Cross-Lingual Reranking with Large Language Models for Low-Resource Languages"
source: "https://aclanthology.org/2024.acl-short.59/"
pdf_url: ""
categories: ['llm-based-ranking-and-recommendation', 'language-technology-cultural-linguistic-diversity']
tags: ['cross-lingual', 'reranking', 'low-resource-languages']
venue: "ACL 2024"
tldr: "A study on zero-shot cross-lingual passage reranking with LLMs targeting low-resource languages to address gaps in multilingual retrieval."
---

# Zero-Shot Cross-Lingual Reranking with Large Language Models for Low-Resource Languages

**Source**: [https://aclanthology.org/2024.acl-short.59/](https://aclanthology.org/2024.acl-short.59/)

**TLDR**: A study on zero-shot cross-lingual passage reranking with LLMs targeting low-resource languages to address gaps in multilingual retrieval.

## Abstract

AbstractLarge language models (LLMs) as listwise rerankers have shown impressive zero-shot capabilities in various passage ranking tasks. Despite their success, there is still a gap in existing literature on their effectiveness in reranking low-resource languages. To address this, we investigate how LLMs function as listwise rerankers in cross-lingual information retrieval (CLIR) systems with queries in English and passages in four African languages: Hausa, Somali, Swahili, and Yoruba. We analyze and compare the effectiveness of monolingual reranking using either query or document translations. We also evaluate the effectiveness of LLMs when leveraging their own generated translations. To grasp the general picture, we examine the effectiveness of multiple LLMs — the proprietary models RankGPT-4 and RankGPT-3.5, along with the open-source model RankZephyr. While the document translation setting, i.e., both queries and documents are in English, leads to the best reranking effectiveness, our results indicate that for specific LLMs, reranking in the African language setting achieves competitive effectiveness with the cross-lingual setting, and even performs better when using the LLM’s own translations.