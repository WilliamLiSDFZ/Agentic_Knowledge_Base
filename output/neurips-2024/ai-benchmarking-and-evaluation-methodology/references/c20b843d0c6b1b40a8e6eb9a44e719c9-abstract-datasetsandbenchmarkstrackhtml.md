---
title: "Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c20b843d0c6b1b40a8e6eb9a44e719c9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['audio-visual-speech-processing-and-benchmarks', 'ai-benchmarking-and-evaluation-methodology']
tags: ['human-interaction', 'video-dataset', 'close-contact']
venue: "NeurIPS 2024"
tldr: "Harmony4D introduces a large-scale in-the-wild video dataset for understanding close human interactions in 3D."
---

# Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c20b843d0c6b1b40a8e6eb9a44e719c9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c20b843d0c6b1b40a8e6eb9a44e719c9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Harmony4D introduces a large-scale in-the-wild video dataset for understanding close human interactions in 3D.

## Abstract

Understanding how humans interact with each other is key to building realistic multi-human virtual reality systems. This area remains relatively unexplored due to the lack of large-scale datasets. Recent datasets focusing on this issue mainly consist of activities captured entirely in controlled indoor environments with choreographed actions, significantly affecting their diversity. To address this, we introduce Harmony4D, a multi-view video dataset for human-human interaction featuring in-the-wild activities such as wrestling, dancing, MMA,and more. We use a flexible multi-view capture system to record these dynamic activities and provide annotations for human detection, tracking, 2D/3D pose estimation, and mesh recovery for closely interacting subjects. We propose a novel markerless algorithm to track 3D human poses in severe occlusion and close interaction to obtain our annotations with minimal manual intervention. Harmony4D consists of 1.66 million images and 3.32 million human instances from more than 20 synchronized cameras with 208 video sequences spanning diverse environments and 24 unique subjects. We rigorously evaluate existing state-of-the-art methods for mesh recovery and highlight their significant limitations in modeling close interaction scenarios. Additionally, we fine-tune a pre-trained HMR2.0 model on Harmony4D and demonstrate an improved performance of 54.8% PVE in scenes with severe occlusion and contact. “Harmony—a cohesive alignment of human behaviors." Code and data are available at https://jyuntins.github.io/harmony4d/.