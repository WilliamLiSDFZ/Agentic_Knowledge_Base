---
title: "Keypoint-based Progressive Chain-of-Thought Distillation for LLMs"
source: "https://proceedings.mlr.press/v235/feng24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24e/feng24e.pdf"
categories: ['knowledge-distillation-methods-and-applications']
tags: ['chain-of-thought', 'knowledge-distillation', 'LLM-reasoning']
venue: "ICML 2024"
tldr: "Introduces keypoint-based progressive chain-of-thought distillation to efficiently transfer reasoning abilities from LLMs to smaller models."
---

# Keypoint-based Progressive Chain-of-Thought Distillation for LLMs

**Source**: [https://proceedings.mlr.press/v235/feng24e.html](https://proceedings.mlr.press/v235/feng24e.html)

**TLDR**: Introduces keypoint-based progressive chain-of-thought distillation to efficiently transfer reasoning abilities from LLMs to smaller models.

## Abstract

Chain-of-thought distillation is a powerful technique for transferring reasoning abilities from large language models (LLMs) to smaller student models. Previous methods typically require the student to mimic the step-by-step rationale produced by LLMs, often facing the following challenges: (i) Tokens within a rationale vary in significance, and treating them equally may fail to accurately mimic keypoint tokens, leading to reasoning errors. (ii) They usually distill knowledge by consistently predicting all the steps in a rationale, which falls short in distinguishing the learning order of step generation. This diverges from the human cognitive progression of starting with easy tasks and advancing to harder ones, resulting in sub-optimal outcomes. To this end, we propose a unified framework, called KPOD, to address these issues. Specifically, we propose a token weighting module utilizing mask learning to encourage accurate mimicry of keypoint tokens by the student during distillation. Besides, we develop an in-rationale progressive distillation strategy, starting with training the student to generate the final reasoning steps and gradually extending to cover the entire rationale. To accomplish this, a weighted token generation loss is proposed to assess step reasoning difficulty, and a value function is devised to schedule the progressive distillation by considering both step difficulty and question diversity. Extensive experiments on four reasoning benchmarks illustrate our KPOD outperforms previous methods by a large margin.