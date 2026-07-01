---
title: "Bag of Tricks: Benchmarking of Jailbreak Attacks on LLMs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/38c1dfb4f7625907b15e9515365e7803-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'ai-benchmarking-and-evaluation-methodology']
tags: ['jailbreak-attacks', 'llm-safety', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "Provides a comprehensive benchmarking framework for systematically evaluating jailbreak attack strategies on large language models."
---

# Bag of Tricks: Benchmarking of Jailbreak Attacks on LLMs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/38c1dfb4f7625907b15e9515365e7803-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/38c1dfb4f7625907b15e9515365e7803-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Provides a comprehensive benchmarking framework for systematically evaluating jailbreak attack strategies on large language models.

## Abstract

Although Large Language Models (LLMs) have demonstrated significant capabilities in executing complex tasks in a zero-shot manner, they are susceptible to jailbreak attacks and can be manipulated to produce harmful outputs. Recently, a growing body of research has categorized jailbreak attacks into token-level and prompt-level attacks.  However, previous work primarily overlooks the diverse key factors of jailbreak attacks, with most studies concentrating on LLM vulnerabilities and lacking exploration of defense-enhanced LLMs. To address these issues, we introduced JailTrickBench to evaluate the impact of various attack settings on LLM performance and provide a baseline for jailbreak attacks, encouraging the adoption of a standardized evaluation framework. Specifically, we evaluate the eight key factors of implementing jailbreak attacks on LLMs from both target-level and attack-level perspectives. We further conduct seven representative jailbreak attacks on six defense methods across two widely used datasets, encompassing approximately 354 experiments with about 55,000 GPU hours on A800-80G. Our experimental results highlight the need for standardized benchmarking to evaluate these attacks on defense-enhanced LLMs. Our code is available at https://github.com/usail-hkust/JailTrickBench.