---
title: "Large Language Models Can Automatically Engineer Features for Few-Shot Tabular Learning"
source: "https://proceedings.mlr.press/v235/han24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24f/han24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['llm', 'feature-engineering', 'tabular-learning']
venue: "ICML 2024"
tldr: "FeatLLM is an in-context learning framework that uses LLMs to automatically engineer features for few-shot tabular learning."
---

# Large Language Models Can Automatically Engineer Features for Few-Shot Tabular Learning

**Source**: [https://proceedings.mlr.press/v235/han24f.html](https://proceedings.mlr.press/v235/han24f.html)

**TLDR**: FeatLLM is an in-context learning framework that uses LLMs to automatically engineer features for few-shot tabular learning.

## Abstract

Large Language Models (LLMs), with their remarkable ability to tackle challenging and unseen reasoning problems, hold immense potential for tabular learning, that is vital for many real-world applications. In this paper, we propose a novel in-context learning framework, FeatLLM, which employs LLMs as feature engineers to produce an input data set that is optimally suited for tabular predictions. The generated features are used to infer class likelihood with a simple downstream machine learning model, such as linear regression and yields high performance few-shot learning. The proposed FeatLLM framework only uses this simple predictive model with the discovered features at inference time. Compared to existing LLM-based approaches, FeatLLM eliminates the need to send queries to the LLM for each sample at inference time. Moreover, it merely requires API-level access to LLMs, and overcomes prompt size limitations. As demonstrated across numerous tabular datasets from a wide range of domains, FeatLLM generates high-quality rules, significantly (10% on average) outperforming alternatives such as TabLLM and STUNT.