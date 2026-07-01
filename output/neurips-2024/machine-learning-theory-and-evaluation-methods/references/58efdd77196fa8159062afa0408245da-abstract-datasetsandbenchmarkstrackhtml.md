---
title: "OAM-TCD: A globally diverse dataset of high-resolution tree cover maps"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/58efdd77196fa8159062afa0408245da-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['tree-cover-mapping', 'high-resolution-segmentation', 'remote-sensing']
venue: "NeurIPS 2024"
tldr: "Presents OAM-TCD, a globally diverse high-resolution dataset for deep learning-based tree cover segmentation and ecosystem monitoring."
---

# OAM-TCD: A globally diverse dataset of high-resolution tree cover maps

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/58efdd77196fa8159062afa0408245da-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/58efdd77196fa8159062afa0408245da-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents OAM-TCD, a globally diverse high-resolution dataset for deep learning-based tree cover segmentation and ecosystem monitoring.

## Abstract

Accurately quantifying tree cover is an important metric for ecosystem monitoring and for assessing progress in restored sites. Recent works have shown that deep learning-based segmentation algorithms are capable of accurately mapping trees at country and continental scales using high-resolution aerial and satellite imagery. Mapping at high (ideally sub-meter) resolution is necessary to identify individual trees, however there are few open-access datasets containing instance level annotations and those that exist are small or not geographically diverse. We present a novel open-access dataset for individual tree crown delineation (TCD) in high-resolution aerial imagery sourced from OpenAerialMap (OAM). Our dataset, OAM-TCD, comprises 5072 2048x2048 px images at 10 cm/px resolution with associated human-labeled instance masks for over 280k individual and 56k groups of trees. By sampling imagery from around the world, we are able to better capture the diversity and morphology of trees in different terrestrial biomes and in both urban and natural environments. Using our dataset, we train reference instance and semantic segmentation models that compare favorably to existing state-of-the-art models. We assess performance through k-fold cross-validation and comparison with existing datasets; additionally we demonstrate compelling results on independent aerial imagery captured over Switzerland and compare to municipal tree inventories and LIDAR-derived canopy maps in the city of Zurich. Our dataset, models and training/benchmark code are publicly released under permissive open-source licenses: Creative Commons (majority CC BY 4.0), and Apache 2.0 respectively.