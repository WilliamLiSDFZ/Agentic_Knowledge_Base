---
title: "Muscles in Time: Learning to Understand Human Motion In-Depth by Simulating Muscle Activations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7c3465ba08732cc2db38f070bfae601a-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['physics-informed-neural-operators-and-simulations', 'wearable-biosignal-gesture-activity-benchmarks']
tags: ['muscle-activation', 'human-motion', 'physics-simulation']
venue: "NeurIPS 2024"
tldr: "A framework that simulates muscle activations to deepen understanding of human motion dynamics from scarce ground-truth data."
---

# Muscles in Time: Learning to Understand Human Motion In-Depth by Simulating Muscle Activations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7c3465ba08732cc2db38f070bfae601a-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7c3465ba08732cc2db38f070bfae601a-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A framework that simulates muscle activations to deepen understanding of human motion dynamics from scarce ground-truth data.

## Abstract

Exploring the intricate dynamics between muscular and skeletal structures is pivotal for understanding human motion. This domain presents substantial challenges, primarily attributed to the intensive resources required for acquiring ground truth muscle activation data, resulting in a scarcity of datasets.In this work, we address this issue by establishing Muscles in Time (MinT), a large-scale synthetic muscle activation dataset.For the creation of MinT, we enriched existing motion capture datasets by incorporating muscle activation simulations derived from biomechanical human body models using the OpenSim platform, a common framework used in biomechanics and human motion research.Starting from simple pose sequences, our pipeline enables us to extract detailed information about the timing of muscle activations within the human musculoskeletal system.Muscles in Time contains over nine hours of simulation data covering 227 subjects and 402 simulated muscle strands. We demonstrate the utility of this dataset by presenting results on neural network-based muscle activation estimation from human pose sequences with two different sequence-to-sequence architectures.