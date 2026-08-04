---
title: "Harnessing Neural Unit Dynamics for Effective and Scalable Class-Incremental Learning"
source: "https://proceedings.mlr.press/v235/li24bk.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bk/li24bk.pdf"
categories: ['continual-learning-memory-plasticity', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['class-incremental-learning', 'neural-dynamics', 'connectionist-models']
venue: "ICML 2024"
tldr: "Proposes a connectionist model exploiting neural unit dynamics to enable effective and scalable class-incremental learning."
---

# Harnessing Neural Unit Dynamics for Effective and Scalable Class-Incremental Learning

**Source**: [https://proceedings.mlr.press/v235/li24bk.html](https://proceedings.mlr.press/v235/li24bk.html)

**TLDR**: Proposes a connectionist model exploiting neural unit dynamics to enable effective and scalable class-incremental learning.

## Abstract

Class-incremental learning (CIL) aims to train a model to learn new classes from non-stationary data streams without forgetting old ones. In this paper, we propose a new kind of connectionist model by tailoring neural unit dynamics that adapt the behavior of neural networks for CIL. In each training session, it introduces a supervisory mechanism to guide network expansion whose growth size is compactly commensurate with the intrinsic complexity of a newly arriving task. This constructs a near-minimal network while allowing the model to expand its capacity when cannot sufficiently hold new classes. At inference time, it automatically reactivates the required neural units to retrieve knowledge and leaves the remaining inactivated to prevent interference. We name our model AutoActivator, which is effective and scalable. To gain insights into the neural unit dynamics, we theoretically analyze the model’s convergence property via a universal approximation theorem on learning sequential mappings, which is under-explored in the CIL community. Experiments show that our method achieves strong CIL performance in rehearsal-free and minimal-expansion settings with different backbones.