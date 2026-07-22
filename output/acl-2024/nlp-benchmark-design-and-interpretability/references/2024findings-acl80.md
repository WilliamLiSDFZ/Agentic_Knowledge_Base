---
title: "Unveiling the Achilles’ Heel of NLG Evaluators: A Unified Adversarial Framework Driven by Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.80/"
categories: ['llm-training-alignment-and-evaluation', 'nlp-benchmark-design-and-interpretability']
tags: ['NLG-evaluation', 'adversarial-robustness', 'automatic-metrics']
venue: "ACL 2024"
tldr: "This paper proposes a unified adversarial framework driven by LLMs to expose vulnerabilities in automatic NLG evaluation metrics."
---

# Unveiling the Achilles’ Heel of NLG Evaluators: A Unified Adversarial Framework Driven by Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.80/](https://aclanthology.org/2024.findings-acl.80/)

**TLDR**: This paper proposes a unified adversarial framework driven by LLMs to expose vulnerabilities in automatic NLG evaluation metrics.

## Abstract

AbstractThe automatic evaluation of natural language generation (NLG) systems presents a long-lasting challenge. Recent studies have highlighted various neural metrics that align well with human evaluations. Yet, the robustness of these evaluators against adversarial perturbations remains largely under-explored due to the unique challenges in obtaining adversarial data for different NLG evaluation tasks. To address the problem, we introduce AdvEval, a novel black-box adversarial framework against NLG evaluators. AdvEval is specially tailored to generate data that yield strong disagreements between human and victim evaluators. Specifically, inspired by the recent success of large language models (LLMs) in text generation and evaluation, we adopt strong LLMs as both the data generator and gold evaluator. Adversarial data are automatically optimized with feedback from the gold and victim evaluator. We conduct experiments on 12 victim evaluators and 11 NLG datasets, spanning tasks including dialogue, summarization, and question evaluation. The results show that AdvEval can lead to significant performance degradation of various victim metrics, thereby validating its efficacy.