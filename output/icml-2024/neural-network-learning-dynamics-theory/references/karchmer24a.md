---
title: "On Stronger Computational Separations Between Multimodal and Unimodal Machine Learning"
source: "https://proceedings.mlr.press/v235/karchmer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/karchmer24a/karchmer24a.pdf"
categories: ['algebraic-structures-in-machine-learning', 'neural-network-learning-dynamics-theory']
tags: ['multimodal-learning', 'computational-complexity', 'theoretical-separations']
venue: "ICML 2024"
tldr: "Develops stronger theoretical computational separations between multimodal and unimodal machine learning models to justify empirical multimodal success."
---

# On Stronger Computational Separations Between Multimodal and Unimodal Machine Learning

**Source**: [https://proceedings.mlr.press/v235/karchmer24a.html](https://proceedings.mlr.press/v235/karchmer24a.html)

**TLDR**: Develops stronger theoretical computational separations between multimodal and unimodal machine learning models to justify empirical multimodal success.

## Abstract

Recently, multimodal machine learning has enjoyed huge empirical success (e.g. GPT-4). Motivated to develop theoretical justification for this empirical success, Lu (NeurIPS ’23, ALT ’24) introduces a theory of multimodal learning, and considers possible separations between theoretical models of multimodal and unimodal learning. In particular, Lu (ALT ’24) shows a computational separation, which is relevant to worst-case instances of the learning task. In this paper, we give a stronger average-case computational separation, where for "typical" instances of the learning task, unimodal learning is computationally hard, but multimodal learning is easy. We then question how "natural" the average-case separation is. Would it be encountered in practice? To this end, we prove that under basic conditions, any given computational separation between average-case unimodal and multimodal learning tasks implies a corresponding cryptographic key agreement protocol. We suggest to interpret this as evidence that very strong computational advantages of multimodal learning may arise infrequently in practice, since they exist only for the "pathological" case of inherently cryptographic distributions. However, this does not apply to possible (super-polynomial) statistical advantages.