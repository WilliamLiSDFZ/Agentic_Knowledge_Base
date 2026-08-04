---
title: "A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts"
source: "https://proceedings.mlr.press/v235/chowdhury24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chowdhury24a/chowdhury24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['mixture-of-experts', 'model-pruning', 'fine-tuning']
venue: "ICML 2024"
tldr: "A provably effective expert pruning method for sparse MoE models after fine-tuning reduces deployment costs while maintaining performance."
---

# A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts

**Source**: [https://proceedings.mlr.press/v235/chowdhury24a.html](https://proceedings.mlr.press/v235/chowdhury24a.html)

**TLDR**: A provably effective expert pruning method for sparse MoE models after fine-tuning reduces deployment costs while maintaining performance.

## Abstract

The sparsely gated mixture of experts (MoE) architecture sends different inputs to different subnetworks (experts), through trainable routers. MoE reduces the training computation significantly for large models, but its deployment can be still memory/computation expensive for some downstream tasks. Model pruning is a popular approach to reduce inference computation, but its application in MoE architecture is largely unexplored. To the best of our knowledge, this paper provides the first provably efficient technique for pruning experts in fine-tuned MoE models. We theoretically prove that prioritizing the pruning of the experts with a smaller change of the router’s $l_2$ norm from the pre-trained model guarantees the preservation of test accuracy, while significantly reducing the model size and the computational requirements. Although our theoretical analysis is centered on binary classification tasks on simplified MoE architecture, our expert pruning method is verified on large vision MoE models such as V-MoE and $\text{E}^3$-MoE fine-tuned on benchmark datasets such as CIFAR-10, CIFAR-100, and ImageNet.