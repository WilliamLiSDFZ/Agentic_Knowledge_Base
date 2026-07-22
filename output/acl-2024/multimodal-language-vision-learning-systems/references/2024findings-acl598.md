---
title: "An Empirical Study on Parameter-Efficient Fine-Tuning for MultiModal Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.598/"
categories: ['multimodal-language-vision-learning-systems']
tags: ['parameter-efficient-fine-tuning', 'multimodal-llm', 'instruction-tuning']
venue: "ACL 2024"
tldr: "Empirically studies parameter-efficient fine-tuning strategies for multimodal large language models across diverse tasks."
---

# An Empirical Study on Parameter-Efficient Fine-Tuning for MultiModal Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.598/](https://aclanthology.org/2024.findings-acl.598/)

**TLDR**: Empirically studies parameter-efficient fine-tuning strategies for multimodal large language models across diverse tasks.

## Abstract

AbstractMultimodal Large Language Models (MLLMs) fine-tuned with multimodal instruction-following data have demonstrated formidable capabilities in multimodal tasks. However, fine-tuning all parameters of MLLMs has become challenging due to the rapid growth of the overall model’s parameters. To address this issue, we study Parameter-Efficient Fine-Tuning (PEFT) methods for MLLMs. We aim to identify effective methods for enhancing performance in scenarios where only a limited number of parameters are trained. This paper conducts empirical studies that employ four widely used PEFT methods to fine-tune the LLM component of open-source MLLMs. We present a comprehensive analysis that encompasses various aspects, including the impact of PEFT methods on various models, parameters and location of PEFT module, fine-tuning data scale, model stability based on PEFT method, MLLM’s generalization, and hallucination. We evaluated four PEFT methods on seven datasets from two different categories, unseen and seen datasets. Across all experiments, we show that the adapter is the best-performing PEFT method in various aspects. At the same time, fine-tuning the connector layers leads to improved performance in most MLLMs.