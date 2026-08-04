---
title: "Effective Federated Graph Matching"
source: "https://proceedings.mlr.press/v235/zhou24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24v/zhou24v.pdf"
categories: ['graph-clustering-and-matching-algorithms', 'privacy-preserving-federated-and-distributed-learning']
tags: ['federated-learning', 'graph-matching', 'privacy-preserving']
venue: "ICML 2024"
tldr: "Proposes UFGM, an unsupervised federated graph matching algorithm that infers matched node pairs across clients while preserving privacy using graphlet theory."
---

# Effective Federated Graph Matching

**Source**: [https://proceedings.mlr.press/v235/zhou24v.html](https://proceedings.mlr.press/v235/zhou24v.html)

**TLDR**: Proposes UFGM, an unsupervised federated graph matching algorithm that infers matched node pairs across clients while preserving privacy using graphlet theory.

## Abstract

Graph matching in the setting of federated learning is still an open problem. This paper proposes an unsupervised federated graph matching algorithm, UFGM, for inferring matched node pairs on different graphs across clients while maintaining privacy requirement, by leveraging graphlet theory and trust region optimization. First, the nodes’ graphlet features are captured to generate pseudo matched node pairs on different graphs across clients as pseudo training data for tackling the dilemma of unsupervised graph matching in federated setting and leveraging the strength of supervised graph matching. An approximate graphlet enumeration method is proposed to sample a small number of graphlets and capture nodes’ graphlet features. Theoretical analysis is conducted to demonstrate that the approximate method is able to maintain the quality of graphlet estimation while reducing its expensive cost. Second, we propose a separate trust region algorithm for pseudo supervised federated graph matching while maintaining the privacy constraints. In order to avoid expensive cost of the second-order Hessian computation in the trust region algorithm, we propose two weak quasi-Newton conditions to construct a positive definite scalar matrix as the Hessian approximation with only first-order gradients. We theoretically derive the error introduced by the separate trust region due to the Hessian approximation and conduct the convergence analysis of the approximation method.