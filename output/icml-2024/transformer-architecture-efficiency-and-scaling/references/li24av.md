---
title: "Sparse Cocktail: Every Sparse Pattern Every Sparse Ratio All At Once"
source: "https://proceedings.mlr.press/v235/li24av.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24av/li24av.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['sparse-neural-networks', 'pruning', 'sparsity-patterns', 'efficiency', 'training']
venue: "ICML 2024"
tldr: "Sparse Cocktail trains a single neural network that supports every sparse pattern and ratio simultaneously without retraining."
---

# Sparse Cocktail: Every Sparse Pattern Every Sparse Ratio All At Once

**Source**: [https://proceedings.mlr.press/v235/li24av.html](https://proceedings.mlr.press/v235/li24av.html)

**TLDR**: Sparse Cocktail trains a single neural network that supports every sparse pattern and ratio simultaneously without retraining.

## Abstract

Sparse Neural Networks (SNNs) have received voluminous attention for mitigating the explosion in computational costs and memory footprints of modern deep neural networks. Despite their popularity, most state-of-the-art training approaches seek to find a single high-quality sparse subnetwork with a preset sparsity pattern and ratio, making them inadequate to satiate platform and resource variability. Recently proposed approaches attempt to jointly train multiple subnetworks (we term as “sparse co-training") with a fixed sparsity pattern, to allow switching sparsity ratios subject to resource requirements. In this work, we take one more step forward and expand the scope of sparse co-training to cover diverse sparsity patterns and multiple sparsity ratios at once. We introduce Sparse Cocktail, the first sparse co-training framework that co-trains a suite of sparsity patterns simultaneously, loaded with multiple sparsity ratios which facilitate harmonious switch across various sparsity patterns and ratios at inference depending on the hardware availability. More specifically, Sparse Cocktail alternatively trains subnetworks generated from different sparsity patterns with a gradual increase in sparsity ratios across patterns and relies on an unified mask generation process and the Dense Pivot Co-training to ensure the subnetworks of different patterns orchestrate their shared parameters without canceling each other’s performance. Experiment results on image classification, object detection, and instance segmentation illustrate the favorable effectiveness and flexibility of Sparse Cocktail, pointing to a promising direction for sparse co-training. Codes will be released.