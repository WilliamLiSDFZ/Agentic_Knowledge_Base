---
title: "ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/25b9960c8a5bd887eb5476c951260403-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['text-to-video', 'time-lapse', 'metamorphic-evaluation']
venue: "NeurIPS 2024"
tldr: "ChronoMagic-Bench, a benchmark evaluating temporal and metamorphic knowledge in text-to-time-lapse video generation models."
---

# ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/25b9960c8a5bd887eb5476c951260403-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/25b9960c8a5bd887eb5476c951260403-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ChronoMagic-Bench, a benchmark evaluating temporal and metamorphic knowledge in text-to-time-lapse video generation models.

## Abstract

We propose a novel text-to-video (T2V) generation benchmark, ChronoMagic-Bench, to evaluate the temporal and metamorphic knowledge skills in time-lapse video generation of the T2V models (e.g. Sora and Lumiere). Compared to existing benchmarks that focus on visual quality and text relevance of generated videos, ChronoMagic-Bench focuses on the models’ ability to generate time-lapse videos with significant metamorphic amplitude and temporal coherence. The benchmark probes T2V models for their physics, biology, and chemistry capabilities, in a free-form text control. For these purposes, ChronoMagic-Bench introduces 1,649 prompts and real-world videos as references, categorized into four major types of time-lapse videos: biological, human creation, meteorological, and physical phenomena, which are further divided into 75 subcategories. This categorization ensures a comprehensive evaluation of the models’ capacity to handle diverse and complex transformations. To accurately align human preference on the benchmark, we introduce two new automatic metrics, MTScore and CHScore, to evaluate the videos' metamorphic attributes and temporal coherence. MTScore measures the metamorphic amplitude, reflecting the degree of change over time, while CHScore assesses the temporal coherence, ensuring the generated videos maintain logical progression and continuity. Based on the ChronoMagic-Bench, we conduct comprehensive manual evaluations of eighteen representative T2V models, revealing their strengths and weaknesses across different categories of prompts, providing a thorough evaluation framework that addresses current gaps in video generation research. More encouragingly, we create a large-scale ChronoMagic-Pro dataset, containing 460k high-quality pairs of 720p time-lapse videos and detailed captions. Each caption ensures high physical content and large metamorphic amplitude, which have a far-reaching impact on the video generation community. The source data and code are publicly available on https://pku-yuangroup.github.io/ChronoMagic-Bench.