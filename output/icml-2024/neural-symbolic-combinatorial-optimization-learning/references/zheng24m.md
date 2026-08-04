---
title: "DPN: Decoupling Partition and Navigation for Neural Solvers of Min-max Vehicle Routing Problems"
source: "https://proceedings.mlr.press/v235/zheng24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24m/zheng24m.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['vehicle-routing', 'min-max-VRP', 'reinforcement-learning', 'neural-combinatorial-optimization']
venue: "ICML 2024"
tldr: "DPN decouples the partition and navigation subproblems in min-max VRP to improve neural solver efficiency and solution quality."
---

# DPN: Decoupling Partition and Navigation for Neural Solvers of Min-max Vehicle Routing Problems

**Source**: [https://proceedings.mlr.press/v235/zheng24m.html](https://proceedings.mlr.press/v235/zheng24m.html)

**TLDR**: DPN decouples the partition and navigation subproblems in min-max VRP to improve neural solver efficiency and solution quality.

## Abstract

The min-max vehicle routing problem (min-max VRP) traverses all given customers by assigning several routes and aims to minimize the length of the longest route. Recently, reinforcement learning (RL)-based sequential planning methods have exhibited advantages in solving efficiency and optimality. However, these methods fail to exploit the problem-specific properties in learning representations, resulting in less effective features for decoding optimal routes. This paper considers the sequential planning process of min-max VRPs as two coupled optimization tasks: customer partition for different routes and customer navigation in each route (i.e., partition and navigation). To effectively process min-max VRP instances, we present a novel attention-based Partition-and-Navigation encoder (P&N Encoder) that learns distinct embeddings for partition and navigation. Furthermore, we utilize an inherent symmetry in decoding routes and develop an effective agent-permutation-symmetric (APS) loss function. Experimental results demonstrate that the proposed Decoupling-Partition-Navigation (DPN) method significantly surpasses existing learning-based methods in both single-depot and multi-depot min-max VRPs. Our code is available at