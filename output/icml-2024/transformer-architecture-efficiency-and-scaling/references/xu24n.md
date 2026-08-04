---
title: "Enhancing Vision Transformer: Amplifying Non-Linearity in Feedforward Network Module"
source: "https://proceedings.mlr.press/v235/xu24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24n/xu24n.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['vision-transformer', 'feedforward-network', 'non-linearity']
venue: "ICML 2024"
tldr: "This paper improves vision transformers by amplifying non-linearity in the feedforward network module to enhance representational capacity."
---

# Enhancing Vision Transformer: Amplifying Non-Linearity in Feedforward Network Module

**Source**: [https://proceedings.mlr.press/v235/xu24n.html](https://proceedings.mlr.press/v235/xu24n.html)

**TLDR**: This paper improves vision transformers by amplifying non-linearity in the feedforward network module to enhance representational capacity.

## Abstract

Transformer models have been gaining substantial interest in the field of computer vision tasks nowadays. Although a vision transformer contains two important components which are self-attention module and feedforward network (FFN) module, the majority of research tends to concentrate on modifying the former while leaving the latter in its original form. In this paper, we focus on improving the FFN module within the vision transformer. Through theoretical analysis, we demonstrate that the effect of the FFN module primarily lies in providing non-linearity, whose degree corresponds to the hidden dimensions. Thus, the computational cost of the FFN module can be reduced by enhancing the degree of non-linearity in the nonlinear function. Leveraging this insight, we propose an improved FFN (IFFN) module for vision transformers which involves the usage of the arbitrary GeLU (AGeLU) function and integrating multiple instances of it to augment non-linearity so that the number of hidden dimensions can be effectively reduced. Besides, a spatial enhancement part is involved to further enrich the non-linearity in the proposed IFFN module. Experimental results show that we can apply our method to a wide range of state-of-the-art vision transformer models irrespective of how they modify their self-attention part and the overall architecture, and reduce FLOPs and parameters without compromising classification accuracy on the ImageNet dataset.