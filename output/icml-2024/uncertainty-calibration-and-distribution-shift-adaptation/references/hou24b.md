---
title: "Decomposing Uncertainty for Large Language Models through Input Clarification Ensembling"
source: "https://proceedings.mlr.press/v235/hou24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hou24b/hou24b.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'large-language-model-alignment-and-capabilities']
tags: ['uncertainty-decomposition', 'llm', 'aleatoric', 'epistemic', 'clarification-ensembling']
venue: "ICML 2024"
tldr: "Introduces input clarification ensembling to decompose total LLM uncertainty into aleatoric and epistemic components without modifying model parameters."
---

# Decomposing Uncertainty for Large Language Models through Input Clarification Ensembling

**Source**: [https://proceedings.mlr.press/v235/hou24b.html](https://proceedings.mlr.press/v235/hou24b.html)

**TLDR**: Introduces input clarification ensembling to decompose total LLM uncertainty into aleatoric and epistemic components without modifying model parameters.

## Abstract

Uncertainty decomposition refers to the task of decomposing the total uncertainty of a predictive model into aleatoric (data) uncertainty, resulting from inherent randomness in the data-generating process, and epistemic (model) uncertainty, resulting from missing information in the model’s training data. In large language models (LLMs) specifically, identifying sources of uncertainty is an important step toward improving reliability, trustworthiness, and interpretability, but remains an important open research question. In this paper, we introduce an uncertainty decomposition framework for LLMs, called input clarification ensembling, which can be applied to any pre-trained LLM. Our approach generates a set of clarifications for the input, feeds them into an LLM, and ensembles the corresponding predictions. We show that, when aleatoric uncertainty arises from ambiguity or under-specification in LLM inputs, this approach makes it possible to factor an (un-clarified) LLM’s predictions into separate aleatoric and epistemic terms, using a decomposition similar to the one employed by Bayesian neural networks. Empirical evaluations demonstrate that input clarification ensembling provides accurate and reliable uncertainty quantification on several language processing tasks. Code and data are available at https://github.com/UCSB-NLP-Chang/llm_uncertainty.