---
title: "Let Go of Your Labels with Unsupervised Transfer"
source: "https://proceedings.mlr.press/v235/gadetsky24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gadetsky24a/gadetsky24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'data-selection-and-active-learning-methods']
tags: ['zero-shot-transfer', 'unsupervised-learning', 'vision-language-models', 'foundation-models']
venue: "ICML 2024"
tldr: "A method for unsupervised transfer from foundation vision-language models that eliminates the need for human-defined category labels at test time."
---

# Let Go of Your Labels with Unsupervised Transfer

**Source**: [https://proceedings.mlr.press/v235/gadetsky24a.html](https://proceedings.mlr.press/v235/gadetsky24a.html)

**TLDR**: A method for unsupervised transfer from foundation vision-language models that eliminates the need for human-defined category labels at test time.

## Abstract

Foundation vision-language models have enabled remarkable zero-shot transferability of the pre-trained representations to a wide range of downstream tasks. However, to solve a new task, zero-shot transfer still necessitates human guidance to define visual categories that appear in the data. Here, we show that fully unsupervised transfer emerges when searching for the labeling of a dataset that induces maximal margin classifiers in representation spaces of different foundation models. We present TURTLE, a fully unsupervised method that effectively employs this guiding principle to uncover the underlying labeling of a downstream dataset without any supervision and task-specific representation learning. We evaluate TURTLE on a diverse benchmark suite of 26 datasets and show that it achieves new state-of-the-art unsupervised performance. Furthermore, TURTLE, although being fully unsupervised, outperforms zero-shot transfer baselines on a wide range of datasets. In particular, TURTLE matches the average performance of CLIP zero-shot on 26 datasets by employing the same representation space, spanning a wide range of architectures and model sizes. By guiding the search for the underlying labeling using the representation spaces of two foundation models, TURTLE surpasses zero-shot transfer and unsupervised prompt tuning baselines, demonstrating the surprising power and effectiveness of unsupervised transfer.