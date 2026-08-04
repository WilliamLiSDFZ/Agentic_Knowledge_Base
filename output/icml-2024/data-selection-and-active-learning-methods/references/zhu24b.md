---
title: "Generative Active Learning for Long-tailed Instance Segmentation"
source: "https://proceedings.mlr.press/v235/zhu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24b/zhu24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['generative-active-learning', 'long-tailed-distribution', 'instance-segmentation']
venue: "ICML 2024"
tldr: "Proposes a generative active learning framework that selectively uses language-image generative models to augment long-tailed instance segmentation training data."
---

# Generative Active Learning for Long-tailed Instance Segmentation

**Source**: [https://proceedings.mlr.press/v235/zhu24b.html](https://proceedings.mlr.press/v235/zhu24b.html)

**TLDR**: Proposes a generative active learning framework that selectively uses language-image generative models to augment long-tailed instance segmentation training data.

## Abstract

Recently, large-scale language-image generative models have gained widespread attention and many works have utilized generated data from these models to further enhance the performance of perception tasks. However, not all generated data can positively impact downstream models, and these methods do not thoroughly explore how to better select and utilize generated data. On the other hand, there is still a lack of research oriented towards active learning on generated data. In this paper, we explore how to perform active learning specifically for generated data in the long-tailed instance segmentation task. Subsequently, we propose BSGAL, a new algorithm that estimates the contribution of the current batch-generated data based on gradient cache. BSGAL is meticulously designed to cater for unlimited generated data and complex downstream segmentation tasks. BSGAL outperforms the baseline approach and effectually improves the performance of long-tailed segmentation.