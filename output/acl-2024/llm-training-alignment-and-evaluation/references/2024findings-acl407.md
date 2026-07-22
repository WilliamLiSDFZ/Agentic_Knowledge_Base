---
title: "ConceptMath: A Bilingual Concept-wise Benchmark for Measuring Mathematical Reasoning of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.407/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['mathematical-reasoning', 'bilingual-benchmark', 'concept-wise-evaluation']
venue: "ACL 2024"
tldr: "Introduces ConceptMath, a bilingual fine-grained benchmark for evaluating LLMs on specific mathematical concepts in English and Chinese."
---

# ConceptMath: A Bilingual Concept-wise Benchmark for Measuring Mathematical Reasoning of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.407/](https://aclanthology.org/2024.findings-acl.407/)

**TLDR**: Introduces ConceptMath, a bilingual fine-grained benchmark for evaluating LLMs on specific mathematical concepts in English and Chinese.

## Abstract

AbstractThis paper introduces ConceptMath, a bilingual (English and Chinese), fine-grained benchmark that evaluates concept-wise mathematical reasoning of Large Language Models (LLMs). Unlike traditional benchmarks that evaluate general mathematical reasoning with an average accuracy, ConceptMath systemically organizes math problems under a hierarchy of math concepts, so that mathematical reasoning can be evaluated at different granularity with concept-wise accuracies. Based on our ConcepthMath, we then evaluate a broad range of LLMs, and we observe existing LLMs, though achieving high average accuracies on traditional benchmarks, exhibit significant performance variations across different math concepts and may even fail catastrophically on the most basic ones. Besides, we also introduce an efficient fine-tuning strategy to enhance the weaknesses of existing LLMs. Finally, we hope ConceptMath could guide the developers to understand the fine-grained mathematical abilities of their models and facilitate the growth of foundation models. Code is available at https://github.com/conceptmath/conceptmath.