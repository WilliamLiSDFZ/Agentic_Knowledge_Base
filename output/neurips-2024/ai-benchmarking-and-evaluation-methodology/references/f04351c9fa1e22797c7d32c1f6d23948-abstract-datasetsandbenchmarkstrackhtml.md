---
title: "Benchmarking Counterfactual Image Generation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f04351c9fa1e22797c7d32c1f6d23948-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['counterfactual-image-generation', 'causal-image-editing', 'benchmark']
venue: "NeurIPS 2024"
tldr: "A benchmark for evaluating counterfactual image generation that assesses whether edits respect causal relationships inherent to the data domain."
---

# Benchmarking Counterfactual Image Generation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f04351c9fa1e22797c7d32c1f6d23948-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f04351c9fa1e22797c7d32c1f6d23948-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark for evaluating counterfactual image generation that assesses whether edits respect causal relationships inherent to the data domain.

## Abstract

Generative AI has revolutionised visual content editing, empowering users to effortlessly modify images and videos. However, not all edits are equal. To perform realistic edits in domains such as natural image or medical imaging, modifications must respect causal relationships inherent to the data generation process. Such image editing falls into the counterfactual image generation regime. Evaluating counterfactual image generation is substantially complex: not only it lacks observable ground truths, but also requires adherence to causal constraints. Although several counterfactual image generation methods and evaluation metrics exist a comprehensive comparison within a unified setting is lacking. We present a comparison framework to thoroughly benchmark counterfactual image generation methods. We evaluate the performance of three conditional image generation model families developed within the Structural Causal Model (SCM) framework. We incorporate several metrics that assess diverse aspects of counterfactuals, such as composition, effectiveness, minimality of interventions, and image realism. We integrate all models that have been used for the task at hand and expand them to novel datasets and causal graphs, demonstrating the superiority of Hierarchical VAEs across most datasets and metrics. Our framework is implemented in a user-friendly Python package that can be extended to incorporate additional SCMs, causal methods, generative models, and datasets for the community to build on. Code: https://github.com/gulnazaki/counterfactual-benchmark.