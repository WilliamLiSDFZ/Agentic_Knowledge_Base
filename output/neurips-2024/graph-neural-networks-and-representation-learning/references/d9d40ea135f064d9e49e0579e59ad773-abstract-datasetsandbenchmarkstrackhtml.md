---
title: "EyeGraph: Modularity-aware Spatio Temporal Graph Clustering for Continuous Event-based Eye Tracking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d9d40ea135f064d9e49e0579e59ad773-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['wearable-biosignal-gesture-activity-benchmarks', 'graph-neural-networks-and-representation-learning']
tags: ['event-camera', 'eye-tracking', 'spatiotemporal-graph-clustering']
venue: "NeurIPS 2024"
tldr: "EyeGraph proposes a modularity-aware spatiotemporal graph clustering method for continuous event-based eye tracking."
---

# EyeGraph: Modularity-aware Spatio Temporal Graph Clustering for Continuous Event-based Eye Tracking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d9d40ea135f064d9e49e0579e59ad773-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d9d40ea135f064d9e49e0579e59ad773-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: EyeGraph proposes a modularity-aware spatiotemporal graph clustering method for continuous event-based eye tracking.

## Abstract

Continuous tracking of eye movement dynamics plays a significant role in developing a broad spectrum of human-centered applications, such as cognitive skills (visual attention and working memory) modeling, human-machine interaction, biometric user authentication, and foveated rendering. Recently neuromorphic cameras have garnered significant interest in the eye-tracking research community, owing to their sub-microsecond latency in capturing intensity changes resulting from eye movements. Nevertheless, the existing approaches for event-based eye tracking suffer from several limitations: dependence on RGB frames, label sparsity, and training on datasets collected in controlled lab environments that do not adequately reflect real-world scenarios. To address these limitations, in this paper, we propose a dynamic graph-based approach that uses a neuromorphic event stream captured by Dynamic Vision Sensors (DVS) for high-fidelity tracking of pupillary movement. More specifically, first, we present EyeGraph, a large-scale multi-modal near-eye tracking dataset collected using a wearable event camera attached to a head-mounted device from 40 participants -- the dataset was curated while mimicking in-the-wild settings, accounting for varying mobility and ambient lighting conditions. Subsequently, to address the issue of label sparsity, we adopt an unsupervised topology-aware approach as a benchmark. To be specific, (a) we first construct a dynamic graph using Gaussian Mixture Models (GMM), resulting in a uniform and detailed representation of eye morphology features, facilitating accurate modeling of pupil and iris. Then (b) apply a novel topologically guided modularity-aware graph clustering approach to precisely track the movement of the pupil and address the label sparsity in event-based eye tracking. We show that our unsupervised approach has comparable performance against the supervised approaches while consistently outperforming the conventional clustering approaches.