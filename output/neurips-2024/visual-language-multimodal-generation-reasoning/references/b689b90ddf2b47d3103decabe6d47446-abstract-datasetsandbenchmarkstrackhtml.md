---
title: "Streaming Detection of Queried Event Start"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b689b90ddf2b47d3103decabe6d47446-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['autonomous-driving-and-trajectory-prediction', 'visual-language-multimodal-generation-reasoning']
tags: ['streaming-detection', 'event-start', 'multimodal-video', 'autonomous-systems', 'real-time']
venue: "NeurIPS 2024"
tldr: "Introduces Streaming Detection of Queried Event Start (SDQES), a novel task for real-time multimodal video understanding in embodied applications."
---

# Streaming Detection of Queried Event Start

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b689b90ddf2b47d3103decabe6d47446-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b689b90ddf2b47d3103decabe6d47446-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces Streaming Detection of Queried Event Start (SDQES), a novel task for real-time multimodal video understanding in embodied applications.

## Abstract

Robotics, autonomous driving, augmented reality, and many embodied computer vision applications must quickly react to user-defined events unfolding in real time. We address this setting by proposing a novel task for multimodal video understanding---Streaming Detection of Queried Event Start (SDQES).The goal of SDQES is to identify the beginning of a complex event as described by a natural language query, with high accuracy and low latency. We introduce a new benchmark based on  the Ego4D dataset, as well as new task-specific metrics to study streaming multimodal detection of diverse events in an egocentric video setting.Inspired by parameter-efficient fine-tuning methods in NLP and for video tasks, we propose adapter-based baselines that enable image-to-video transfer learning, allowing for efficient online video modeling.We evaluate three vision-language backbones and three adapter architectures on both short-clip and untrimmed video settings.