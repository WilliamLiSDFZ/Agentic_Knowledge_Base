---
title: "LinkTransformer: A Unified Package for Record Linkage with Transformer Language Models"
source: "https://aclanthology.org/2024.acl-demos.21/"
pdf_url: ""
categories: ['string-to-string-alignment-algorithms-library\n\nwait,-let-me-reconsider-for-conciseness-(3-7-words):\n\n`string-similarity-and-alignment-algorithms', 'natural-language-processing-information-extraction']
tags: ['record-linkage', 'transformer', 'string-matching']
venue: "ACL 2024"
tldr: "LinkTransformer is a unified package leveraging transformer language models for record linkage across noisy text datasets."
---

# LinkTransformer: A Unified Package for Record Linkage with Transformer Language Models

**Source**: [https://aclanthology.org/2024.acl-demos.21/](https://aclanthology.org/2024.acl-demos.21/)

**TLDR**: LinkTransformer is a unified package leveraging transformer language models for record linkage across noisy text datasets.

## Abstract

AbstractMany computational analyses require linking information across noisy text datasets. While large language models (LLMs) offer significant promise, approximate string matching packages in popular statistical softwares such as R and Stata remain predominant in academic applications. These packages have simple interfaces and can be easily extended to a diversity of languages and settings, and for academic applications, ease-of-use and extensibility are essential. In contrast, packages for record linkage with LLMs require significant familiarity with deep learning frameworks and often focus on specialized applications of commercial value in English. The open-source package LinkTransformer aims to bridge this gap by providing an end-to-end software for performing record linkage and other data cleaning tasks with transformer LLMs, treating linkage as a text retrieval problem. At its core is an off-the-shelf toolkit for applying transformer models to record linkage. LinkTransformer contains a rich repository of pre-trained models for multiple languages and supports easy integration of any transformer language model from Hugging Face or OpenAI, providing the extensibility required for many scholarly applications. Its APIs also perform common data processing tasks, e.g., aggregation, noisy de-duplication, and translation-free cross-lingual linkage. LinkTransformer contains comprehensive tools for efficient model tuning, allowing for highly customized applications, and users can easily contribute their custom-trained models to its model hub to ensure reproducibility. Using a novel benchmark dataset geared towards academic applications, we show that LinkTransformer - with both custom models and Hugging Face or OpenAI models off-the-shelf - outperforms string matching by a wide margin. By combining transformer LMs with intuitive APIs, LinkTransformer aims to democratize these performance gains for those who lack familiarity with deep learning frameworks.