---
title: "Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7ebcdd0de471c027e67a11959c666d74-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-safety-robustness-and-privacy-defenses']
tags: ['ai-safety', 'benchmarking', 'safety-evaluation', 'model-capabilities', 'benchmark-validity']
venue: "NeurIPS 2024"
tldr: "Critically examines whether AI safety benchmarks genuinely measure safety progress or merely reflect general model capability scaling."
---

# Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7ebcdd0de471c027e67a11959c666d74-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7ebcdd0de471c027e67a11959c666d74-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Critically examines whether AI safety benchmarks genuinely measure safety progress or merely reflect general model capability scaling.

## Abstract

Performance on popular ML benchmarks is highly correlated with model scale, suggesting that most benchmarks tend to measure a similar underlying factor of general model capabilities. However, substantial research effort remains devoted to designing new benchmarks, many of which claim to measure novel phenomena. In the spirit of the Bitter Lesson, we leverage spectral analysis to measure an underlying capabilities component, the direction in benchmark-performance-space which explains most variation in model performance. In an extensive analysis of existing safety benchmarks, we find that variance in model performance on many safety benchmarks is largely explained by the capabilities component. In response, we argue that safety research should prioritize metrics which are not highly correlated with scale. Our work provides a lens to analyze both novel safety benchmarks and novel safety methods, which we hope will enable future work to make differential progress on safety.