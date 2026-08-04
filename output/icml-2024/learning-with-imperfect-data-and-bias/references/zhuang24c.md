---
title: "COALA: A Practical and Vision-Centric Federated Learning Platform"
source: "https://proceedings.mlr.press/v235/zhuang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhuang24c/zhuang24c.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['federated-learning', 'computer-vision', 'benchmarks', 'heterogeneity', 'platform']
venue: "ICML 2024"
tldr: "COALA is a vision-centric federated learning platform with benchmarks covering 15 computer vision tasks across task, data, and model heterogeneity levels."
---

# COALA: A Practical and Vision-Centric Federated Learning Platform

**Source**: [https://proceedings.mlr.press/v235/zhuang24c.html](https://proceedings.mlr.press/v235/zhuang24c.html)

**TLDR**: COALA is a vision-centric federated learning platform with benchmarks covering 15 computer vision tasks across task, data, and model heterogeneity levels.

## Abstract

We present COALA, a vision-centric Federated Learning (FL) platform, and a suite of benchmarks for practical FL scenarios, which we categorize as task, data, and model levels. At the task level, COALA extends support from simple classification to 15 computer vision tasks, including object detection, segmentation, pose estimation, and more. It also facilitates federated multiple-task learning, allowing clients to train on multiple tasks simultaneously. At the data level, COALA goes beyond supervised FL to benchmark both semi-supervised FL and unsupervised FL. It also benchmarks feature distribution shifts other than commonly considered label distribution shifts. In addition to dealing with static data, it supports federated continual learning for continuously changing data in real-world scenarios. At the model level, COALA benchmarks FL with split models and different models in different clients. COALA platform offers three degrees of customization for these practical FL scenarios, including configuration customization, components customization, and workflow customization. We conduct systematic benchmarking experiments for the practical FL scenarios and highlight potential opportunities for further advancements in FL.