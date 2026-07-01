---
title: "LucidAction: A Hierarchical and Multi-model Dataset for Comprehensive Action Quality Assessment"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/aecf6978509d8b306f74c0d09508f9bc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'audio-visual-speech-processing-and-benchmarks']
tags: ['action-quality-assessment', 'multimodal-dataset', 'hierarchical-annotation']
venue: "NeurIPS 2024"
tldr: "LucidAction is a hierarchical multi-modal dataset for comprehensive action quality assessment addressing limitations of existing mono-modal benchmarks."
---

# LucidAction: A Hierarchical and Multi-model Dataset for Comprehensive Action Quality Assessment

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/aecf6978509d8b306f74c0d09508f9bc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/aecf6978509d8b306f74c0d09508f9bc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: LucidAction is a hierarchical multi-modal dataset for comprehensive action quality assessment addressing limitations of existing mono-modal benchmarks.

## Abstract

Action Quality Assessment (AQA) research confronts formidable obstacles due to limited, mono-modal datasets sourced from one-shot competitions, which hinder the generalizability and comprehensiveness of AQA models. To address these limitations, we present LucidAction, the first systematically collected multi-view AQA dataset structured on curriculum learning principles. LucidAction features a three-tier hierarchical structure, encompassing eight diverse sports events with four curriculum levels, facilitating sequential skill mastery and supporting a wide range of athletic abilities. The dataset encompasses multi-modal data, including multi-view RGB video, 2D and 3D pose sequences, enhancing the richness of information available for analysis. Leveraging a high-precision multi-view Motion Capture (MoCap) system ensures precise capture of complex movements. Meticulously annotated data, incorporating detailed penalties from professional gymnasts, ensures the establishment of robust and comprehensive ground truth annotations. Experimental evaluations employing diverse contrastive regression baselines on LucidAction elucidate the dataset's complexities. Through ablation studies, we investigate the advantages conferred by multi-modal data and fine-grained annotations, offering insights into improving AQA performance. The data and code will be openly released to support advancements in the AI sports field.