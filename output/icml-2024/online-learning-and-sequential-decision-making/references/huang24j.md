---
title: "In-Context Decision Transformer: Reinforcement Learning via Hierarchical Chain-of-Thought"
source: "https://proceedings.mlr.press/v235/huang24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24j/huang24j.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['in-context-reinforcement-learning', 'decision-transformer', 'chain-of-thought']
venue: "ICML 2024"
tldr: "Introduces a hierarchical chain-of-thought decision transformer for in-context offline reinforcement learning on online tasks."
---

# In-Context Decision Transformer: Reinforcement Learning via Hierarchical Chain-of-Thought

**Source**: [https://proceedings.mlr.press/v235/huang24j.html](https://proceedings.mlr.press/v235/huang24j.html)

**TLDR**: Introduces a hierarchical chain-of-thought decision transformer for in-context offline reinforcement learning on online tasks.

## Abstract

In-context learning is a promising approach for offline reinforcement learning (RL) to handle online tasks, which can be achieved by providing task prompts. Recent works demonstrated that in-context RL could emerge with self-improvement in a trial-and-error manner when treating RL tasks as an across-episodic sequential prediction problem. Despite the self-improvement not requiring gradient updates, current works still suffer from high computational costs when the across-episodic sequence increases with task horizons. To this end, we propose an In-context Decision Transformer (IDT) to achieve self-improvement in a high-level trial-and-error manner. Specifically, IDT is inspired by the efficient hierarchical structure of human decision-making and thus reconstructs the sequence to consist of high-level decisions instead of low-level actions that interact with environments. As one high-level decision can guide multi-step low-level actions, IDT naturally avoids excessively long sequences and solves online tasks more efficiently. Experimental results show that IDT achieves state-of-the-art in long-horizon tasks over current in-context RL methods. In particular, the online evaluation time of our IDT is 36$\times$ times faster than baselines in the D4RL benchmark and 27$\times$ times faster in the Grid World benchmark.