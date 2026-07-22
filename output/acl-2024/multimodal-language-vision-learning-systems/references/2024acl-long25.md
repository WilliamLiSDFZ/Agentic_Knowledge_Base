---
title: "Mementos: A Comprehensive Benchmark for Multimodal Large Language Model Reasoning over Image Sequences"
source: "https://aclanthology.org/2024.acl-long.25/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'llm-training-alignment-and-evaluation']
tags: ['multimodal-benchmark', 'image-sequences', 'temporal-reasoning']
venue: "ACL 2024"
tldr: "Mementos is a benchmark for evaluating multimodal LLMs on reasoning over sequences of images requiring temporal and causal understanding."
---

# Mementos: A Comprehensive Benchmark for Multimodal Large Language Model Reasoning over Image Sequences

**Source**: [https://aclanthology.org/2024.acl-long.25/](https://aclanthology.org/2024.acl-long.25/)

**TLDR**: Mementos is a benchmark for evaluating multimodal LLMs on reasoning over sequences of images requiring temporal and causal understanding.

## Abstract

AbstractMultimodal Large Language Models (MLLMs) have demonstrated proficiency in handling a variety of visual-language tasks. However, current MLLM benchmarks are predominantly designed to evaluate reasoning based on static information about a single image, and the ability of modern MLLMs to extrapolate from image sequences, which is essential for understanding our ever-changing world, has been less investigated. To address this challenge, this paper introduces Mementos, a new benchmark designed to assess MLLMs’ sequential image reasoning abilities. Mementos features 4,761 diverse image sequences with varying lengths. We also employ a GPT-4 assisted method to evaluate MLLM reasoning performance. Through a careful evaluation of nine recent MLLMs on Mementos, including GPT-4V and Gemini, we find that they struggle to accurately describe dynamic information about given image sequences, often leading to hallucinations/misrepresentations of objects and their corresponding behaviors. Our quantitative analysis and case studies identify three key factors impacting MLLMs’ sequential image reasoning: the correlation between object and behavioral hallucinations, the influence of co-occurring behaviors, and the compounding impact of behavioral hallucinations.