---
title: "How to Leverage Diverse Demonstrations in Offline Imitation Learning"
source: "https://proceedings.mlr.press/v235/yue24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yue24c/yue24c.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'online-learning-and-sequential-decision-making']
tags: ['offline-imitation-learning', 'imperfect-demonstrations', 'behavior-extraction']
venue: "ICML 2024"
tldr: "A framework for leveraging diverse imperfect demonstrations in offline imitation learning by extracting positive behaviors from noisy data."
---

# How to Leverage Diverse Demonstrations in Offline Imitation Learning

**Source**: [https://proceedings.mlr.press/v235/yue24c.html](https://proceedings.mlr.press/v235/yue24c.html)

**TLDR**: A framework for leveraging diverse imperfect demonstrations in offline imitation learning by extracting positive behaviors from noisy data.

## Abstract

Offline Imitation Learning (IL) with imperfect demonstrations has garnered increasing attention owing to the scarcity of expert data in many real-world domains. A fundamental problem in this scenario is how to extract positive behaviors from noisy data. In general, current approaches to the problem select data building on state-action similarity to given expert demonstrations, neglecting precious information in (potentially abundant) diverse state-actions that deviate from expert ones. In this paper, we introduce a simple yet effective data selection method that identifies positive behaviors based on their resultant states - a more informative criterion enabling explicit utilization of dynamics information and effective extraction of both expert and beneficial diverse behaviors. Further, we devise a lightweight behavior cloning algorithm capable of leveraging the expert and selected data correctly. In the experiments, we evaluate our method on a suite of complex and high-dimensional offline IL benchmarks, including continuous-control and vision-based tasks. The results demonstrate that our method achieves state-of-the-art performance, outperforming existing methods on 20/21 benchmarks, typically by 2-5x, while maintaining a comparable runtime to Behavior Cloning (BC).