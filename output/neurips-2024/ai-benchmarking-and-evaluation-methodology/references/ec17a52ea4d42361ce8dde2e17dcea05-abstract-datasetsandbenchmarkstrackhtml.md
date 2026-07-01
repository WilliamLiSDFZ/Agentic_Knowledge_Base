---
title: "VastTrack: Vast Category Visual Object Tracking"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ec17a52ea4d42361ce8dde2e17dcea05-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['visual-object-tracking', 'benchmark', 'large-scale-categories']
venue: "NeurIPS 2024"
tldr: "Introduces VastTrack, a large-scale visual tracking benchmark covering 2,115 object categories to promote general tracking research."
---

# VastTrack: Vast Category Visual Object Tracking

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ec17a52ea4d42361ce8dde2e17dcea05-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ec17a52ea4d42361ce8dde2e17dcea05-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces VastTrack, a large-scale visual tracking benchmark covering 2,115 object categories to promote general tracking research.

## Abstract

In this paper, we propose a novel benchmark, named VastTrack, aiming to facilitate the development of general visual tracking via encompassing abundant classes and videos. VastTrack consists of a few attractive properties: (1) Vast Object Category. In particular, it covers targets from 2,115 categories, significantly surpassing object classes of existing popular benchmarks (e.g., GOT-10k with 563 classes and LaSOT with 70 categories). Through providing such vast object classes, we expect to learn more general object tracking. (2) Larger scale. Compared with current benchmarks, VastTrack provides 50,610 videos with 4.2 million frames, which makes it to date the largest dataset in term of the number of videos, and hence could benefit training even more powerful visual trackers in the deep learning era. (3) Rich Annotation. Besides conventional bounding box annotations, VastTrack also provides linguistic descriptions with more than 50K sentences for the videos. Such rich annotations of VastTrack enable the development of both vision-only and vision-language tracking. In order to ensure precise annotation, each frame in the videos is manually labeled with multi-stage of careful inspections and refinements. To understand performance of existing trackers and to provide baselines for future comparison, we extensively evaluate 25 representative trackers. The results, not surprisingly, display significant drops compared to those on current datasets due to lack of abundant categories and videos from diverse scenarios for training, and more efforts are urgently required to improve general visual tracking. Our VastTrack, the toolkit, and evaluation results are publicly available at https://github.com/HengLan/VastTrack.