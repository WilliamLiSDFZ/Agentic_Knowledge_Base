---
title: "AegisFL: Efficient and Flexible Privacy-Preserving Byzantine-Robust Cross-silo Federated Learning"
source: "https://proceedings.mlr.press/v235/chen24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ag/chen24ag.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'adversarial-robustness-and-model-security']
tags: ['federated-learning', 'homomorphic-encryption', 'Byzantine-robustness', 'privacy']
venue: "ICML 2024"
tldr: "Introduces AegisFL, an efficient privacy-preserving federated learning framework that simultaneously defends against privacy and poisoning attacks using improved homomorphic encryption."
---

# AegisFL: Efficient and Flexible Privacy-Preserving Byzantine-Robust Cross-silo Federated Learning

**Source**: [https://proceedings.mlr.press/v235/chen24ag.html](https://proceedings.mlr.press/v235/chen24ag.html)

**TLDR**: Introduces AegisFL, an efficient privacy-preserving federated learning framework that simultaneously defends against privacy and poisoning attacks using improved homomorphic encryption.

## Abstract

Privacy attacks and poisoning attacks are two of the thorniest problems in federation learning (FL). Homomorphic encryption (HE), which allows certain mathematical operations to be done in the ciphertext state, provides a way to solve these two problems simultaneously. However, existing Paillier-based and CKKS-based privacy-preserving byzantine-robust FL (PBFL) solutions not only suffer from low efficiency but also expose the final model to the server. Additionally, these methods are limited to one robust aggregation algorithm (AGR) and are therefore vulnerable to AGR-tailored poisoning attacks. In this paper, we present AegisFL, an efficient PBLF system that provides the flexibility to change the AGR. We first observe that the core of the existing advanced AGRs is to calculate the inner products, $L_2$ norms and mean values for vectors. Based on this observation, we tailor a packing scheme for PBFL, which fits perfectly with RLWE-based fully homomorphic encryption. Under this packing scheme, the server only needs to perform one ciphertext multiplication to construct any required AGR, while the global model only belongs to honest clients. Finally, we conduct extensive experiments on different datasets and adversary settings, which also confirm the effectiveness and efficiency of our scheme.