---
title: "Soft Prompt Recovers Compressed LLMs, Transferably"
source: "https://proceedings.mlr.press/v235/xu24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24s/xu24s.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['model-compression', 'soft-prompts', 'LLM']
venue: "ICML 2024"
tldr: "Soft prompt tuning is shown to effectively recover performance of compressed LLMs in a transferable manner without extensive re-engineering."
---

# Soft Prompt Recovers Compressed LLMs, Transferably

**Source**: [https://proceedings.mlr.press/v235/xu24s.html](https://proceedings.mlr.press/v235/xu24s.html)

**TLDR**: Soft prompt tuning is shown to effectively recover performance of compressed LLMs in a transferable manner without extensive re-engineering.

## Abstract

Model compression is one of the most popular approaches to improve the accessibility of Large Language Models (LLMs) by reducing their memory footprint. However, the gaining of such efficiency benefits often simultaneously demands extensive engineering efforts and intricate designs to mitigate the performance decline. In this work, we leverage (Soft) Prompt Tuning in its most vanilla form and discover such conventionally learned soft prompts can recover the performance of compressed LLMs. More surprisingly, we observe such recovery effect to be transferable among different tasks and models (albeit natural tokenizer and dimensionality limitations), resulting in further overhead reduction and yet, subverting the common belief that learned soft prompts are task-specific. Our work is fully orthogonal and compatible with model compression frameworks such as pruning and quantization, where we enable up to $8\times$ compressed LLM (with a joint 4-bit quantization and 50% weight pruning compression) to match its uncompressed counterparts on popular benchmarks. We note that we are the first to reveal vanilla Parameter-Efficient Fine-Tuning (PEFT) techniques have the potential to be utilized under a compression recovery context, opening a new line of opportunities for model accessibility advancement while freeing our fellow researchers from the previously present engineering burdens and constraints. The code is available at https://github.com/zirui-ray-liu/compress-then-prompt.