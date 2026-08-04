---
title: "Efficient Exploration for LLMs"
source: "https://proceedings.mlr.press/v235/dwaracherla24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dwaracherla24a/dwaracherla24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['exploration', 'reinforcement-learning-from-human-feedback', 'active-learning', 'reward-modeling', 'large-language-models']
venue: "ICML 2024"
tldr: "Demonstrates that efficient exploration via Thompson sampling and other strategies substantially improves LLM alignment from human feedback."
---

# Efficient Exploration for LLMs

**Source**: [https://proceedings.mlr.press/v235/dwaracherla24a.html](https://proceedings.mlr.press/v235/dwaracherla24a.html)

**TLDR**: Demonstrates that efficient exploration via Thompson sampling and other strategies substantially improves LLM alignment from human feedback.

## Abstract

We present evidence of substantial benefit from efficient exploration in gathering human feedback to improve large language models. In our experiments, an agent sequentially generates queries while fitting a reward model to the feedback received. Our best-performing agent generates queries using double Thompson sampling, with uncertainty represented by an epistemic neural network. Our results demonstrate that efficient exploration enables high levels of performance with far fewer queries. Further, both uncertainty estimation and the choice of exploration scheme play critical roles.