---
title: "Random Masking Finds Winning Tickets for Parameter Efficient Fine-tuning"
source: "https://proceedings.mlr.press/v235/xu24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24ag/xu24ag.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'data-selection-and-active-learning-methods']
tags: ['parameter-efficient-fine-tuning', 'random-masking', 'lottery-ticket']
venue: "ICML 2024"
tldr: "Shows that random masking can find winning tickets for parameter-efficient fine-tuning of large language models without training additional parameters."
---

# Random Masking Finds Winning Tickets for Parameter Efficient Fine-tuning

**Source**: [https://proceedings.mlr.press/v235/xu24ag.html](https://proceedings.mlr.press/v235/xu24ag.html)

**TLDR**: Shows that random masking can find winning tickets for parameter-efficient fine-tuning of large language models without training additional parameters.

## Abstract

Fine-tuning large language models (LLM) can be costly. Parameter-efficient fine-tuning (PEFT) addresses the problems by training a fraction of the parameters, whose success reveals the expressiveness and flexibility of pretrained models. This paper studies the limit of PEFT, by further simplifying its design and reducing the number of trainable parameters beyond standard setups. To this end, we use Random Masking to fine-tune the pretrained model. Despite its simplicity, we show that Random Masking is surprisingly effective: with a larger-than-expected learning rate, Random Masking can match the performance of standard PEFT algorithms such as LoRA on various tasks, using fewer trainable parameters. We provide both empirical and theoretical explorations into the success of Random Masking. We show that masking induces a flatter loss landscape and more distant solutions, which allows for and necessitates large learning rates.