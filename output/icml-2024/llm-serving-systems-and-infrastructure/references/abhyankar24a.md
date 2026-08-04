---
title: "InferCept: Efficient Intercept Support for Augmented Large Language Model Inference"
source: "https://proceedings.mlr.press/v235/abhyankar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/abhyankar24a/abhyankar24a.pdf"
categories: ['llm-serving-systems-and-infrastructure']
tags: ['llm-inference', 'augmented-llm', 'tool-use', 'intercept-scheduling']
venue: "ICML 2024"
tldr: "InferCept is an efficient LLM inference system that supports mid-sequence interception for tool/agent calls without wasting GPU compute."
---

# InferCept: Efficient Intercept Support for Augmented Large Language Model Inference

**Source**: [https://proceedings.mlr.press/v235/abhyankar24a.html](https://proceedings.mlr.press/v235/abhyankar24a.html)

**TLDR**: InferCept is an efficient LLM inference system that supports mid-sequence interception for tool/agent calls without wasting GPU compute.

## Abstract

Large language models are increasingly integrated with external environments, tools, and agents like ChatGPT plugins to extend their capability beyond language-centric tasks. However, today’s LLM inference systems are designed for standalone LLMs. They treat each external interaction as the end of LLM generation and form a new request when the interaction finishes, causing unnecessary recomputation of already computed contexts, which accounts for 37-40% of total model forwarding time. This paper presents InferCept, the first LLM inference framework targeting augmented LLMs and supporting the efficient interception of LLM generation. InferCept minimizes the GPU resource waste caused by LLM interceptions and dedicates saved memory for serving more requests.InferCept improves the overall serving throughput by 1.6x-2x and completes 2x more requests per second compared to the state-of-the-art LLM inference systems.