---
title: "KISA: A Unified Keyframe Identifier and Skill Annotator for Long-Horizon Robotics Demonstrations"
source: "https://proceedings.mlr.press/v235/kou24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kou24b/kou24b.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'continual-learning-memory-plasticity']
tags: ['robotics', 'keyframe-identification', 'skill-annotation', 'long-horizon', 'imitation-learning']
venue: "ICML 2024"
tldr: "A unified framework that simultaneously identifies keyframes and annotates skills from long-horizon robotic manipulation demonstrations."
---

# KISA: A Unified Keyframe Identifier and Skill Annotator for Long-Horizon Robotics Demonstrations

**Source**: [https://proceedings.mlr.press/v235/kou24b.html](https://proceedings.mlr.press/v235/kou24b.html)

**TLDR**: A unified framework that simultaneously identifies keyframes and annotates skills from long-horizon robotic manipulation demonstrations.

## Abstract

Robotic manipulation tasks often span over long horizons and encapsulate multiple subtasks with different skills. Learning policies directly from long-horizon demonstrations is challenging without intermediate keyframes guidance and corresponding skill annotations. Existing approaches for keyframe identification often struggle to offer reliable decomposition for low accuracy and fail to provide semantic relevance between keyframes and skills. For this, we propose a unified Keyframe Identifier and Skill Anotator (KISA) that utilizes pretrained visual-language representations for precise and interpretable decomposition of unlabeled demonstrations. Specifically, we develop a simple yet effective temporal enhancement module that enriches frame-level representations with expanded receptive fields to capture semantic dynamics at the video level. We further propose coarse contrastive learning and fine-grained monotonic encouragement to enhance the alignment between visual representations from keyframes and language representations from skills. The experimental results across three benchmarks demonstrate that KISA outperforms competitive baselines in terms of accuracy and interpretability of keyframe identification. Moreover, KISA exhibits robust generalization capabilities and the flexibility to incorporate various pretrained representations.