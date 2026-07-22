---
title: "Benchmarking and Improving Long-Text Translation with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.428/"
categories: ['llm-training-alignment-and-evaluation', 'speech-and-language-multimodal-generation-systems']
tags: ['machine-translation', 'long-text', 'LLM-benchmark']
venue: "ACL 2024"
tldr: "A benchmark is introduced to evaluate and improve LLM performance on long-document machine translation tasks."
---

# Benchmarking and Improving Long-Text Translation with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.428/](https://aclanthology.org/2024.findings-acl.428/)

**TLDR**: A benchmark is introduced to evaluate and improve LLM performance on long-document machine translation tasks.

## Abstract

AbstractRecent studies have illuminated the promising capabilities of large language models (LLMs) in handling long texts. However, their performance in machine translation (MT) of long documents remains underexplored. This paper aims to shed light on how LLMs navigate this complex task, offering a comprehensive evaluation of their capabilities and limitations in long-text MT. First, we collect and construct an instruction-based benchmark dataset, specifically designed for the finetuning and evaluation of LLMs, encompassing multilingual, multi-domain, and document-level parallel data. Second, we conduct a comprehensive comparison between MT and LLM models concerning document-level translation. Our analysis uncovers that LLMs exhibit shortcomings in long-text domains, and their performance diminishes as document size escalates. By exploiting various extrapolation strategies, we enhance the capacity of LLMs to translate longer texts. We release data, code, and models at https://github.com/longyuewangdcu/Document-MT-LLM.