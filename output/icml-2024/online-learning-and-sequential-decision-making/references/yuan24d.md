---
title: "Self-Rewarding Language Models"
source: "https://proceedings.mlr.press/v235/yuan24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yuan24d/yuan24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['self-rewarding', 'llm-alignment', 'iterative-training', 'preference-learning']
venue: "ICML 2024"
tldr: "Self-Rewarding Language Models iteratively improve by using the model itself to generate and evaluate its own training signal."
---

# Self-Rewarding Language Models

**Source**: [https://proceedings.mlr.press/v235/yuan24d.html](https://proceedings.mlr.press/v235/yuan24d.html)

**TLDR**: Self-Rewarding Language Models iteratively improve by using the model itself to generate and evaluate its own training signal.

## Abstract

We posit that to achieve superhuman agents, future models require superhuman feedback in order to provide an adequate training signal. Current approaches commonly train reward models from human preferences, which may then be bottlenecked by human performance level, and secondly these reward models require additional human preferences data to further improve.In this work, we study Self-Rewarding Language Models, where the language model itself is used via LLM-as-a-Judge prompting to provide its own rewards during training. We show that during Iterative DPO training, not only does instruction following ability improve, but also the ability to provide high-quality rewards to itself. Fine-tuning Llama 2 70B on three iterations of our approach yields a model that outperforms many existing systems on the AlpacaEval 2.0 leaderboard, including Claude 2, Gemini Pro, and GPT-4 0613. While there is much left still to explore, this work opens the door to the possibility of models that can continually improve in both axes.