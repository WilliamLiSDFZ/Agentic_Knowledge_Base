---
title: "Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution"
source: "https://proceedings.mlr.press/v235/fernando24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fernando24a/fernando24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['prompt-optimization', 'evolutionary-algorithms', 'llm-self-improvement']
venue: "ICML 2024"
tldr: "Promptbreeder is a self-referential system that uses LLMs to evolve and improve task prompts and mutation operators automatically."
---

# Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution

**Source**: [https://proceedings.mlr.press/v235/fernando24a.html](https://proceedings.mlr.press/v235/fernando24a.html)

**TLDR**: Promptbreeder is a self-referential system that uses LLMs to evolve and improve task prompts and mutation operators automatically.

## Abstract

Popular prompt strategies like Chain-of-Thought Prompting can dramatically improve the reasoning abilities of Large Language Models (LLMs) in various domains. However, such hand-crafted prompt-strategies are often sub-optimal. In this paper, we present Promptbreeder, a general-purpose self-referential self-improvement mechanism that evolves and adapts prompts for a given domain. Driven by an LLM, Promptbreeder mutates a population of task-prompts, evaluates them for fitness on a training set, and repeats this process over multiple generations to evolve task-prompts. Crucially, the mutation of these task-prompts is governed by mutation-prompts that the LLM generates and improves throughout evolution in a self-referential way. That is, Promptbreeder is not just improving task-prompts, but it is also improving the mutation-prompts that improve these task-prompts. Promptbreeder outperforms state-of-the-art prompt strategies such as Chain-of-Thought and Plan-and-Solve Prompting on commonly used arithmetic and commonsense reasoning benchmarks. Furthermore, Promptbreeder is able to evolve intricate task-prompts for the challenging problem of hate speech classification.