---
title: "Evaluating Multiview Object Consistency in Humans and Image Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4cc613494d5a4f2feef21ecc229c06f5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['multiview-consistency', '3d-shape-inference', 'human-model-alignment']
venue: "NeurIPS 2024"
tldr: "A benchmark evaluating alignment between human observers and vision models on 3D object consistency judgments across multiple viewpoints."
---

# Evaluating Multiview Object Consistency in Humans and Image Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4cc613494d5a4f2feef21ecc229c06f5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4cc613494d5a4f2feef21ecc229c06f5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark evaluating alignment between human observers and vision models on 3D object consistency judgments across multiple viewpoints.

## Abstract

We introduce a benchmark to directly evaluate the alignment between human observers and vision models on a 3D shape inference task. We leverage an experimental design from the cognitive sciences: given a set of images, participants identify which contain the same/different objects, despite considerable viewpoint variation. We draw from a diverse range of images that include common objects (e.g., chairs) as well as abstract shapes (i.e., procedurally generated 'nonsense' objects). After constructing over 2000 unique image sets, we administer these tasks to human participants, collecting 35K trials of behavioral data from over 500 participants. This includes explicit choice behaviors as well as intermediate measures, such as reaction time and gaze data. We then evaluate the performance of common vision models (e.g., DINOv2, MAE, CLIP). We find that humans outperform all models by a wide margin. Using a multi-scale evaluation approach, we identify underlying similarities and differences between models and humans: while human-model performance is correlated, humans allocate more time/processing on challenging trials. All images, data, and code can be accessed via our project page.