---
title: "PrE-Text: Training Language Models on Private Federated Data in the Age of LLMs"
source: "https://proceedings.mlr.press/v235/hou24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hou24c/hou24c.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'large-language-model-alignment-and-capabilities']
tags: ['federated-learning', 'privacy', 'llm', 'synthetic-data', 'differential-privacy']
venue: "ICML 2024"
tldr: "Proposes PrE-Text, a framework using LLMs to generate differentially private synthetic text for training models on private federated data without on-device training."
---

# PrE-Text: Training Language Models on Private Federated Data in the Age of LLMs

**Source**: [https://proceedings.mlr.press/v235/hou24c.html](https://proceedings.mlr.press/v235/hou24c.html)

**TLDR**: Proposes PrE-Text, a framework using LLMs to generate differentially private synthetic text for training models on private federated data without on-device training.

## Abstract

On-device training is currently the most common approach for training machine learning (ML) models on private, distributed user data. Despite this, on-device training has several drawbacks: (1) most user devices are too small to train large models on-device, (2) on-device training is communication- and computation-intensive, and (3) on-device training can be difficult to debug and deploy. To address these problems, we propose Private Evolution-Text (PrE-Text), a method for generating differentially private (DP) synthetic textual data. First, we show that across multiple datasets, training small models (models that fit on user devices) with PrE-Text synthetic data outperforms small models trained on-device under practical privacy regimes ($\epsilon=1.29$, $\epsilon=7.58$). We achieve these results while using 9$\times$ fewer rounds, 6$\times$ less client computation per round, and 100$\times$ less communication per round. Second, finetuning large models on PrE-Text’s DP synthetic data improves large language model (LLM) performance on private data across the same range of privacy budgets. Altogether, these results suggest that training on DP synthetic data can be a better option than training a model on-device on private distributed data. Code is available at https://github.com/houcharlie/PrE-Text.