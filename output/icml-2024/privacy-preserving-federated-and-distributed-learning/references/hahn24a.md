---
title: "Pursuing Overall Welfare in Federated Learning through Sequential Decision Making"
source: "https://proceedings.mlr.press/v235/hahn24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hahn24a/hahn24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'fairness', 'sequential-decision-making', 'aggregation', 'client-welfare']
venue: "ICML 2024"
tldr: "A sequential decision-making approach to federated learning aggregation that pursues overall client-level fairness."
---

# Pursuing Overall Welfare in Federated Learning through Sequential Decision Making

**Source**: [https://proceedings.mlr.press/v235/hahn24a.html](https://proceedings.mlr.press/v235/hahn24a.html)

**TLDR**: A sequential decision-making approach to federated learning aggregation that pursues overall client-level fairness.

## Abstract

In traditional federated learning, a single global model cannot perform equally well for all clients. Therefore, the need to achieve the client-level fairness in federated system has been emphasized, which can be realized by modifying the static aggregation scheme for updating the global model to an adaptive one, in response to the local signals of the participating clients. Our work reveals that existing fairness-aware aggregation strategies can be unified into an online convex optimization framework, in other words, a central server’s sequential decision making process. To enhance the decision making capability, we propose simple and intuitive improvements for suboptimal designs within existing methods, presenting $\texttt{AAggFF}$. Considering practical requirements, we further subdivide our method tailored for the cross-device and the cross-silo settings, respectively. Theoretical analyses guarantee sublinear regret upper bounds for both settings: $\mathcal{O}(\sqrt{T \log{K}})$ for the cross-device setting, and $\mathcal{O}(K \log{T})$ for the cross-silo setting, with $K$ clients and $T$ federation rounds. Extensive experiments demonstrate that the federated system equipped with $\texttt{AAggFF}$ achieves better degree of client-level fairness than existing methods in both practical settings.