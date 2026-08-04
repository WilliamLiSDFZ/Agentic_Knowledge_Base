---
title: "Agent Instructs Large Language Models to be General Zero-Shot Reasoners"
source: "https://proceedings.mlr.press/v235/crispino24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/crispino24a/crispino24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['llm-reasoning', 'zero-shot', 'autonomous-agent']
venue: "ICML 2024"
tldr: "Introduces an agent-based method that instructs LLMs to improve zero-shot reasoning on general language understanding tasks."
---

# Agent Instructs Large Language Models to be General Zero-Shot Reasoners

**Source**: [https://proceedings.mlr.press/v235/crispino24a.html](https://proceedings.mlr.press/v235/crispino24a.html)

**TLDR**: Introduces an agent-based method that instructs LLMs to improve zero-shot reasoning on general language understanding tasks.

## Abstract

We introduce a method to improve the zero-shot reasoning abilities of large language models on general language understanding tasks. Specifically, we build an autonomous agent to instruct the reasoning process of large language models. To enable this, our agent only needs to generate a single set of instructions for each task. These instructions turn out to be extremely effective for improving the reasoning process of different large language models across all task instances. We show this approach further unleashes the zero-shot reasoning abilities of large language models to more tasks. We study the performance of our method on a wide set of datasets spanning generation, classification, and reasoning. We show that our method generalizes to most tasks and obtains state-of-the-art zero-shot performance on 20 of the 29 datasets that we evaluate. For instance, our method boosts the performance of state-of-the-art large language models by a large margin, including Vicuna-13b, Llama-2-70b-chat, and GPT-3.5 Turbo. Compared to zero-shot chain of thought, our improvement in reasoning is striking. With our method, Llama-2-70b-chat outperforms zero-shot GPT-3.5 Turbo significantly.