---
title: "UAV3D: A Large-scale 3D Perception Benchmark for Unmanned Aerial Vehicles"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/643ea9b3843bd8f525ad8801437a2022-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['multi-view-clustering-and-3d-perception']
tags: ['UAV', '3D-perception', 'benchmark']
venue: "NeurIPS 2024"
tldr: "UAV3D introduces a large-scale benchmark for 3D object detection and tracking from unmanned aerial vehicle perspectives."
---

# UAV3D: A Large-scale 3D Perception Benchmark for Unmanned Aerial Vehicles

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/643ea9b3843bd8f525ad8801437a2022-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/643ea9b3843bd8f525ad8801437a2022-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: UAV3D introduces a large-scale benchmark for 3D object detection and tracking from unmanned aerial vehicle perspectives.

## Abstract

Unmanned Aerial Vehicles (UAVs), equipped with cameras, are employed in numerous applications, including aerial photography, surveillance, and agriculture. In these applications, robust object detection and tracking are essential for the effective deployment of UAVs. However, existing benchmarks for UAV applications are mainly designed for traditional 2D perception tasks, restricting thedevelopment of real-world applications that require a 3D understanding of the environment. Furthermore, despite recent advancements in single-UAV perception, limited views of a single UAV platform significantly constrain its perception capabilities over long distances or in occluded areas. To address these challenges, we introduce UAV3D – a benchmark designed to advance research in both 3D andcollaborative 3D perception tasks with UAVs. UAV3D comprises 1,000 scenes, each of which has 20 frames with fully annotated 3D bounding boxes on vehicles. We provide the benchmark for four 3D perception tasks: single-UAV 3D object detection, single-UAV object tracking, collaborative-UAV 3D object detection, and collaborative-UAV object tracking. Our dataset and code are available athttps://huiyegit.github.io/UAV3D_Benchmark/.