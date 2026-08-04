---
title: "Hierarchical Novelty Detection via Fine-Grained Evidence Allocation"
source: "https://proceedings.mlr.press/v235/pyakurel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pyakurel24a/pyakurel24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'clustering-methods-and-multi-view-learning']
tags: ['novelty-detection', 'hierarchical-classification', 'OOD-detection']
venue: "ICML 2024"
tldr: "A hierarchical novelty detection method that allocates fine-grained evidence to pair novel samples with their closest known parent class."
---

# Hierarchical Novelty Detection via Fine-Grained Evidence Allocation

**Source**: [https://proceedings.mlr.press/v235/pyakurel24a.html](https://proceedings.mlr.press/v235/pyakurel24a.html)

**TLDR**: A hierarchical novelty detection method that allocates fine-grained evidence to pair novel samples with their closest known parent class.

## Abstract

By leveraging a hierarchical structure of known classes, Hierarchical Novelty Detection (HND) offers fine-grained detection results that pair detected novel samples with their closest (known) parent class in the hierarchy. Prior knowledge on the parent class provides valuable insights to better understand these novel samples. However, traditional novelty detection methods try to separate novel samples from all known classes using uncertainty or distance based metrics so they are incapable of locating the closest known parent class. Since the novel class is also part of the hierarchy, the model can more easily get confused between samples from known classes and those from novel ones. To achieve effective HND, we propose to augment the known (leaf-level) classes with a set of novel classes, each of which is associated with one parent (i.e., non-leaf) class in the original hierarchy. Such a structure allows us to perform novel fine-grained evidence allocation to differentiate known and novel classes guided by a uniquely designed loss function. Our thorough theoretical analysis shows that fine-grained evidence allocation creates an evidence margin to more precisely separate known and novel classes. Extensive experiments conducted on real-world hierarchical datasets demonstrate the proposed model outperforms the strongest baselines and achieves the best HND performance.