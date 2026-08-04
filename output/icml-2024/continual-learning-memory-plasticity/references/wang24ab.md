---
title: "Rapid Learning without Catastrophic Forgetting in the Morris Water Maze"
source: "https://proceedings.mlr.press/v235/wang24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ab/wang24ab.pdf"
categories: ['continual-learning-memory-plasticity', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['continual-learning', 'catastrophic-forgetting', 'Morris-water-maze', 'neurobiological-tasks']
venue: "ICML 2024"
tldr: "A sequential Morris Water Maze task is introduced alongside a model that enables rapid learning without catastrophic forgetting."
---

# Rapid Learning without Catastrophic Forgetting in the Morris Water Maze

**Source**: [https://proceedings.mlr.press/v235/wang24ab.html](https://proceedings.mlr.press/v235/wang24ab.html)

**TLDR**: A sequential Morris Water Maze task is introduced alongside a model that enables rapid learning without catastrophic forgetting.

## Abstract

Animals can swiftly adapt to novel tasks, while maintaining proficiency on previously trained tasks. This contrasts starkly with machine learning models, which struggle on these capabilities. We first propose a new task, the sequential Morris Water Maze (sWM), which extends a widely used task in the psychology and neuroscience fields and requires both rapid and continual learning. It has frequently been hypothesized that inductive biases from brains could help build better ML systems, but the addition of constraints typically hurts rather than helping ML performance. We draw inspiration from biology to show that combining 1) a content-addressable heteroassociative memory based on the entorhinal-hippocampal circuit with grid cells that retain shared across-environment structural representations and hippocampal cells that acquire environment-specific information; 2) a spatially invariant convolutional network architecture for rapid adaptation across unfamiliar environments; and 3) the ability to perform remapping, which orthogonalizes internal representations; leads to good generalization, rapid learning, and continual learning without forgetting, respectively. Our model outperforms ANN baselines from continual learning contexts applied to the task. It retains knowledge of past environments while rapidly acquiring the skills to navigate new ones, thereby addressing the seemingly opposing challenges of quick knowledge transfer and sustaining proficiency in previously learned tasks. These biologically motivated results may point the way toward ML algorithms with similar properties.