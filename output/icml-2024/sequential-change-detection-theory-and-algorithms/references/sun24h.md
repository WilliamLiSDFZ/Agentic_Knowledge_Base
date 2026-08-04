---
title: "Online Adaptive Anomaly Thresholding with Confidence Sequences"
source: "https://proceedings.mlr.press/v235/sun24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24h/sun24h.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'sequential-change-detection-theory-and-algorithms']
tags: ['anomaly-detection', 'adaptive-thresholding', 'confidence-sequences', 'distribution-shift', 'online-learning']
venue: "ICML 2024"
tldr: "An online adaptive anomaly thresholding method using confidence sequences is proposed to handle distribution shifts in unsupervised anomaly detection."
---

# Online Adaptive Anomaly Thresholding with Confidence Sequences

**Source**: [https://proceedings.mlr.press/v235/sun24h.html](https://proceedings.mlr.press/v235/sun24h.html)

**TLDR**: An online adaptive anomaly thresholding method using confidence sequences is proposed to handle distribution shifts in unsupervised anomaly detection.

## Abstract

Selecting appropriate thresholds for anomaly detection in online, unsupervised settings is a challenging task, especially in the presence of data distribution shifts. Addressing these challenges is critical in many practical large scale systems, such as infrastructure monitoring and network intrusion detection. This paper proposes an algorithm that connects online thresholding with constructing confidence sequences achieving (1) adaptive online threshold selection robust to distribution shifts, (2) statistical guarantees on false positive and false negative rates without any distributional assumptions, and (3) improved performance when given relevant offline data to warm-start the online algorithm, while having bounded degradation if the offline data is irrelevant. We complement our theoretical results by empirical evidence that our method outperforms commonly used baselines across synthetic and real world datasets.