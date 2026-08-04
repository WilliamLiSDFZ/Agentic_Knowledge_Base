---
title: "Unsupervised Representation Learning of Brain Activity via Bridging Voxel Activity and Functional Connectivity"
source: "https://proceedings.mlr.press/v235/behrouz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/behrouz24a/behrouz24a.pdf"
categories: ['multi-region-brain-connectivity-modeling', 'clustering-methods-and-multi-view-learning']
tags: ['brain-representation-learning', 'fMRI', 'functional-connectivity', 'voxel-activity', 'unsupervised-learning']
venue: "ICML 2024"
tldr: "Presents an unsupervised framework that bridges voxel-level activity and functional connectivity for improved brain representation learning."
---

# Unsupervised Representation Learning of Brain Activity via Bridging Voxel Activity and Functional Connectivity

**Source**: [https://proceedings.mlr.press/v235/behrouz24a.html](https://proceedings.mlr.press/v235/behrouz24a.html)

**TLDR**: Presents an unsupervised framework that bridges voxel-level activity and functional connectivity for improved brain representation learning.

## Abstract

Effective brain representation learning is a key step toward the understanding of cognitive processes and diagnosis of neurological diseases/disorders. Existing studies have focused on either (1) voxel-level activity, where only a single weight relating the voxel activity to the task (i.e., aggregation of voxel activity over a time window) is considered, missing their temporal dynamics, or (2) functional connectivity of the brain in the level of region of interests, missing voxel-level activities. We bridge this gap and design BrainMixer, an unsupervised learning framework that effectively utilizes both functional connectivity and associated time series of voxels to learn voxel-level representation in an unsupervised manner. BrainMixer employs two simple yet effective MLP-based encoders to simultaneously learn the dynamics of voxel-level signals and their functional correlations. To encode voxel activity, BrainMixer fuses information across both time and voxel dimensions via a dynamic attention mechanism. To learn the structure of the functional connectivity, BrainMixer presents a temporal graph patching and encodes each patch by combining its nodes’ features via a new adaptive temporal pooling. Our experiments show that BrainMixer attains outstanding performance and outperforms 14 baselines in different downstream tasks and setups.