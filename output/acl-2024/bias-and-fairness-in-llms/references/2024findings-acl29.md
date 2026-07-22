---
title: "Benchmarking Cognitive Biases in Large Language Models as Evaluators"
source: "https://aclanthology.org/2024.findings-acl.29/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['llm-evaluators', 'cognitive-bias', 'preference-ranking']
venue: "ACL 2024"
tldr: "Benchmarks 16 LLMs as automatic evaluators to identify and measure cognitive biases introduced when LLMs judge each other's responses."
---

# Benchmarking Cognitive Biases in Large Language Models as Evaluators

**Source**: [https://aclanthology.org/2024.findings-acl.29/](https://aclanthology.org/2024.findings-acl.29/)

**TLDR**: Benchmarks 16 LLMs as automatic evaluators to identify and measure cognitive biases introduced when LLMs judge each other's responses.

## Abstract

AbstractLarge Language Models (LLMs) have recently been shown to be effective as automatic evaluators with simple prompting and in-context learning. In this work, we assemble 16 LLMs encompassing four different size ranges and evaluate their output responses by preference ranking from the other LLMs as evaluators, such as System Star is better than System Square. We then evaluate the quality of ranking outputs introducing the Cognitive Bias Benchmark for LLMs as Evaluators (CoBBLer), a benchmark to measure six different cognitive biases in LLM evaluation outputs, such as the Egocentric bias where a model prefers to rank its own outputs highly in evaluation. We find that LLMs are biased text quality evaluators, exhibiting strong indications on our bias benchmark (40% of comparisons made by all models) within each of their evaluations that question their robustness as evaluators. Furthermore, we examine the correlation between human and machine preferences and calculate the average Rank-Biased Overlap (RBO) score to be 44%, indicating that machine preferences are misaligned with humans. According to our findings, LLMs may still be unable to be utilized for automatic annotation aligned with human preferences.