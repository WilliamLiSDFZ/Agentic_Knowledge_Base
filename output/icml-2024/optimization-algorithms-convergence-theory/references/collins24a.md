---
title: "Provable Multi-Task Representation Learning by Two-Layer ReLU Neural Networks"
source: "https://proceedings.mlr.press/v235/collins24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/collins24a/collins24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['multi-task-learning', 'representation-learning', 'relu-networks']
venue: "ICML 2024"
tldr: "Provides provable guarantees for multi-task representation learning using two-layer ReLU networks with theoretical analysis of downstream task performance."
---

# Provable Multi-Task Representation Learning by Two-Layer ReLU Neural Networks

**Source**: [https://proceedings.mlr.press/v235/collins24a.html](https://proceedings.mlr.press/v235/collins24a.html)

**TLDR**: Provides provable guarantees for multi-task representation learning using two-layer ReLU networks with theoretical analysis of downstream task performance.

## Abstract

An increasingly popular machine learning paradigm is to pretrain a neural network (NN) on many tasks offline, then adapt it to downstream tasks, often by re-training only the last linear layer of the network. This approach yields strong downstream performance in a variety of contexts, demonstrating that multitask pretraining leads to effective feature learning. Although several recent theoretical studies have shown that shallow NNs learn meaningful features when either (i) they are trained on a single task or (ii) they are linear, very little is known about the closer-to-practice case of nonlinear NNs trained on multiple tasks. In this work, we present the first results proving that feature learning occurs during training with a nonlinear model on multiple tasks. Our key insight is that multi-task pretraining induces a pseudo-contrastive loss that favors representations that align points that typically have the same label across tasks. Using this observation, we show that when the tasks are binary classification tasks with labels depending on the projection of the data onto an $r$-dimensional subspace within the $d\gg r$-dimensional input space, a simple gradient-based multitask learning algorithm on a two-layer ReLU NN recovers this projection, allowing for generalization to downstream tasks with sample and neuron complexity independent of $d$. In contrast, we show that with high probability over the draw of a single task, training on this single task cannot guarantee to learn all $r$ ground-truth features.