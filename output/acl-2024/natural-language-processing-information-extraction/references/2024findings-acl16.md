---
title: "P-TA: Using Proximal Policy Optimization to Enhance Tabular Data Augmentation via Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.16/"
categories: ['llm-training-alignment-and-evaluation', 'natural-language-processing-information-extraction']
tags: ['tabular-data', 'augmentation', 'reinforcement-learning']
venue: "ACL 2024"
tldr: "Uses proximal policy optimization with LLMs to enhance the quality and diversity of augmented tabular data for downstream tasks."
---

# P-TA: Using Proximal Policy Optimization to Enhance Tabular Data Augmentation via Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.16/](https://aclanthology.org/2024.findings-acl.16/)

**TLDR**: Uses proximal policy optimization with LLMs to enhance the quality and diversity of augmented tabular data for downstream tasks.

## Abstract

AbstractA multitude of industries depend on accurate and reasonable tabular data augmentation for their business processes. Contemporary methodologies in generating tabular data revolve around utilizing Generative Adversarial Networks (GAN) or fine-tuning Large Language Models (LLM). However, GAN-based approaches are documented to produce samples with common-sense errors attributed to the absence of external knowledge. On the other hand, LLM-based methods exhibit a limited capacity to capture the disparities between synthesized and actual data distribution due to the absence of feedback from a discriminator during training. Furthermore, the decoding of LLM-based generation introduces gradient breakpoints, impeding the backpropagation of loss from a discriminator, thereby complicating the integration of these two approaches. To solve this challenge, we propose using proximal policy optimization (PPO) to apply GANs, guiding LLMs to enhance the probability distribution of tabular features. This approach enables the utilization of LLMs as generators for GANs in synthesizing tabular data. Our experiments demonstrate that PPO leads to an approximately 4% improvement in the accuracy of models trained on synthetically generated data over state-of-the-art across three real-world datasets.