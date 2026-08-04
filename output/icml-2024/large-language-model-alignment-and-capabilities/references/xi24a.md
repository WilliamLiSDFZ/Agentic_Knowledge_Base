---
title: "Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/xi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xi24a/xi24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['large-language-models', 'reasoning', 'reinforcement-learning', 'reverse-curriculum', 'process-supervision']
venue: "ICML 2024"
tldr: "Proposes R³, a reverse curriculum reinforcement learning method that achieves process supervision benefits using only outcome supervision for LLM reasoning."
---

# Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/xi24a.html](https://proceedings.mlr.press/v235/xi24a.html)

**TLDR**: Proposes R³, a reverse curriculum reinforcement learning method that achieves process supervision benefits using only outcome supervision for LLM reasoning.

## Abstract

In this paper, we propose R$^3$: Learning Reasoning through Reverse Curriculum Reinforcement Learning (RL), a novel method that employs only outcome supervision to achieve the benefits of process supervision for large language models. The core challenge in applying RL to complex reasoning is to identify a sequence of actions that result in positive rewards and provide appropriate supervision for optimization. Outcome supervision provides sparse rewards for final results without identifying error locations, whereas process supervision offers step-wise rewards but requires extensive manual annotation. R$^3$ overcomes these limitations by learning from correct demonstrations. Specifically, R$^3$ progressively slides the start state of reasoning from a demonstration’s end to its beginning, facilitating easier model exploration at all stages. Thus, R$^3$ establishes a step-wise curriculum, allowing outcome supervision to offer step-level signals and precisely pinpoint errors. Using Llama2-7B, our method surpasses RL baseline on eight reasoning tasks by $4.1$ points on average. Notably, in program-based reasoning, 7B-scale models perform comparably to larger models or closed-source models with our R$^3$.