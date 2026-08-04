---
title: "Is In-Context Learning in Large Language Models Bayesian? A Martingale Perspective"
source: "https://proceedings.mlr.press/v235/falck24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/falck24a/falck24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['in-context-learning', 'large-language-models', 'bayesian-inference', 'martingale', 'exchangeability']
venue: "ICML 2024"
tldr: "Uses martingale theory to analyze whether in-context learning in LLMs is truly Bayesian, revealing necessary and sufficient conditions via exchangeability."
---

# Is In-Context Learning in Large Language Models Bayesian? A Martingale Perspective

**Source**: [https://proceedings.mlr.press/v235/falck24a.html](https://proceedings.mlr.press/v235/falck24a.html)

**TLDR**: Uses martingale theory to analyze whether in-context learning in LLMs is truly Bayesian, revealing necessary and sufficient conditions via exchangeability.

## Abstract

In-context learning (ICL) has emerged as a particularly remarkable characteristic of Large Language Models (LLM): given a pretrained LLM and an observed dataset, LLMs can make predictions for new data points from the same distribution without fine-tuning. Numerous works have postulated ICL as approximately Bayesian inference, rendering this a natural hypothesis. In this work, we analyse this hypothesis from a new angle through the martingale property, a fundamental requirement of a Bayesian learning system for exchangeable data. We show that the martingale property is a necessary condition for unambiguous predictions in such scenarios, and enables a principled, decomposed notion of uncertainty vital in trustworthy, safety-critical systems. We derive actionable checks with corresponding theory and test statistics which must hold if the martingale property is satisfied. We also examine if uncertainty in LLMs decreases as expected in Bayesian learning when more data is observed. In three experiments, we provide evidence for violations of the martingale property, and deviations from a Bayesian scaling behaviour of uncertainty, falsifying the hypothesis that ICL is Bayesian.