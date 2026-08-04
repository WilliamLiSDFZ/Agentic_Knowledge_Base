---
title: "Towards Modular LLMs by Building and Reusing a Library of LoRAs"
source: "https://proceedings.mlr.press/v235/ostapenko24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ostapenko24a/ostapenko24a.pdf"
categories: ['large-language-model-alignment-and-capabilities']
tags: ['LoRA', 'parameter-efficient-finetuning', 'adapter-reuse', 'multi-task-learning', 'LLM']
venue: "ICML 2024"
tldr: "Develops techniques to build and reuse a library of LoRA adapters across tasks for improved modular LLM performance."
---

# Towards Modular LLMs by Building and Reusing a Library of LoRAs

**Source**: [https://proceedings.mlr.press/v235/ostapenko24a.html](https://proceedings.mlr.press/v235/ostapenko24a.html)

**TLDR**: Develops techniques to build and reuse a library of LoRA adapters across tasks for improved modular LLM performance.

## Abstract

Given the increasing number of parameter-efficient adapters of large language models (LLMs), how can we reuse them to improve LLM performance on new tasks? We study how to best build a library of adapters given multi-task data and devise techniques for both zero-shot and supervised task generalization through routing in such library. We benchmark existing approaches to build this library and introduce model-based clustering, $\texttt{MBC}$, a method that groups tasks based on the similarity of their adapter parameters, indirectly optimizing for transfer across the multi-task dataset. In order to reuse the library, we present a novel zero-shot routing mechanism, $\texttt{Arrow}$, which enables dynamic selection of the most relevant adapters for new inputs without the need for retraining. We experiment with several LLMs, such as Phi-2 and Mistral, on a wide array of held-out tasks, verifying that MBC-based adapters and Arrow routing lead to superior generalization to new tasks. Thus, we make steps towards creating modular, adaptable LLMs that can match or outperform traditional joint training.