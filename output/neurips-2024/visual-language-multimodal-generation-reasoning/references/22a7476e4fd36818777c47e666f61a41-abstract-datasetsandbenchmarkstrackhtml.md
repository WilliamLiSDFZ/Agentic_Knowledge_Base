---
title: "ShareGPT4Video: Improving Video Understanding and Generation with Better Captions"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/22a7476e4fd36818777c47e666f61a41-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['video-understanding', 'video-captioning', 'GPT4V', 'large-video-language-models', 'text-to-video']
venue: "NeurIPS 2024"
tldr: "ShareGPT4Video improves video understanding and generation by providing dense, precise GPT4V-annotated video captions."
---

# ShareGPT4Video: Improving Video Understanding and Generation with Better Captions

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/22a7476e4fd36818777c47e666f61a41-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/22a7476e4fd36818777c47e666f61a41-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ShareGPT4Video improves video understanding and generation by providing dense, precise GPT4V-annotated video captions.

## Abstract

We present the ShareGPT4Video series, aiming to facilitate the video understanding of large video-language models (LVLMs) and the video generation of text-to-video models (T2VMs) via dense and precise captions. The series comprises: 1) ShareGPT4Video, 40K GPT4V annotated dense captions of videos with various lengths and sources, developed through carefully designed data filtering and annotating strategy. 2) ShareCaptioner-Video, an efficient and capable captioning model for arbitrary videos, with 4.8M high-quality aesthetic videos annotated by it. 3) ShareGPT4Video-8B, a simple yet superb LVLM that reached SOTA performance on three advancing video benchmarks. To achieve this, taking aside the non-scalable costly human annotators, we find using GPT4V to caption video with a naive multi-frame or frame-concatenation input strategy leads to less detailed and sometimes temporal-confused results. We argue the challenge of designing a high-quality video captioning strategy lies in three aspects: 1) Inter-frame precise temporal change understanding. 2) Intra-frame detailed content description. 3) Frame-number scalability for arbitrary-length videos. To this end, we meticulously designed a differential video captioning strategy, which is stable, scalable, and efficient for generating captions for videos with arbitrary resolution, aspect ratios, and length. Based on it, we construct ShareGPT4Video, which contains 40K high-quality videos spanning a wide range of categories, and the resulting captions encompass rich world knowledge, object attributes, camera movements, and crucially, detailed and precise temporal descriptions of events. Based on ShareGPT4Video, we further develop ShareCaptioner-Video, a superior captioner capable of efficiently generating high-quality captions for arbitrary videos. We annotated 4.8M aesthetically appealing videos by it and verified their effectiveness on a 10-second text2video generation task. For video understanding, we verified the effectiveness of ShareGPT4Video on several current LVLM architectures and presented our superb new LVLM ShareGPT4Video-8B. All the models, strategies, and annotations will be open-sourced and we hope this project can serve as a pivotal resource for advancing both the LVLMs and T2VMs community.