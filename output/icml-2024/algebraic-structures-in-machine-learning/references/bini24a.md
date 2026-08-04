---
title: "ETHER: Efficient Finetuning of Large-Scale Models with Hyperplane Reflections"
source: "https://proceedings.mlr.press/v235/bini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bini24a/bini24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'algebraic-structures-in-machine-learning']
tags: ['parameter-efficient-finetuning', 'hyperplane-reflections', 'foundation-models', 'PEFT']
venue: "ICML 2024"
tldr: "ETHER introduces a parameter-efficient finetuning method using hyperplane reflections to adapt large-scale models with minimal additional parameters and compute."
---

# ETHER: Efficient Finetuning of Large-Scale Models with Hyperplane Reflections

**Source**: [https://proceedings.mlr.press/v235/bini24a.html](https://proceedings.mlr.press/v235/bini24a.html)

**TLDR**: ETHER introduces a parameter-efficient finetuning method using hyperplane reflections to adapt large-scale models with minimal additional parameters and compute.

## Abstract

Parameter-efficient finetuning (PEFT) has become ubiquitous to adapt foundation models to downstream task requirements while retaining their generalization ability. However, the amount of additionally introduced parameters and compute for successful adaptation and hyperparameter searches can explode quickly, especially when deployed at scale to serve numerous individual requests. To ensure effective, parameter-efficient, and hyperparameter-robust adaptation, we propose the ETHER transformation family, which performs Efficient fineTuning via HypErplane Reflections. By design, ETHER transformations require a minimal number of parameters, are less likely to deteriorate model performance, and exhibit robustness to hyperparameter and learning rate choices. In particular, we introduce ETHER and its relaxation ETHER+, which match or outperform existing PEFT methods with significantly fewer parameters ($\sim$$10$-$100$ times lower than LoRA or OFT) across multiple image synthesis and natural language tasks without exhaustive hyperparameter tuning. Finally, we investigate the recent emphasis on Hyperspherical Energy retention for adaptation and raise questions on its practical utility. The code is available at https://github.com/mwbini/ether.