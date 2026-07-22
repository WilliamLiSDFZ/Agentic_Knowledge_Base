---
title: "Sparsity-Accelerated Training for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.875/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization', 'llm-training-alignment-and-evaluation']
tags: ['sparsity', 'llm-training', 'efficient-fine-tuning']
venue: "ACL 2024"
tldr: "Proposes sparsity-accelerated training to reduce computational costs of continual pre-training and fine-tuning of large language models."
---

# Sparsity-Accelerated Training for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.875/](https://aclanthology.org/2024.findings-acl.875/)

**TLDR**: Proposes sparsity-accelerated training to reduce computational costs of continual pre-training and fine-tuning of large language models.

## Abstract

AbstractLarge language models (LLMs) have demonstrated proficiency across various natural language processing (NLP) tasks but often require additional training, such as continual pre-training and supervised fine-tuning. However, the costs associated with this, primarily due to their large parameter count, remain high. This paper proposes leveraging sparsity in pre-trained LLMs to expedite this training process. By observing sparsity in activated neurons during forward iterations, we identify the potential for computational speed-ups by excluding inactive neurons. We address associated challenges by extending existing neuron importance evaluation metrics and introducing a ladder omission rate scheduler. Our experiments on Llama-2 demonstrate that Sparsity-Accelerated Training (SAT) achieves comparable or superior performance to standard training while significantly accelerating the process. Specifically, SAT achieves a 45% throughput improvement in continual pre-training and saves 38% training time in supervised fine-tuning. It offers a simple, hardware-agnostic, and easily deployable framework for additional LLM training.