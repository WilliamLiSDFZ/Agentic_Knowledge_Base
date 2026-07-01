---
title: "Learning rigid-body simulators over implicit shapes for large-scale scenes and vision"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e3abc125ecacb71786cefb9f67b08c5d-Abstract-Conference.html"
categories: ['physics-informed-neural-operators-and-simulations', 'neural-geometric-shape-representation-learning']
tags: ['rigid-body-simulation', 'implicit-shapes', 'large-scale-scenes']
venue: "NeurIPS 2024"
tldr: "A learned rigid-body simulator operating over implicit shape representations is proposed to handle large-scale scenes with many objects and bridge simulation to vision applications."
---

# Learning rigid-body simulators over implicit shapes for large-scale scenes and vision

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e3abc125ecacb71786cefb9f67b08c5d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/e3abc125ecacb71786cefb9f67b08c5d-Abstract-Conference.html)

**TLDR**: A learned rigid-body simulator operating over implicit shape representations is proposed to handle large-scale scenes with many objects and bridge simulation to vision applications.

## Abstract

Simulating large scenes with many rigid objects is crucial for a variety of applications, such as robotics, engineering, film and video games. Rigid interactions are notoriously hard to model: small changes to the initial state or the simulation parameters can lead to large changes in the final state. Recently, learned simulators based on graph networks (GNNs) were developed as an alternative to hand-designed simulators like MuJoCo and Bullet. They are able to accurately capture dynamics of real objects directly from real-world observations. However, current state-of-the-art learned simulators operate on meshes and scale poorly to scenes with many objects or detailed shapes. Here we present SDF-Sim, the first learned rigid-body simulator designed for scale. We use learned signed-distance functions (SDFs) to represent the object shapes and to speed up distance computation. We design the simulator to leverage SDFs and avoid the fundamental bottleneck of the previous simulators associated with collision detection.For the first time in literature, we demonstrate that we can scale the GNN-based simulators to scenes with hundreds of objects and up to 1.1 million nodes, where mesh-based approaches run out of memory. Finally, we show that SDF-Sim can be applied to real world scenes by extracting SDFs from multi-view images.