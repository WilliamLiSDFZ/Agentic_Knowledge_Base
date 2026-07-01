---
title: "cPAPERS: A Dataset of Situated and Multimodal Interactive Conversations in Scientific Papers"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7a19a9d527ed544d1272f07b0f8f934e-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multimodal-conversations', 'scientific-papers', 'situated-interaction', 'dataset', 'benchmark']
venue: "NeurIPS 2024"
tldr: "cPAPERS is a dataset of situated multimodal interactive conversations grounded in scientific paper components like figures and equations."
---

# cPAPERS: A Dataset of Situated and Multimodal Interactive Conversations in Scientific Papers

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7a19a9d527ed544d1272f07b0f8f934e-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7a19a9d527ed544d1272f07b0f8f934e-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: cPAPERS is a dataset of situated multimodal interactive conversations grounded in scientific paper components like figures and equations.

## Abstract

An emerging area of research in situated and multimodal interactive conversations (SIMMC) includes interactions in scientific papers. Since scientific papers are primarily composed of text, equations, figures, and tables, SIMMC methods must be developed specifically for each component to support the depth of inquiry and interactions required by research scientists.      This work introduces $Conversational Papers$ (cPAPERS), a dataset of conversational question-answer pairs from reviews of academic papers grounded in these paper components and their associated references from scientific documents available on arXiv. We present a data collection strategy to collect these question-answer pairs from OpenReview and associate them with contextual information from $LaTeX$ source files. Additionally, we present a series of baseline approaches utilizing Large Language Models (LLMs) in both zero-shot and fine-tuned configurations to address the cPAPERS dataset.