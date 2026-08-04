---
title: "Robustness of Deep Learning for Accelerated MRI: Benefits of Diverse Training Data"
source: "https://proceedings.mlr.press/v235/lin24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24h/lin24h.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'adversarial-robustness-and-model-security']
tags: ['MRI-reconstruction', 'deep-learning-robustness', 'training-data-diversity']
venue: "ICML 2024"
tldr: "A study showing that diverse training data improves deep learning robustness for accelerated MRI reconstruction under distribution shift."
---

# Robustness of Deep Learning for Accelerated MRI: Benefits of Diverse Training Data

**Source**: [https://proceedings.mlr.press/v235/lin24h.html](https://proceedings.mlr.press/v235/lin24h.html)

**TLDR**: A study showing that diverse training data improves deep learning robustness for accelerated MRI reconstruction under distribution shift.

## Abstract

Deep learning based methods for image reconstruction are state-of-the-art for a variety of imaging tasks. However, neural networks often perform worse if the training data differs significantly from the data they are applied to. For example, a model trained for accelerated magnetic resonance imaging (MRI) on one scanner performs worse on another scanner. In this work, we investigate the impact of the training data on a model’s performance and robustness for accelerated MRI. We find that models trained on the combination of various data distributions, such as those obtained from different MRI scanners and anatomies, exhibit robustness equal or superior to models trained on the best single distribution for a specific target distribution. Thus training on such diverse data tends to improve robustness. Furthermore, training on such a diverse dataset does not compromise in-distribution performance, i.e., a model trained on diverse data yields in-distribution performance at least as good as models trained on the more narrow individual distributions. Our results suggest that training a model for imaging on a variety of distributions tends to yield a more effective and robust model than maintaining separate models for individual distributions.