---
title: "Autaptic Synaptic Circuit Enhances Spatio-temporal Predictive Learning of Spiking Neural Networks"
source: "https://proceedings.mlr.press/v235/wang24ci.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ci/wang24ci.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['spiking-neural-networks', 'autaptic-synapse', 'spatio-temporal-learning']
venue: "ICML 2024"
tldr: "An autaptic synaptic circuit is introduced to enhance spatio-temporal predictive learning in spiking neural networks beyond the standard leaky integrate-and-fire model."
---

# Autaptic Synaptic Circuit Enhances Spatio-temporal Predictive Learning of Spiking Neural Networks

**Source**: [https://proceedings.mlr.press/v235/wang24ci.html](https://proceedings.mlr.press/v235/wang24ci.html)

**TLDR**: An autaptic synaptic circuit is introduced to enhance spatio-temporal predictive learning in spiking neural networks beyond the standard leaky integrate-and-fire model.

## Abstract

Spiking Neural Networks (SNNs) emulate the integrated-fire-leak mechanism found in biological neurons, offering a compelling combination of biological realism and energy efficiency. In recent years, they have gained considerable research interest. However, existing SNNs predominantly rely on the Leaky Integrate-and-Fire (LIF) model and are primarily suited for simple, static tasks. They lack the ability to effectively model long-term temporal dependencies and facilitate spatial information interaction, which is crucial for tackling complex, dynamic spatio-temporal prediction tasks. To tackle these challenges, this paper draws inspiration from the concept of autaptic synapses in biology and proposes a novel Spatio-Temporal Circuit (STC) model. The STC model integrates two learnable adaptive pathways, enhancing the spiking neurons’ temporal memory and spatial coordination. We conduct theoretical analysis of the dynamic parameters in the STC model, highlighting their contribution in establishing long-term memory and mitigating the issue of gradient vanishing. Through extensive experiments on multiple spatio-temporal prediction datasets, we demonstrate that our model outperforms other adaptive models. Furthermore, our model is compatible with existing spiking neuron models, thereby augmenting their dynamic representations. In essence, our work enriches the specificity and topological complexity of SNNs.