---
title: "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/53384f2090c6a5cac952c598fd67992f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-benchmarks-for-clinical-healthcare']
tags: ['dataset-contamination', 'mathematical-reasoning', 'benchmark-evaluation', 'grade-school-arithmetic']
venue: "NeurIPS 2024"
tldr: "Examines whether LLM performance on grade school arithmetic benchmarks reflects genuine reasoning or dataset contamination."
---

# A Careful Examination of Large Language Model Performance on Grade School Arithmetic

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/53384f2090c6a5cac952c598fd67992f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/53384f2090c6a5cac952c598fd67992f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Examines whether LLM performance on grade school arithmetic benchmarks reflects genuine reasoning or dataset contamination.

## Abstract

Large language models (LLMs) have achieved impressive success on many benchmarks for mathematical reasoning.However, there is growing concern that some of this performance actually reflects dataset contamination, where data closely resembling benchmark questions leaks into the training data, instead of true reasoning ability.To investigate this claim rigorously, we commission Grade School Math 1000 (GSM1k). GSM1k is designed to mirror the style and complexity of the established GSM8k benchmark,the gold standard for measuring elementary mathematical reasoning. We ensure that the two benchmarks are comparable across important metrics such as human solve rates, number of steps in solution, answer magnitude, and more.When evaluating leading open- and closed-source LLMs on GSM1k, we observe accuracy drops of up to 8%, with several families of models showing evidence of systematic overfitting across almost all model sizes.Further analysis suggests a positive relationship (Spearman's r^2=0.36) between a model's probability of generating an example from GSM8k and its performance gap between GSM8k and GSM1k, suggesting that some models may have partially memorized GSM8k.Nevertheless, many models, especially those on the frontier, show minimal signs of overfitting, and all models broadly demonstrate generalization to novel math problems guaranteed to not be in their training data.