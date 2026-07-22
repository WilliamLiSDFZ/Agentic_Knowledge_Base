---
title: "DocFinQA: A Long-Context Financial Reasoning Dataset"
source: "https://aclanthology.org/2024.acl-short.42/"
categories: ['financial-reasoning-llm-benchmarks-and-datasets', 'llm-training-alignment-and-evaluation']
tags: ['financial-reasoning', 'long-context', 'document-qa']
venue: "ACL 2024"
tldr: "Introduces DocFinQA, a long-context financial reasoning dataset requiring LLMs to process multi-page financial documents for realistic QA tasks."
---

# DocFinQA: A Long-Context Financial Reasoning Dataset

**Source**: [https://aclanthology.org/2024.acl-short.42/](https://aclanthology.org/2024.acl-short.42/)

**TLDR**: Introduces DocFinQA, a long-context financial reasoning dataset requiring LLMs to process multi-page financial documents for realistic QA tasks.

## Abstract

AbstractFor large language models (LLMs) to be effective in the financial domain – where each decision can have a significant impact – it is necessary to investigate realistic tasks and data. Financial professionals often interact with documents spanning hundreds of pages, but most financial research datasets only deal with short excerpts from these documents. To address this, we introduce a long-document financial QA task. We augment 7,437 questions from the existing FinQA dataset with full-document context, extending the average context length from under 700 words in FinQA to 123k words in DocFinQA. We conduct extensive experiments over retrieval-based QA pipelines and long-context language models. Based on our experiments, DocFinQA proves a significant challenge for even state-of-the-art systems. We also provide a case study on a subset of the longest documents in DocFinQA and find that models particularly struggle with these documents. Addressing these challenges may have a wide-reaching impact across applications where specificity and long-range contexts are critical, like gene sequences and legal document contract analysis. DocFinQA dataset is publicly accessible.