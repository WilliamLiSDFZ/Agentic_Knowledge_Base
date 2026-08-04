---
title: "eCeLLM: Generalizing Large Language Models for E-commerce from Large-scale, High-quality Instruction Data"
source: "https://proceedings.mlr.press/v235/peng24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peng24c/peng24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'information-retrieval-and-recommendation-systems']
tags: ['e-commerce', 'large-language-models', 'instruction-tuning', 'generalization', 'out-of-domain']
venue: "ICML 2024"
tldr: "Introduces eCeLLM, a large-scale instruction-tuned LLM for generalizable e-commerce modeling across diverse tasks and cold-start scenarios."
---

# eCeLLM: Generalizing Large Language Models for E-commerce from Large-scale, High-quality Instruction Data

**Source**: [https://proceedings.mlr.press/v235/peng24c.html](https://proceedings.mlr.press/v235/peng24c.html)

**TLDR**: Introduces eCeLLM, a large-scale instruction-tuned LLM for generalizable e-commerce modeling across diverse tasks and cold-start scenarios.

## Abstract

With tremendous efforts on developing effective e-commerce models, conventional e-commerce models show limited success in generalist e-commerce modeling, and suffer from unsatisfactory performance on new users and new products – a typical out-of-domain generalization challenge. Meanwhile, large language models (LLMs) demonstrate outstanding performance in generalist modeling and out-of-domain generalizability in many fields. Toward fully unleashing their power for e-commerce, in this paper, we construct ECInstruct, the first open-sourced, large-scale, and high-quality benchmark instruction dataset for e-commerce. Leveraging ECInstruct, we develop eCeLLM, a series of e-commerce LLMs, by instruction-tuning general-purpose LLMs. Our comprehensive experiments and evaluation demonstrate that eCeLLM models substantially outperform baseline models, including the most advanced GPT-4, and the state-of-the-art task-specific models in in-domain evaluation. Moreover, eCeLLM exhibits excellent generalizability to out-of-domain settings, including unseen products and unseen instructions, highlighting its superiority as a generalist e-commerce model. Both the ECInstruct dataset and the eCeLLM models show great potential in empowering versatile and effective LLMs for e-commerce. ECInstruct and eCeLLM models are publicly accessible through this link.