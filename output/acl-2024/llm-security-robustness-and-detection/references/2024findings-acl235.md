---
title: "SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.235/"
categories: ['llm-security-robustness-and-detection', 'nlp-for-asian-languages']
tags: ['safety-benchmark', 'hierarchical-evaluation', 'LLM-robustness']
venue: "ACL 2024"
tldr: "Introduces SALAD-Bench, a hierarchical and comprehensive benchmark for evaluating LLM safety, attack methods, and defense strategies."
---

# SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.235/](https://aclanthology.org/2024.findings-acl.235/)

**TLDR**: Introduces SALAD-Bench, a hierarchical and comprehensive benchmark for evaluating LLM safety, attack methods, and defense strategies.

## Abstract

AbstractIn the rapidly evolving landscape of Large Language Models (LLMs), ensuring robust safety measures is paramount. To meet this crucial need, we propose SALAD-Bench, a safety benchmark specifically designed for evaluating LLMs, attack, and defense methods. Distinguished by its breadth, SALAD-Bench transcends conventional benchmarks through its large scale, rich diversity, intricate taxonomy spanning three levels, and versatile functionalities.SALAD-Bench is crafted with a meticulous array of questions, from standard queries to complex ones enriched with attack, defense modifications and multiple-choice. To effectively manage the inherent complexity, we introduce an innovative evaluators: the LLM-based MD-Judge for QA pairs with a particular focus on attack-enhanced queries, ensuring a seamless, and reliable evaluation. Above components extend SALAD-Bench from standard LLM safety evaluation to both LLM attack and defense methods evaluation, ensuring the joint-purpose utility. Our extensive experiments shed light on the resilience of LLMs against emerging threats and the efficacy of contemporary defense tactics. Data and evaluator are released under https://github.com/OpenSafetyLab/SALAD-BENCH