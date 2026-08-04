---
title: "Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers"
source: "https://proceedings.mlr.press/v235/lin24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24r/lin24r.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['instruction-optimization', 'neural-bandits', 'LLMs']
venue: "ICML 2024"
tldr: "A neural bandit coupled with transformers approach for automated instruction optimization of large language models."
---

# Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers

**Source**: [https://proceedings.mlr.press/v235/lin24r.html](https://proceedings.mlr.press/v235/lin24r.html)

**TLDR**: A neural bandit coupled with transformers approach for automated instruction optimization of large language models.

## Abstract

Large language models (LLMs) have shown remarkable instruction-following capabilities and achieved impressive performances in various applications. However, the performances of LLMs depend heavily on the instructions given to them, which are typically manually tuned with substantial human efforts. Recent work has used the query-efficient Bayesian optimization (BO) algorithm to automatically optimize the instructions given to black-box LLMs. However, BO usually falls short when optimizing highly sophisticated (e.g., high-dimensional) objective functions, such as the functions mapping an instruction to the performance of an LLM. This is mainly due to the limited expressive power of the Gaussian process (GP) which is used by BO as a surrogate to model the objective function. Meanwhile, it has been repeatedly shown that neural networks (NNs), especially pre-trained transformers, possess strong expressive power and can model highly complex functions. So, we adopt a neural bandit algorithm which replaces the GP in BO by an NN surrogate to optimize instructions for black-box LLMs. More importantly, the neural bandit algorithm allows us to naturally couple the NN surrogate with the hidden representation learned by a pre-trained transformer (i.e., an open-source LLM), which significantly boosts its performance. These motivate us to propose our INSTruction optimization usIng Neural bandits Coupled with Transformers (INSTINCT) algorithm. We perform instruction optimization for ChatGPT and use extensive experiments to show that INSTINCT consistently outperforms baselines in different tasks, e.g., various instruction induction tasks and the task of improving zero-shot chain-of-thought instructions. Our code is available at https://github.com/xqlin98/INSTINCT.