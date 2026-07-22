---
title: "InstructEd: Soft-Instruction Tuning for Model Editing with Hops"
source: "https://aclanthology.org/2024.findings-acl.888/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation']
tags: ['model-editing', 'soft-instruction', 'multi-hop']
venue: "ACL 2024"
tldr: "Proposes InstructEd, a soft-instruction tuning approach for multi-hop model editing that reduces over-memorization in LLMs."
---

# InstructEd: Soft-Instruction Tuning for Model Editing with Hops

**Source**: [https://aclanthology.org/2024.findings-acl.888/](https://aclanthology.org/2024.findings-acl.888/)

**TLDR**: Proposes InstructEd, a soft-instruction tuning approach for multi-hop model editing that reduces over-memorization in LLMs.

## Abstract

AbstractThe task of model editing becomes popular for correcting inaccurate or outdated parametric knowledge in Large Language Models (LLMs). However, there are major limitations of state of the art (SOTA) model editing methods, including the excessive memorization issue caused by the direct editing methods, as well as the error propagation and knowledge conflict issues from the memory enhancement methods, resulting in hindering models’ *portability*, e.g., the ability to transfer the new knowledge to related one-hop or multi-hop content. To address these issues, we propose the InstructEd method, the idea of which is to insert soft instructions into the attention module so as to facilitate interactions between instructions and questions and to understand and utilize new facts. Our main findings are: (i) InstructEd has achieved SOTA performance on three datasets for one-hop/multi-hop evaluation with LLaMAs and GPT2, achieving 10% (5%) improvement in one-hop (multi-hop) model editing.(ii) Different from earlier methods on editing parameters in FFN, we show that editing attention can also help. (iii) Model editing is highly related to retrieval augmented methods, which can help improve the locality of model editing while slightly decrease the editing performance with hops.