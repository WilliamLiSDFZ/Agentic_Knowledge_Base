---
title: "Integrated Hardware Architecture and Device Placement Search"
source: "https://proceedings.mlr.press/v235/wang24bp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bp/wang24bp.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['hardware-architecture-search', 'device-placement', 'distributed-training', 'co-optimization']
venue: "ICML 2024"
tldr: "First work to jointly optimize hardware accelerator architecture and device placement strategy for distributed deep learning training."
---

# Integrated Hardware Architecture and Device Placement Search

**Source**: [https://proceedings.mlr.press/v235/wang24bp.html](https://proceedings.mlr.press/v235/wang24bp.html)

**TLDR**: First work to jointly optimize hardware accelerator architecture and device placement strategy for distributed deep learning training.

## Abstract

Distributed execution of deep learning training involves a dynamic interplay between hardware accelerator architecture and device placement strategy. This is the first work to explore the co-optimization of determining the optimal architecture and device placement strategy through novel algorithms, improving the balance of computational resources, memory usage, and data distribution. Our architecture search leverages tensor and vector units, determining their quantity and dimensionality, and on-chip and off-chip memory configurations. It also determines the microbatch size and decides whether to recompute or stash activations, balancing the memory footprint of training and storage size. For each explored architecture configuration, we use an Integer Linear Program (ILP) to find the optimal schedule for executing operators on the accelerator. The ILP results then integrate with a dynamic programming solution to identify the most effective device placement strategy, combining data, pipeline, and tensor model parallelism across multiple accelerators. Our approach achieves higher throughput on large language models compared to the state-of-the-art TPUv4 and the Spotlight accelerator search framework. The entire source code of PHAZE is available at https://github.com/msr-fiddle/phaze.