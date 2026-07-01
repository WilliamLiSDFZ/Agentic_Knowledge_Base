---
title: "A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/80f0cd0305f7741659304f5325f3bf6d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['referring-expression-comprehension', 'human-centric', 'multimodal-benchmark']
venue: "NeurIPS 2024"
tldr: "A large-scale benchmark for evaluating large multimodal models on human-centric referring expression comprehension tasks."
---

# A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/80f0cd0305f7741659304f5325f3bf6d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/80f0cd0305f7741659304f5325f3bf6d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large-scale benchmark for evaluating large multimodal models on human-centric referring expression comprehension tasks.

## Abstract

Prior research in human-centric AI has primarily addressed single-modality tasks like pedestrian detection, action recognition, and pose estimation. However, the emergence of large multimodal models (LMMs) such as GPT-4V has redirected attention towards integrating language with visual content. Referring expression comprehension (REC) represents a prime example of this multimodal approach. Current human-centric REC benchmarks, typically sourced from general datasets, fall short in the LMM era due to their limitations, such as insufficient testing samples, overly concise referring expressions, and limited vocabulary, making them inadequate for evaluating the full capabilities of modern REC models. In response, we present HC-RefLoCo (Human-Centric Referring Expression Comprehension with Long Context), a benchmark that includes 13,452 images, 24,129 instances, and 44,738 detailed annotations, encompassing a vocabulary of 18,681 words. Each annotation, meticulously reviewed for accuracy, averages 93.2 words and includes topics such as appearance, human-object interaction, location, action, celebrity, and OCR. HC-RefLoCo provides a wider range of instance scales and diverse evaluation protocols, encompassing accuracy with various IoU criteria, scale-aware evaluation, and subject-specific assessments. Our experiments, which assess 24 models, highlight HC-RefLoCo’s potential to advance human-centric AI by challenging contemporary REC models with comprehensive and varied data. Our benchmark, along with the evaluation code, are available at https://github.com/ZhaoJingjing713/HC-RefLoCo.