---
title: "Linear Explanations for Individual Neurons"
source: "https://proceedings.mlr.press/v235/oikarinen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oikarinen24a/oikarinen24a.pdf"
categories: ['llm-geometry-and-interpretability-research']
tags: ['neuron-explanation', 'linear-explanations', 'interpretability', 'activation-analysis']
venue: "ICML 2024"
tldr: "Proposes linear explanations for individual neurons that go beyond highest activations to better characterize neuron function."
---

# Linear Explanations for Individual Neurons

**Source**: [https://proceedings.mlr.press/v235/oikarinen24a.html](https://proceedings.mlr.press/v235/oikarinen24a.html)

**TLDR**: Proposes linear explanations for individual neurons that go beyond highest activations to better characterize neuron function.

## Abstract

In recent years many methods have been developed to understand the internal workings of neural networks, often by describing the function of individual neurons in the model. However, these methods typically only focus on explaining the very highest activations of a neuron. In this paper we show this is not sufficient, and that the highest activation range is only responsible for a very small percentage of the neuron’s causal effect. In addition, inputs causing lower activations are often very different and can’t be reliably predicted by only looking at high activations. We propose that neurons should instead be understood as a linear combination of concepts, and develop an efficient method for producing these linear explanations. In addition, we show how to automatically evaluate description quality using simulation, i.e. predicting neuron activations on unseen inputs in vision setting.