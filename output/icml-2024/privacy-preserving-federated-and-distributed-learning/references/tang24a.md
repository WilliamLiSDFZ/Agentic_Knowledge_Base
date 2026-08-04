---
title: "Causally Motivated Personalized Federated Invariant Learning with Shortcut-Averse Information-Theoretic Regularization"
source: "https://proceedings.mlr.press/v235/tang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24a/tang24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'invariant-learning', 'spurious-correlations']
venue: "ICML 2024"
tldr: "A causally motivated personalized federated learning method uses information-theoretic regularization to mitigate shortcut learning under heterogeneous distributions."
---

# Causally Motivated Personalized Federated Invariant Learning with Shortcut-Averse Information-Theoretic Regularization

**Source**: [https://proceedings.mlr.press/v235/tang24a.html](https://proceedings.mlr.press/v235/tang24a.html)

**TLDR**: A causally motivated personalized federated learning method uses information-theoretic regularization to mitigate shortcut learning under heterogeneous distributions.

## Abstract

Exploiting invariant relations and mitigating spurious correlation (a.k.a., shortcut) between representation and target across varied data distributions can tackle the challenging out-of-distribution (OOD) generalization problem. In personalized federated learning (PFL), heterogeneous data distribution across local clients offers the inherent prerequisites to extract the invariant features that maintain invariant relation with target. Nevertheless, personalized features are closely entangled with spurious features in PFL since they exhibit similar variability across different clients, which makes preserving personalization knowledge and eliminating shortcuts two conflicting objectives in PFL. To address the above challenge, we analyse the heterogeneous data generation on local clients through the lens of structured causal model and propose a crucial causal signature which can distinguish personalized features from spurious features with global invariant features as the anchor. Then the causal signature is quantified as an information-theoretic constraint that facilitates the shortcut-averse personalized invariant learning on each client. Theoretical analysis demonstrates our method, FedPIN, can yield a tighter bound on generalization error than the prevalent PFL approaches when train-test distribution shift exists on clients. Moreover, we provide a theoretical guarantee on the convergence rate of FedPIN in this paper. The results of extensive experiments show that our method can achieve superior OOD generalization performance compared with the state-of-the-art competitors.