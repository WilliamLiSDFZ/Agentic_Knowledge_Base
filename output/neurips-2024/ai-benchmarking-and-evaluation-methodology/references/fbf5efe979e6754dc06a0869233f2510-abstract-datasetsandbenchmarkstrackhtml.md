---
title: "Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fbf5efe979e6754dc06a0869233f2510-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['visual-riddles', 'commonsense-reasoning', 'vision-language-benchmark']
venue: "NeurIPS 2024"
tldr: "A benchmark of visual riddles requiring commonsense and world knowledge to evaluate large vision-language models on contextual visual inference."
---

# Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fbf5efe979e6754dc06a0869233f2510-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fbf5efe979e6754dc06a0869233f2510-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark of visual riddles requiring commonsense and world knowledge to evaluate large vision-language models on contextual visual inference.

## Abstract

Imagine observing someone scratching their arm; to understand why, additional context would be necessary. However, spotting a mosquito nearby would immediately offer a likely explanation for the person’s discomfort, thereby alleviating the need for further information. This example illustrates how subtle visual cues can challenge our cognitive skills and demonstrates the complexity of interpreting visual scenarios. To study these skills, we present Visual Riddles, a benchmark aimed to test vision and language models on visual riddles requiring commonsense and world knowledge. The benchmark comprises 400 visual riddles, each featuring a unique image created by a variety of text-to-image models, question, ground-truth answer, textual hint, and attribution. Human evaluation reveals that existing models lag significantly behind human performance, which is at 82% accuracy, with Gemini-Pro-1.5 leading with 40% accuracy. Our benchmark comes with automatic evaluation tasks to make assessment scalable. These findings underscore the potential of Visual Riddles as a valuable resource for enhancing vision and language models’ capabilities in interpreting complex visual scenarios. Data, code, and leaderboard are available at https://visual-riddles.github.io/.