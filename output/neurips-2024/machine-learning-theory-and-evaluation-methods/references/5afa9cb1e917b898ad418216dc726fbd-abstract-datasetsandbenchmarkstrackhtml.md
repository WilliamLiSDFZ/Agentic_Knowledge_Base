---
title: "Benchmarking Uncertainty Disentanglement: Specialized Uncertainties for Specialized Tasks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5afa9cb1e917b898ad418216dc726fbd-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['uncertainty-quantification', 'disentanglement', 'out-of-distribution-detection']
venue: "NeurIPS 2024"
tldr: "Benchmarks uncertainty disentanglement methods across specialized tasks including abstained prediction and aleatoric uncertainty quantification."
---

# Benchmarking Uncertainty Disentanglement: Specialized Uncertainties for Specialized Tasks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5afa9cb1e917b898ad418216dc726fbd-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5afa9cb1e917b898ad418216dc726fbd-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Benchmarks uncertainty disentanglement methods across specialized tasks including abstained prediction and aleatoric uncertainty quantification.

## Abstract

Uncertainty quantification, once a singular task, has evolved into a spectrum of tasks, including abstained prediction, out-of-distribution detection, and aleatoric uncertainty quantification. The latest goal is disentanglement: the construction of multiple estimators that are each tailored to one and only one source of uncertainty. This paper presents the first benchmark of uncertainty disentanglement. We reimplement and evaluate a comprehensive range of uncertainty estimators, from Bayesian over evidential to deterministic ones, across a diverse range of uncertainty tasks on ImageNet. We find that, despite recent theoretical endeavors, no existing approach provides pairs of disentangled uncertainty estimators in practice. We further find that specialized uncertainty tasks are harder than predictive uncertainty tasks, where we observe saturating performance. Our results provide both practical advice for which uncertainty estimators to use for which specific task, and reveal opportunities for future research toward task-centric and disentangled uncertainties. All our reimplementations and Weights & Biases logs are available at https://github.com/bmucsanyi/untangle.