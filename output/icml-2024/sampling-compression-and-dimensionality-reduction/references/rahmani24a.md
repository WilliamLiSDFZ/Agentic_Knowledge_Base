---
title: "Fundamental Limits of Distributed Covariance Matrix Estimation Under Communication Constraints"
source: "https://proceedings.mlr.press/v235/rahmani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rahmani24a/rahmani24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'privacy-preserving-federated-and-distributed-learning']
tags: ['covariance-estimation', 'communication-constraints', 'distributed-learning', 'high-dimensional-statistics', 'fundamental-limits']
venue: "ICML 2024"
tldr: "Establishes fundamental limits for distributed high-dimensional covariance matrix estimation under communication constraints."
---

# Fundamental Limits of Distributed Covariance Matrix Estimation Under Communication Constraints

**Source**: [https://proceedings.mlr.press/v235/rahmani24a.html](https://proceedings.mlr.press/v235/rahmani24a.html)

**TLDR**: Establishes fundamental limits for distributed high-dimensional covariance matrix estimation under communication constraints.

## Abstract

Estimating high-dimensional covariance matrices is crucial in various domains. This work considers a scenario where two collaborating agents access disjoint dimensions of $m$ samples from a high–dimensional random vector, and they can only communicate a limited number of bits to a central server, which wants to accurately approximate the covariance matrix. We analyze the fundamental trade–off between communication cost, number of samples, and estimation accuracy. We prove a lower bound on the error achievable by any estimator, highlighting the impact of dimensions, number of samples, and communication budget. Furthermore, we present an algorithm that achieves this lower bound up to a logarithmic factor, demonstrating its near-optimality in practical settings.