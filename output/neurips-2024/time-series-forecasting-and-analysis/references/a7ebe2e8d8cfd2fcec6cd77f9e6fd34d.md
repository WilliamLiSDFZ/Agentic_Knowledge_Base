---
title: "Optimized Feature Generation for Tabular Data via LLMs with Decision Tree Reasoning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a7ebe2e8d8cfd2fcec6cd77f9e6fd34d-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'time-series-forecasting-and-analysis']
tags: ['feature-engineering', 'tabular-data', 'LLM-reasoning']
venue: "NeurIPS 2024"
tldr: "An LLM-driven feature generation method for tabular data that uses decision tree reasoning to guide optimized feature construction."
---

# Optimized Feature Generation for Tabular Data via LLMs with Decision Tree Reasoning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a7ebe2e8d8cfd2fcec6cd77f9e6fd34d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a7ebe2e8d8cfd2fcec6cd77f9e6fd34d-Abstract-Conference.html)

**TLDR**: An LLM-driven feature generation method for tabular data that uses decision tree reasoning to guide optimized feature construction.

## Abstract

In tabular prediction tasks, tree-based models combined with automated feature engineering methods often outperform deep learning approaches that rely on learned representations. While these feature engineering techniques are effective, they typically depend on a pre-defined search space and primarily use validation scores for feature selection, thereby missing valuable insights from previous experiments.To address these limitations, we propose a novel tabular learning framework that utilizes large language models (LLMs), termed Optimizing Column feature generator with decision Tree reasoning (OCTree). Our key idea is to leverage the reasoning capabilities of LLMs to identify effective feature generation rules without manually specifying the search space and provide language-based reasoning information highlighting past experiments as feedback for iterative rule improvements. We use decision trees to convey this reasoning information, as they can be easily represented in natural language, effectively providing knowledge from prior experiments (i.e., the impact of the generated features on performance) to the LLMs. Our empirical results demonstrate that OCTree consistently enhances the performance of various prediction models across diverse benchmarks, outperforming competing automated feature engineering methods. Code is available at https://github.com/jaehyun513/OCTree.