---
title: "Cross-domain Open-world Discovery"
source: "https://proceedings.mlr.press/v235/wen24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wen24b/wen24b.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'test-time-adaptation-methods-and-evaluation']
tags: ['open-world-discovery', 'novel-class-detection', 'distribution-shift', 'domain-adaptation']
venue: "ICML 2024"
tldr: "A method that simultaneously handles novel class discovery and feature distribution shifts during test-time in cross-domain open-world settings."
---

# Cross-domain Open-world Discovery

**Source**: [https://proceedings.mlr.press/v235/wen24b.html](https://proceedings.mlr.press/v235/wen24b.html)

**TLDR**: A method that simultaneously handles novel class discovery and feature distribution shifts during test-time in cross-domain open-world settings.

## Abstract

In many real-world applications, test data may commonly exhibit categorical shifts, characterized by the emergence of novel classes, as well as distribution shifts arising from feature distributions different from the ones the model was trained on. However, existing methods either discover novel classes in the open-world setting or assume domain shifts without the ability to discover novel classes. In this work, we consider a cross-domain open-world discovery setting, where the goal is to assign samples to seen classes and discover unseen classes under a domain shift. To address this challenging problem, we present CROW, a prototype-based approach that introduces a cluster-then-match strategy enabled by a well-structured representation space of foundation models. In this way, CROW discovers novel classes by robustly matching clusters with previously seen classes, followed by fine-tuning the representation space using an objective designed for cross-domain open-world discovery. Extensive experimental results on image classification benchmark datasets demonstrate that CROW outperforms alternative baselines, achieving an 8% average performance improvement across 75 experimental settings.