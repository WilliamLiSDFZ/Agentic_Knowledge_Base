---
title: "Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9ee3a664ccfeabc0da16ac6f1f1cfe59-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multimodal-LLM', 'vision-centric', 'visual-representation']
venue: "NeurIPS 2024"
tldr: "Cambrian-1 is a vision-centric multimodal LLM family that systematically explores visual representation design choices for enhanced multimodal capabilities."
---

# Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9ee3a664ccfeabc0da16ac6f1f1cfe59-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/9ee3a664ccfeabc0da16ac6f1f1cfe59-Abstract-Conference.html)

**TLDR**: Cambrian-1 is a vision-centric multimodal LLM family that systematically explores visual representation design choices for enhanced multimodal capabilities.

## Abstract

We introduce Cambrian-1, a family of multimodal LLMs (MLLMs) designed with a vision-centric approach. While stronger language models can enhance multimodal capabilities, the design choices for vision components are often insufficiently explored and disconnected from visual representation learning research. This gap hinders accurate sensory grounding in real-world scenarios. Our study uses LLMs and visual instruction tuning as an interface to evaluate various visual representations, offering new insights into different models and architectures—self-supervised, strongly supervised, or combinations thereof—based on experiments with over 15 vision models. We critically examine existing MLLM benchmarks, addressing the difficulties involved in consolidating and interpreting results from various tasks. To further improve visual grounding, we propose spatial vision aggregator (SVA), a dynamic and spatially-aware connector that integrates vision features with LLMs while reducing the number of tokens. Additionally, we discuss the curation of high-quality visual instruction-tuning data from publicly available sources, emphasizing the importance of distribution balancing. Collectively, Cambrian-1 not only achieves state-of-the-art performances but also serves as a comprehensive, open cookbook for instruction-tuned MLLMs. We provide model weights, code, supporting tools, datasets, and detailed instruction-tuning and evaluation recipes. We hope our release will inspire and accelerate advancements in multimodal systems and visual representation learning.