---
title: "DOGE: Domain Reweighting with Generalization Estimation"
source: "https://proceedings.mlr.press/v235/fan24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fan24e/fan24e.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['domain-reweighting', 'pretraining-data', 'LLM-generalization']
venue: "ICML 2024"
tldr: "Proposes a principled domain reweighting method for LLM pretraining data to improve generalization across domains."
---

# DOGE: Domain Reweighting with Generalization Estimation

**Source**: [https://proceedings.mlr.press/v235/fan24e.html](https://proceedings.mlr.press/v235/fan24e.html)

**TLDR**: Proposes a principled domain reweighting method for LLM pretraining data to improve generalization across domains.

## Abstract

The coverage and composition of the pretraining data significantly impacts the generalization ability of Large Language Models (LLMs). Despite its importance, recent LLMs still rely on heuristics and trial and error to increase or reduce the influence of data-domains. We propose DOmain reweighting with Generalization Estimation (DoGE), which optimizes the probability of sampling from each domain (domain weights) in a principled way. Our approach is a two stage process consisting (i) training a proxy model to obtain domain weights using a bi-level optimization algorithm; (ii) training a larger base model by sampling training domains according to the learnt domain weights. In our experiments, we extensively show how DoGE improves the generalization of the base model to any target data mixture. On the SlimPajama dataset, our base model gets a better perplexity and few-shot reasoning accuracies across 6 tasks compared to baseline methods. Moreover, aiming to generalize to out-of-domain target tasks, which is unseen in the pretraining corpus (OOD domain), DoGE can effectively identify inter-domain dependencies, consistently achieves better test perplexity on the target domain.