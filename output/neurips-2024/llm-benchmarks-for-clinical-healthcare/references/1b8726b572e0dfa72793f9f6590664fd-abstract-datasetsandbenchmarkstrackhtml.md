---
title: "Touchstone Benchmark: Are We on the Right Way for Evaluating AI Algorithms for Medical Segmentation?"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1b8726b572e0dfa72793f9f6590664fd-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-benchmarks-for-clinical-healthcare']
tags: ['medical-segmentation', 'benchmarking', 'evaluation-methodology', 'AI-performance']
venue: "NeurIPS 2024"
tldr: "Touchstone introduces a large-scale, rigorously designed benchmark for evaluating AI algorithms in medical image segmentation to address shortcomings in standard benchmarks."
---

# Touchstone Benchmark: Are We on the Right Way for Evaluating AI Algorithms for Medical Segmentation?

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1b8726b572e0dfa72793f9f6590664fd-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1b8726b572e0dfa72793f9f6590664fd-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Touchstone introduces a large-scale, rigorously designed benchmark for evaluating AI algorithms in medical image segmentation to address shortcomings in standard benchmarks.

## Abstract

How can we test AI performance? This question seems trivial, but it isn't. Standard benchmarks often have problems such as in-distribution and small-size test sets, oversimplified metrics, unfair comparisons, and short-term outcome pressure. As a consequence, good performance on standard benchmarks does not guarantee success in real-world scenarios. To address these problems, we present Touchstone, a large-scale collaborative segmentation benchmark of 9 types of abdominal organs. This benchmark is based on 5,195 training CT scans from 76 hospitals around the world and 5,903 testing CT scans from 11 additional hospitals. This diverse test set enhances the statistical significance of benchmark results and rigorously evaluates AI algorithms across various out-of-distribution scenarios. We invited 14 inventors of 19 AI algorithms to train their algorithms, while our team, as a third party, independently evaluated these algorithms on three test sets. In addition, we also evaluated pre-existing AI frameworks---which, differing from algorithms, are more flexible and can support different algorithms—including MONAI from NVIDIA, nnU-Net from DKFZ, and numerous other open-source frameworks. We are committed to expanding this benchmark to encourage more innovation of AI algorithms for the medical domain.