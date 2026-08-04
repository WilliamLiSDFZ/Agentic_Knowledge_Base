---
title: "MaSS: Multi-attribute Selective Suppression for Utility-preserving Data Transformation from an Information-theoretic Perspective"
source: "https://proceedings.mlr.press/v235/chen24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24f/chen24f.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'fairness-aware-algorithmic-decision-making']
tags: ['attribute-suppression', 'information-theoretic', 'privacy', 'data-transformation']
venue: "ICML 2024"
tldr: "An information-theoretic framework for selectively suppressing sensitive attributes from data while preserving utility for downstream tasks."
---

# MaSS: Multi-attribute Selective Suppression for Utility-preserving Data Transformation from an Information-theoretic Perspective

**Source**: [https://proceedings.mlr.press/v235/chen24f.html](https://proceedings.mlr.press/v235/chen24f.html)

**TLDR**: An information-theoretic framework for selectively suppressing sensitive attributes from data while preserving utility for downstream tasks.

## Abstract

The growing richness of large-scale datasets has been crucial in driving the rapid advancement and wide adoption of machine learning technologies. The massive collection and usage of data, however, pose an increasing risk for people’s private and sensitive information due to either inadvertent mishandling or malicious exploitation. Besides legislative solutions, many technical approaches have been proposed towards data privacy protection. However, they bear various limitations such as leading to degraded data availability and utility, or relying on heuristics and lacking solid theoretical bases. To overcome these limitations, we propose a formal information-theoretic definition for this utility-preserving privacy protection problem, and design a data-driven learnable data transformation framework that is capable of selectively suppressing sensitive attributes from target datasets while preserving the other useful attributes, regardless of whether or not they are known in advance or explicitly annotated for preservation. We provide rigorous theoretical analyses on the operational bounds for our framework, and carry out comprehensive experimental evaluations using datasets of a variety of modalities, including facial images, voice audio clips, and human activity motion sensor signals. Results demonstrate the effectiveness and generalizability of our method under various configurations on a multitude of tasks. Our source code is available at this URL.