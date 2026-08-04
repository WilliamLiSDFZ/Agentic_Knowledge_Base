---
title: "On Prompt-Driven Safeguarding for Large Language Models"
source: "https://proceedings.mlr.press/v235/zheng24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24n/zheng24n.pdf"
categories: ['llm-geometry-and-interpretability-research']
tags: ['LLM-safety', 'safety-prompts', 'mechanistic-interpretability', 'prompt-optimization']
venue: "ICML 2024"
tldr: "This paper investigates the working mechanisms of safety prompts in LLMs and uses these insights to enable automatic optimization of safeguarding prompts."
---

# On Prompt-Driven Safeguarding for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/zheng24n.html](https://proceedings.mlr.press/v235/zheng24n.html)

**TLDR**: This paper investigates the working mechanisms of safety prompts in LLMs and uses these insights to enable automatic optimization of safeguarding prompts.

## Abstract

Prepending model inputs with safety prompts is a common practice for safeguarding large language models (LLMs) against queries with harmful intents. However, the underlying working mechanisms of safety prompts have not been unraveled yet, restricting the possibility of automatically optimizing them to improve LLM safety. In this work, we investigate how LLMs’ behavior (i.e., complying with or refusing user queries) is affected by safety prompts from the perspective of model representation. We find that in the representation space, the input queries are typically moved by safety prompts in a "higher-refusal" direction, in which models become more prone to refusing to provide assistance, even when the queries are harmless. On the other hand, LLMs are naturally capable of distinguishing harmful and harmless queries without safety prompts. Inspired by these findings, we propose a method for safety prompt optimization, namely DRO (Directed Representation Optimization). Treating a safety prompt as continuous, trainable embeddings, DRO learns to move the queries’ representations along or opposite the refusal direction, depending on their harmfulness. Experiments with eight LLMs on out-of-domain and jailbreak benchmarks demonstrate that DRO remarkably improves the safeguarding performance of human-crafted safety prompts, without compromising the models’ general performance.