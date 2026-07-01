---
title: "LAVIB: A Large-scale Video Interpolation Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/333f81766b242b1837fa65c2172afb76-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['video-frame-interpolation', 'benchmark', 'high-resolution']
venue: "NeurIPS 2024"
tldr: "A large-scale high-resolution benchmark for evaluating video frame interpolation methods sourced through an automated web pipeline."
---

# LAVIB: A Large-scale Video Interpolation Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/333f81766b242b1837fa65c2172afb76-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/333f81766b242b1837fa65c2172afb76-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large-scale high-resolution benchmark for evaluating video frame interpolation methods sourced through an automated web pipeline.

## Abstract

This paper introduces a LArge-scale Video Interpolation Benchmark (LAVIB) for the low-level video task of Video Frame Interpolation (VFI). LAVIB comprises a large collection of high-resolution videos sourced from the web through an automated pipeline with minimal requirements for human verification. Metrics are computed for each video's motion magnitudes, luminance conditions, frame sharpness, and contrast. The collection of videos and the creation of quantitative challenges based on these metrics are under-explored by current low-level video task datasets. In total, LAVIB includes 283K clips from 17K ultra-HD videos, covering 77.6 hours. Benchmark train, val, and test sets maintain similar video metric distributions. Further splits are also created for out-of-distribution (OOD) challenges, with train and test splits including videos of dissimilar attributes.