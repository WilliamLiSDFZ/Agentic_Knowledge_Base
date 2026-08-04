---
title: "One Prompt is not Enough: Automated Construction of a Mixture-of-Expert Prompts"
source: "https://proceedings.mlr.press/v235/wang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24b/wang24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['prompt-optimization', 'mixture-of-experts', 'LLM', 'automated-prompt-design', 'in-context-learning']
venue: "ICML 2024"
tldr: "Automated construction of mixture-of-expert prompts improves LLM generalization by combining diverse specialized prompts for complex tasks."
---

# One Prompt is not Enough: Automated Construction of a Mixture-of-Expert Prompts

**Source**: [https://proceedings.mlr.press/v235/wang24b.html](https://proceedings.mlr.press/v235/wang24b.html)

**TLDR**: Automated construction of mixture-of-expert prompts improves LLM generalization by combining diverse specialized prompts for complex tasks.

## Abstract

Large Language Models (LLMs) exhibit strong generalization capabilities to novel tasks when prompted with language instructions and in-context demos. Since this ability sensitively depends on the quality of prompts, various methods have been explored to automate the instruction design. While these methods demonstrated promising results, they also restricted the searched prompt to one instruction. Such simplification significantly limits their capacity, as a single demo-free instruction might not be able to cover the entire complex problem space of the targeted task. To alleviate this issue, we adopt the Mixture-of-Expert paradigm and divide the problem space into a set of sub-regions; Each sub-region is governed by a specialized expert, equipped with both an instruction and a set of demos. A two-phase process is developed to construct the specialized expert for each region: (1) demo assignment: Inspired by the theoretical connection between in-context learning and kernel regression, we group demos into experts based on their semantic similarity; (2) instruction assignment: A region-based joint search of an instruction per expert complements the demos assigned to it, yielding a synergistic effect. The resulting method, codenamed Mixture-of-Prompts (MoP), achieves an average win rate of 81% against prior arts across several major benchmarks.