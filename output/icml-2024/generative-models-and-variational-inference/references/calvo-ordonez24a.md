---
title: "Partially Stochastic Infinitely Deep Bayesian Neural Networks"
source: "https://proceedings.mlr.press/v235/calvo-ordonez24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/calvo-ordonez24a/calvo-ordonez24a.pdf"
categories: ['generative-models-and-variational-inference', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['Bayesian-neural-networks', 'infinite-depth', 'stochastic-processes', 'variational-inference']
venue: "ICML 2024"
tldr: "Introduces partially stochastic infinitely deep Bayesian neural networks that improve computational efficiency while maintaining probabilistic expressiveness."
---

# Partially Stochastic Infinitely Deep Bayesian Neural Networks

**Source**: [https://proceedings.mlr.press/v235/calvo-ordonez24a.html](https://proceedings.mlr.press/v235/calvo-ordonez24a.html)

**TLDR**: Introduces partially stochastic infinitely deep Bayesian neural networks that improve computational efficiency while maintaining probabilistic expressiveness.

## Abstract

In this paper, we present Partially Stochastic Infinitely Deep Bayesian Neural Networks, a novel family of architectures that integrates partial stochasticity into the framework of infinitely deep neural networks. Our new class of architectures is designed to improve the computational efficiency of existing architectures at training and inference time. To do this, we leverage the advantages of partial stochasticity in the infinite-depth limit which include the benefits of full stochasticity e.g. robustness, uncertainty quantification, and memory efficiency, whilst improving their limitations around computational complexity. We present a variety of architectural configurations, offering flexibility in network design including different methods for weight partition. We also provide mathematical guarantees on the expressivity of our models by establishing that our network family qualifies as Universal Conditional Distribution Approximators. Lastly, empirical evaluations across multiple tasks show that our proposed architectures achieve better downstream task performance and uncertainty quantification than their counterparts while being significantly more efficient. The code can be found at https://github.com/Sergio20f/part_stoch_inf_deep