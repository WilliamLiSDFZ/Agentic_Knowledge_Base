---
title: "Kuro Siwo: 33 billion $m^2$ under the water. A global multi-temporal satellite dataset for rapid flood mapping"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/43612b0662cb6a4986edf859fd6ebafe-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'radar-based-scene-understanding-deep-learning']
tags: ['flood-mapping', 'satellite-imagery', 'multi-temporal-dataset']
venue: "NeurIPS 2024"
tldr: "Presents a large-scale global multi-temporal satellite dataset for rapid flood mapping covering 33 billion square meters."
---

# Kuro Siwo: 33 billion $m^2$ under the water. A global multi-temporal satellite dataset for rapid flood mapping

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/43612b0662cb6a4986edf859fd6ebafe-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/43612b0662cb6a4986edf859fd6ebafe-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents a large-scale global multi-temporal satellite dataset for rapid flood mapping covering 33 billion square meters.

## Abstract

Global flash floods, exacerbated by climate change, pose severe threats to humanlife, infrastructure, and the environment. Recent catastrophic events in Pakistan andNew Zealand underscore the urgent need for precise flood mapping to guide restoration efforts, understand vulnerabilities, and prepare for future occurrences. While Synthetic Aperture Radar (SAR) remote sensing offers day-and-night, all-weatherimaging capabilities, its application in deep learning for flood segmentation is limited by the lack of large annotated datasets. To address this, we introduce KuroSiwo, a manually annotated multi-temporal dataset, spanning 43 flood events globally. Our dataset maps more than 338 billion $m^2$ of land, with 33 billion designatedas either flooded areas or permanent water bodies. Kuro Siwo includes a highlyprocessed product optimized for flash flood mapping based on SAR Ground RangeDetected, and a primal SAR Single Look Complex product with minimal preprocessing, designed to promote research on the exploitation of both the phase and amplitude information and to offer maximum flexibility for downstream task preprocessing. To leverage advances in large scale self-supervised pretraining methodsfor remote sensing data, we augment Kuro Siwo with a large unlabeled set of SARsamples. Finally, we provide an extensive benchmark, namely BlackBench, offering strong baselines for a diverse set of flood events globally. All data and code arepublished in our Github repository: https://github.com/Orion-AI-Lab/KuroSiwo.