---
title: "FedCal: Achieving Local and Global Calibration in Federated Learning via Aggregated Parameterized Scaler"
source: "https://proceedings.mlr.press/v235/peng24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peng24g/peng24g.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['federated-learning', 'calibration', 'data-heterogeneity', 'aggregation', 'non-iid']
venue: "ICML 2024"
tldr: "Proposes FedCal, achieving both local and global calibration in federated learning via aggregated parameterized scalers under data heterogeneity."
---

# FedCal: Achieving Local and Global Calibration in Federated Learning via Aggregated Parameterized Scaler

**Source**: [https://proceedings.mlr.press/v235/peng24g.html](https://proceedings.mlr.press/v235/peng24g.html)

**TLDR**: Proposes FedCal, achieving both local and global calibration in federated learning via aggregated parameterized scalers under data heterogeneity.

## Abstract

Federated learning (FL) enables collaborative machine learning across distributed data owners, but data heterogeneity poses a challenge for model calibration. While prior work focused on improving accuracy for non-iid data, calibration remains under-explored. This study reveals existing FL aggregation approaches lead to sub-optimal calibration, and theoretical analysis shows despite constraining variance in clients’ label distributions, global calibration error is still asymptotically lower bounded. To address this, we propose a novel Federated Calibration (FedCal) approach, emphasizing both local and global calibration. It leverages client-specific scalers for local calibration to effectively correct output misalignment without sacrificing prediction accuracy. These scalers are then aggregated via weight averaging to generate a global scaler, minimizing the global calibration error. Extensive experiments demonstrate that FedCal significantly outperforms the best-performing baseline, reducing global calibration error by 47.66% on average.