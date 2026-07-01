---
title: "A Synthetic Dataset for Personal Attribute Inference"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/daa1816b84ca2d5051c87fb4d37dd540-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'llm-benchmarks-for-clinical-healthcare']
tags: ['llm-privacy', 'attribute-inference', 'synthetic-dataset']
venue: "NeurIPS 2024"
tldr: "A synthetic dataset is introduced to study and benchmark LLM-based personal attribute inference as a privacy threat."
---

# A Synthetic Dataset for Personal Attribute Inference

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/daa1816b84ca2d5051c87fb4d37dd540-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/daa1816b84ca2d5051c87fb4d37dd540-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A synthetic dataset is introduced to study and benchmark LLM-based personal attribute inference as a privacy threat.

## Abstract

Recently powerful Large Language Models (LLMs) have become easily accessible to hundreds of millions of users world-wide. However, their strong capabilities and vast world knowledge do not come without associated privacy risks. In this work, we focus on the emerging privacy threat LLMs pose – the ability to accurately infer personal information from online texts. Despite the growing importance of LLM-based author profiling, research in this area has been hampered by a lack of suitable public datasets, largely due to ethical and privacy concerns associated with real personal data. We take two steps to address this problem: (i) we construct a simulation framework for the popular social media platform Reddit using LLM agents seeded with synthetic personal profiles; (ii) using this framework, we generate SynthPAI, a diverse synthetic dataset of over 7800 comments manually labeled for personal attributes. We validate our dataset with a human study showing that humans barely outperform random guessing on the task of distinguishing our synthetic comments from real ones. Further, we verify that our dataset enables meaningful personal attribute inference research by showing across 18 state-of-the-art LLMs that our synthetic comments allow us to draw the same conclusions as real-world data. Combined, our experimental results, dataset and pipeline form a strong basis for future privacy-preserving research geared towards understanding and mitigating inference-based privacy threats that LLMs pose.