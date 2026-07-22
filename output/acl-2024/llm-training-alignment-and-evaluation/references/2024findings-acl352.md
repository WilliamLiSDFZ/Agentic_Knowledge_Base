---
title: "Model Editing by Standard Fine-Tuning"
source: "https://aclanthology.org/2024.findings-acl.352/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation']
tags: ['model-editing', 'fine-tuning', 'knowledge-updating']
venue: "ACL 2024"
tldr: "Demonstrates that standard fine-tuning can be competitive with specialized model editing methods under the right conditions."
---

# Model Editing by Standard Fine-Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.352/](https://aclanthology.org/2024.findings-acl.352/)

**TLDR**: Demonstrates that standard fine-tuning can be competitive with specialized model editing methods under the right conditions.

## Abstract

AbstractStandard fine-tuning is considered not as effective as specialized methods for model editing due to its comparatively poor performance. However, it is simple, agnostic to the architectural details of the model being edited, and able to leverage advances in standard training techniques with no additional work (e.g., black-box PEFT for computational efficiency), making it an appealing choice for a model editor. In this work, we show that standard fine-tuning alone can yield competitive model editing performance with two minor modifications. First, we optimize the conditional likelihood rather than the full likelihood. Second, in addition to the typical practice of training on randomly paraphrased edit prompts to encourage generalization, we also train on random or similar unedited facts to encourage locality. Our experiments on the ZsRE and CounterFact datasets demonstrate that these simple modifications allow standard fine-tuning to match or outperform highly specialized editors in terms of edit score.