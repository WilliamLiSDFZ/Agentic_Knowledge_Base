---
title: "Parameter Symmetry and Noise Equilibrium of Stochastic Gradient Descent"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/aa933b5abc1be30baece1d230ec575a7-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory']
tags: ['parameter-symmetry', 'stochastic-gradient-descent', 'noise-equilibrium']
venue: "NeurIPS 2024"
tldr: "The interplay between exponential parameter symmetries and SGD noise is analyzed to characterize noise equilibrium in neural network training."
---

# Parameter Symmetry and Noise Equilibrium of Stochastic Gradient Descent

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/aa933b5abc1be30baece1d230ec575a7-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/aa933b5abc1be30baece1d230ec575a7-Abstract-Conference.html)

**TLDR**: The interplay between exponential parameter symmetries and SGD noise is analyzed to characterize noise equilibrium in neural network training.

## Abstract

Symmetries are prevalent in deep learning and can significantly influence the learning dynamics of neural networks. In this paper, we examine how exponential symmetries -- a broad subclass of continuous symmetries present in the model architecture or loss function -- interplay with stochastic gradient descent (SGD). We first prove that gradient noise creates a systematic motion (a ``Noether flow") of the parameters $\theta$ along the degenerate direction to a unique initialization-independent fixed point $\theta^*$. These points are referred to as the noise equilibria because, at these points, noise contributions from different directions are balanced and aligned. Then, we show that the balance and alignment of gradient noise can serve as a novel alternative mechanism for explaining important phenomena such as progressive sharpening/flattening and representation formation within neural networks and have practical implications for understanding techniques like representation normalization and warmup.