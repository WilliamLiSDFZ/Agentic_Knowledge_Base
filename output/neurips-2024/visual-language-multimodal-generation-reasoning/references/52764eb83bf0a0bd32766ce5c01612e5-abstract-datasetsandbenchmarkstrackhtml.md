---
title: "II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/52764eb83bf0a0bd32766ce5c01612e5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning']
tags: ['multimodal-llm', 'image-implication', 'visual-reasoning-benchmark']
venue: "NeurIPS 2024"
tldr: "Proposes II-Bench, a benchmark evaluating multimodal LLMs on understanding implicit meanings and implications in images."
---

# II-Bench: An Image Implication Understanding Benchmark for Multimodal Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/52764eb83bf0a0bd32766ce5c01612e5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/52764eb83bf0a0bd32766ce5c01612e5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Proposes II-Bench, a benchmark evaluating multimodal LLMs on understanding implicit meanings and implications in images.

## Abstract

The rapid advancements in the development of multimodal large language models (MLLMs) have consistently led to new breakthroughs on various benchmarks. In response, numerous challenging and comprehensive benchmarks have been proposed to more accurately assess the capabilities of MLLMs. However, there is a dearth of exploration of the higher-order perceptual capabilities of MLLMs. To fill this gap, we propose the Image Implication understanding Benchmark, II-Bench, which aims to evaluate the model's higher-order perception of images. Through extensive experiments on II-Bench across multiple MLLMs, we have made significant findings. Initially, a substantial gap is observed between the performance of MLLMs and humans on II-Bench. The pinnacle accuracy of MLLMs attains 74.8%, whereas human accuracy averages 90%, peaking at an impressive 98%. Subsequently, MLLMs perform worse on abstract and complex images, suggesting limitations in their ability to understand high-level semantics and capture image details. Finally, it is observed that most models exhibit enhanced accuracy when image sentiment polarity hints are incorporated into the prompts. This observation underscores a notable deficiency in their inherent understanding of image sentiment. We believe that II-Bench will inspire the community to develop the next generation of MLLMs, advancing the journey towards expert  artificial general intelligence (AGI). II-Bench is publicly available at https://huggingface.co/datasets/m-a-p/II-Bench.