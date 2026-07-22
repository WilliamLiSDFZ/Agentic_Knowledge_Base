---
title: "Unexpected Phenomenon: LLMs’ Spurious Associations in Information Extraction"
source: "https://aclanthology.org/2024.findings-acl.545/"
pdf_url: ""
categories: ['natural-language-processing-information-extraction', 'llm-hallucination-detection-and-mitigation']
tags: ['information-extraction', 'spurious-correlations', 'relation-extraction']
venue: "ACL 2024"
tldr: "Identifies and analyzes a spurious association phenomenon in LLMs applied to information extraction tasks like relation extraction."
---

# Unexpected Phenomenon: LLMs’ Spurious Associations in Information Extraction

**Source**: [https://aclanthology.org/2024.findings-acl.545/](https://aclanthology.org/2024.findings-acl.545/)

**TLDR**: Identifies and analyzes a spurious association phenomenon in LLMs applied to information extraction tasks like relation extraction.

## Abstract

AbstractInformation extraction plays a critical role in natural language processing. When applying large language models (LLMs) to this domain, we discover an unexpected phenomenon: LLMs’ spurious associations. In tasks such as relation extraction, LLMs can accurately identify entity pairs, even if the given relation (label) is semantically unrelated to the pre-defined original one. To find these labels, we design two strategies in this study, including forward label extension and backward label validation. We also leverage the extended labels to improve model performance. Our comprehensive experiments show that spurious associations occur consistently in both Chinese and English datasets across various LLM sizes. Moreover, the use of extended labels significantly enhances LLM performance in information extraction tasks. Remarkably, there is a performance increase of 9.55%, 11.42%, and 21.27% in F1 scores on the SciERC, ACE05, and DuEE datasets, respectively.