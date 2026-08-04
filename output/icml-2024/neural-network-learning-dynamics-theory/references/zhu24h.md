---
title: "Catapults in SGD: spikes in the training loss and their impact on generalization through feature learning"
source: "https://proceedings.mlr.press/v235/zhu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24h/zhu24h.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['SGD', 'training-loss-spikes', 'catapults', 'generalization', 'feature-learning']
venue: "ICML 2024"
tldr: "This paper explains that loss spikes during SGD training are catapult phenomena and shows their role in generalization through feature learning."
---

# Catapults in SGD: spikes in the training loss and their impact on generalization through feature learning

**Source**: [https://proceedings.mlr.press/v235/zhu24h.html](https://proceedings.mlr.press/v235/zhu24h.html)

**TLDR**: This paper explains that loss spikes during SGD training are catapult phenomena and shows their role in generalization through feature learning.

## Abstract

In this paper, we first present an explanation regarding the common occurrence of spikes in the training loss when neural networks are trained with stochastic gradient descent (SGD). We provide evidence that the spikes in the training loss of SGD are "catapults", an optimization phenomenon originally observed in GD with large learning rates in Lewkowycz et al. (2020). We empirically show that these catapults occur in a low-dimensional subspace spanned by the top eigenvectors of the tangent kernel, for both GD and SGD. Second, we posit an explanation for how catapults lead to better generalization by demonstrating that catapults increase feature learning by increasing alignment with the Average Gradient Outer Product (AGOP) of the true predictor. Furthermore, we demonstrate that a smaller batch size in SGD induces a larger number of catapults, thereby improving AGOP alignment and test performance.