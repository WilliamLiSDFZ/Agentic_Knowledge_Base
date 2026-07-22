---
title: "Ranking Large Language Models without Ground Truth"
source: "https://aclanthology.org/2024.findings-acl.143/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-based-ranking-and-recommendation']
tags: ['LLM-evaluation', 'ranking', 'ground-truth-free', 'benchmark']
venue: "ACL 2024"
tldr: "Proposes a method for ranking large language models without requiring ground truth by leveraging model agreement and consistency signals."
---

# Ranking Large Language Models without Ground Truth

**Source**: [https://aclanthology.org/2024.findings-acl.143/](https://aclanthology.org/2024.findings-acl.143/)

**TLDR**: Proposes a method for ranking large language models without requiring ground truth by leveraging model agreement and consistency signals.

## Abstract

AbstractEvaluation and ranking of large language models (LLMs) has become an important problem with the proliferation of these models and their impact. Evaluation methods either require human responses which are expensive to acquire or use pairs of LLMs to evaluate each other which can be unreliable. In this paper, we provide a novel perspective where, given a dataset of prompts (viz. questions, instructions, etc.) and a set of LLMs, we rank them without access to any ground truth or reference responses. Inspired by real life where both an expert and a knowledgeable person can identify a novice our main idea is to consider triplets of models, where each one of them evaluates the other two, correctly identifying the worst model in the triplet with high probability. We also analyze our idea and provide sufficient conditions for it to succeed. Applying this idea repeatedly we propose two methods to rank LLMs. In experiments on different generative tasks (summarization, multiple-choice, and dialog), our methods reliably recover true rankings without reference data. This points to a viable low-resource mechanism for practical use.