---
title: "Verification of Machine Unlearning is Fragile"
source: "https://proceedings.mlr.press/v235/zhang24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24h/zhang24h.pdf"
categories: ['adversarial-robustness-and-model-security', 'privacy-preserving-federated-and-distributed-learning']
tags: ['machine-unlearning', 'verification', 'adversarial']
venue: "ICML 2024"
tldr: "Demonstrates that existing verification schemes for machine unlearning are fragile and susceptible to adversarial manipulation by model providers."
---

# Verification of Machine Unlearning is Fragile

**Source**: [https://proceedings.mlr.press/v235/zhang24h.html](https://proceedings.mlr.press/v235/zhang24h.html)

**TLDR**: Demonstrates that existing verification schemes for machine unlearning are fragile and susceptible to adversarial manipulation by model providers.

## Abstract

As privacy concerns escalate in the realm of machine learning, data owners now have the option to utilize machine unlearning to remove their data from machine learning models, following recent legislation. To enhance transparency in machine unlearning and avoid potential dishonesty by model providers, various verification strategies have been proposed. These strategies enable data owners to ascertain whether their target data has been effectively unlearned from the model. However, our understanding of the safety issues of machine unlearning verification remains nascent. In this paper, we explore the novel research question of whether model providers can circumvent verification strategies while retaining the information of data supposedly unlearned. Our investigation leads to a pessimistic answer: the verification of machine unlearning is fragile. Specifically, we categorize the current verification strategies regarding potential dishonesty among model providers into two types. Subsequently, we introduce two novel adversarial unlearning processes capable of circumventing both types. We validate the efficacy of our methods through theoretical analysis and empirical experiments using real-world datasets. This study highlights the vulnerabilities and limitations in machine unlearning verification, paving the way for further research into the safety of machine unlearning.