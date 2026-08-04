---
title: "Locally Differentially Private Decentralized Stochastic Bilevel Optimization with Guaranteed Convergence Accuracy"
source: "https://proceedings.mlr.press/v235/chen24ap.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ap/chen24ap.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['differential-privacy', 'decentralized-optimization', 'bilevel-optimization', 'convergence']
venue: "ICML 2024"
tldr: "Develops a locally differentially private decentralized stochastic bilevel optimization algorithm with guaranteed convergence accuracy."
---

# Locally Differentially Private Decentralized Stochastic Bilevel Optimization with Guaranteed Convergence Accuracy

**Source**: [https://proceedings.mlr.press/v235/chen24ap.html](https://proceedings.mlr.press/v235/chen24ap.html)

**TLDR**: Develops a locally differentially private decentralized stochastic bilevel optimization algorithm with guaranteed convergence accuracy.

## Abstract

Decentralized bilevel optimization based machine learning techniques are achieving remarkable success in a wide variety of domains. However, the intensive exchange of information (involving nested-loops of consensus or communication iterations) in existing decentralized bilevel optimization algorithms leads to a great challenge to ensure rigorous differential privacy, which, however, is necessary to bring the benefits of machine learning to domains where involved data are sensitive. By proposing a new decentralized stochastic bilevel-optimization algorithm which avoids nested-loops of information-exchange iterations, we achieve, for the first time, both differential privacy and accurate convergence in decentralized bilevel optimization. This is significant since even for single-level decentralized optimization and learning, existing differential-privacy solutions have to sacrifice convergence accuracy for privacy. Besides characterizing the convergence rate under nonconvex/convex/strongly convex conditions, we also rigorously quantify the price of differential privacy in the convergence rate. Experimental results on machine learning models confirm the efficacy of our algorithm.