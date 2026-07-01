---
title: "BertaQA: How Much Do Language Models Know About Local Culture?"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3bb42f6bb1b1ab6809afd6c90865b087-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-values-ethics-alignment-evaluation']
tags: ['cultural-knowledge', 'LLM-evaluation', 'local-culture']
venue: "NeurIPS 2024"
tldr: "Introduces BertaQA to benchmark LLMs on local Basque cultural knowledge, revealing significant gaps compared to global topics."
---

# BertaQA: How Much Do Language Models Know About Local Culture?

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3bb42f6bb1b1ab6809afd6c90865b087-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3bb42f6bb1b1ab6809afd6c90865b087-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces BertaQA to benchmark LLMs on local Basque cultural knowledge, revealing significant gaps compared to global topics.

## Abstract

Large Language Models (LLMs) exhibit extensive knowledge about the world, but most evaluations have been limited to global or anglocentric subjects. This raises the question of how well these models perform on topics relevant to other cultures, whose presence on the web is not that prominent. To address this gap, we introduce BertaQA, a multiple-choice trivia dataset that is parallel in English and Basque. The dataset consists of a local subset with questions pertinent to the Basque culture, and a global subset with questions of broader interest. We find that state-of-the-art LLMs struggle with local cultural knowledge, even as they excel on global topics. However, we show that continued pre-training in Basque significantly improves the models' performance on Basque culture, even when queried in English. To our knowledge, this is the first solid evidence of knowledge transfer from a low-resource to a high-resource language. Our analysis sheds light on the complex interplay between language and knowledge, and reveals that some prior findings do not fully hold when reassessed on local topics. Our dataset and evaluation code are available under open licenses at https://github.com/juletx/BertaQA.