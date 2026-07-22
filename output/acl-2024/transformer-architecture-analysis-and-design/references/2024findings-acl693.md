---
title: "Instruction Position Matters in Sequence Generation with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.693/"
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['instruction-tuning', 'sequence-generation', 'position-sensitivity']
venue: "ACL 2024"
tldr: "This paper demonstrates that the position of task instructions relative to input in fine-tuning sequences significantly affects LLM performance on conditional generation tasks."
---

# Instruction Position Matters in Sequence Generation with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.693/](https://aclanthology.org/2024.findings-acl.693/)

**TLDR**: This paper demonstrates that the position of task instructions relative to input in fine-tuning sequences significantly affects LLM performance on conditional generation tasks.

## Abstract

AbstractLarge language models (LLMs) are capable of performing conditional sequence generation tasks, such as translation or summarization, through instruction fine-tuning. The fine-tuning data is generally sequentially concatenated from a specific task instruction, an input sentence, and the corresponding response. Considering the locality modeled by the self-attention mechanism of LLMs, these models face the risk of instruction forgetting when generating responses for long input sentences. To mitigate this issue, we propose enhancing the instruction-following capability of LLMs by shifting the position of task instructions after the input sentences. Theoretical analysis suggests that our straightforward method can alter the model’s learning focus, thereby emphasizing the training of instruction-following capabilities. Concurrently, experimental results demonstrate that our approach consistently outperforms traditional settings across various model scales (1B / 7B / 13B) and different sequence generation tasks (translation and summarization), without any additional data or annotation costs. Notably, our method significantly improves the zero-shot performance on conditional sequence generation, e.g., up to 9.7 BLEU points on WMT zero-shot translation tasks. Further analysis reveals that our method can significantly improve the tranditional model’s instruction following ability by 1x over traditional approch.