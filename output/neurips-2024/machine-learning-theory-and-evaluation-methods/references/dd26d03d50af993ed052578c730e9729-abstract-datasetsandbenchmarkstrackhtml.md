---
title: "Stronger Than You Think: Benchmarking Weak Supervision on Realistic Tasks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/dd26d03d50af993ed052578c730e9729-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['weak-supervision', 'benchmarking', 'label-efficient-learning', 'noisy-labels']
venue: "NeurIPS 2024"
tldr: "A comprehensive benchmark evaluating weak supervision methods on realistic tasks, revealing practical challenges in assessing their true value."
---

# Stronger Than You Think: Benchmarking Weak Supervision on Realistic Tasks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/dd26d03d50af993ed052578c730e9729-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/dd26d03d50af993ed052578c730e9729-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A comprehensive benchmark evaluating weak supervision methods on realistic tasks, revealing practical challenges in assessing their true value.

## Abstract

Weak supervision (WS) is a popular approach for label-efficient learning, leveraging diverse sources of noisy but inexpensive weak labels to automatically annotate training data. Despite its wide usage, WS and its practical value are challenging to benchmark due to the many knobs in its setup, including: data sources, labeling functions (LFs), aggregation techniques (called label models), and end model pipelines. Existing evaluation suites tend to be limited, focusing on particular components or specialized use cases. Moreover, they often involve simplistic benchmark tasks or de-facto LF sets that are suboptimally written, producing insights that may not generalize to real-world settings. We address these limitations by introducing a new benchmark, BOXWRENCH, designed to more accurately reflect real-world usages of WS. This benchmark features tasks with (1) higher class cardinality and imbalance, (2) notable domain expertise requirements, and (3) opportunities to re-use LFs across parallel multilingual corpora. For all tasks, LFs are written using a careful procedure aimed at mimicking real-world settings. In contrast to existing WS benchmarks, we show that supervised learning requires substantial amounts (1000+) of labeled examples to match WS in many settings.