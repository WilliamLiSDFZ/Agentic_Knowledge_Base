---
title: "JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/734abb86d3caa949f44da8a093717f61-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['vision-language-benchmark', 'multimodal-evaluation', 'generated-images', 'visual-understanding', 'language-bias']
venue: "NeurIPS 2024"
tldr: "Introduces JourneyBench, a challenging VLU benchmark using generated images to reduce language bias and test deeper visual understanding."
---

# JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/734abb86d3caa949f44da8a093717f61-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/734abb86d3caa949f44da8a093717f61-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces JourneyBench, a challenging VLU benchmark using generated images to reduce language bias and test deeper visual understanding.

## Abstract

Existing vision-language understanding benchmarks largely consist of images of objects in their usual contexts.As a consequence, recent multimodal large language models can perform well with only a shallow visual understanding by relying on background language biases. Thus, strong performance on these benchmarks does not necessarily correlate with strong visual understanding. In this paper, we release JourneyBench, a comprehensive human-annotated benchmark of generated images designed to assess the model's fine-grained multimodal reasoning abilities across five tasks: complementary multimodal chain of thought, multi-image VQA, imaginary image captioning, VQA with hallucination triggers, and fine-grained retrieval with sample-specific distractors.Unlike existing benchmarks, JourneyBench explicitly requires fine-grained multimodal reasoning in unusual imaginary scenarios where language bias and holistic image gist are insufficient. We benchmark state-of-the-art models on JourneyBench and analyze performance along a number of fine-grained dimensions. Results across all five tasks show that JourneyBench is exceptionally challenging for even the best models, indicating that models' visual reasoning abilities are not as strong as they first appear. We discuss the implications of our findings and propose avenues for further research.