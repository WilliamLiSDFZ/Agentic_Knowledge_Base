---
title: "Which Frequencies do CNNs Need? Emergent Bottleneck Structure in Feature Learning"
source: "https://proceedings.mlr.press/v235/wen24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wen24d/wen24d.pdf"
categories: ['neural-network-learning-dynamics-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['CNN', 'frequency-analysis', 'feature-learning', 'bottleneck-structure']
venue: "ICML 2024"
tldr: "CNNs develop an emergent convolution bottleneck where early layers compress inputs to a few frequencies and channels before final-layer mapping."
---

# Which Frequencies do CNNs Need? Emergent Bottleneck Structure in Feature Learning

**Source**: [https://proceedings.mlr.press/v235/wen24d.html](https://proceedings.mlr.press/v235/wen24d.html)

**TLDR**: CNNs develop an emergent convolution bottleneck where early layers compress inputs to a few frequencies and channels before final-layer mapping.

## Abstract

We describe the emergence of a Convolution Bottleneck (CBN) structure in CNNs, where the network uses its first few layers to transform the input representation into a representation that is supported only along a few frequencies and channels, before using the last few layers to map back to the outputs. We define the CBN rank, which describes the number and type of frequencies that are kept inside the bottleneck, and partially prove that the parameter norm required to represent a function $f$ scales as depth times the CBN rank $f$. We also show that the parameter norm depends at next order on the regularity of $f$. We show that any network with almost optimal parameter norm will exhibit a CBN structure in both the weights and - under the assumption that the network is stable under large learning rate - the activations, which motivates the common practice of down-sampling; and we verify that the CBN results still hold with down-sampling. Finally we use the CBN structure to interpret the functions learned by CNNs on a number of tasks.