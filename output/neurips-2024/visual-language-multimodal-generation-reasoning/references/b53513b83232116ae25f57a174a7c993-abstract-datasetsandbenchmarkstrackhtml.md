---
title: "Enhancing vision-language models for medical imaging: bridging the 3D gap with innovative slice selection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b53513b83232116ae25f57a174a7c993-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'llm-benchmarks-for-clinical-healthcare']
tags: ['vision-language-models', 'medical-imaging', '3D-slice-selection']
venue: "NeurIPS 2024"
tldr: "Bridges the 2D-to-3D gap in vision-language models for medical imaging through an innovative slice selection strategy."
---

# Enhancing vision-language models for medical imaging: bridging the 3D gap with innovative slice selection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b53513b83232116ae25f57a174a7c993-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b53513b83232116ae25f57a174a7c993-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Bridges the 2D-to-3D gap in vision-language models for medical imaging through an innovative slice selection strategy.

## Abstract

Recent approaches to vision-language tasks are built on the remarkable capabilities of large vision-language models (VLMs). These models excel in zero-shot and few-shot learning, enabling them to learn new tasks without parameter updates. However, their primary challenge lies in their design, which primarily accommodates 2D input, thus limiting their effectiveness for medical images, particularly radiological images like MRI and CT, which are typically 3D. To bridge the gap between state-of-the-art 2D VLMs and 3D medical image data, we developed an innovative, one-pass, unsupervised representative slice selection method called Vote-MI, which selects representative 2D slices from 3D medical imaging. To evaluate the effectiveness of vote-MI when implemented with VLMs, we introduce BrainMD, a robust, multimodal dataset comprising 2,453 annotated 3D MRI brain scans with corresponding textual radiology reports and electronic health records. Based on BrainMD, we further develop two benchmarks, BrainMD-select (including the most representative 2D slice of 3D image) and BrainBench (including various vision-language downstream tasks). Extensive experiments on the BrainMD dataset and its two corresponding benchmarks demonstrate that our representative selection method significantly improves performance in zero-shot and few-shot learning tasks. On average, Vote-MI achieves a 14.6\% and 16.6\% absolute gain for zero-shot and few-shot learning, respectively, compared to randomly selecting examples. Our studies represent a significant step toward integrating AI in medical imaging to enhance patient care and facilitate medical research. We hope this work will serve as a foundation for data selection as vision-language models are increasingly applied to new tasks.