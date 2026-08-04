---
title: "Memorization Through the Lens of Curvature of Loss Function Around Samples"
source: "https://proceedings.mlr.press/v235/garg24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/garg24a/garg24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['memorization', 'loss-curvature', 'neural-networks']
venue: "ICML 2024"
tldr: "Proposes using loss function curvature around training samples as a lens to study memorization in overparameterized neural networks."
---

# Memorization Through the Lens of Curvature of Loss Function Around Samples

**Source**: [https://proceedings.mlr.press/v235/garg24a.html](https://proceedings.mlr.press/v235/garg24a.html)

**TLDR**: Proposes using loss function curvature around training samples as a lens to study memorization in overparameterized neural networks.

## Abstract

Deep neural networks are over-parameterized and easily overfit to and memorize the datasets that they train on. In the extreme case, it has been shown that networks can memorize a randomly labeled dataset. In this paper, we propose using the curvature of the loss function around each training sample, averaged over training epochs, as a measure of memorization of a sample. We show that this curvature metric effectively captures memorization statistics, both qualitatively and quantitatively in popular image datasets. We provide quantitative validation of the proposed metric against memorization scores released by Feldman & Zhang (2020). Further, experiments on mislabeled data detection show that corrupted samples are learned with high curvature and using curvature for identifying mislabelled examples outperforms existing approaches. Qualitatively, we find that high curvature samples correspond to long-tailed, mislabeled, or conflicting instances, indicating a likelihood of memorization. Notably, this analysis helps us find, to the best of our knowledge, a novel failure mode on the CIFAR100 and ImageNet datasets: that of duplicated images with differing labels.