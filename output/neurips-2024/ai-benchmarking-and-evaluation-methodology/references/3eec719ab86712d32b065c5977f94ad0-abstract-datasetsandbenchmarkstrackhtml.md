---
title: "NewTerm: Benchmarking Real-Time New Terms for Large Language Models with Annual Updates"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3eec719ab86712d32b065c5977f94ad0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['LLM-benchmarking', 'real-time-knowledge', 'knowledge-cutoff']
venue: "NeurIPS 2024"
tldr: "Introduces NewTerm, an annually updated benchmark evaluating LLM performance on emerging terms beyond training knowledge cutoffs."
---

# NewTerm: Benchmarking Real-Time New Terms for Large Language Models with Annual Updates

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3eec719ab86712d32b065c5977f94ad0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3eec719ab86712d32b065c5977f94ad0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces NewTerm, an annually updated benchmark evaluating LLM performance on emerging terms beyond training knowledge cutoffs.

## Abstract

Despite their remarkable abilities in various tasks, large language models (LLMs) still struggle with real-time information (e.g., new facts and terms) due to the knowledge cutoff in their development process. However, existing benchmarks focus on outdated content and limited fields, facing difficulties in real-time updating and leaving new terms unexplored. To address this problem, we propose an adaptive benchmark, NewTerm, for real-time evaluation of new terms. We design a highly automated construction method to ensure high-quality benchmark construction with minimal human effort, allowing flexible updates for real-time information. Empirical results on various LLMs demonstrate over 20% performance reduction caused by new terms. Additionally, while updates to the knowledge cutoff of LLMs can cover some of the new terms, they are unable to generalize to more distant new terms. We also analyze which types of terms are more challenging and why LLMs struggle with new terms, paving the way for future research. Finally, we construct NewTerm 2022 and 2023 to evaluate the new terms updated each year and will continue updating annually. The benchmark and codes can be found at https://anonymous.4open.science/r/NewTerms.