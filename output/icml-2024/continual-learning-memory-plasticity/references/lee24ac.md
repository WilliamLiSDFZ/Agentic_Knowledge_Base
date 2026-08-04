---
title: "STELLA: Continual Audio-Video Pre-training with SpatioTemporal Localized Alignment"
source: "https://proceedings.mlr.press/v235/lee24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24ac/lee24ac.pdf"
categories: ['continual-learning-memory-plasticity', 'audio-and-music-generation-diffusion-models']
tags: ['continual-learning', 'audio-video', 'pre-training', 'spatiotemporal-alignment']
venue: "ICML 2024"
tldr: "Proposes STELLA for continual audio-video pre-training with spatiotemporal localized alignment to handle evolving audio-visual semantics."
---

# STELLA: Continual Audio-Video Pre-training with SpatioTemporal Localized Alignment

**Source**: [https://proceedings.mlr.press/v235/lee24ac.html](https://proceedings.mlr.press/v235/lee24ac.html)

**TLDR**: Proposes STELLA for continual audio-video pre-training with spatiotemporal localized alignment to handle evolving audio-visual semantics.

## Abstract

Continuously learning a variety of audio-video semantics over time is crucial for audio-related reasoning tasks in our ever-evolving world. However, this is a nontrivial problem and poses two critical challenges: sparse spatio-temporal correlation between audio-video pairs and multimodal correlation overwriting that forgets audio-video relations. To tackle this problem, we propose a new continual audio-video pre-training method with two novel ideas: (1) Localized Patch Importance Scoring: we introduce a multimodal encoder to determine the importance score for each patch, emphasizing semantically intertwined audio-video patches. (2) Replay-guided Correlation Assessment: to reduce the corruption of previously learned audiovisual knowledge due to drift, we propose to assess the correlation of the current patches on the past steps to identify the patches exhibiting high correlations with the past steps. Based on the results from the two ideas, we perform probabilistic patch selection for effective continual audio-video pre-training. Experimental validation on multiple benchmarks shows that our method achieves a $3.69%$p of relative performance gain in zero-shot retrieval tasks compared to strong continual learning baselines, while reducing memory consumption by $\sim 45 %$.