---
title: "CycleAlign: Iterative Distillation from Black-box LLM to White-box Models for Better Human Alignment"
source: "https://aclanthology.org/2024.findings-acl.869/"
categories: ['llm-training-alignment-and-evaluation', 'online-discourse-mental-health-language-analysis']
tags: ['alignment', 'distillation', 'RLHF', 'human-values', 'white-box']
venue: "ACL 2024"
tldr: "CycleAlign iteratively distills alignment knowledge from black-box LLMs to smaller white-box models for safer responses."
---

# CycleAlign: Iterative Distillation from Black-box LLM to White-box Models for Better Human Alignment

**Source**: [https://aclanthology.org/2024.findings-acl.869/](https://aclanthology.org/2024.findings-acl.869/)

**TLDR**: CycleAlign iteratively distills alignment knowledge from black-box LLMs to smaller white-box models for safer responses.

## Abstract

AbstractLanguage models trained on large-scale corpus often generate harmful responses that are harmful and contrary to human values. A prevalent approach for human alignment is reinforcement learning from human feedback (RLHF), utilizing algorithms such as proximal policy optimization (PPO). However, these methods are often characterized by complexity, instability, and substantial resource consumption. Considering that existing large language models (LLMs) like ChatGPT are already relatively well-aligned and cost-friendly, researchers propose to align the language model with human preferences from AI feedback. Nevertheless, the common practices, that unidirectionally distill the responses, are constrained by the inherent capability of LLMs. To address it, we introduce CycleAlign, a framework that distills alignment capabilities from the parameter-invisible LLMs (black-box) to the parameter-visible models (white-box) in an iterative manner. CycleAlign iteratively improves both the white-box and black-box models by integrating static and dynamic in-context learning and a belief alignment method.Empirical results illustrate that the model fine-tuned by CycleAlign remarkably exceeds existing methods, and achieves the state-of-the-art performance in alignment with human value.