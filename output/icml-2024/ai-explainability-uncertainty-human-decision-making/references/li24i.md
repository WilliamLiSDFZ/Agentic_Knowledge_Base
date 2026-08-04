---
title: "GiLOT: Interpreting Generative Language Models via Optimal Transport"
source: "https://proceedings.mlr.press/v235/li24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24i/li24i.pdf"
categories: ['llm-geometry-and-interpretability-research', 'ai-explainability-uncertainty-human-decision-making']
tags: ['LLM-interpretability', 'feature-attribution', 'optimal-transport', 'generative-models', 'explanation']
venue: "ICML 2024"
tldr: "Introduces GiLOT, an optimal transport-based feature attribution method for interpreting generative large language models faithfully."
---

# GiLOT: Interpreting Generative Language Models via Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/li24i.html](https://proceedings.mlr.press/v235/li24i.html)

**TLDR**: Introduces GiLOT, an optimal transport-based feature attribution method for interpreting generative large language models faithfully.

## Abstract

While large language models (LLMs) surge with the rise of generative AI, algorithms to explain LLMs highly desire. Existing feature attribution methods adequate for discriminative language models like BERT often fail to deliver faithful explanations for LLMs, primarily due to two issues: (1) For every specific prediction, the LLM outputs a probability distribution over the vocabulary–a large number of tokens with unequal semantic distance; (2) As an autoregressive language model, the LLM handles input tokens while generating a sequence of probability distributions of various tokens. To address above two challenges, this work proposes GiLOT that leverages Optimal Transport to measure the distributional change of all possible generated sequences upon the absence of every input token, while taking into account the tokens’ similarity, so as to faithfully estimate feature attribution for LLMs. We have carried out extensive experiments on top of Llama families and their fine-tuned derivatives across various scales to validate the effectiveness of GiLOT for estimating the input attributions. The results show that GiLOT outperforms existing solutions on a number of faithfulness metrics under fair comparison settings. Source code is publicly available at https://github.com/holyseven/GiLOT.