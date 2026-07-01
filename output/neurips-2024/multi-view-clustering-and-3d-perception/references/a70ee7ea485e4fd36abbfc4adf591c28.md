---
title: "Multi-scale Consistency for Robust 3D Registration via Hierarchical Sinkhorn Tree"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a70ee7ea485e4fd36abbfc4adf591c28-Abstract-Conference.html"
categories: ['multi-view-clustering-and-3d-perception']
tags: ['point-cloud-registration', 'multi-scale-consistency', 'Sinkhorn', 'correspondence-matching']
venue: "NeurIPS 2024"
tldr: "A hierarchical Sinkhorn tree enforces multi-scale consistency to achieve robust and accurate 3D point cloud registration."
---

# Multi-scale Consistency for Robust 3D Registration via Hierarchical Sinkhorn Tree

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a70ee7ea485e4fd36abbfc4adf591c28-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a70ee7ea485e4fd36abbfc4adf591c28-Abstract-Conference.html)

**TLDR**: A hierarchical Sinkhorn tree enforces multi-scale consistency to achieve robust and accurate 3D point cloud registration.

## Abstract

We study the problem of retrieving accurate correspondence through multi-scale consistency (MSC) for robust point cloud registration. Existing works in a coarse-to-fine manner either suffer from severe noisy correspondences caused by unreliable coarse matching or struggle to form outlier-free coarse-level correspondence sets. To tackle this, we present Hierarchical Sinkhorn Tree (HST), a pruned tree structure designed to hierarchically measure the local consistency of each coarse correspondence across multiple feature scales, thereby filtering out the local dissimilar ones. In this way, we convert the modeling of MSC for each correspondence into a BFS traversal with pruning of a K-ary tree rooted at the superpoint, with its K nearest neighbors in the feature pyramid serving as child nodes. To achieve efficient pruning and accurate vicinity characterization, we further propose a novel overlap-aware Sinkhorn Distance, which retains only the most likely overlapping points for local measurement and next level exploration. The modeling process essentially involves traversing a pair of HSTs synchronously and aggregating the consistency measures of corresponding tree nodes. Extensive experiments demonstrate HST consistently outperforms the state-of-the-art methods on both indoor and outdoor benchmarks.