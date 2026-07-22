---
title: "Teacher-Student Training for Debiasing: General Permutation Debiasing for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.81/"
pdf_url: ""
categories: ['bias-and-fairness-in-llms', 'llm-training-alignment-and-evaluation']
tags: ['debiasing', 'permutation-sensitivity', 'LLM', 'teacher-student', 'fairness']
venue: "ACL 2024"
tldr: "Proposes a teacher-student training framework to reduce permutation sensitivity bias in large language models across NLP tasks."
---

# Teacher-Student Training for Debiasing: General Permutation Debiasing for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.81/](https://aclanthology.org/2024.findings-acl.81/)

**TLDR**: Proposes a teacher-student training framework to reduce permutation sensitivity bias in large language models across NLP tasks.

## Abstract

AbstractLarge Language Models (LLMs) have demonstrated impressive zero-shot capabilities and versatility in NLP tasks, however they sometimes fail to maintain crucial invariances for specific tasks. One example is permutation sensitivity, where LLMs’ outputs may significantly vary depending on the order of the input options. While debiasing techniques can mitigate these issues, and yield better performance and reliability, they often come with a high computational cost at inference. This paper addresses this inefficiency at inference time. The aim is to distill the capabilities of a computationally intensive, debiased, teacher model into a more compact student model. We explore two variants of student models: one based on pure distillation, and the other on an error-correction approach for more complex tasks, where the student corrects a single biased decision from the teacher to achieve a debiased output. Our approach is general and can be applied to both black-box and white-box LLMs. Furthermore, we demonstrate that our compact, encoder-only student models can outperform their larger, biased teacher counterparts, achieving better results with significantly fewer parameters.