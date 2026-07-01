---
title: "FUSU: A Multi-temporal-source Land Use Change Segmentation Dataset for Fine-grained Urban Semantic Understanding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/eeb3df2d70affd52f65ff3b9abb32487-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['urban-building-environment-data-infrastructure']
tags: ['land-use-change', 'urban-segmentation', 'multi-temporal-remote-sensing']
venue: "NeurIPS 2024"
tldr: "A multi-temporal multi-source dataset for fine-grained urban land use change segmentation from remote sensing imagery."
---

# FUSU: A Multi-temporal-source Land Use Change Segmentation Dataset for Fine-grained Urban Semantic Understanding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/eeb3df2d70affd52f65ff3b9abb32487-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/eeb3df2d70affd52f65ff3b9abb32487-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A multi-temporal multi-source dataset for fine-grained urban land use change segmentation from remote sensing imagery.

## Abstract

Fine urban change segmentation using multi-temporal remote sensing images is essential for understanding human-environment interactions in urban areas. Although there have been advances in high-quality land cover datasets that reveal the physical features of urban landscapes, the lack of fine-grained land use datasets hinders a deeper understanding of how human activities are distributed across landscapes and the impact of these activities on the environment, thus constraining proper technique development. To address this, we introduce FUSU, the first fine-grained land use change segmentation dataset for Fine-grained Urban Semantic Understanding. FUSU features the most detailed land use classification system to date, with 17 classes and 30 billion pixels of annotations. It includes bi-temporal high-resolution satellite images with 0.2-0.5 m ground sample distance and monthly optical and radar satellite time series, covering 847 km^2 across five urban areas in the southern and northern of China with different geographical features. The fine-grained land use pixel-wise annotations and high spatial-temporal resolution data provide a robust foundation for developing proper deep learning models to provide contextual insights on human activities and urbanization. To fully leverage FUSU, we propose a unified time-series architecture for both change detection and segmentation. We benchmark FUSU on various methods for several tasks. Dataset and code are available at: https://github.com/yuanshuai0914/FUSU.