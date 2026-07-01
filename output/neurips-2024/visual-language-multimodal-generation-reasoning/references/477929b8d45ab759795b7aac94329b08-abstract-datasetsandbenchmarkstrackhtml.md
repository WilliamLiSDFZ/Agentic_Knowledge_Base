---
title: "VERIFIED: A Video Corpus Moment Retrieval Benchmark for Fine-Grained Video Understanding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/477929b8d45ab759795b7aac94329b08-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['video-retrieval', 'fine-grained-understanding', 'benchmark']
venue: "NeurIPS 2024"
tldr: "VERIFIED proposes a fine-grained video corpus moment retrieval benchmark requiring precise localization from detailed natural language queries."
---

# VERIFIED: A Video Corpus Moment Retrieval Benchmark for Fine-Grained Video Understanding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/477929b8d45ab759795b7aac94329b08-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/477929b8d45ab759795b7aac94329b08-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: VERIFIED proposes a fine-grained video corpus moment retrieval benchmark requiring precise localization from detailed natural language queries.

## Abstract

Existing Video Corpus Moment Retrieval (VCMR) is limited to coarse-grained understanding that hinders precise video moment localization when given fine-grained queries. In this paper, we propose a more challenging fine-grained VCMR benchmark requiring methods to localize the best-matched moment from the corpus with other partially matched candidates. To improve the dataset construction efficiency and guarantee high-quality data annotations, we propose VERIFIED, an automatic \underline{V}id\underline{E}o-text annotation pipeline to generate captions with \underline{R}el\underline{I}able \underline{FI}n\underline{E}-grained statics and \underline{D}ynamics. Specifically, we resort to large language models (LLM) and large multimodal models (LMM) with our proposed Statics and Dynamics Enhanced Captioning modules to generate diverse fine-grained captions for each video. To filter out the inaccurate annotations caused by the LLM hallucination, we propose a Fine-Granularity Aware Noise Evaluator where we fine-tune a video foundation model with disturbed hard-negatives augmented contrastive and matching losses. With VERIFIED, we construct a more challenging fine-grained VCMR benchmark containing Charades-FIG, DiDeMo-FIG, and ActivityNet-FIG which demonstrate a high level of annotation quality. We evaluate several state-of-the-art VCMR models on the proposed dataset, revealing that there is still significant scope for fine-grained video understanding in VCMR.