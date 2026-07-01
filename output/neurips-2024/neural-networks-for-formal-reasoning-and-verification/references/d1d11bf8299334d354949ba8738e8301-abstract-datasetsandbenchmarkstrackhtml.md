---
title: "A Neuro-Symbolic Benchmark Suite for Concept Quality and Reasoning Shortcuts"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d1d11bf8299334d354949ba8738e8301-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'neural-networks-for-formal-reasoning-and-verification']
tags: ['neuro-symbolic', 'benchmark', 'reasoning-shortcuts', 'concept-quality', 'learning-and-reasoning']
venue: "NeurIPS 2024"
tldr: "Introduces a neuro-symbolic benchmark suite to evaluate concept quality and diagnose reasoning shortcuts in models that combine learning and logical reasoning."
---

# A Neuro-Symbolic Benchmark Suite for Concept Quality and Reasoning Shortcuts

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d1d11bf8299334d354949ba8738e8301-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d1d11bf8299334d354949ba8738e8301-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a neuro-symbolic benchmark suite to evaluate concept quality and diagnose reasoning shortcuts in models that combine learning and logical reasoning.

## Abstract

The advent of powerful neural classifiers has increased interest in problems that require both learning and reasoning.These problems are critical for understanding important properties of models, such as trustworthiness, generalization, interpretability, and compliance to safety and structural constraints. However, recent research observed that tasks requiring both learning and reasoning on background knowledge often suffer from reasoning shortcuts (RSs): predictors can solve the downstream reasoning task without associating the correct concepts to the high-dimensional data. To address this issue, we introduce rsbench, a comprehensive benchmark suite designed to systematically evaluate the impact of RSs on models by providing easy access to highly customizable tasks affected by RSs. Furthermore, rsbench implements common metrics for evaluating concept quality and introduces novel formal verification procedures for assessing the presence of RSs in learning tasks. Using rsbench, we highlight that obtaining high quality concepts in both purely neural and neuro-symbolic models is a far-from-solved problem. rsbench is available at: https://unitn-sml.github.io/rsbench.