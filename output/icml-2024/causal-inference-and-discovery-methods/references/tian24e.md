---
title: "Towards the Theory of Unsupervised Federated Learning: Non-asymptotic Analysis of Federated EM Algorithms"
source: "https://proceedings.mlr.press/v235/tian24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tian24e/tian24e.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'causal-inference-and-discovery-methods']
tags: ['federated-EM', 'unsupervised-federated-learning', 'non-asymptotic-analysis']
venue: "ICML 2024"
tldr: "Non-asymptotic convergence guarantees are established for federated EM algorithms, providing theoretical foundations for unsupervised federated learning."
---

# Towards the Theory of Unsupervised Federated Learning: Non-asymptotic Analysis of Federated EM Algorithms

**Source**: [https://proceedings.mlr.press/v235/tian24e.html](https://proceedings.mlr.press/v235/tian24e.html)

**TLDR**: Non-asymptotic convergence guarantees are established for federated EM algorithms, providing theoretical foundations for unsupervised federated learning.

## Abstract

While supervised federated learning approaches have enjoyed significant success, the domain of unsupervised federated learning remains relatively underexplored. Several federated EM algorithms have gained popularity in practice, however, their theoretical foundations are often lacking. In this paper, we first introduce a federated gradient EM algorithm (FedGrEM) designed for the unsupervised learning of mixture models, which supplements the existing federated EM algorithms by considering task heterogeneity and potential adversarial attacks. We present a comprehensive finite-sample theory that holds for general mixture models, then apply this general theory on specific statistical models to characterize the explicit estimation error of model parameters and mixture proportions. Our theory elucidates when and how FedGrEM outperforms local single-task learning with insights extending to existing federated EM algorithms. This bridges the gap between their practical success and theoretical understanding. Our numerical results validate our theory, and demonstrate FedGrEM’s superiority over existing unsupervised federated learning benchmarks.