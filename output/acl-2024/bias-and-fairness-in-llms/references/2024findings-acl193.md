---
title: "Likelihood-based Mitigation of Evaluation Bias in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.193/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['evaluation-bias', 'likelihood-bias', 'LLM-evaluation']
venue: "ACL 2024"
tldr: "Proposes likelihood-based methods to mitigate superficial evaluation bias in LLMs used as automated NLG metrics."
---

# Likelihood-based Mitigation of Evaluation Bias in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.193/](https://aclanthology.org/2024.findings-acl.193/)

**TLDR**: Proposes likelihood-based methods to mitigate superficial evaluation bias in LLMs used as automated NLG metrics.

## Abstract

AbstractLarge Language Models (LLMs) are widely used to evaluate natural language generation tasks as automated metrics.However, the likelihood, a measure of LLM’s plausibility for a sentence, can vary due to superficial differences in sentences, such as word order and sentence structure.It is therefore possible that there might be a likelihood bias if LLMs are used for evaluation: they might overrate sentences with higher likelihoods while underrating those with lower likelihoods.In this paper, we investigate the presence and impact of likelihood bias in LLM-based evaluators.We also propose a method to mitigate the likelihood bias.Our method utilizes highly biased instances as few-shot examples for in-context learning.Our experiments in evaluating the data-to-text and grammatical error correction tasks reveal that several LLMs we test display a likelihood bias.Furthermore, our proposed method successfully mitigates this bias, also improving evaluation performance (in terms of correlation of models with human scores) significantly.