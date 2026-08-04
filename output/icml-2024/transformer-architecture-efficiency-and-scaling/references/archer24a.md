---
title: "Practical Performance Guarantees for Pipelined DNN Inference"
source: "https://proceedings.mlr.press/v235/archer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/archer24a/archer24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'dynamic-algorithms-and-complexity-theory']
tags: ['pipeline-parallelism', 'DNN-inference', 'graph-partitioning', 'bottleneck-optimization']
venue: "ICML 2024"
tldr: "Provides practical algorithms and performance guarantees for pipelined DNN inference via optimal k-stage graph partitioning."
---

# Practical Performance Guarantees for Pipelined DNN Inference

**Source**: [https://proceedings.mlr.press/v235/archer24a.html](https://proceedings.mlr.press/v235/archer24a.html)

**TLDR**: Provides practical algorithms and performance guarantees for pipelined DNN inference via optimal k-stage graph partitioning.

## Abstract

We optimize pipeline parallelism for deep neural network (DNN) inference by partitioning model graphs into $k$ stages and minimizing the running time of the bottleneck stage, including communication. We give practical and effective algorithms for this NP-hard problem, but our emphasis is on tackling the practitioner’s dilemma of deciding when a solution is good enough. To this end, we design novel mixed integer programming (MIP) relaxations for proving lower bounds. Applying these methods to a diverse testbed of 369 production models, for $k \in \\{2, 4, 8, 16, 32, 64\\}$, we empirically show that these lower bounds are strong enough to be useful in practice. Our lower bounds are substantially stronger than standard combinatorial bounds. For example, evaluated via geometric means across a production testbed with $k = 16$ pipeline stages, our MIP formulations raise the lower bound from 0.4598 to 0.9452, expressed as a fraction of the best partition found. In other words, our improved lower bounds close the optimality gap by a factor of 9.855x.