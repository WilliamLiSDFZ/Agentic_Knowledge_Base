---
title: "Task Me Anything"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/237ffa9a473eff1c66d085dba7f813ba-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'visual-language-multimodal-generation-reasoning']
tags: ['benchmark', 'multimodal-llm', 'task-adaptive-evaluation']
venue: "NeurIPS 2024"
tldr: "Task Me Anything is an agent-driven benchmark that dynamically generates targeted evaluations for multimodal language models."
---

# Task Me Anything

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/237ffa9a473eff1c66d085dba7f813ba-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/237ffa9a473eff1c66d085dba7f813ba-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Task Me Anything is an agent-driven benchmark that dynamically generates targeted evaluations for multimodal language models.

## Abstract

Benchmarks for large multimodal language models (MLMs) now serve to simultaneously assess the general capabilities of models instead of evaluating for a specific capability. As a result, when a developer wants to identify which models to use for their application, they are overwhelmed by the number of benchmarks and remain uncertain about which benchmark's results are most reflective of their specific use case. This paper introduces Task-Me-Anything, a benchmark generation engine which produces a benchmark tailored to a user's needs. Task-Me-Anything maintains an extendable taxonomy of visual assets and can programmatically generate a vast number of task instances. Additionally, it algorithmically addresses user queries regarding MLM performance efficiently within a computational budget. It contains 113K images, 10K videos, 2K 3D object assets, over 365 object categories, 655 attributes, and 335 relationships. It can generate 500M image/video question-answering pairs, which focus on evaluating MLM perceptual capabilities. Task-Me-Anything reveals critical insights: open-source MLMs excel in object and attribute recognition but lack spatial and temporal understanding; each model exhibits unique strengths and weaknesses; larger models generally perform better, though exceptions exist; and GPT4O demonstrates challenges in recognizing rotating/moving objects and distinguishing colors.