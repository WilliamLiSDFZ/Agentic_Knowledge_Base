---
title: "Can We Continually Edit Language Models? On the Knowledge Attenuation in Sequential Model Editing"
source: "https://aclanthology.org/2024.findings-acl.323/"
pdf_url: ""
categories: ['continual-learning-for-nlp-tasks', 'llm-training-alignment-and-evaluation']
tags: ['model-editing', 'knowledge-attenuation', 'sequential-editing', 'LLM', 'continual-learning']
venue: "ACL 2024"
tldr: "Sequential model editing causes knowledge attenuation where previously updated knowledge degrades with each subsequent edit."
---

# Can We Continually Edit Language Models? On the Knowledge Attenuation in Sequential Model Editing

**Source**: [https://aclanthology.org/2024.findings-acl.323/](https://aclanthology.org/2024.findings-acl.323/)

**TLDR**: Sequential model editing causes knowledge attenuation where previously updated knowledge degrades with each subsequent edit.

## Abstract

AbstractModel editing has become a promising method for precisely and effectively updating knowledge in language models. In this paper, we investigate knowledge attenuation, in which the retention of updated knowledge within the language model decreases as the number of edits increases after sequential editing. Through empirical study, we discovered that existing editing methods generally suffer from knowledge attenuation. We attribute this phenomenon to two aspects: (1) redundant parameters interference and (2) update weight disentanglement. To this end, we propose the AdaPLE method. It not only mitigates the knowledge attenuation issue but also improves the performance on existing benchmarks. To the best of our knowledge, we are the first to investigate the cause and mitigation of knowledge attenuation in sequential LLM editing.