---
title: "Sparse-IFT: Sparse Iso-FLOP Transformations for Maximizing Training Efficiency"
source: "https://proceedings.mlr.press/v235/thangarasa24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/thangarasa24a/thangarasa24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['weight-sparsity', 'iso-FLOP', 'training-efficiency']
venue: "ICML 2024"
tldr: "Sparse Iso-FLOP Transformations improve deep network training efficiency by redistributing FLOPs via structured sparsity while maintaining accuracy."
---

# Sparse-IFT: Sparse Iso-FLOP Transformations for Maximizing Training Efficiency

**Source**: [https://proceedings.mlr.press/v235/thangarasa24a.html](https://proceedings.mlr.press/v235/thangarasa24a.html)

**TLDR**: Sparse Iso-FLOP Transformations improve deep network training efficiency by redistributing FLOPs via structured sparsity while maintaining accuracy.

## Abstract

Recent research has focused on weight sparsity in deep neural network training to reduce FLOPs, aiming for improved efficiency (test accuracy w.r.t training FLOPs). However, sparse weight training often compromises accuracy, requiring extended training schedules to attain the accuracy of dense models. In contrast, our approach, Sparse Iso-FLOP Transformations (Sparse-IFT), uses sparsity to improve accuracy while maintaining dense model FLOPs. Using a single hyperparameter (i.e., the sparsity level), Sparse-IFTs efficiently replace dense layers, expanding the search space for optimal sparse masks. In addition, dynamic sparse training (DST) with Sparse-IFT models effectively navigate this larger sparse mask-weight space, which is evidenced by a spectral analysis using Ramanujan graph properties. Our study reveals a robust correlation among mask topology, weights, and final performance. Notably, without adjusting any training hyperparameters, replacing dense layers with Sparse-IFT yields significant improvements, such as a +3.5% boost for ResNet-18 on ImageNet and +0.9% for GPT-3 Small on the Open LLM leaderboard. To the best of our knowledge, this is the first work to demonstrate the use of sparsity for improving the accuracy of dense models through a set of simple-to-use sparse transformations. Code is available at: https://github.com/CerebrasResearch/Sparse-IFT.