---
title: "MathPile: A Billion-Token-Scale Pretraining Corpus for Math"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2d0be3cd5173c10b6ec075d1c393a13d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-training-and-optimization-techniques']
tags: ['math-pretraining', 'corpus-curation', 'foundation-models']
venue: "NeurIPS 2024"
tldr: "MathPile is a 9.5-billion-token diverse math-centric pretraining corpus built on a "less is more" quality-first principle for training math foundation models."
---

# MathPile: A Billion-Token-Scale Pretraining Corpus for Math

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2d0be3cd5173c10b6ec075d1c393a13d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2d0be3cd5173c10b6ec075d1c393a13d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MathPile is a 9.5-billion-token diverse math-centric pretraining corpus built on a "less is more" quality-first principle for training math foundation models.

## Abstract

High-quality, large-scale corpora are the cornerstone of building foundation models. In this work, we introduce MathPile, a diverse and high-quality math-centric corpus comprising about 9.5 billion tokens. Throughout its creation, we adhered to the principle of “less is more”, firmly believing in the supremacy of data quality over quantity, even in the pre-training phase. Our meticulous data collection and processing efforts included a complex suite of preprocessing, prefiltering, language identification, cleaning, filtering, and deduplication, ensuring the high quality of our corpus. Furthermore, we performed data contamination detection on downstream benchmark test sets to eliminate duplicates and conducted continual pre-training experiments, booting the performance on common mathematical reasoning benchmarks. We aim for our MathPile to boost language models’ mathematical reasoning abilities and open-source its different versions and processing scripts to advance the field.