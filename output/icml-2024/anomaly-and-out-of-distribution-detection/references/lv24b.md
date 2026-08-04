---
title: "Contamination-Resilient Anomaly Detection via Adversarial Learning on Partially-Observed Normal and Anomalous Data"
source: "https://proceedings.mlr.press/v235/lv24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lv24b/lv24b.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'adversarial-robustness-and-model-security']
tags: ['anomaly-detection', 'data-contamination', 'adversarial-learning', 'partial-labels']
venue: "ICML 2024"
tldr: "A contamination-resilient anomaly detection method using adversarial learning on partially-observed normal and anomalous data."
---

# Contamination-Resilient Anomaly Detection via Adversarial Learning on Partially-Observed Normal and Anomalous Data

**Source**: [https://proceedings.mlr.press/v235/lv24b.html](https://proceedings.mlr.press/v235/lv24b.html)

**TLDR**: A contamination-resilient anomaly detection method using adversarial learning on partially-observed normal and anomalous data.

## Abstract

Many existing anomaly detection methods assume the availability of a large-scale normal dataset. But for many applications, limited by resources, removing all anomalous samples from a large un-labeled dataset is unrealistic, resulting in contaminated datasets. To detect anomalies accurately under such scenarios, from the probabilistic perspective, the key question becomes how to learn the normal-data distribution from a contaminated dataset. To this end, we propose to collect two additional small datasets that are comprised of partially-observed normal and anomaly samples, and then use them to help learn the distribution under an adversarial learning scheme. We prove that under some mild conditions, the proposed method is able to learn the correct normal-data distribution. Then, we consider the overfitting issue caused by the small size of the two additional datasets, and a correctness-guaranteed flipping mechanism is further developed to alleviate it. Theoretical results under incomplete observed anomaly types are also presented. Extensive experimental results demonstrate that our method outperforms representative baselines when detecting anomalies under contaminated datasets.