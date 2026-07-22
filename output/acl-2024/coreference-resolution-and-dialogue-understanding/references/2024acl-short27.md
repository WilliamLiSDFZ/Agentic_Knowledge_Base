---
title: "Generating Harder Cross-document Event Coreference Resolution Datasets using Metaphoric Paraphrasing"
source: "https://aclanthology.org/2024.acl-short.27/"
pdf_url: ""
categories: ['coreference-resolution-and-dialogue-understanding']
tags: ['coreference-resolution', 'metaphoric-paraphrasing', 'dataset-generation']
venue: "ACL 2024"
tldr: "Uses metaphoric paraphrasing to create harder cross-document event coreference resolution datasets with greater lexical diversity."
---

# Generating Harder Cross-document Event Coreference Resolution Datasets using Metaphoric Paraphrasing

**Source**: [https://aclanthology.org/2024.acl-short.27/](https://aclanthology.org/2024.acl-short.27/)

**TLDR**: Uses metaphoric paraphrasing to create harder cross-document event coreference resolution datasets with greater lexical diversity.

## Abstract

AbstractThe most popular Cross-Document Event Coreference Resolution (CDEC) datasets fail to convey the true difficulty of the task, due to the lack of lexical diversity between coreferring event triggers (words or phrases that refer to an event). Furthermore, there is a dearth of event datasets for figurative language, limiting a crucial avenue of research in event comprehension. We address these two issues by introducing ECB+META, a lexically rich variant of Event Coref Bank Plus (ECB+) for CDEC on symbolic and metaphoric language. We use ChatGPT as a tool for the metaphoric transformation of sentences in the documents of ECB+, then tag the original event triggers in the transformed sentences in a semi-automated manner. In this way, we avoid the re-annotation of expensive coreference links. We present results that show existing methods that work well on ECB+ struggle with ECB+META, thereby paving the way for CDEC research on a much more challenging dataset. Code/data: https://github.com/ahmeshaf/llms_coref