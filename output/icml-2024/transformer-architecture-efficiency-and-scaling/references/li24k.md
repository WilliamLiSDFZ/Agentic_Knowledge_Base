---
title: "Evolving Subnetwork Training for Large Language Models"
source: "https://proceedings.mlr.press/v235/li24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24k/li24k.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['large-language-models', 'subnetwork-training', 'parameter-redundancy', 'efficient-training', 'scaling']
venue: "ICML 2024"
tldr: "Proposes evolving subnetwork training to reduce the training cost of large language models by exploiting parameter redundancy."
---

# Evolving Subnetwork Training for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/li24k.html](https://proceedings.mlr.press/v235/li24k.html)

**TLDR**: Proposes evolving subnetwork training to reduce the training cost of large language models by exploiting parameter redundancy.

## Abstract

Large language models have ushered in a new era of artificial intelligence research. However, their substantial training costs hinder further development and widespread adoption. In this paper, inspired by the redundancy in the parameters of large language models, we propose a novel training paradigm: Evolving Subnetwork Training (EST). EST samples subnetworks from the layers of the large language model and from commonly used modules within each layer, Multi-Head Attention (MHA) and Multi-Layer Perceptron (MLP). By gradually increasing the size of the subnetworks during the training process, EST can save the cost of training. We apply EST to train GPT2 model and TinyLlama model, resulting in 26.7% FLOPs saving for GPT2 and 25.0% for TinyLlama without an increase in loss on the pre-training dataset. Moreover, EST leads to performance improvements in downstream tasks, indicating that it benefits generalization. Additionally, we provide intuitive theoretical studies based on training dynamics and Dropout theory to ensure the feasibility of EST.