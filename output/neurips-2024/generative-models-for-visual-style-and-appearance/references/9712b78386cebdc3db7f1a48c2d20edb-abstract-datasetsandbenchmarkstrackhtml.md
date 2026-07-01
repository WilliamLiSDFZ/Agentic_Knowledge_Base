---
title: "Codec Avatar Studio: Paired Human Captures for Complete, Driveable, and Generalizable Avatars"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9712b78386cebdc3db7f1a48c2d20edb-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['generative-models-for-visual-style-and-appearance', 'visual-language-multimodal-generation-reasoning']
tags: ['photorealistic-avatars', 'human-modeling', 'paired-captures', 'full-body', 'generalization']
venue: "NeurIPS 2024"
tldr: "Presents Codec Avatar Studio using paired human captures to build complete, driveable, and generalizable photorealistic full-body avatars."
---

# Codec Avatar Studio: Paired Human Captures for Complete, Driveable, and Generalizable Avatars

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9712b78386cebdc3db7f1a48c2d20edb-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9712b78386cebdc3db7f1a48c2d20edb-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents Codec Avatar Studio using paired human captures to build complete, driveable, and generalizable photorealistic full-body avatars.

## Abstract

To build photorealistic avatars that users can embody, human modelling must be complete (cover the full body), driveable (able to reproduce the current motion and appearance from the user), and generalizable (i.e., easily adaptable to novel identities).Towards these goals, paired captures, that is, captures of the same subject obtained from systems of diverse quality and availability, are crucial.However, paired captures are rarely available to researchers outside of dedicated industrial labs: Codec Avatar Studio is our proposal to close this gap.Towards generalization and driveability, we introduce a dataset of 256 subjects captured in two modalities: high resolution multi-view scans of their heads, and video from the internal cameras of a headset.Towards completeness, we introduce a dataset of 4 subjects captured in eight modalities: high quality relightable multi-view captures of heads and hands, full body multi-view captures with minimal and regular clothes, and corresponding head, hands and body phone captures.Together with our data, we also provide code and pre-trained models for different state-of-the-art human generation models.Our datasets and code are available at https://github.com/facebookresearch/ava-256 and https://github.com/facebookresearch/goliath.