---
title: "Balanced Resonate-and-Fire Neurons"
source: "https://proceedings.mlr.press/v235/higuchi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/higuchi24a/higuchi24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'neural-network-learning-dynamics-theory']
tags: ['spiking-neurons', 'resonate-and-fire', 'neuromorphic', 'biological-plausibility']
venue: "ICML 2024"
tldr: "Introduces a balanced resonate-and-fire neuron model that fixes instability issues of prior formulations while remaining biologically plausible."
---

# Balanced Resonate-and-Fire Neurons

**Source**: [https://proceedings.mlr.press/v235/higuchi24a.html](https://proceedings.mlr.press/v235/higuchi24a.html)

**TLDR**: Introduces a balanced resonate-and-fire neuron model that fixes instability issues of prior formulations while remaining biologically plausible.

## Abstract

The resonate-and-fire (RF) neuron, introduced over two decades ago, is a simple, efficient, yet biologically plausible spiking neuron model, which can extract frequency patterns within the time domain due to its resonating membrane dynamics. However, previous RF formulations suffer from intrinsic shortcomings that limit effective learning and prevent exploiting the principled advantage of RF neurons. Here, we introduce the balanced RF (BRF) neuron, which alleviates some of the intrinsic limitations of vanilla RF neurons and demonstrates its effectiveness within recurrent spiking neural networks (RSNNs) on various sequence learning tasks. We show that networks of BRF neurons achieve overall higher task performance, produce only a fraction of the spikes, and require significantly fewer parameters as compared to modern RSNNs. Moreover, BRF-RSNN consistently provide much faster and more stable training convergence, even when bridging many hundreds of time steps during backpropagation through time (BPTT). These results underscore that our BRF-RSNN is a strong candidate for future large-scale RSNN architectures, further lines of research in SNN methodology, and more efficient hardware implementations.