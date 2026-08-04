---
title: "TinyTrain: Resource-Aware Task-Adaptive Sparse Training of DNNs at the Data-Scarce Edge"
source: "https://proceedings.mlr.press/v235/kwon24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kwon24c/kwon24c.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'continual-learning-memory-plasticity']
tags: ['on-device-training', 'sparse-training', 'resource-constrained', 'edge-AI']
venue: "ICML 2024"
tldr: "A resource-aware sparse training framework for adapting deep neural networks on memory-constrained edge devices with scarce labeled data."
---

# TinyTrain: Resource-Aware Task-Adaptive Sparse Training of DNNs at the Data-Scarce Edge

**Source**: [https://proceedings.mlr.press/v235/kwon24c.html](https://proceedings.mlr.press/v235/kwon24c.html)

**TLDR**: A resource-aware sparse training framework for adapting deep neural networks on memory-constrained edge devices with scarce labeled data.

## Abstract

On-device training is essential for user personalisation and privacy. With the pervasiveness of IoT devices and microcontroller units (MCUs), this task becomes more challenging due to the constrained memory and compute resources, and the limited availability of labelled user data. Nonetheless, prior works neglect the data scarcity issue, require excessively long training time ($\textit{e.g.}$ a few hours), or induce substantial accuracy loss ($\geq$10%). In this paper, we propose TinyTrain, an on-device training approach that drastically reduces training time by selectively updating parts of the model and explicitly coping with data scarcity. TinyTrain introduces a task-adaptive sparse-update method that $\textit{dynamically}$ selects the layer/channel to update based on a multi-objective criterion that jointly captures user data, the memory, and the compute capabilities of the target device, leading to high accuracy on unseen tasks with reduced computation and memory footprint. TinyTrain outperforms vanilla fine-tuning of the entire network by 3.6-5.0% in accuracy, while reducing the backward-pass memory and computation cost by up to 1,098$\times$ and 7.68$\times$, respectively. Targeting broadly used real-world edge devices, TinyTrain achieves 9.5$\times$ faster and 3.5$\times$ more energy-efficient training over status-quo approaches, and 2.23$\times$ smaller memory footprint than SOTA methods, while remaining within the 1 MB memory envelope of MCU-grade platforms.