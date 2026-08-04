---
title: "Enhancing Adversarial Robustness in SNNs with Sparse Gradients"
source: "https://proceedings.mlr.press/v235/liu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24f/liu24f.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['spiking-neural-networks', 'adversarial-robustness', 'sparse-gradients']
venue: "ICML 2024"
tldr: "This paper enhances the adversarial robustness of spiking neural networks by leveraging sparse gradient mechanisms."
---

# Enhancing Adversarial Robustness in SNNs with Sparse Gradients

**Source**: [https://proceedings.mlr.press/v235/liu24f.html](https://proceedings.mlr.press/v235/liu24f.html)

**TLDR**: This paper enhances the adversarial robustness of spiking neural networks by leveraging sparse gradient mechanisms.

## Abstract

Spiking Neural Networks (SNNs) have attracted great attention for their energy-efficient operations and biologically inspired structures, offering potential advantages over Artificial Neural Networks (ANNs) in terms of energy efficiency and interpretability. Nonetheless, similar to ANNs, the robustness of SNNs remains a challenge, especially when facing adversarial attacks. Existing techniques, whether adapted from ANNs or specifically designed for SNNs, exhibit limitations in training SNNs or defending against strong attacks. In this paper, we propose a novel approach to enhance the robustness of SNNs through gradient sparsity regularization. We observe that SNNs exhibit greater resilience to random perturbations compared to adversarial perturbations, even at larger scales. Motivated by this, we aim to narrow the gap between SNNs under adversarial and random perturbations, thereby improving their overall robustness. To achieve this, we theoretically prove that this performance gap is upper bounded by the gradient sparsity of the probability associated with the true label concerning the input image, laying the groundwork for a practical strategy to train robust SNNs by regularizing the gradient sparsity. We validate the effectiveness of our approach through extensive experiments on both image-based and event-based datasets. The results demonstrate notable improvements in the robustness of SNNs. Our work highlights the importance of gradient sparsity in SNNs and its role in enhancing robustness.