---
title: "AFBench: A Large-scale Benchmark for Airfoil Design"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/96bc329285d3f028dc5972d7146c7e2f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'neural-geometric-shape-representation-learning']
tags: ['airfoil-design', 'inverse-design', 'generative-models', 'benchmark', 'mechanical-design']
venue: "NeurIPS 2024"
tldr: "Introduces AFBench, a large-scale open-source benchmark dataset and evaluation suite for data-driven airfoil inverse design."
---

# AFBench: A Large-scale Benchmark for Airfoil Design

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/96bc329285d3f028dc5972d7146c7e2f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/96bc329285d3f028dc5972d7146c7e2f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces AFBench, a large-scale open-source benchmark dataset and evaluation suite for data-driven airfoil inverse design.

## Abstract

Data-driven generative models have emerged as promising approaches towards achieving efficient mechanical inverse design. However, due to prohibitively high cost in time and money, there is still lack of open-source and large-scale benchmarks in this field. It is mainly the case for airfoil inverse design, which requires to generate and edit diverse geometric-qualified  and aerodynamic-qualified airfoils following the multimodal instructions, \emph{i.e.,} dragging points and physical parameters. This paper presents the open-source endeavors in airfoil inverse design, \emph{AFBench}, including a large-scale dataset with 200 thousand airfoils and high-quality aerodynamic and geometric labels, two novel and practical airfoil inverse design tasks, \emph{i.e.,} conditional generation on multimodal physical parameters, controllable editing, and comprehensive metrics to evaluate various existing airfoil inverse design methods. Our aim is to establish \emph{AFBench} as an ecosystem for training and evaluating airfoil inverse design methods, with a specific focus on data-driven controllable inverse design models by multimodal instructions capable of bridging the gap between ideas and execution, the academic research and industrial applications. We have provided baseline models, comprehensive experimental observations, and analysis to accelerate future research. Our baseline model is trained on an RTX 3090 GPU within 16 hours. The codebase, datasets and benchmarks will be available at \url{https://hitcslj.github.io/afbench/}.