---
title: "How Learning by Reconstruction Produces Uninformative Features For Perception"
source: "https://proceedings.mlr.press/v235/balestriero24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/balestriero24b/balestriero24b.pdf"
categories: ['generative-models-and-variational-inference', 'test-time-adaptation-methods-and-evaluation']
tags: ['reconstruction-learning', 'representation-learning', 'uninformative-features']
venue: "ICML 2024"
tldr: "This paper shows that learning by reconstruction allocates model capacity toward perceptually uninformative features, misaligning with perception tasks."
---

# How Learning by Reconstruction Produces Uninformative Features For Perception

**Source**: [https://proceedings.mlr.press/v235/balestriero24b.html](https://proceedings.mlr.press/v235/balestriero24b.html)

**TLDR**: This paper shows that learning by reconstruction allocates model capacity toward perceptually uninformative features, misaligning with perception tasks.

## Abstract

Input space reconstruction is an attractive representation learning paradigm. Despite interpretability benefit of reconstruction and generation, we identify a misalignment between learning to reconstruct, and learning for perception. We show that the former allocates a model’s capacity towards a subspace of the data explaining the observed variance–a subspace with uninformative features for the latter. For example, the supervised TinyImagenet task with images projected onto the top subspace explaining 90% of the pixel variance can be solved with 45% test accuracy. Using the bottom subspace instead, accounting for only 20% of the pixel variance, reaches 55% test accuracy. Learning by reconstruction is also wasteful as the features for perception are learned last, pushing the need for long training schedules. We finally prove that learning by denoising can alleviate that misalignment for some noise strategies, e.g., masking. While tuning the noise strategy without knowledge of the perception task seems challenging, we provide a solution to detect if a noise strategy is never beneficial regardless of the perception task, e.g., additive Gaussian noise.