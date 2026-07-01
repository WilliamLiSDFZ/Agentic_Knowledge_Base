---
title: "Self-Labeling the Job Shop Scheduling Problem"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/be8987a75afeeadfa65007cf7ee25de0-Abstract-Conference.html"
categories: ['neural-combinatorial-optimization-and-learning', 'combinatorial-optimization-and-assembly-problems']
tags: ['self-supervised-learning', 'job-shop-scheduling', 'combinatorial-optimization']
venue: "NeurIPS 2024"
tldr: "A self-supervised training strategy for job shop scheduling eliminates the need for expensive exact solver labels by using generative models to produce self-consistent pseudo-targets."
---

# Self-Labeling the Job Shop Scheduling Problem

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/be8987a75afeeadfa65007cf7ee25de0-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/be8987a75afeeadfa65007cf7ee25de0-Abstract-Conference.html)

**TLDR**: A self-supervised training strategy for job shop scheduling eliminates the need for expensive exact solver labels by using generative models to produce self-consistent pseudo-targets.

## Abstract

This work proposes a self-supervised training strategy designed for combinatorial problems. An obstacle in applying supervised paradigms to such problems is the need for costly target solutions often produced with exact solvers. Inspired by semi- and self-supervised learning, we show that generative models can be trained by sampling multiple solutions and using the best one according to the problem objective as a pseudo-label. In this way, we iteratively improve the model generation capability by relying only on its self-supervision, eliminating the need for optimality information. We validate this Self-Labeling Improvement Method (SLIM) on the Job Shop Scheduling (JSP), a complex combinatorial problem that is receiving much attention from the neural combinatorial community. We propose a generative model based on the well-known Pointer Network and train it with SLIM. Experiments on popular benchmarks demonstrate the potential of this approach as the resulting models outperform constructive heuristics and state-of-the-art learning proposals for the JSP. Lastly, we prove the robustness of SLIM to various parameters and its generality by applying it to the Traveling Salesman Problem.