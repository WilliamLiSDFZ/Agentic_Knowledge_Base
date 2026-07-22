---
title: "Improving LLM Generations via Fine-Grained Self-Endorsement"
source: "https://aclanthology.org/2024.findings-acl.499/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-training-alignment-and-evaluation']
tags: ['hallucination-mitigation', 'self-endorsement', 'fact-checking', 'inference-time']
venue: "ACL 2024"
tldr: "Proposes a self-endorsement framework using fine-grained fact-level comparisons across multiple sampled responses to reduce hallucinations at inference time."
---

# Improving LLM Generations via Fine-Grained Self-Endorsement

**Source**: [https://aclanthology.org/2024.findings-acl.499/](https://aclanthology.org/2024.findings-acl.499/)

**TLDR**: Proposes a self-endorsement framework using fine-grained fact-level comparisons across multiple sampled responses to reduce hallucinations at inference time.

## Abstract

AbstractThis work studies mitigating fact-conflicting hallucinations for large language model (LLM) at inference time.Particularly, we propose a self-endorsement framework that leverages the fine-grained fact-level comparisons across multiple sampled responses.Compared with prior ensemble methods (e.g., self-consistency) that perform response-level selection, our approach can better alleviate hallucinations for knowledge-intensive tasks.Our approach can broadly benefit smaller and open-source LLMs as it mainly conducts simple content-based comparisons.Experiments on Biographies show that our method can effectively improve the factuality of generations with simple and intuitive prompts across different scales of LLMs.Besides, comprehensive analyses on TriviaQA and GSM8K demonstrate the potential of self-endorsement for broader application.