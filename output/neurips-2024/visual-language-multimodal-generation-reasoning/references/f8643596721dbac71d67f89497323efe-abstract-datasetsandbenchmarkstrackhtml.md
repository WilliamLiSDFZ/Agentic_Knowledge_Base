---
title: "ActionAtlas: A VideoQA Benchmark for Domain-specialized Action Recognition"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f8643596721dbac71d67f89497323efe-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['video-question-answering', 'benchmark', 'action-recognition', 'fine-grained', 'multimodal']
venue: "NeurIPS 2024"
tldr: "ActionAtlas is a VideoQA benchmark for evaluating multimodal models on domain-specialized fine-grained action recognition."
---

# ActionAtlas: A VideoQA Benchmark for Domain-specialized Action Recognition

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f8643596721dbac71d67f89497323efe-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f8643596721dbac71d67f89497323efe-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ActionAtlas is a VideoQA benchmark for evaluating multimodal models on domain-specialized fine-grained action recognition.

## Abstract

Our world is full of varied actions and moves in specialized fields that we, as humans, seek to identify and learn about. To evaluate the effectiveness of multi-modal models in helping us recognize such fine-grained actions, we introduce ActionAtlas, a video question answering (VideoQA) benchmark on fine-grained action recognition with short videos across various sports. ActionAtlas contains 554 videos spanning 284 actions across 42 sports with 1161 actions as total potential choices. Unlike most existing action recognition benchmarks that focus on simplistic actions, often identifiable from a single frame, ActionAtlas focuses on intricate movements and tests the models' ability to discern subtle differences. Additionally, each video in ActionAtlas also includes a question, which helps to more accurately pinpoint the action's performer in scenarios where multiple individuals are involved in different activities. We evaluate proprietary and open models on this benchmark and show that the state-of-the-art models only perform at most 48.73% accurately where random chance is 20%. Furthermore, our results show that a high frame sampling rate is essential for recognizing actions in ActionAtlas, a feature that current top proprietary models like Gemini lack in their default settings.