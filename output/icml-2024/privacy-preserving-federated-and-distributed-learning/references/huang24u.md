---
title: "Self-Driven Entropy Aggregation for Byzantine-Robust Heterogeneous Federated Learning"
source: "https://proceedings.mlr.press/v235/huang24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24u/huang24u.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'adversarial-robustness-and-model-security']
tags: ['federated-learning', 'byzantine-robustness', 'entropy-aggregation']
venue: "ICML 2024"
tldr: "Proposes self-driven entropy aggregation to defend against Byzantine attacks in heterogeneous federated learning settings."
---

# Self-Driven Entropy Aggregation for Byzantine-Robust Heterogeneous Federated Learning

**Source**: [https://proceedings.mlr.press/v235/huang24u.html](https://proceedings.mlr.press/v235/huang24u.html)

**TLDR**: Proposes self-driven entropy aggregation to defend against Byzantine attacks in heterogeneous federated learning settings.

## Abstract

Federated learning presents massive potential for privacy-friendly collaboration. However, the performance of federated learning is deeply affected by byzantine attacks, where malicious clients deliberately upload crafted vicious updates. While various robust aggregations have been proposed to defend against such attacks, they are subject to certain assumptions: homogeneous private data and related proxy datasets. To address these limitations, we propose Self-Driven Entropy Aggregation (SDEA), which leverages the random public dataset to conduct Byzantine-robust aggregation in heterogeneous federated learning. For Byzantine attackers, we observe that benign ones typically present more confident (sharper) predictions than evils on the public dataset. Thus, we highlight benign clients by introducing learnable aggregation weight to minimize the instance-prediction entropy of the global model on the random public dataset. Besides, with inherent data heterogeneity in federated learning, we reveal that it brings heterogeneous sharpness. Specifically, clients are optimized under distinct distribution and thus present fruitful predictive preferences. The learnable aggregation weight blindly allocates high attention to limited ones for sharper predictions, resulting in a biased global model. To alleviate this problem, we encourage the global model to offer diverse predictions via batch-prediction entropy maximization and conduct clustering to equally divide honest weights to accommodate different tendencies. This endows SDEA to detect Byzantine attackers in heterogeneous federated learning. Empirical results demonstrate the effectiveness.