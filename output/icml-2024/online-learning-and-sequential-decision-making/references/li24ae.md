---
title: "Q-Probe: A Lightweight Approach to Reward Maximization for Language Models"
source: "https://proceedings.mlr.press/v235/li24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ae/li24ae.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['language-model', 'reward-maximization', 'Q-learning', 'finetuning', 'alignment']
venue: "ICML 2024"
tldr: "Q-probing is a lightweight method to adapt pre-trained language models to maximize task-specific rewards without full finetuning."
---

# Q-Probe: A Lightweight Approach to Reward Maximization for Language Models

**Source**: [https://proceedings.mlr.press/v235/li24ae.html](https://proceedings.mlr.press/v235/li24ae.html)

**TLDR**: Q-probing is a lightweight method to adapt pre-trained language models to maximize task-specific rewards without full finetuning.

## Abstract

We present an approach called Q-probing to adapt a pre-trained language model to maximize a task-specific reward function. At a high level, Q-probing sits between heavier approaches such as finetuning and lighter approaches such as few shot prompting, but can also be combined with either. The idea is to learn a simple linear function on a model’s embedding space that can be used to reweight candidate completions. We theoretically show that this sampling procedure is equivalent to a KL-constrained maximization of the Q-probe as the number of samples increases. To train the Q-probes we consider either reward modeling or a class of novel direct policy learning objectives based on importance-weighted policy gradients. With this technique, we see gains in domains with ground-truth rewards (code generation) as well as implicit rewards defined by preference data, even outperforming finetuning in data-limited regimes. Moreover, a Q-probe can be trained on top of an API since it only assumes access to sampling and embeddings. Code: https://github.com/likenneth/q_probe.