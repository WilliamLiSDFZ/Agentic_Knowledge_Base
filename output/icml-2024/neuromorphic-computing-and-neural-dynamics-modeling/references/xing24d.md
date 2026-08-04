---
title: "SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms"
source: "https://proceedings.mlr.press/v235/xing24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xing24d/xing24d.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['spiking-neural-networks', 'language-modeling', 'binary-activation']
venue: "ICML 2024"
tldr: "SpikeLM proposes elastic bi-spiking mechanisms to enable general spike-driven language modeling with energy-efficient binary activations for large-scale NLP tasks."
---

# SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms

**Source**: [https://proceedings.mlr.press/v235/xing24d.html](https://proceedings.mlr.press/v235/xing24d.html)

**TLDR**: SpikeLM proposes elastic bi-spiking mechanisms to enable general spike-driven language modeling with energy-efficient binary activations for large-scale NLP tasks.

## Abstract

Towards energy-efficient artificial intelligence similar to the human brain, the bio-inspired spiking neural networks (SNNs) have advantages of biological plausibility, event-driven sparsity, and binary activation. Recently, large-scale language models exhibit promising generalization capability, making it a valuable issue to explore more general spike-driven models. However, the binary spikes in existing SNNs fail to encode adequate semantic information, placing technological challenges for generalization. This work proposes the first fully spiking mechanism for general language tasks, including both discriminative and generative ones. Different from previous spikes with 0,1 levels, we propose a more general spike formulation with bi-directional, elastic amplitude, and elastic frequency encoding, while still maintaining the addition nature of SNNs. In a single time step, the spike is enhanced by direction and amplitude information; in spike frequency, a strategy to control spike firing rate is well designed. We plug this elastic bi-spiking mechanism in language modeling, named SpikeLM. It is the first time to handle general language tasks with fully spike-driven models, which achieve much higher accuracy than previously possible. SpikeLM also greatly bridges the performance gap between SNNs and ANNs in language modeling. Our code is available at https://github.com/Xingrun-Xing/SpikeLM.