---
title: "What Would Gauss Say About Representations? Probing Pretrained Image Models using Synthetic Gaussian Benchmarks"
source: "https://proceedings.mlr.press/v235/ko24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ko24a/ko24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'clustering-methods-and-multi-view-learning']
tags: ['representation-learning', 'pretrained-models', 'synthetic-benchmarks', 'Gaussian', 'probing']
venue: "ICML 2024"
tldr: "A synthetic Gaussian benchmark framework for probing and evaluating the quality of pretrained image model representations."
---

# What Would Gauss Say About Representations? Probing Pretrained Image Models using Synthetic Gaussian Benchmarks

**Source**: [https://proceedings.mlr.press/v235/ko24a.html](https://proceedings.mlr.press/v235/ko24a.html)

**TLDR**: A synthetic Gaussian benchmark framework for probing and evaluating the quality of pretrained image model representations.

## Abstract

Recent years have witnessed a paradigm shift in deep learning from task-centric model design to task-agnostic representation learning and task-specific fine-tuning. Pretrained model representations are commonly evaluated extensively across various real-world tasks and used as a foundation for different downstream tasks. This paper proposes a solution for assessing the quality of representations in a task-agnostic way. To circumvent the need for real-world data in evaluation, we explore the use of synthetic binary classification tasks with Gaussian mixtures to probe pretrained models and compare the robustness-accuracy performance on pretrained representations with an idealized reference. Our approach offers a holistic evaluation, revealing intrinsic model capabilities and reducing the dependency on real-life data for model evaluation. Evaluated with various pretrained image models, the experimental results confirm that our task-agnostic evaluation correlates with actual linear probing performance on downstream tasks and can also guide parameter choice in robust linear probing to achieve a better robustness-accuracy trade-off.