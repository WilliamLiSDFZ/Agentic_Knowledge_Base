---
title: "A Semantic Distance Metric Learning approach for Lexical Semantic Change Detection"
source: "https://aclanthology.org/2024.findings-acl.451/"
pdf_url: ""
categories: ['lexical-semantic-change-detection-methods', 'language-model-representations-and-embedding-spaces']
tags: ['lexical-semantic-change', 'metric-learning', 'word-embeddings']
venue: "ACL 2024"
tldr: "Proposes a semantic distance metric learning approach to detect lexical semantic change across different time periods."
---

# A Semantic Distance Metric Learning approach for Lexical Semantic Change Detection

**Source**: [https://aclanthology.org/2024.findings-acl.451/](https://aclanthology.org/2024.findings-acl.451/)

**TLDR**: Proposes a semantic distance metric learning approach to detect lexical semantic change across different time periods.

## Abstract

AbstractDetecting temporal semantic changes of words is an important task for various NLP applications that must make time-sensitive predictions.Lexical Semantic Change Detection (SCD) task involves predicting whether a given target word, w, changes its meaning between two different text corpora, C1 and C2.For this purpose, we propose a supervised two-staged SCD method that uses existing Word-in-Context (WiC) datasets.In the first stage, for a target word w, we learn two sense-aware encoders that represent the meaning of w in a given sentence selected from a corpus.Next, in the second stage, we learn a sense-aware distance metric that compares the semantic representations of a target word across all of its occurrences in C1 and C2.Experimental results on multiple benchmark datasets for SCD show that our proposed method achieves strong performance in multiple languages.Additionally, our method achieves significant improvements on WiC benchmarks compared to a sense-aware encoder with conventional distance functions.