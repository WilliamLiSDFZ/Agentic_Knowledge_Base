---
title: "PUB: A Pragmatics Understanding Benchmark for Assessing LLMs’ Pragmatics Capabilities"
source: "https://aclanthology.org/2024.findings-acl.719/"
pdf_url: ""
categories: ['language-model-human-cognitive-linguistic-alignment', 'nlp-benchmark-design-and-interpretability']
tags: ['pragmatics', 'LLM-evaluation', 'benchmark']
venue: "ACL 2024"
tldr: "Releases PUB, a 14-task benchmark evaluating LLMs' understanding of pragmatic phenomena like implicature and presupposition."
---

# PUB: A Pragmatics Understanding Benchmark for Assessing LLMs’ Pragmatics Capabilities

**Source**: [https://aclanthology.org/2024.findings-acl.719/](https://aclanthology.org/2024.findings-acl.719/)

**TLDR**: Releases PUB, a 14-task benchmark evaluating LLMs' understanding of pragmatic phenomena like implicature and presupposition.

## Abstract

AbstractLLMs have demonstrated remarkable capability for understanding semantics, but their understanding of pragmatics is not well studied. To this end, we release a Pragmatics Understanding Benchmark (PUB) dataset consisting of fourteen tasks in four pragmatics phenomena, namely; Implicature, Presupposition, Reference, and Deixis. We curate high-quality test sets for each task, consisting of Multiple Choice Question Answers (MCQA). PUB includes a total of 28k data points, 6.1k are newly annotated. We evaluate nine models varying in the number of parameters and type of training. Our study reveals several key observations about the pragmatic capabilities of LLMs: 1. chat-fine-tuning strongly benefits smaller models, 2. large base models are competitive with their chat-fine-tuned counterparts, 3. there is a huge variance in performance across different pragmatics phenomena, and 4. a noticeable performance gap between human capabilities and model capabilities. We hope that PUB will enable comprehensive evaluation of LLM’s pragmatic reasoning capabilities.