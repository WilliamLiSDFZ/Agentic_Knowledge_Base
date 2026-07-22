---
title: "From Discrimination to Generation: Low-Resource Intent Detection with Language Model Instruction Tuning"
source: "https://aclanthology.org/2024.findings-acl.605/"
categories: ['language-model-human-cognitive-linguistic-alignment', 'nlp-text-classification-applied-tasks']
tags: ['intent-detection', 'low-resource', 'instruction-tuning']
venue: "ACL 2024"
tldr: "Proposes a generative instruction-tuning approach to enable LLMs to detect new intents in low-resource settings."
---

# From Discrimination to Generation: Low-Resource Intent Detection with Language Model Instruction Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.605/](https://aclanthology.org/2024.findings-acl.605/)

**TLDR**: Proposes a generative instruction-tuning approach to enable LLMs to detect new intents in low-resource settings.

## Abstract

AbstractIntent detection aims to identify user goals from utterances, and is a ubiquitous step towards the satisfaction of user desired needs in many interaction systems. As dynamic and varied intents arise, models that are capable of identifying new intents promptly are required. However, existing studies usually fine-tune discriminative models on the specific defined intent classes, precluding them from being directly adopted to new intent domains. In this paper, we introduce a generative pre-trained intent model that can recognize new intents from different domains in low-resource scenarios. We reformulate intent detection into a generation task and design descriptive and regularized instructions to guide the model effectively to detect new intents in open domains with no parameter updates. To validate the proposed method, we introduce a new intent detection benchmark, including the Meta-Intent Dataset and three types of representative evaluation settings. We conduct extensive experiments which demonstrate that our method outperforms a range of strong baselines that needs further fine-tuning or domain-specific samples.