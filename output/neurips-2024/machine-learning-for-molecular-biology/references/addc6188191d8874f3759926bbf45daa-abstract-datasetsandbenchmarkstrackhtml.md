---
title: "MultiOrg: A Multi-rater Organoid-detection Dataset"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/addc6188191d8874f3759926bbf45daa-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-for-molecular-biology']
tags: ['organoid-detection', 'multi-rater', 'biomedical-imaging']
venue: "NeurIPS 2024"
tldr: "Presents MultiOrg, a multi-rater annotated dataset for high-throughput organoid detection in biomedical imaging."
---

# MultiOrg: A Multi-rater Organoid-detection Dataset

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/addc6188191d8874f3759926bbf45daa-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/addc6188191d8874f3759926bbf45daa-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents MultiOrg, a multi-rater annotated dataset for high-throughput organoid detection in biomedical imaging.

## Abstract

High-throughput image analysis in the biomedical domain has gained significant attention in recent years, driving advancements in drug discovery, disease prediction, and personalized medicine. Organoids, specifically, are an active area of research, providing excellent models for human organs and their functions. Automating the quantification of organoids in microscopy images would provide an effective solution to overcome substantial manual quantification bottlenecks, particularly in high-throughput image analysis. However, there is a notable lack of open biomedical datasets, in contrast to other domains, such as autonomous driving, and, notably, only few of them have attempted to quantify annotation uncertainty. In this work, we present MultiOrg a comprehensive organoid dataset tailored for object detection tasks with uncertainty quantification. This dataset comprises over 400 high-resolution 2d microscopy images and curated annotations of more than 60,000 organoids. Most importantly, it includes three label sets for the test data, independently annotated by two experts at distinct time points. We additionally provide a benchmark for organoid detection, and make the best model available through an easily installable, interactive plugin for the popular image visualization tool Napari, to perform organoid quantification.