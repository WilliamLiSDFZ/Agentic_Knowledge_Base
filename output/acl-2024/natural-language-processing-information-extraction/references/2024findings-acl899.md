---
title: "LMDX: Language Model-based Document Information Extraction and Localization"
source: "https://aclanthology.org/2024.findings-acl.899/"
pdf_url: ""
categories: ['document-understanding-and-information-extraction', 'natural-language-processing-information-extraction']
tags: ['document-information-extraction', 'LLMs', 'visually-rich-documents', 'localization', 'structured-extraction']
venue: "ACL 2024"
tldr: "LMDX applies LLMs to extract and localize information from visually rich documents, addressing a core challenge in document understanding."
---

# LMDX: Language Model-based Document Information Extraction and Localization

**Source**: [https://aclanthology.org/2024.findings-acl.899/](https://aclanthology.org/2024.findings-acl.899/)

**TLDR**: LMDX applies LLMs to extract and localize information from visually rich documents, addressing a core challenge in document understanding.

## Abstract

AbstractLarge Language Models (LLM) have revolutionized Natural Language Processing (NLP), improving state-of-the-art and exhibiting emergent capabilities across various tasks. However, their application in extracting information from visually rich documents, which is at the core of many document processing workflows and involving the extraction of key entities from semi-structured documents, has not yet been successful. The main obstacles to adopting LLMs for this task include the absence of layout encoding within LLMs, which is critical for high quality extraction, and the lack of a grounding mechanism to localize the predicted entities within the document. In this paper, we introduce Language Model-based Document Information EXtraction and Localization (LMDX), a methodology to reframe the document information extraction task for a LLM. LMDX enables extraction of singular, repeated, and hierarchical entities, both with and without training data, while providing grounding guarantees and localizing the entities within the document. Finally, we apply LMDX to the PaLM 2-S and Gemini Pro LLMs and evaluate it on VRDU and CORD benchmarks, setting a new state-of-the-art and showing how LMDX enables the creation of high quality, data-efficient parsers.