---
title: "Fundamental Limits of Prompt Compression: A Rate-Distortion Framework for Black-Box Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ac8fbba029dadca99d6b8c3f913d3ed6-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques']
tags: ['prompt-compression', 'rate-distortion', 'black-box-LLMs', 'information-theory', 'token-level-compression']
venue: "NeurIPS 2024"
tldr: "A rate-distortion framework formalizes prompt compression for black-box LLMs and derives fundamental limits via a linear program."
---

# Fundamental Limits of Prompt Compression: A Rate-Distortion Framework for Black-Box Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ac8fbba029dadca99d6b8c3f913d3ed6-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ac8fbba029dadca99d6b8c3f913d3ed6-Abstract-Conference.html)

**TLDR**: A rate-distortion framework formalizes prompt compression for black-box LLMs and derives fundamental limits via a linear program.

## Abstract

We formalize the problem of prompt compression for large language models (LLMs) and present a framework to unify token-level prompt compression methods which create hard prompts for black-box models. We derive the distortion-rate function for this setup as a linear program, and provide an efficient algorithm to compute this fundamental limit via the dual of the linear program. Using the distortion-rate function as the baseline, we study the performance of existing compression schemes on a synthetic dataset consisting of prompts generated from a Markov chain, natural language queries, and their respective answers. Our empirical analysis demonstrates the criticality of query-aware prompt compression, where the compressor has knowledge of the downstream task/query for the black-box LLM. We show that there is a large gap between the performance of current prompt compression methods and the optimal strategy, and propose Adaptive QuerySelect, a query-aware, variable-rate adaptation of a prior work to close the gap. We extend our experiments to a small natural language dataset to further confirm our findings on our synthetic dataset.