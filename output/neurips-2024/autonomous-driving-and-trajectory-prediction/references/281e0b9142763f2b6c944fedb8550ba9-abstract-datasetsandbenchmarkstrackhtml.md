---
title: "Is Your HD Map Constructor Reliable under Sensor Corruptions?"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/281e0b9142763f2b6c944fedb8550ba9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['autonomous-driving-and-trajectory-prediction']
tags: ['HD-map-construction', 'sensor-corruption', 'robustness-evaluation']
venue: "NeurIPS 2024"
tldr: "A benchmark evaluating HD map constructors under various sensor corruptions and adverse conditions reveals significant reliability gaps in current methods."
---

# Is Your HD Map Constructor Reliable under Sensor Corruptions?

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/281e0b9142763f2b6c944fedb8550ba9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/281e0b9142763f2b6c944fedb8550ba9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark evaluating HD map constructors under various sensor corruptions and adverse conditions reveals significant reliability gaps in current methods.

## Abstract

Driving systems often rely on high-definition (HD) maps for precise environmental information, which is crucial for planning and navigation. While current HD map constructors perform well under ideal conditions, their resilience to real-world challenges, \eg, adverse weather and sensor failures, is not well understood, raising safety concerns. This work introduces MapBench, the first comprehensive benchmark designed to evaluate the robustness of HD map construction methods against various sensor corruptions. Our benchmark encompasses a total of 29 types of corruptions that occur from cameras and LiDAR sensors. Extensive evaluations across 31 HD map constructors reveal significant performance degradation of existing methods under adverse weather conditions and sensor failures, underscoring critical safety concerns. We identify effective strategies for enhancing robustness, including innovative approaches that leverage multi-modal fusion, advanced data augmentation, and architectural techniques. These insights provide a pathway for developing more reliable HD map construction methods, which are essential for the advancement of autonomous driving technology. The benchmark toolkit and affiliated code and model checkpoints have been made publicly accessible.