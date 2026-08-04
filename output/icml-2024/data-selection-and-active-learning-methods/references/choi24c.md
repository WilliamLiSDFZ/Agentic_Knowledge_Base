---
title: "BWS: Best Window Selection Based on Sample Scores for Data Pruning across Broad Ranges"
source: "https://proceedings.mlr.press/v235/choi24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/choi24c/choi24c.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['data-pruning', 'dataset-distillation', 'sample-selection']
venue: "ICML 2024"
tldr: "Best Window Selection (BWS) is a data pruning method based on sample scores that performs well across both high and low data selection ratios."
---

# BWS: Best Window Selection Based on Sample Scores for Data Pruning across Broad Ranges

**Source**: [https://proceedings.mlr.press/v235/choi24c.html](https://proceedings.mlr.press/v235/choi24c.html)

**TLDR**: Best Window Selection (BWS) is a data pruning method based on sample scores that performs well across both high and low data selection ratios.

## Abstract

Data subset selection aims to find a smaller yet informative subset of a large dataset that can approximate the full-dataset training, addressing challenges associated with training neural networks on large-scale datasets. However, existing methods tend to specialize in either high or low selection ratio regimes, lacking a universal approach that consistently achieves competitive performance across a broad range of selection ratios. We introduce a universal and efficient data subset selection method, Best Window Selection (BWS), by proposing a method to choose the best window subset from samples ordered based on their difficulty scores. This approach offers flexibility by allowing the choice of window intervals that span from easy to difficult samples. Furthermore, we provide an efficient mechanism for selecting the best window subset by evaluating its quality using kernel ridge regression. Our experimental results demonstrate the superior performance of BWS compared to other baselines across a broad range of selection ratios over datasets, including CIFAR-10/100 and ImageNet, and the scenarios involving training from random initialization or fine-tuning of pre-trained models.