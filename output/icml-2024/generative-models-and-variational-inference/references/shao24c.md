---
title: "Language Generation with Strictly Proper Scoring Rules"
source: "https://proceedings.mlr.press/v235/shao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shao24c/shao24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'generative-models-and-variational-inference']
tags: ['language-generation', 'scoring-rules', 'maximum-likelihood-estimation']
venue: "ICML 2024"
tldr: "This paper explores using strictly proper scoring rules beyond log-likelihood for language generation to improve text generation quality."
---

# Language Generation with Strictly Proper Scoring Rules

**Source**: [https://proceedings.mlr.press/v235/shao24c.html](https://proceedings.mlr.press/v235/shao24c.html)

**TLDR**: This paper explores using strictly proper scoring rules beyond log-likelihood for language generation to improve text generation quality.

## Abstract

Language generation based on maximum likelihood estimation (MLE) has become the fundamental approach for text generation. Maximum likelihood estimation is typically performed by minimizing the log-likelihood loss, also known as the logarithmic score in statistical decision theory. The logarithmic score is strictly proper in the sense that it encourages honest forecasts, where the expected score is maximized only when the model reports true probabilities. Although many strictly proper scoring rules exist, the logarithmic score is the only local scoring rule among them that depends exclusively on the probability of the observed sample, making it capable of handling the exponentially large sample space of natural text. In this work, we propose a straightforward strategy for adapting scoring rules to language generation, allowing for language modeling with any non-local scoring rules. Leveraging this strategy, we train language generation models using two classic strictly proper scoring rules, the Brier score and the Spherical score, as alternatives to the logarithmic score. Experimental results indicate that simply substituting the loss function, without adjusting other hyperparameters, can yield substantial improvements in model’s generation capabilities. Moreover, these improvements can scale up to large language models (LLMs) such as LLaMA-7B and LLaMA-13B. Source code: https://github.com/shaochenze/ScoringRulesLM.