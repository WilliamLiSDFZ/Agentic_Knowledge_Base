---
title: "Representation Surgery for Multi-Task Model Merging"
source: "https://proceedings.mlr.press/v235/yang24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24t/yang24t.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'continual-learning-memory-plasticity']
tags: ['model-merging', 'multi-task-learning', 'representation-surgery']
venue: "ICML 2024"
tldr: "A representation surgery technique to correct feature distribution misalignment when merging independently trained models for multi-task learning."
---

# Representation Surgery for Multi-Task Model Merging

**Source**: [https://proceedings.mlr.press/v235/yang24t.html](https://proceedings.mlr.press/v235/yang24t.html)

**TLDR**: A representation surgery technique to correct feature distribution misalignment when merging independently trained models for multi-task learning.

## Abstract

Multi-task learning (MTL) compresses the information from multiple tasks into a unified backbone to improve computational efficiency and generalization. Recent work directly merges multiple independently trained models to perform MTL instead of collecting their raw data for joint training, greatly expanding the application scenarios of MTL. However, by visualizing the representation distribution of existing model merging schemes, we find that the merged model often suffers from the dilemma of representation bias. That is, there is a significant discrepancy in the representation distribution between the merged and individual models, resulting in poor performance of merged MTL. In this paper, we propose a representation surgery solution called “Surgery" to reduce representation bias in the merged model. Specifically, Surgery is a lightweight task-specific plugin that takes the representation of the merged model as input and attempts to output the biases contained in the representation from the merged model. We then designed an unsupervised optimization objective that updates the Surgery plugin by minimizing the distance between the merged model’s representation and the individual model’s representation. Extensive experiments demonstrate significant MTL performance improvements when our Surgery plugin is applied to state-of-the-art (SOTA) model merging schemes.