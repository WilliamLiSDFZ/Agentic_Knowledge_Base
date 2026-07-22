---
title: "FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation"
source: "https://aclanthology.org/2024.findings-acl.813/"
pdf_url: ""
categories: ['web-data-quality-and-llm-evaluation']
tags: ['dynamic-QA', 'search-augmentation', 'knowledge-freshness']
venue: "ACL 2024"
tldr: "FreshQA is a benchmark for testing LLMs on time-sensitive questions, and FreshPrompt uses search engine augmentation to improve accuracy."
---

# FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.813/](https://aclanthology.org/2024.findings-acl.813/)

**TLDR**: FreshQA is a benchmark for testing LLMs on time-sensitive questions, and FreshPrompt uses search engine augmentation to improve accuracy.

## Abstract

AbstractSince most large language models (LLMs) are trained once and never updated, they struggle to dynamically adapt to our ever-changing world. In this work, we present FreshQA, a dynamic QA benchmark that tests a model’s ability to answer questions that may require reasoning over up-to-date world knowledge. We develop a two-mode human evaluation procedure to measure both correctness and hallucination, which we use to benchmark both closed and open-source LLMs by collecting >50K human judgments. We observe that all LLMs struggle to answer questions that require fast-changing world knowledge as well as questions with false premises that need to be debunked. In response, we develop FreshPrompt, a few-shot prompting method that curates and organizes relevant information from a search engine into an LLM’s prompt. Our experiments show that FreshPrompt outperforms both competing search engine-augmented prompting methods such as Self-Ask (Press et al., 2022) as well as commercial systems such as Perplexity.AI. To facilitate future work, we additionally develop FreshEval, a reliable autorater for quick evaluation and comparison on FreshQA. Our latest results with FreshEval suggest that open-source LLMs such as Mixtral (Jiang et al., 2024), when combined with FreshPrompt, are competitive with closed-source and commercial systems on search-augmented QA.