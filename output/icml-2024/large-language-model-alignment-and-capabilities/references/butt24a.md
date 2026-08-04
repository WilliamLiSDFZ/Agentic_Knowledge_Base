---
title: "CodeIt: Self-Improving Language Models with Prioritized Hindsight Replay"
source: "https://proceedings.mlr.press/v235/butt24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/butt24a/butt24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'continual-learning-memory-plasticity']
tags: ['self-improvement', 'hindsight-replay', 'ARC-benchmark', 'program-synthesis']
venue: "ICML 2024"
tldr: "CodeIt is a self-improving LLM framework using prioritized hindsight replay to tackle abstract reasoning benchmarks like ARC."
---

# CodeIt: Self-Improving Language Models with Prioritized Hindsight Replay

**Source**: [https://proceedings.mlr.press/v235/butt24a.html](https://proceedings.mlr.press/v235/butt24a.html)

**TLDR**: CodeIt is a self-improving LLM framework using prioritized hindsight replay to tackle abstract reasoning benchmarks like ARC.

## Abstract

Large language models are increasingly solving tasks that are commonly believed to require human-level reasoning ability. However, these models still perform very poorly on benchmarks of general intelligence such as the Abstraction and Reasoning Corpus (ARC). In this paper, we approach the ARC as a programming-by-examples problem, and introduce a novel and scalable method for language model self-improvement called Code Iteration (CodeIt). Our method iterates between 1) program sampling and hindsight relabeling, and 2) learning from prioritized experience replay. By relabeling the goal of an episode (i.e., the program output given input) to the output actually produced by the sampled program, our method effectively deals with the extreme sparsity of rewards in program synthesis. Applying CodeIt to the ARC dataset, we demonstrate that prioritized hindsight replay, along with pre-training and data-augmentation, leads to successful inter-task generalization. CodeIt is the first neuro-symbolic approach that scales to the full ARC evaluation dataset. Our method solves 15% of ARC evaluation tasks, achieving state-of-the-art performance and outperforming existing neural and symbolic baselines. Our code is available at https://github.com/Qualcomm-AI-research/codeit.