---
title: "Revisiting Few-Shot Object Detection with Vision-Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/22b2067b8f680812624032025864c5a1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['few-shot-object-detection', 'vision-language-models', 'open-world', 'zero-shot', 'foundational-models']
venue: "NeurIPS 2024"
tldr: "Revisits few-shot object detection in the era of foundational vision-language models, revealing new insights on zero-shot baselines."
---

# Revisiting Few-Shot Object Detection with Vision-Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/22b2067b8f680812624032025864c5a1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/22b2067b8f680812624032025864c5a1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Revisits few-shot object detection in the era of foundational vision-language models, revealing new insights on zero-shot baselines.

## Abstract

The era of vision-language models (VLMs) trained on web-scale datasets challenges conventional formulations of “open-world" perception. In this work, we revisit the task of few-shot object detection (FSOD) in the context of recent foundational VLMs. First, we point out that zero-shot predictions from VLMs such as GroundingDINO significantly outperform state-of-the-art few-shot detectors (48 vs. 33 AP) on COCO. Despite their strong zero-shot performance, such foundation models may still be sub-optimal. For example, trucks on the web may be defined differently from trucks for a target applications such as autonomous vehicle perception. We argue that the task of few-shot recognition can be reformulated as aligning foundation models to target concepts using a few examples. Interestingly, such examples can be multi-modal, using both text and visual cues, mimicking instructions that are often given to human annotators when defining a target concept of interest. Concretely, we propose Foundational FSOD, a new benchmark protocol that evaluates detectors pre-trained on any external data and fine-tuned on multi-modal (text and visual) K-shot examples per target class. We repurpose nuImages for Foundational FSOD, benchmark several popular open-source VLMs, and provide an empirical analysis of state-of-the-art methods. Lastly, we discuss our recent CVPR 2024 Foundational FSOD competition and share insights from the community. Notably, the winning team significantly outperforms our baseline by 23.3 mAP!