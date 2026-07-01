---
title: "Easy2Hard-Bench: Standardized Difficulty Labels for Profiling LLM Performance and Generalization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4e6f22305275966513990f53cec908e0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['difficulty-labels', 'llm-benchmarking', 'generalization-evaluation']
venue: "NeurIPS 2024"
tldr: "Easy2Hard-Bench provides standardized continuous difficulty labels for benchmark datasets to enable profiling of LLM generalization across complexity levels."
---

# Easy2Hard-Bench: Standardized Difficulty Labels for Profiling LLM Performance and Generalization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4e6f22305275966513990f53cec908e0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4e6f22305275966513990f53cec908e0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Easy2Hard-Bench provides standardized continuous difficulty labels for benchmark datasets to enable profiling of LLM generalization across complexity levels.

## Abstract

Despite the abundance of datasets available for assessing large language models (LLMs), the scarcity of continuous and reliable difficulty labels for individual data points, in most cases, curtails their capacity to benchmark model generalization performance across different levels of complexity. Addressing this limitation, we present Easy2Hard, an innovative collection of 6 benchmark datasets featuring standardized difficulty labels spanning a wide range of domains, such as mathematics and programming problems, chess puzzles, and reasoning questions, providing a much-needed tool for those in demand of a dataset with varying degrees of difficulty for LLM assessment. We estimate the difficulty of individual problems by leveraging the performance data of many human subjects and LLMs on prominent leaderboards. Harnessing the rich human performance data, we employ widely recognized difficulty ranking systems, including the Item Response Theory (IRT) and Glicko-2 models, to uniformly assign difficulty scores to problems. The Easy2Hard datasets distinguish themselves from previous collections by incorporating a significantly higher proportion of challenging problems, presenting a novel and demanding test for state-of-the-art LLMs. Through extensive experiments conducted with six state-of-the-art LLMs on the Easy2Hard datasets, we offer valuable insights into their performance and generalization capabilities across varying degrees of difficulty, setting the stage for future research in LLM generalization.