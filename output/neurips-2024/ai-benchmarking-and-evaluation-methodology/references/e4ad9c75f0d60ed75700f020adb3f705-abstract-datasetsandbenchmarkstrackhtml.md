---
title: "INQUIRE: A Natural World Text-to-Image Retrieval Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e4ad9c75f0d60ed75700f020adb3f705-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['text-to-image-retrieval', 'benchmark', 'natural-world']
venue: "NeurIPS 2024"
tldr: "INQUIRE is an expert-level text-to-image retrieval benchmark over five million natural world images paired with 250 specialist queries."
---

# INQUIRE: A Natural World Text-to-Image Retrieval Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e4ad9c75f0d60ed75700f020adb3f705-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e4ad9c75f0d60ed75700f020adb3f705-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: INQUIRE is an expert-level text-to-image retrieval benchmark over five million natural world images paired with 250 specialist queries.

## Abstract

We introduce INQUIRE, a text-to-image retrieval benchmark designed to challenge multimodal vision-language models on expert-level queries. INQUIRE includes iNaturalist 2024 (iNat24), a new dataset of five million natural world images, along with 250 expert-level retrieval queries. These queries are paired with all relevant images comprehensively labeled within iNat24, comprising 33,000 total matches. Queries span categories such as species identification, context, behavior, and appearance, emphasizing tasks that require nuanced image understanding and domain expertise. Our benchmark evaluates two core retrieval tasks: (1) INQUIRE-Fullrank, a full dataset ranking task, and (2) INQUIRE-Rerank, a reranking task for refining top-100 retrievals. Detailed evaluation of a range of recent multimodal models demonstrates that INQUIRE poses a significant challenge, with the best models failing to achieve an mAP@50 above 50%. In addition, we show that reranking with more powerful multimodal models can enhance retrieval performance, yet there remains a significant margin for improvement. By focusing on scientifically-motivated ecological challenges, INQUIRE aims to bridge the gap between AI capabilities and the needs of real-world scientific inquiry, encouraging the development of retrieval systems that can assist with accelerating ecological and biodiversity research.