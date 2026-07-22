---
title: "The Art of Defending: A Systematic Evaluation and Analysis of LLM Defense Strategies on Safety and Over-Defensiveness"
source: "https://aclanthology.org/2024.findings-acl.776/"
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['LLM-safety', 'defense-strategies', 'over-defensiveness', 'evaluation', 'red-teaming']
venue: "ACL 2024"
tldr: "This paper systematically evaluates LLM defense strategies, analyzing trade-offs between safety improvement and over-defensiveness across multiple approaches."
---

# The Art of Defending: A Systematic Evaluation and Analysis of LLM Defense Strategies on Safety and Over-Defensiveness

**Source**: [https://aclanthology.org/2024.findings-acl.776/](https://aclanthology.org/2024.findings-acl.776/)

**TLDR**: This paper systematically evaluates LLM defense strategies, analyzing trade-offs between safety improvement and over-defensiveness across multiple approaches.

## Abstract

AbstractAs Large Language Models (LLMs) play an increasingly pivotal role in natural language processing applications, their safety concerns become critical areas of NLP research. This has resulted in the development of various LLM defense strategies. Unfortunately, despite the shared goal of improving the safety of LLMs, the evaluation suites across various research works are disjoint and lack diverse inputs to ensure accurate and precise evaluation estimates. Furthermore, the important factor of ‘over-defensiveness’ on the safe inputs has largely remained overlooked. Addressing these limitations, this paper presents a systematic evaluation, comparison, and analysis of various LLM defense strategies over both ‘safety’ and ‘over-defensiveness’. To this end, we compile a large and diverse collection of safe and unsafe prompts, design precise evaluation methodology, and study the efficacy of various LLM defense strategies on multiple state-of-the-art LLMs. Our work reveals a number of crucial findings that we believe will pave the way and also facilitate further research in the critical area of improving the safety of LLMs.