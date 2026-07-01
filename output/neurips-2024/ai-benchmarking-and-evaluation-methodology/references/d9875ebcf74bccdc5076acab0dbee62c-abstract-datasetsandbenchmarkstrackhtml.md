---
title: "APEBench: A Benchmark for Autoregressive Neural Emulators of PDEs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d9875ebcf74bccdc5076acab0dbee62c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['physics-informed-neural-operators-and-simulations', 'ai-benchmarking-and-evaluation-methodology']
tags: ['pde-emulation', 'autoregressive-models', 'jax-benchmark']
venue: "NeurIPS 2024"
tldr: "APEBench is a JAX-based benchmark suite for evaluating autoregressive neural emulators of PDEs with integrated differentiable simulation."
---

# APEBench: A Benchmark for Autoregressive Neural Emulators of PDEs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d9875ebcf74bccdc5076acab0dbee62c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d9875ebcf74bccdc5076acab0dbee62c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: APEBench is a JAX-based benchmark suite for evaluating autoregressive neural emulators of PDEs with integrated differentiable simulation.

## Abstract

We introduce the Autoregressive PDE Emulator Benchmark (APEBench),  a comprehensive benchmark suite to evaluate autoregressive neural emulators for solving partial differential equations. APEBench is based on JAX and provides a seamlessly integrated differentiable simulation framework employing efficient pseudo-spectral methods, enabling 46 distinct PDEs across 1D, 2D, and 3D. Facilitating systematic analysis and comparison of learned emulators, we propose a novel taxonomy for unrolled training and introduce a unique identifier for PDE dynamics that directly relates to the stability criteria of classical numerical methods. APEBench enables the evaluation of diverse neural architectures, and unlike existing benchmarks, its tight integration of the solver enables support for differentiable physics training and neural-hybrid emulators. Moreover, APEBench emphasizes rollout metrics to understand temporal generalization, providing insights into the long-term behavior of emulating PDE dynamics. In several experiments, we highlight the similarities between neural emulators and numerical simulators. The code is available at github.com/tum-pbs/apebench and APEBench can be installed via pip install apebench.