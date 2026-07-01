---
title: "STimage-1K4M: A histopathology image-gene expression dataset for spatial transcriptomics"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3ef2b740cb22dcce67c20989cb3d3fce-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'machine-learning-for-molecular-biology']
tags: ['spatial-transcriptomics', 'histopathology', 'image-gene-expression']
venue: "NeurIPS 2024"
tldr: "Presents STimage-1K4M, a large dataset pairing histopathology images with gene expression profiles for spatial transcriptomics research."
---

# STimage-1K4M: A histopathology image-gene expression dataset for spatial transcriptomics

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3ef2b740cb22dcce67c20989cb3d3fce-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3ef2b740cb22dcce67c20989cb3d3fce-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents STimage-1K4M, a large dataset pairing histopathology images with gene expression profiles for spatial transcriptomics research.

## Abstract

Recent advances in multi-modal algorithms have driven and been driven by the increasing availability of large image-text datasets, leading to significant strides in various fields, including computational pathology. However, in most existing medical image-text datasets, the text typically provides high-level summaries that may not sufficiently describe sub-tile regions within a large pathology image. For example, an image might cover an extensive tissue area containing cancerous and healthy regions, but the accompanying text might only specify that this image is a cancer slide, lacking the nuanced details needed for in-depth analysis. In this study, we introduce STimage-1K4M, a novel dataset designed to bridge this gap by providing genomic features for sub-tile images. STimage-1K4M contains 1,149 images derived from spatial transcriptomics data, which captures gene expression information at the level of individual spatial spots within a pathology image. Specifically, each image in the dataset is broken down into smaller sub-image tiles, with each tile paired with $15,000-30,000$ dimensional gene expressions. With $4,293,195$ pairs of sub-tile images and gene expressions, STimage-1K4M offers unprecedented granularity, paving the way for a wide range of advanced research in multi-modal data analysis an innovative applications in computational pathology, and beyond.