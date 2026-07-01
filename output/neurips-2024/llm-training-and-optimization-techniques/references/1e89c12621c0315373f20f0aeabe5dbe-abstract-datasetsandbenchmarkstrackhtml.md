---
title: "Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1e89c12621c0315373f20f0aeabe5dbe-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['llm-evaluation', 'benchmark-automation', 'dataset-updating']
venue: "NeurIPS 2024"
tldr: "Proposes an automated pipeline for continuously updating evaluation datasets to maintain reliable and timely LLM benchmarking."
---

# Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1e89c12621c0315373f20f0aeabe5dbe-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1e89c12621c0315373f20f0aeabe5dbe-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Proposes an automated pipeline for continuously updating evaluation datasets to maintain reliable and timely LLM benchmarking.

## Abstract

Large language models (LLMs) have achieved impressive performance across various natural language benchmarks, prompting a continual need to curate more difficult datasets for larger LLMs, which is costly and time-consuming. In this paper, we propose to automate dataset updating and provide systematical analysis regarding its effectiveness in dealing with benchmark leakage issue, difficulty control, and stability. Thus, once current benchmark has been mastered or leaked, we can update it for timely and reliable evaluation. There are two updating strategies: 1) mimicking strategy to generate similar samples based on original data, preserving stylistic and contextual essence, and 2) extending strategy that further expands existing samples at varying cognitive levels by adapting Bloom’s taxonomy of educational objectives. Extensive experiments on updated MMLU and BIG-Bench demonstrate the stability of the proposed strategies and find that the mimicking strategy can effectively alleviate issues of overestimation from benchmark leakage. In cases where the efficient mimicking strategy fails, our extending strategy still shows promising results. Additionally, by controlling the difficulty, we can better discern the models’ performance and enable fine-grained analysis — neither too difficult nor too easy an exam can fairly judge students’ learning status. To the best of our knowledge, we are the first to automate updating benchmarks for reliable and timely evaluation. Our demo leaderboard can be found at https://yingjiahao14.github.io/Automating-DatasetUpdates/.