---
title: "LibMOON: A Gradient-based MultiObjective OptimizatioN Library in PyTorch"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/03ce71224741e6596059b8680a62978b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'multi-task-learning-group-optimization']
tags: ['multiobjective-optimization', 'pareto-front', 'pytorch-library']
venue: "NeurIPS 2024"
tldr: "LibMOON is a PyTorch library providing gradient-based solvers for multiobjective optimization problems with applications in multi-task and fair ML."
---

# LibMOON: A Gradient-based MultiObjective OptimizatioN Library in PyTorch

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/03ce71224741e6596059b8680a62978b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/03ce71224741e6596059b8680a62978b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: LibMOON is a PyTorch library providing gradient-based solvers for multiobjective optimization problems with applications in multi-task and fair ML.

## Abstract

Multiobjective optimization problems (MOPs) are prevalent in machine learning, with applications in multi-task learning, learning under fairness or robustness constraints, etc. Instead of reducing multiple objective functions into a scalar objective, MOPs aim to optimize for the so-called Pareto optimality or Pareto set learning, which involves optimizing more than one objective function simultaneously, over models with thousands to millions of parameters. Existing benchmark libraries for MOPs mainly focus on evolutionary algorithms, most of which are zeroth-order or meta-heuristic methods that do not effectively utilize higher-order information from objectives and cannot scale to large-scale models with millions of parameters. In light of the above challenges, this paper introduces \algoname, the first multiobjective optimization library that supports state-of-the-art gradient-based methods, provides a fair and comprehensive benchmark, and is open-sourced for the community.