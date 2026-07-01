---
title: "Lean Workbook: A large-scale Lean problem set formalized from natural language math problems"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/bf236666a2cc5f3ae05d2e08485efc4c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'llm-training-and-optimization-techniques']
tags: ['lean', 'formal-theorem-proving', 'math-problem-formalization']
venue: "NeurIPS 2024"
tldr: "Lean Workbook presents a large-scale dataset of formalized math problems in Lean derived from natural language to advance LLM-based formal theorem proving."
---

# Lean Workbook: A large-scale Lean problem set formalized from natural language math problems

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/bf236666a2cc5f3ae05d2e08485efc4c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/bf236666a2cc5f3ae05d2e08485efc4c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Lean Workbook presents a large-scale dataset of formalized math problems in Lean derived from natural language to advance LLM-based formal theorem proving.

## Abstract

Large language models have demonstrated impressive capabilities across various natural language processing tasks, especially in solving mathematical problems. However, large language models are not good at math theorem proving using formal languages like Lean. A significant challenge in this area is the scarcity of training data available in these formal languages. To address this issue, we propose a novel pipeline that iteratively generates and filters synthetic data to translate natural language mathematical problems into Lean 4 statements, and vice versa. Our results indicate that the synthetic data pipeline can provide useful training data and improve the performance of LLMs in translating and understanding complex mathematical problems and proofs. Our final dataset contains about 57K formal-informal question pairs along with searched proof from the math contest forum and 21 new IMO questions. We open-source our code at \url{https://github.com/InternLM/InternLM-Math} and our data at \url{https://huggingface.co/datasets/InternLM/Lean-Workbook}.