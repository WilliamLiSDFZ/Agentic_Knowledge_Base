---
title: "UrbanDataLayer: A Unified Data Pipeline for Urban Science"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0db7f135f6991e8cec5e516ecc66bfba-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['urban-building-environment-data-infrastructure', 'ai-benchmarking-and-evaluation-methodology']
tags: ['urban-data', 'unified-pipeline', 'urban-computing', 'data-infrastructure', 'geospatial']
venue: "NeurIPS 2024"
tldr: "UrbanDataLayer provides a unified data pipeline standardizing diverse urban datasets to facilitate urban science research."
---

# UrbanDataLayer: A Unified Data Pipeline for Urban Science

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0db7f135f6991e8cec5e516ecc66bfba-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0db7f135f6991e8cec5e516ecc66bfba-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: UrbanDataLayer provides a unified data pipeline standardizing diverse urban datasets to facilitate urban science research.

## Abstract

The rapid progression of urbanization has generated a diverse array of urban data, facilitating significant advancements in urban science and urban computing. Current studies often work on separate problems case by case using diverse data, e.g., air quality prediction, and built-up areas classification. This fragmented approach hinders the urban research field from advancing at the pace observed in Computer Vision and Natural Language Processing, due to two primary reasons. On the one hand, the diverse data processing steps lead to the lack of large-scale benchmarks and therefore decelerate iterative methodology improvement on a single problem. On the other hand, the disparity in multi-modal data formats hinders the combination of the related modal data to stimulate more research findings. To address these challenges, we propose UrbanDataLayer (UDL), a suite of standardized data structures and pipelines for city data engineering, providing a unified data format for researchers. This allows researchers to easily build up large-scale benchmarks and combine multi-modal data, thus expediting the development of multi-modal urban foundation models. To verify the effectiveness of our work, we present four distinct urban problem tasks utilizing the proposed data layer. UrbanDataLayer aims to enhance standardization and operational efficiency within the urban science research community. The examples and source code are available at https://github.com/SJTU-CILAB/udl.