---
title: "Accurate and Nuanced Open-QA Evaluation Through Textual Entailment"
source: "https://aclanthology.org/2024.findings-acl.151/"
categories: ['llm-training-alignment-and-evaluation', 'nlp-benchmark-design-and-interpretability']
tags: ['open-QA', 'evaluation', 'textual-entailment']
venue: "ACL 2024"
tldr: "An evaluation framework for open-domain QA using textual entailment to achieve more accurate and nuanced answer assessment."
---

# Accurate and Nuanced Open-QA Evaluation Through Textual Entailment

**Source**: [https://aclanthology.org/2024.findings-acl.151/](https://aclanthology.org/2024.findings-acl.151/)

**TLDR**: An evaluation framework for open-domain QA using textual entailment to achieve more accurate and nuanced answer assessment.

## Abstract

AbstractOpen-domain question answering (Open-QA) is a common task for evaluating large language models (LLMs). However, current Open-QA evaluations are criticized for the ambiguity in questions and the lack of semantic understanding in evaluators. Complex evaluators, powered by foundation models or LLMs and pertaining to semantic equivalence, still deviate from human judgments by a large margin. We propose to study the entailment relations of answers to identify more informative and more general system answers, offering a much closer evaluation to human judgment on both NaturalQuestions and TriviaQA while being learning-free. The entailment-based evaluation we propose allows the assignment of bonus or partial marks by quantifying the inference gap between answers, enabling a nuanced ranking of answer correctness that has higher AUC than current methods.