---
title: "Needle In A Multimodal Haystack"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/24a8968affe71ffe4067d022b9d16566-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['multimodal-llm', 'long-context', 'evaluation-benchmark', 'needle-in-haystack', 'multimodal-understanding']
venue: "NeurIPS 2024"
tldr: "Introduces a benchmark to evaluate multimodal large language models on retrieving and reasoning over long multimodal content."
---

# Needle In A Multimodal Haystack

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/24a8968affe71ffe4067d022b9d16566-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/24a8968affe71ffe4067d022b9d16566-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a benchmark to evaluate multimodal large language models on retrieving and reasoning over long multimodal content.

## Abstract

With the rapid advancement of multimodal large language models (MLLMs), their evaluation has become increasingly comprehensive. However, understanding long multimodal content, as a foundational ability for real-world applications, remains underexplored. In this work, we present Needle In A Multimodal Haystack (MM-NIAH), the first benchmark specifically designed to systematically evaluate the capability of existing MLLMs to comprehend long multimodal documents. Our benchmark includes three types of evaluation tasks: multimodal retrieval, counting, and reasoning. In each task, the model is required to answer the questions according to different key information scattered throughout the given multimodal document. Evaluating the leading MLLMs on MM-NIAH, we observe that existing models still have significant room for improvement on these tasks, especially on vision-centric evaluation. We hope this work can provide a platform for further research on long multimodal document comprehension and contribute to the advancement of MLLMs. Code and benchmark are released at https://github.com/OpenGVLab/MM-NIAH.