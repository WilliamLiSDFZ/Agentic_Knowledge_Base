---
title: "Evaluating Numerical Reasoning in Text-to-Image Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4a70f0c8443593ca59a88ebc8a937ed6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['text-to-image', 'numerical-reasoning', 'evaluation', 'generative-models']
venue: "NeurIPS 2024"
tldr: "A comprehensive evaluation of text-to-image models on numerical reasoning tasks reveals systematic failures even in state-of-the-art systems."
---

# Evaluating Numerical Reasoning in Text-to-Image Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4a70f0c8443593ca59a88ebc8a937ed6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4a70f0c8443593ca59a88ebc8a937ed6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A comprehensive evaluation of text-to-image models on numerical reasoning tasks reveals systematic failures even in state-of-the-art systems.

## Abstract

Text-to-image generative models are capable of producing high-quality images that often faithfully depict concepts described using natural language. In this work, we comprehensively evaluate a range of text-to-image models on numerical reasoning tasks of varying difficulty, and show that even the most advanced models have only rudimentary numerical skills. Specifically, their ability to correctly generate an exact number of objects in an image is limited to small numbers, it is highly dependent on the context the number term appears in, and it deteriorates quickly with each successive number. We also demonstrate that models have poor understanding of linguistic quantifiers (such as “few” or “as many as”), the concept of zero, and struggle with more advanced concepts such as fractional representations. We bundle prompts, generated images and human annotations into GeckoNum, a novel benchmark for evaluation of numerical reasoning.