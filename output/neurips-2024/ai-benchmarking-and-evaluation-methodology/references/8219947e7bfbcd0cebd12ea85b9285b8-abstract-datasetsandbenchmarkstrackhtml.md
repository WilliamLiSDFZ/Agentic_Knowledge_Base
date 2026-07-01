---
title: "ViLCo-Bench: VIdeo Language COntinual learning Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8219947e7bfbcd0cebd12ea85b9285b8-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['continual-learning', 'video-language', 'benchmark']
venue: "NeurIPS 2024"
tldr: "ViLCo-Bench introduces a benchmark for evaluating video-language continual learning across tasks requiring retention of prior knowledge while adapting to new multimodal inputs."
---

# ViLCo-Bench: VIdeo Language COntinual learning Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8219947e7bfbcd0cebd12ea85b9285b8-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8219947e7bfbcd0cebd12ea85b9285b8-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ViLCo-Bench introduces a benchmark for evaluating video-language continual learning across tasks requiring retention of prior knowledge while adapting to new multimodal inputs.

## Abstract

Video language continual learning involves continuously adapting to information from video and text inputs, enhancing a model’s ability to handle new tasks while retaining prior knowledge. This field is a relatively under-explored area, and establishing appropriate datasets is crucial for facilitating communication and research in this field. In this study, we present the first dedicated benchmark, ViLCo-Bench, designed to evaluate continual learning models across a range of video-text tasks. The dataset comprises ten-minute-long videos and corresponding language queries collected from publicly available datasets. Additionally, we introduce a novel memory-efficient framework that incorporates self-supervised learning and mimics long-term and short-term memory effects. This framework addresses challenges including memory complexity from long video clips, natural language complexity from open queries, and text-video misalignment. We posit that ViLCo-Bench, with greater complexity compared to existing continual learning benchmarks, would serve as a critical tool for exploring the video-language domain, extending beyond conventional class-incremental tasks, and addressing complex and limited annotation issues. The curated data, evaluations, and our novel method are available at https://github.com/cruiseresearchgroup/ViLCo.