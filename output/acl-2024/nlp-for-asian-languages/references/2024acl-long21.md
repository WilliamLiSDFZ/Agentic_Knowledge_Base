---
title: "Retrieval-Augmented Multilingual Knowledge Editing"
source: "https://aclanthology.org/2024.acl-long.21/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'nlp-for-asian-languages']
tags: ['knowledge-editing', 'multilingual', 'retrieval-augmented']
venue: "ACL 2024"
tldr: "Proposes a retrieval-augmented framework for editing and updating knowledge in LLMs across multiple languages simultaneously."
---

# Retrieval-Augmented Multilingual Knowledge Editing

**Source**: [https://aclanthology.org/2024.acl-long.21/](https://aclanthology.org/2024.acl-long.21/)

**TLDR**: Proposes a retrieval-augmented framework for editing and updating knowledge in LLMs across multiple languages simultaneously.

## Abstract

AbstractKnowledge represented in Large Language Models (LLMs) is quite often incorrect and can also become obsolete over time. Updating knowledge via fine-tuning is computationally resource-hungry and not reliable, and so knowledge editing (KE) has developed as an effective and economical alternative to inject new knowledge or to fix factual errors in LLMs. Although there has been considerable interest in this area, current KE research exclusively focuses on monolingual settings, typically in English. However, what happens if the new knowledge is supplied in one language, but we would like to query an LLM in a different language? To address the problem of multilingual knowledge editing, we propose Retrieval-Augmented Multilingual Knowledge Editor (ReMaKE) to update knowledge in LLMs. ReMaKE can be used to perform model-agnostic knowledge editing in a multilingual setting. ReMaKE concatenates the new knowledge retrieved from a multilingual knowledge base with users’ prompts before querying an LLM. Our experimental results show that ReMaKE outperforms baseline knowledge editing methods by a significant margin and is scalable to real-word application scenarios. Our multilingual knowledge editing dataset (MzsRE) in 12 languages, the code, and additional project information are available at https://github.com/weixuan-wang123/ReMaKE.