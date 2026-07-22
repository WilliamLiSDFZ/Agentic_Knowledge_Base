---
title: "WilKE: Wise-Layer Knowledge Editor for Lifelong Knowledge Editing"
source: "https://aclanthology.org/2024.findings-acl.207/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-hallucination-detection-and-mitigation']
tags: ['knowledge-editing', 'lifelong-editing', 'layer-selection']
venue: "ACL 2024"
tldr: "Proposes WilKE, a wise-layer knowledge editor that identifies optimal editing layers to enable effective lifelong knowledge editing in LLMs."
---

# WilKE: Wise-Layer Knowledge Editor for Lifelong Knowledge Editing

**Source**: [https://aclanthology.org/2024.findings-acl.207/](https://aclanthology.org/2024.findings-acl.207/)

**TLDR**: Proposes WilKE, a wise-layer knowledge editor that identifies optimal editing layers to enable effective lifelong knowledge editing in LLMs.

## Abstract

AbstractKnowledge editing aims to rectify inaccuracies in large language models (LLMs) without costly retraining for outdated or erroneous knowledge. However, current knowledge editing methods primarily focus on single editing, failing to meet the requirements for lifelong editing. This study reveals a performance degradation encountered by knowledge editing in lifelong editing, characterized by toxicity buildup and toxicity flash, with the primary cause identified as pattern unmatch. We introduce a knowledge editing approach named Wise-Layer Knowledge Editor (WilKE), which selects editing layer based on the pattern matching degree of editing knowledge across different layers in language models. Experimental results demonstrate that, in lifelong editing, WilKE exhibits an average improvement of 46.2% and 67.8% on editing GPT2-XL and GPT-J relative to state-of-the-art knowledge editing methods.