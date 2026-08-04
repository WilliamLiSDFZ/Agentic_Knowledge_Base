---
title: "Sign Gradient Descent-based Neuronal Dynamics: ANN-to-SNN Conversion Beyond ReLU Network"
source: "https://proceedings.mlr.press/v235/oh24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oh24b/oh24b.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['spiking-neural-networks', 'ANN-to-SNN-conversion', 'neuromorphic-computing', 'sign-gradient-descent']
venue: "ICML 2024"
tldr: "Introduces sign gradient descent-based neuronal dynamics to enable ANN-to-SNN conversion beyond ReLU networks."
---

# Sign Gradient Descent-based Neuronal Dynamics: ANN-to-SNN Conversion Beyond ReLU Network

**Source**: [https://proceedings.mlr.press/v235/oh24b.html](https://proceedings.mlr.press/v235/oh24b.html)

**TLDR**: Introduces sign gradient descent-based neuronal dynamics to enable ANN-to-SNN conversion beyond ReLU networks.

## Abstract

Spiking neural network (SNN) is studied in multidisciplinary domains to (i) enable order-of-magnitudes energy-efficient AI inference, and (ii) computationally simulate neuroscientific mechanisms. The lack of discrete theory obstructs the practical application of SNN by limiting its performance and nonlinearity support. We present a new optimization-theoretic perspective of the discrete dynamics of spiking neuron. We prove that a discrete dynamical system of simple integrate-and-fire models approximates the subgradient method over unconstrained optimization problems. We practically extend our theory to introduce a novel sign gradient descent (signGD)-based neuronal dynamics that can (i) approximate diverse nonlinearities beyond ReLU, and (ii) advance ANN-to-SNN conversion performance in low time-steps. Experiments on large-scale datasets show that our technique achieve (i) state-of-the-art performance in ANN-to-SNN conversion, and (ii) is first to convert new DNN architectures, e.g., ConvNext, MLP-Mixer, and ResMLP. We publicly share our source code at www.github.com/snuhcs/snn_signgd .