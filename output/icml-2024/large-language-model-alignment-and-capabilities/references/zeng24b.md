---
title: "tnGPS: Discovering Unknown Tensor Network Structure Search Algorithms via Large Language Models (LLMs)"
source: "https://proceedings.mlr.press/v235/zeng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeng24b/zeng24b.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['tensor-networks', 'structure-search', 'LLM-driven-optimization']
venue: "ICML 2024"
tldr: "LLMs are used to discover novel tensor network structure search algorithms, outperforming manually crafted heuristics."
---

# tnGPS: Discovering Unknown Tensor Network Structure Search Algorithms via Large Language Models (LLMs)

**Source**: [https://proceedings.mlr.press/v235/zeng24b.html](https://proceedings.mlr.press/v235/zeng24b.html)

**TLDR**: LLMs are used to discover novel tensor network structure search algorithms, outperforming manually crafted heuristics.

## Abstract

Tensor networks are efficient for extremely high-dimensional representation, but their model selection, known as tensor network structure search (TN-SS), is a challenging problem. Although several works have targeted TN-SS, most existing algorithms are manually crafted heuristics with poor performance, suffering from the curse of dimensionality and local convergence. In this work, we jump out of the box, studying how to harness large language models (LLMs) to automatically discover new TN-SS algorithms, replacing the involvement of human experts. By observing how human experts innovate in research, we model their common workflow and propose an automatic algorithm discovery framework called tnGPS. The proposed framework is an elaborate prompting pipeline that instruct LLMs to generate new TN-SS algorithms through iterative refinement and enhancement. The experimental results demonstrate that the algorithms discovered by tnGPS exhibit superior performance in benchmarks compared to the current state-of-the-art methods. Our code is available at https://github.com/ChaoLiAtRIKEN/tngps.