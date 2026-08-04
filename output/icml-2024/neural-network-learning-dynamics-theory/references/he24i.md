---
title: "The Effect of Weight Precision on the Neuron Count in Deep ReLU Networks"
source: "https://proceedings.mlr.press/v235/he24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24i/he24i.pdf"
categories: ['neural-network-learning-dynamics-theory', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['weight-precision', 'ReLU-networks', 'neuron-count']
venue: "ICML 2024"
tldr: "Analyzes how weight precision interacts with network depth and neuron count in deep ReLU networks."
---

# The Effect of Weight Precision on the Neuron Count in Deep ReLU Networks

**Source**: [https://proceedings.mlr.press/v235/he24i.html](https://proceedings.mlr.press/v235/he24i.html)

**TLDR**: Analyzes how weight precision interacts with network depth and neuron count in deep ReLU networks.

## Abstract

Deep neural networks (DNNs) have become pivotal in machine learning, but the impact of weight precision, such as in networks with rectified linear units (ReLU), remains underexplored. We analytically investigate the interplay of three key factors: the precision of ReLU network weights, the number of neurons, and the time of the preprocessing algorithm that generates the network description. Our study, which, to the best of our knowledge, is the first formal work on weight precision, yields three main results. (1) We present an exponential time preprocessing algorithm that showcases the possibility of trading ReLU nodes for weight precision. Specifically, our method achieves an exponential reduction in neuron count when computing any function of high complexity with boolean input encoding. What is the implication of the above result in theoretical and practical works? (2) In theory of computing, in general, there is no free lunch. In our case, if you significantly reduce the number of neurons then you should pay the cost in weight precision. To address this, we introduce a notion of network size that considers weight precision in addition to the network’s number of neurons. We establish that under this redefined notion of network size, it is generally impossible to exchange neurons for weight precision in ReLU networks of the same (redefined) size. (3) In practice, we show that high weight precision alone cannot help in reducing the neuron count. If instead of our exponential time preprocessing algorithm one uses any polynomial time algorithm, then it is impossible to non-trivially reduce the neuron count, regardless of the high weight precision.