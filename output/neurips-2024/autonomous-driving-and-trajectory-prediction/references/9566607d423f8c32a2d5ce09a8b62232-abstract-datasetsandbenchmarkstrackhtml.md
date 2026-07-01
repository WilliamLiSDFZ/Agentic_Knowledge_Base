---
title: "TAPVid-3D: A Benchmark for Tracking Any Point in 3D"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9566607d423f8c32a2d5ce09a8b62232-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'autonomous-driving-and-trajectory-prediction']
tags: ['3D-point-tracking', 'benchmark', 'video-understanding']
venue: "NeurIPS 2024"
tldr: "Presents TAPVid-3D, the first benchmark for evaluating long-range 3D point tracking in real-world videos."
---

# TAPVid-3D: A Benchmark for Tracking Any Point in 3D

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9566607d423f8c32a2d5ce09a8b62232-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9566607d423f8c32a2d5ce09a8b62232-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents TAPVid-3D, the first benchmark for evaluating long-range 3D point tracking in real-world videos.

## Abstract

We introduce a new benchmark, TAPVid-3D, for evaluating the task of long-range Tracking Any Point in 3D (TAP-3D). While point tracking in two dimensions (TAP-2D) has many benchmarks measuring performance on real-world videos, such as TAPVid-DAVIS, three-dimensional point tracking has none. To this end, leveraging existing footage, we build a new benchmark for 3D point tracking featuring 4,000+ real-world videos, composed of three different data sources spanning a variety of object types, motion patterns, and indoor and outdoor environments. To measure performance on the TAP-3D task, we formulate a collection of metrics that extend the Jaccard-based metric used in TAP-2D to handle the complexities of ambiguous depth scales across models, occlusions, and multi-track spatio-temporal smoothness. We manually verify a large sample of trajectories to ensure correct video annotations, and assess the current state of the TAP-3D task by constructing competitive baselines using existing tracking models. We anticipate this benchmark will serve as a guidepost to improve our ability to understand precise 3D motion and surface deformation from monocular video.