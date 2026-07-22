---
title: "Language Models can Evaluate Themselves via Probability Discrepancy"
source: "https://aclanthology.org/2024.findings-acl.291/"
categories: ['llm-training-alignment-and-evaluation', 'llm-hallucination-detection-and-mitigation']
tags: ['LLM-self-evaluation', 'probability-discrepancy', 'hallucination', 'output-distribution', 'self-assessment']
venue: "ACL 2024"
tldr: "Shows LLMs can evaluate their own response quality by measuring probability discrepancy, correlating uniform distributions with accuracy."
---

# Language Models can Evaluate Themselves via Probability Discrepancy

**Source**: [https://aclanthology.org/2024.findings-acl.291/](https://aclanthology.org/2024.findings-acl.291/)

**TLDR**: Shows LLMs can evaluate their own response quality by measuring probability discrepancy, correlating uniform distributions with accuracy.

## Abstract

AbstractIn this paper, we begin by illustrating that, when presented with a query, Large Language Models (LLMs) capable of providing accurate responses tend to exhibit a more uniform probability distribution compared to their less proficient counterparts. Building upon this observation, we introduce a novel self-assessment criterion termed ProbDiff for evaluating the performance of diverse LLMs. This method eliminates the need for training an additional evaluation model or relying on external proprietary models such as GPT-4 as a judger. Instead, it solely relies on the LLMs under evaluation to compute the probability discrepancy between the original response generation and its revised versions. A higher discrepancy in two LLMs for the same query suggests a relatively weaker ability. We discover that ProbDiff yields comparable results to mainstream GPT-4-based evaluations on various scenarios including NLG tasks like translation and summarization, as well as LLM evaluation benchmarks such as AlignBench, MT-Bench, and AlpacaEval, across LLMs of different sizes.