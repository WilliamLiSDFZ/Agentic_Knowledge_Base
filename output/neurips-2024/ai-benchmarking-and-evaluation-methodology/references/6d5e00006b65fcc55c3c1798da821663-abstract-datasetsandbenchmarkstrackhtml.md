---
title: "Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6d5e00006b65fcc55c3c1798da821663-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['benchmarking', 'generative-models', 'visual-programming', 'computational-thinking']
venue: "NeurIPS 2024"
tldr: "Benchmarks generative models on elementary visual programming tasks to reveal limitations in computational thinking despite strong general performance."
---

# Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6d5e00006b65fcc55c3c1798da821663-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6d5e00006b65fcc55c3c1798da821663-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Benchmarks generative models on elementary visual programming tasks to reveal limitations in computational thinking despite strong general performance.

## Abstract

Generative models have demonstrated human-level proficiency in various benchmarks across domains like programming, natural sciences, and general knowledge. Despite these promising results on competitive benchmarks, they still struggle with seemingly simple problem-solving tasks typically carried out by elementary-level students. How do state-of-the-art models perform on standardized programming-related tests designed to assess computational thinking and problem-solving skills at schools? In this paper, we curate a novel benchmark involving computational thinking tests grounded in elementary visual programming domains. Our initial results show that state-of-the-art models like GPT-4o and Llama3 barely match the performance of an average school student. To further boost the performance of these models, we fine-tune them using a novel synthetic data generation methodology. The key idea is to develop a comprehensive dataset using symbolic methods that capture different skill levels, ranging from recognition of visual elements to multi-choice quizzes to synthesis-style tasks. We showcase how various aspects of symbolic information in synthetic data help improve fine-tuned models' performance. We will release the full implementation and datasets to facilitate further research on enhancing computational thinking in generative models.