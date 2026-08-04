---
title: "Human-like Category Learning by Injecting Ecological Priors from Large Language Models into Neural Networks"
source: "https://proceedings.mlr.press/v235/jagadish24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jagadish24a/jagadish24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'neural-network-learning-dynamics-theory']
tags: ['category-learning', 'ecological-rationality', 'LLM-priors', 'neural-networks', 'cognitive-science']
venue: "ICML 2024"
tldr: "This work injects ecologically valid priors from LLMs into neural networks to model human-like category learning and test ecological rationality."
---

# Human-like Category Learning by Injecting Ecological Priors from Large Language Models into Neural Networks

**Source**: [https://proceedings.mlr.press/v235/jagadish24a.html](https://proceedings.mlr.press/v235/jagadish24a.html)

**TLDR**: This work injects ecologically valid priors from LLMs into neural networks to model human-like category learning and test ecological rationality.

## Abstract

Ecological rationality refers to the notion that humans are rational agents adapted to their environment. However, testing this theory remains challenging due to two reasons: the difficulty in defining what tasks are ecologically valid and building rational models for these tasks. In this work, we demonstrate that large language models can generate cognitive tasks, specifically category learning tasks, that match the statistics of real-world tasks, thereby addressing the first challenge. We tackle the second challenge by deriving rational agents adapted to these tasks using the framework of meta-learning, leading to a class of models called ecologically rational meta-learned inference (ERMI). ERMI quantitatively explains human data better than seven other cognitive models in two different experiments. It additionally matches human behavior on a qualitative level: (1) it finds the same tasks difficult that humans find difficult, (2) it becomes more reliant on an exemplar-based strategy for assigning categories with learning, and (3) it generalizes to unseen stimuli in a human-like way. Furthermore, we show that ERMI’s ecologically valid priors allow it to achieve state-of-the-art performance on the OpenML-CC18 classification benchmark.