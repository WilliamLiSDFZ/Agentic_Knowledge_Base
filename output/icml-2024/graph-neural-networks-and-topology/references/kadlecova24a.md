---
title: "Surprisingly Strong Performance Prediction with Neural Graph Features"
source: "https://proceedings.mlr.press/v235/kadlecova24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kadlecova24a/kadlecova24a.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['neural-architecture-search', 'performance-prediction', 'graph-features']
venue: "ICML 2024"
tldr: "Demonstrates surprisingly strong NAS performance prediction using neural graph features without requiring expensive training data."
---

# Surprisingly Strong Performance Prediction with Neural Graph Features

**Source**: [https://proceedings.mlr.press/v235/kadlecova24a.html](https://proceedings.mlr.press/v235/kadlecova24a.html)

**TLDR**: Demonstrates surprisingly strong NAS performance prediction using neural graph features without requiring expensive training data.

## Abstract

Performance prediction has been a key part of the neural architecture search (NAS) process, allowing to speed up NAS algorithms by avoiding resource-consuming network training. Although many performance predictors correlate well with ground truth performance, they require training data in the form of trained networks. Recently, zero-cost proxies have been proposed as an efficient method to estimate network performance without any training. However, they are still poorly understood, exhibit biases with network properties, and their performance is limited. Inspired by the drawbacks of zero-cost proxies, we propose neural graph features (GRAF), simple to compute properties of architectural graphs. GRAF offers fast and interpretable performance prediction while outperforming zero-cost proxies and other common encodings. In combination with other zero-cost proxies, GRAF outperforms most existing performance predictors at a fraction of the cost.