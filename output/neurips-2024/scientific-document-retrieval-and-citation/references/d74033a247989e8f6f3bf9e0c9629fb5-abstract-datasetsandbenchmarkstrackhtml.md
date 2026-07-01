---
title: "SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d74033a247989e8f6f3bf9e0c9629fb5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['scientific-document-retrieval-and-citation']
tags: ['multimodal-qa', 'scientific-papers', 'benchmark']
venue: "NeurIPS 2024"
tldr: "SPIQA introduces a large-scale multimodal question-answering dataset for scientific papers incorporating both textual and visual content."
---

# SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d74033a247989e8f6f3bf9e0c9629fb5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/d74033a247989e8f6f3bf9e0c9629fb5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SPIQA introduces a large-scale multimodal question-answering dataset for scientific papers incorporating both textual and visual content.

## Abstract

Seeking answers to questions within long scientific research articles is a crucial area of study that aids readers in quickly addressing their inquiries. However, existing question-answering (QA) datasets based on scientific papers are limited in scale and focus solely on textual content. We introduce SPIQA (Scientific Paper Image Question Answering), the first large-scale QA dataset specifically designed to interpret complex figures and tables within the context of scientific research articles across various domains of computer science. Leveraging the breadth of expertise and ability of multimodal large language models (MLLMs) to understand figures, we employ automatic and manual curation to create the dataset. We craft an information-seeking task on interleaved images and text that involves multiple images covering a wide variety of plots, charts, tables, schematic diagrams, and result visualizations. SPIQA comprises 270K questions divided into training, validation, and three different evaluation splits. Through extensive experiments with 12 prominent foundational models, we evaluate the ability of current multimodal systems to comprehend the nuanced aspects of research articles. Additionally, we propose a Chain-of-Thought (CoT) evaluation strategy with in-context retrieval that allows fine-grained, step-by-step assessment and improves model performance. We further explore the upper bounds of performance enhancement with additional textual information, highlighting its promising potential for future research and the dataset’s impact on revolutionizing how we interact with scientific literature.