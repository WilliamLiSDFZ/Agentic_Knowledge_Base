---
title: "Gradient Rewiring for Editable Graph Neural Network Training"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/716ddcbb5aa8802f56a7dfd94c4df3db-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'machine-learning-theory-and-evaluation-methods']
tags: ['model-editing', 'graph-neural-networks', 'gradient-rewiring']
venue: "NeurIPS 2024"
tldr: "Proposes a gradient rewiring method for efficiently editing graph neural networks to correct prediction errors after deployment without full retraining."
---

# Gradient Rewiring for Editable Graph Neural Network Training

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/716ddcbb5aa8802f56a7dfd94c4df3db-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/716ddcbb5aa8802f56a7dfd94c4df3db-Abstract-Conference.html)

**TLDR**: Proposes a gradient rewiring method for efficiently editing graph neural networks to correct prediction errors after deployment without full retraining.

## Abstract

Deep neural networks are ubiquitously adopted in many applications, such as computer vision, natural language processing, and graph analytics. However, well-trained neural networks can make prediction errors after deployment as the world changes. \textit{Model editing} involves updating the base model to correct prediction errors with less accessible training data and computational resources.Despite recent advances in model editors in computer vision and natural language processing, editable training in graph neural networks (GNNs) is rarely explored. The challenge with editable GNN training lies in the inherent information aggregation across neighbors, which can lead model editors to affect the predictions of other nodes unintentionally. In this paper, we first observe the gradient of cross-entropy loss for the target node and training nodes with significant inconsistency, which indicates that directly fine-tuning the base model using the loss on the target node deteriorates the performance on training nodes. Motivated by the gradient inconsistency observation, we propose a simple yet effective \underline{G}radient \underline{R}ewiring method for \underline{E}ditable graph neural network training, named \textbf{GRE}. Specifically, we first store the anchor gradient of the loss on training nodes to preserve the locality. Subsequently, we rewire the gradient of the loss on the target node to preserve performance on the training node using anchor gradient. Experiments demonstrate the effectiveness of GRE on various model architectures and graph datasets in terms of multiple editing situations. The source code is available at \url{https://github.com/zhimengj0326/Gradientrewiringediting}.