---
title: "Flextron: Many-in-One Flexible Large Language Model"
source: "https://proceedings.mlr.press/v235/cai24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24e/cai24e.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['LLM', 'flexible-inference', 'elastic-networks', 'multi-in-one', 'deployment']
venue: "ICML 2024"
tldr: "Flextron is a flexible LLM architecture supporting many deployment configurations from a single training run to handle diverse compute and memory constraints."
---

# Flextron: Many-in-One Flexible Large Language Model

**Source**: [https://proceedings.mlr.press/v235/cai24e.html](https://proceedings.mlr.press/v235/cai24e.html)

**TLDR**: Flextron is a flexible LLM architecture supporting many deployment configurations from a single training run to handle diverse compute and memory constraints.

## Abstract

Training modern LLMs is extremely resource intensive, and customizing them for various deployment scenarios characterized by limited compute and memory resources through repeated training is impractical. In this paper, we introduce Flextron, a network architecture and post-training model optimization framework supporting flexible model deployment. The Flextron architecture utilizes a nested elastic structure to rapidly adapt to specific user-defined latency and accuracy targets during inference with no additional fine-tuning required. It is also input-adaptive, and can automatically route tokens through its sub-networks for improved performance and efficiency. We present a sample-efficient training method and associated routing algorithms for systematically transforming an existing trained LLM into a Flextron model. We evaluate Flextron on the GPT-3 and LLama-2 family of LLMs, and demonstrate superior performance over multiple end-to-end trained variants and other state-of-the-art elastic networks, all with a single pretraining run that consumes a mere 7.63% tokens compared to original pretraining.