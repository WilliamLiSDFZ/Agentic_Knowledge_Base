---
title: "Multi-Modal Retrieval For Large Language Model Based Speech Recognition"
source: "https://aclanthology.org/2024.findings-acl.262/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems']
tags: ['multi-modal-retrieval', 'speech-recognition', 'llm']
venue: "ACL 2024"
tldr: "Extends retrieval-augmented language modeling to multi-modal settings for improving large language model based speech recognition."
---

# Multi-Modal Retrieval For Large Language Model Based Speech Recognition

**Source**: [https://aclanthology.org/2024.findings-acl.262/](https://aclanthology.org/2024.findings-acl.262/)

**TLDR**: Extends retrieval-augmented language modeling to multi-modal settings for improving large language model based speech recognition.

## Abstract

AbstractRetrieval is a widely adopted approach for improving language models leveraging external information. As the field moves towards multi-modal large language models, it is important to extend the pure text based methods to incorporate other modalities in retrieval as well for applications across the wide spectrum of machine learning tasks and data types. In this work, we propose multi-modal retrieval with two approaches: kNN-LM and cross-attention techniques. We demonstrate the effectiveness of our retrieval approaches empirically by applying them to automatic speech recognition tasks with access to external information. Under this setting, we show that speech-based multi-modal retrieval outperforms text based retrieval, and yields up to improvement in word error rate over the multi-modal language model baseline. Furthermore, we achieve state-of-the-art recognition results on the Spoken-Squad question answering dataset.