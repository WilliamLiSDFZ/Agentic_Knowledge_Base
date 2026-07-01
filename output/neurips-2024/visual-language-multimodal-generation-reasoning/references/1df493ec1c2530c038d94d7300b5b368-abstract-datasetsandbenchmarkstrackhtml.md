---
title: "LVD-2M: A Long-take Video Dataset with Temporally Dense Captions"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1df493ec1c2530c038d94d7300b5b368-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'time-series-forecasting-and-analysis']
tags: ['video-generation', 'long-video', 'dense-captions', 'training-dataset', 'temporal']
venue: "NeurIPS 2024"
tldr: "Presents LVD-2M, a long-take video dataset with temporally dense captions designed to improve long video generation model training."
---

# LVD-2M: A Long-take Video Dataset with Temporally Dense Captions

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1df493ec1c2530c038d94d7300b5b368-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1df493ec1c2530c038d94d7300b5b368-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents LVD-2M, a long-take video dataset with temporally dense captions designed to improve long video generation model training.

## Abstract

The efficacy of video generation models heavily depends on the quality of their training datasets. Most previous video generation models are trained on short video clips, while recently there has been increasing interest in training long video generation models directly on longer videos. However, the lack of such high-quality long videos impedes the advancement long video generation. To promote research in long video generation, we desire a new dataset with four key features essential for training long video generation models: (1) long videos covering at least 10 seconds, (2) long-take videos without cuts, (3) large motion and diverse contents, and (4) temporally dense captions. To achieve this, we introduce a new pipeline for filtering high-quality long-take videos and generating temporally dense captions. Specifically, we define a set of metrics to quantitatively assess video quality including scene cuts, dynamic degrees, and semantic-level scores, enabling us to filter high-quality long-take videos from a large amount of source videos. Subsequently, we develop a hierarchical video captioning pipeline to annotate long videos with temporally-dense captions. With this pipeline, we curate the first long-take video dataset, LVD-2M, comprising 2 million long-take videos, each covering more than 10 seconds and annotated with temporally dense captions. We further validate the effectiveness of LVD-2M by fine-tuning video generation models to generate long videos with dynamic motions. We believe it will significantly contribute to future research in long video generation.