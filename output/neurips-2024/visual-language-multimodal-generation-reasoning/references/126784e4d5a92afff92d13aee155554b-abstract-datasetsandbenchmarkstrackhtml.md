---
title: "UKnow: A Unified Knowledge Protocol with Multimodal Knowledge Graph Datasets for Reasoning and Vision-Language Pre-Training"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/126784e4d5a92afff92d13aee155554b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['knowledge-graph', 'multimodal-reasoning', 'vision-language-pretraining']
venue: "NeurIPS 2024"
tldr: "UKnow presents a unified knowledge protocol with multimodal knowledge graph datasets spanning five knowledge types for vision-language reasoning."
---

# UKnow: A Unified Knowledge Protocol with Multimodal Knowledge Graph Datasets for Reasoning and Vision-Language Pre-Training

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/126784e4d5a92afff92d13aee155554b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/126784e4d5a92afff92d13aee155554b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: UKnow presents a unified knowledge protocol with multimodal knowledge graph datasets spanning five knowledge types for vision-language reasoning.

## Abstract

This work presents a unified knowledge protocol, called UKnow, which facilitates knowledge-based studies from the perspective of data. Particularly focusing on visual and linguistic modalities, we categorize data knowledge into five unit types, namely, in-image, in-text, cross-image, cross-text, and image-text, and set up an efficient pipeline to help construct the multimodal knowledge graph from any data collection. Thanks to the logical information naturally contained in knowledge graph, organizing datasets under UKnow format opens up more possibilities of data usage compared to the commonly used image-text pairs. Following UKnow protocol, we collect, from public international news, a large-scale multimodal knowledge graph dataset that consists of 1,388,568 nodes (with 571,791 vision-related ones) and 3,673,817 triplets. The dataset is also annotated with rich event tags, including 11 coarse labels and 9,185 fine labels. Experiments on four benchmarks demonstrate the potential of UKnow in supporting common-sense reasoning and boosting vision-language pre-training with a single dataset, benefiting from its unified form of knowledge organization. Code, dataset, and models will be made publicly available. See Appendix to download the dataset.