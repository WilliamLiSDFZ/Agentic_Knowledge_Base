---
title: "WebUOT-1M: Advancing Deep Underwater Object Tracking with A Million-Scale Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/59bd8ec7f4906e309b8a7727beedde18-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['underwater-object-tracking', 'benchmark', 'deep-learning']
venue: "NeurIPS 2024"
tldr: "A million-scale benchmark for underwater object tracking advancing diversity and scale for evaluating deep tracking algorithms."
---

# WebUOT-1M: Advancing Deep Underwater Object Tracking with A Million-Scale Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/59bd8ec7f4906e309b8a7727beedde18-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/59bd8ec7f4906e309b8a7727beedde18-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A million-scale benchmark for underwater object tracking advancing diversity and scale for evaluating deep tracking algorithms.

## Abstract

Underwater Object Tracking (UOT) is essential for identifying and tracking submerged objects in underwater videos, but existing datasets are limited in scale, diversity of target categories and scenarios covered, impeding the development of advanced tracking algorithms. To bridge this gap, we take the first step and introduce WebUOT-1M, \ie, the largest public UOT benchmark to date, sourced from complex and realistic underwater environments. It comprises 1.1 million frames across 1,500 video clips filtered from 408 target categories, largely surpassing previous UOT datasets, \eg, UVOT400. Through meticulous manual annotation and verification, we provide high-quality bounding boxes for underwater targets. Additionally, WebUOT-1M includes language prompts for video sequences, expanding its application areas, \eg, underwater vision-language tracking. Given that most existing trackers are designed for open-air conditions and perform poorly in underwater environments due to domain gaps, we propose a novel framework that uses omni-knowledge distillation to train a student Transformer model effectively. To the best of our knowledge, this framework is the first to effectively transfer open-air domain knowledge to the UOT model through knowledge distillation, as demonstrated by results on both existing UOT datasets and the newly proposed WebUOT-1M. We have thoroughly tested WebUOT-1M with 30 deep trackers, showcasing its potential as a benchmark for future UOT research. The complete dataset, along with codes and tracking results, are publicly accessible at \href{https://github.com/983632847/Awesome-Multimodal-Object-Tracking}{\color{magenta}{here}}.