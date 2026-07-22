---
title: "Unveiling the Power of Integration: Block Diagram Summarization through Local-Global Fusion"
source: "https://aclanthology.org/2024.findings-acl.822/"
pdf_url: ""
categories: ['document-understanding-and-information-extraction', 'multimodal-language-vision-learning-systems']
tags: ['block-diagram', 'summarization', 'local-global-fusion']
venue: "ACL 2024"
tldr: "Proposes a local-global fusion approach for summarizing block diagrams to support document understanding and question answering."
---

# Unveiling the Power of Integration: Block Diagram Summarization through Local-Global Fusion

**Source**: [https://aclanthology.org/2024.findings-acl.822/](https://aclanthology.org/2024.findings-acl.822/)

**TLDR**: Proposes a local-global fusion approach for summarizing block diagrams to support document understanding and question answering.

## Abstract

AbstractBlock Diagrams play an essential role in visualizing the relationships between components or systems. Generating summaries of block diagrams is important for document understanding or question answering (QA) tasks by providing concise overviews of complex systems. However, it’s a challenging task as it requires compressing complex relationships into informative descriptions. In this paper, we present “BlockNet”, a fusion framework that summarizes block diagrams by integrating local and global information, catering to both English and Korean languages. Additionally, we introduce a new multilingual method to produce block diagram data, resulting in a high-quality dataset called “BD-EnKo”. In BlockNet, we develop “BlockSplit”, an Optical Character Recognition (OCR) based algorithm employing the divide-and-conquer principle for local information extraction. We train an OCR-free transformer architecture for global information extraction using BD-EnKo and public data. To assess the effectiveness of our model, we conduct thorough experiments on different datasets. The assessment shows that BlockNet surpasses all previous methods and models, including GPT-4V, for block diagram summarization.