---
title: "Debatrix: Multi-dimensional Debate Judge with Iterative Chronological Analysis Based on LLM"
source: "https://aclanthology.org/2024.findings-acl.868/"
categories: ['llm-training-alignment-and-evaluation', 'legal-nlp-benchmarks-and-applications']
tags: ['debate-judging', 'LLM', 'multi-dimensional-evaluation', 'argumentation', 'iterative-analysis']
venue: "ACL 2024"
tldr: "Introduces Debatrix, an LLM-based automated debate judge that performs iterative chronological multi-dimensional evaluation of multi-turn debates."
---

# Debatrix: Multi-dimensional Debate Judge with Iterative Chronological Analysis Based on LLM

**Source**: [https://aclanthology.org/2024.findings-acl.868/](https://aclanthology.org/2024.findings-acl.868/)

**TLDR**: Introduces Debatrix, an LLM-based automated debate judge that performs iterative chronological multi-dimensional evaluation of multi-turn debates.

## Abstract

AbstractHow can we construct an automated debate judge to evaluate an extensive, vibrant, multi-turn debate? This task is challenging, as judging a debate involves grappling with lengthy texts, intricate argument relationships, and multi-dimensional assessments.At the same time, current research mainly focuses on short dialogues, rarely touching upon the evaluation of an entire debate.In this paper, by leveraging Large Language Models (LLMs), we propose Debatrix, which makes the analysis and assessment of multi-turn debates more aligned with majority preferences. Specifically, Debatrix features a vertical, iterative chronological analysis and a horizontal, multi-dimensional evaluation collaboration.To align with real-world debate scenarios, we introduced the PanelBench benchmark, comparing our system’s performance to actual debate outcomes.The findings indicate a notable enhancement over directly using LLMs for debate evaluation.Source code and benchmark data are available at https://github.com/ljcleo/debatrix.