---
title: "Online Isolation Forest"
source: "https://proceedings.mlr.press/v235/leveni24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/leveni24a/leveni24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'online-learning-and-sequential-decision-making']
tags: ['anomaly-detection', 'online-learning', 'isolation-forest', 'data-streams', 'unsupervised']
venue: "ICML 2024"
tldr: "Extends Isolation Forest to an online streaming setting, addressing practical constraints of offline anomaly detection methods."
---

# Online Isolation Forest

**Source**: [https://proceedings.mlr.press/v235/leveni24a.html](https://proceedings.mlr.press/v235/leveni24a.html)

**TLDR**: Extends Isolation Forest to an online streaming setting, addressing practical constraints of offline anomaly detection methods.

## Abstract

The anomaly detection literature is abundant with offline methods, which require repeated access to data in memory, and impose impractical assumptions when applied to a streaming context. Existing online anomaly detection methods also generally fail to address these constraints, resorting to periodic retraining to adapt to the online context. We propose Online-iForest, a novel method explicitly designed for streaming conditions that seamlessly tracks the data generating process as it evolves over time. Experimental validation on real-world datasets demonstrated that Online-iForest is on par with online alternatives and closely rivals state-of-the-art offline anomaly detection techniques that undergo periodic retraining. Notably, Online-iForest consistently outperforms all competitors in terms of efficiency, making it a promising solution in applications where fast identification of anomalies is of primary importance such as cybersecurity, fraud and fault detection.