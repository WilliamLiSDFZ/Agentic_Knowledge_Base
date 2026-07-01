---
title: "BiVLC: Extending Vision-Language Compositionality Evaluation with Text-to-Image Retrieval"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b8b93c48f5bfa385d071342089d70422-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['vision-language-compositionality', 'bidirectional-retrieval', 'benchmark']
venue: "NeurIPS 2024"
tldr: "BiVLC extends compositionality evaluation benchmarks to include text-to-image retrieval alongside image-to-text for more complete assessment of VLMs."
---

# BiVLC: Extending Vision-Language Compositionality Evaluation with Text-to-Image Retrieval

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b8b93c48f5bfa385d071342089d70422-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b8b93c48f5bfa385d071342089d70422-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: BiVLC extends compositionality evaluation benchmarks to include text-to-image retrieval alongside image-to-text for more complete assessment of VLMs.

## Abstract

Existing Vision-Language Compositionality (VLC) benchmarks like SugarCrepe are formulated as image-to-text retrieval problems, where, given an image, the models need to select between the correct textual description and a synthetic hard negative text. In this work, we present the Bidirectional Vision-Language Compositionality (BiVLC) dataset. The novelty of BiVLC is to add a synthetic hard negative image generated from the synthetic text, resulting in two image-to-text retrieval examples (one for each image) and, more importantly, two text-to-image retrieval examples (one for each text). Human annotators filter out ill-formed examples ensuring the validity of the benchmark. The experiments on BiVLC uncover a weakness of current multimodal models, as they perform poorly in the text-to-image direction. In fact, when considering both retrieval directions, the conclusions obtained in previous works change significantly. In addition to the benchmark, weshow that a contrastive model trained using synthetic images and texts significantly improves over the base model in SugarCrepe and in BiVLC for both retrieval directions. The gap to human performance in BiVLC confirms that Vision-Language Compositionality is still a challenging problem.