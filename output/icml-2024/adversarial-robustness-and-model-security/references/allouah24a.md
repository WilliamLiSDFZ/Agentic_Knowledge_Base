---
title: "Byzantine-Robust Federated Learning: Impact of Client Subsampling and Local Updates"
source: "https://proceedings.mlr.press/v235/allouah24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/allouah24a/allouah24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'adversarial-robustness-and-model-security']
tags: ['Byzantine-robustness', 'federated-learning', 'client-subsampling']
venue: "ICML 2024"
tldr: "This paper analyzes how client subsampling and local updates affect Byzantine-robustness in federated learning with robust aggregation."
---

# Byzantine-Robust Federated Learning: Impact of Client Subsampling and Local Updates

**Source**: [https://proceedings.mlr.press/v235/allouah24a.html](https://proceedings.mlr.press/v235/allouah24a.html)

**TLDR**: This paper analyzes how client subsampling and local updates affect Byzantine-robustness in federated learning with robust aggregation.

## Abstract

The possibility of adversarial (a.k.a., Byzantine) clients makes federated learning (FL) prone to arbitrary manipulation. The natural approach to robustify FL against adversarial clients is to replace the simple averaging operation at the server in the standard $\mathsf{FedAvg}$ algorithm by a robust averaging rule. While a significant amount of work has been devoted to studying the convergence of federated robust averaging (which we denote by $\mathsf{FedRo}$), prior work has largely ignored the impact of client subsampling and local steps, two fundamental FL characteristics. While client subsampling increases the effective fraction of Byzantine clients, local steps increase the drift between the local updates computed by honest (i.e., non-Byzantine) clients. Consequently, a careless deployment of $\mathsf{FedRo}$ could yield poor performance. We validate this observation by presenting an in-depth analysis of $\mathsf{FedRo}$ tightly analyzing the impact of client subsampling and local steps. Specifically, we present a sufficient condition on client subsampling for nearly-optimal convergence of $\mathsf{FedRo}$ (for smooth non-convex loss). Also, we show that the rate of improvement in learning accuracy diminishes with respect to the number of clients subsampled, as soon as the sample size exceeds a threshold value. Interestingly, we also observe that under a careful choice of step-sizes, the learning error due to Byzantine clients decreases with the number of local steps. We validate our theory by experiments on the FEMNIST and CIFAR-$10$ image classification tasks.