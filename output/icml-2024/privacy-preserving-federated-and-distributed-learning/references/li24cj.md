---
title: "Seesaw: Compensating for Nonlinear Reduction with Linear Computations for Private Inference"
source: "https://proceedings.mlr.press/v235/li24cj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cj/li24cj.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['private-inference', 'secure-computation', 'nonlinear-operations']
venue: "ICML 2024"
tldr: "Seesaw compensates for costly nonlinear computations in privacy-preserving machine learning using efficient linear approximations."
---

# Seesaw: Compensating for Nonlinear Reduction with Linear Computations for Private Inference

**Source**: [https://proceedings.mlr.press/v235/li24cj.html](https://proceedings.mlr.press/v235/li24cj.html)

**TLDR**: Seesaw compensates for costly nonlinear computations in privacy-preserving machine learning using efficient linear approximations.

## Abstract

With increasingly serious data privacy concerns and strict regulations, privacy-preserving machine learning (PPML) has emerged to securely execute machine learning tasks without violating privacy. Unfortunately, the computational cost to securely execute nonlinear computations in PPML remains significant, calling for new model architecture designs with fewer nonlinear operations. We propose Seesaw, a novel neural architecture search method tailored for PPML. Seesaw exploits a previously unexplored opportunity to leverage more linear computations and nonlinear result reuse, in order to compensate for the accuracy loss due to nonlinear reduction. It incorporates specifically designed pruning and search strategies, not only to efficiently handle the much larger design space of both linear and nonlinear operators, but also to achieve a better balance between the model accuracy and the online/offline execution latencies. Compared to the state-of-the-art design for image classification on ImageNet, Seesaw achieves 1.68$\times$ lower online latency and 1.55$\times$ lower total online + offline latency at 71% iso-accuracy, or 3.65% higher accuracy at iso-latency of 190 seconds, while using much simpler and faster search and training methods.