---
title: "CHAMP: A Competition-level Dataset for Fine-Grained Analyses of LLMs’ Mathematical Reasoning Capabilities"
source: "https://aclanthology.org/2024.findings-acl.785/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['mathematical-reasoning', 'competition-benchmarks', 'chain-of-thought']
venue: "ACL 2024"
tldr: "Introduces CHAMP, a competition-level benchmark for fine-grained evaluation of LLMs' mathematical reasoning with hints and solution steps."
---

# CHAMP: A Competition-level Dataset for Fine-Grained Analyses of LLMs’ Mathematical Reasoning Capabilities

**Source**: [https://aclanthology.org/2024.findings-acl.785/](https://aclanthology.org/2024.findings-acl.785/)

**TLDR**: Introduces CHAMP, a competition-level benchmark for fine-grained evaluation of LLMs' mathematical reasoning with hints and solution steps.

## Abstract

AbstractRecent large language models (LLMs) have shown indications of mathematical reasoning ability on challenging competition-level problems, especially with self-generated verbalizations of intermediate reasoning steps (i.e., chain-of-thought prompting). However, current evaluations mainly focus on the end-to-end final answer correctness, and it is unclear whether LLMs can make use of helpful side information such as problem-specific hints. In this paper, we propose a challenging benchmark dataset for enabling such analyses. The Concept and Hint-Annotated Math Problems (CHAMP) consists of high school math competition problems, annotated with concepts, or general math facts, and hints, or problem-specific tricks. These annotations allow us to explore the effects of additional information, such as relevant hints, misleading concepts, or related problems. This benchmark is difficult, with the best model only scoring 58.1% in standard settings. With concepts and hints, performance sometimes improves, indicating that some models can make use of such side information. Furthermore, we annotate model-generated solutions for their correctness. Using this corpus, we find that models often arrive at the correct final answer through wrong reasoning steps. In addition, we test whether models are able to verify these solutions, and find that most models struggle.