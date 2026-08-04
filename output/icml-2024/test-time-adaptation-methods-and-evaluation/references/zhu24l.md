---
title: "Model Tailor: Mitigating Catastrophic Forgetting in Multi-modal Large Language Models"
source: "https://proceedings.mlr.press/v235/zhu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24l/zhu24l.pdf"
categories: ['continual-learning-memory-plasticity', 'test-time-adaptation-methods-and-evaluation']
tags: ['catastrophic-forgetting', 'multimodal-LLMs', 'fine-tuning', 'continual-learning', 'model-patching']
venue: "ICML 2024"
tldr: "This paper analyzes catastrophic forgetting in multimodal large language models and proposes Model Tailor to mitigate it during fine-tuning."
---

# Model Tailor: Mitigating Catastrophic Forgetting in Multi-modal Large Language Models

**Source**: [https://proceedings.mlr.press/v235/zhu24l.html](https://proceedings.mlr.press/v235/zhu24l.html)

**TLDR**: This paper analyzes catastrophic forgetting in multimodal large language models and proposes Model Tailor to mitigate it during fine-tuning.

## Abstract

Catastrophic forgetting emerges as a critical challenge when fine-tuning multi-modal large language models (MLLMs), where improving performance on unseen tasks often leads to a significant performance drop on the original tasks. This paper presents a comprehensive analysis of catastrophic forgetting in MLLMs and introduces a post-training adjustment method called Model Tailor. Our method primarily preserves the pre-trained parameters while replacing a small number ($\leq$ 10%) of fine-tuned parameters, maintaining $\sim$ 99% effectiveness on original tasks versus pre-training, and achieving $\sim$ 97% on new tasks compared to standard fine-tuning. Specifically, we derive a sparse mask to identify the model patch, based on a fusion strategy that integrates salience and sensitivity analysis. Subsequently, a compensation mechanism is introduced to decorate the patch, enhancing the model’s performance on both target and original tasks. Additionally, our method is adaptable to multi-task scenarios. Through extensive experiments on InstructBLIP and LLaVA-1.5 in both image captioning and visual question answering tasks, our approach demonstrates significant task adaptability while preserving inherent pre-trained capabilities.