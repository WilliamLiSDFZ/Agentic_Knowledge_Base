---
title: "CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fde7f40f8ced5735006810534dc66b33-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare', 'ai-benchmarking-and-evaluation-methodology']
tags: ['medical-vision-language-models', 'trustworthiness', 'benchmark', 'healthcare-ai', 'evaluation']
venue: "NeurIPS 2024"
tldr: "CARES is a comprehensive benchmark for evaluating the trustworthiness of Medical Large Vision Language Models across multiple dimensions."
---

# CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fde7f40f8ced5735006810534dc66b33-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fde7f40f8ced5735006810534dc66b33-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: CARES is a comprehensive benchmark for evaluating the trustworthiness of Medical Large Vision Language Models across multiple dimensions.

## Abstract

Artificial intelligence has significantly impacted medical applications, particularly with the advent of Medical Large Vision Language Models (Med-LVLMs), sparking optimism for the future of automated and personalized healthcare. However, the trustworthiness of Med-LVLMs remains unverified, posing significant risks for future model deployment. In this paper, we introduce CARES and aim to comprehensively evaluate the Trustworthiness of Med-LVLMs across the medical domain. We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. CARES comprises about 41K question-answer pairs in both closed and open-ended formats, covering 16 medical image modalities and 27 anatomical regions. Our analysis reveals that the models consistently exhibit concerns regarding trustworthiness, often displaying factual inaccuracies and failing to maintain fairness across different demographic groups. Furthermore, they are vulnerable to attacks and demonstrate a lack of privacy awareness. We publicly release our benchmark and code in https://github.com/richard-peng-xia/CARES.