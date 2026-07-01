---
title: "OVT-B: A New Large-Scale Benchmark for Open-Vocabulary Multi-Object Tracking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1adeeac24ce6168e20bcee85645720e9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'autonomous-driving-and-trajectory-prediction']
tags: ['open-vocabulary', 'multi-object-tracking', 'benchmark', 'novel-classes', 'detection']
venue: "NeurIPS 2024"
tldr: "OVT-B is a large-scale benchmark for open-vocabulary multi-object tracking targeting novel unseen object categories."
---

# OVT-B: A New Large-Scale Benchmark for Open-Vocabulary Multi-Object Tracking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1adeeac24ce6168e20bcee85645720e9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1adeeac24ce6168e20bcee85645720e9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: OVT-B is a large-scale benchmark for open-vocabulary multi-object tracking targeting novel unseen object categories.

## Abstract

Open-vocabulary object perception has become an important topic in artificial intelligence, which aims to identify objects with novel classes that have not been seen during training. Under this setting, open-vocabulary object detection (OVD) in a single image has been studied in many literature. However, open-vocabulary object tracking (OVT) from a video has been studied less, and one reason is the shortage of benchmarks. In this work, we have built a new large-scale benchmark for open-vocabulary multi-object tracking namely OVT-B. OVT-B contains 1,048 categories of objects and 1,973 videos with 637,608 bounding box annotations, which is much larger than the sole open-vocabulary tracking dataset, i.e., OVTAO-val dataset (200+ categories, 900+ videos). The proposed OVT-B can be used as a new benchmark to pave the way for OVT research. We also develop a simple yet effective baseline method for OVT. It integrates the motion features for object tracking, which is an important feature for MOT but is ignored in previous OVT methods. Experimental results have verified the usefulness of the proposed benchmark and the effectiveness of our method. We have released the benchmark to the public at https://github.com/Coo1Sea/OVT-B-Dataset.