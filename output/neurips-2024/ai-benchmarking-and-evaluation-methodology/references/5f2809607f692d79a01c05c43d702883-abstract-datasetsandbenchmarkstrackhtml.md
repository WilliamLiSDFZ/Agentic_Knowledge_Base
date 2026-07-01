---
title: "HourVideo: 1-Hour Video-Language Understanding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5f2809607f692d79a01c05c43d702883-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['video-language-understanding', 'long-video-benchmark', 'visual-reasoning']
venue: "NeurIPS 2024"
tldr: "HourVideo is a benchmark for hour-long video-language understanding spanning summarization, perception, visual reasoning, and navigation tasks."
---

# HourVideo: 1-Hour Video-Language Understanding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5f2809607f692d79a01c05c43d702883-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5f2809607f692d79a01c05c43d702883-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: HourVideo is a benchmark for hour-long video-language understanding spanning summarization, perception, visual reasoning, and navigation tasks.

## Abstract

We present HourVideo, a benchmark dataset for hour-long video-language understanding. Our dataset consists of a novel task suite comprising summarization, perception (recall, tracking), visual reasoning (spatial, temporal, predictive, causal, counterfactual), and navigation (room-to-room, object retrieval) tasks. HourVideo includes 500 manually curated egocentric videos from the Ego4D dataset, spanning durations of 20 to 120 minutes, and features 12,976 high-quality, five-way multiple-choice questions. Benchmarking results reveal that multimodal models, including GPT-4 and LLaVA-NeXT, achieve marginal improvements over random chance. In stark contrast, human experts significantly outperform the state-of-the-art long-context multimodal model, Gemini Pro 1.5 (85.0\% vs. 37.3\%), highlighting a substantial gap in multimodal capabilities. Our benchmark, evaluation toolkit, prompts, and documentation are available at https://hourvideo.stanford.edu.