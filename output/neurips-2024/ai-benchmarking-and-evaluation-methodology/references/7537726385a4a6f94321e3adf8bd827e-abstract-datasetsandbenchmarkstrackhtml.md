---
title: "Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7537726385a4a6f94321e3adf8bd827e-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-values-ethics-alignment-evaluation']
tags: ['situational-awareness', 'LLM-self-knowledge', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces the Situational Awareness Dataset (SAD) to evaluate whether LLMs reliably know and act on knowledge about their own nature and deployment context."
---

# Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7537726385a4a6f94321e3adf8bd827e-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7537726385a4a6f94321e3adf8bd827e-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces the Situational Awareness Dataset (SAD) to evaluate whether LLMs reliably know and act on knowledge about their own nature and deployment context.

## Abstract

AI assistants such as ChatGPT are trained to respond to users by saying, "I am a large language model”.This raises questions. Do such models "know'' that they are LLMs and reliably act on this knowledge? Are they "aware" of their current circumstances, such as being deployed to the public?We refer to a model's knowledge of itself and its circumstances as situational awareness.To quantify situational awareness in LLMs, we introduce a range of behavioral tests, based on question answering and instruction following. These tests form the Situational Awareness Dataset (SAD), a benchmark comprising 7 task categories and over 13,000 questions.The benchmark tests numerous abilities, including the capacity of LLMs to (i) recognize their own generated text, (ii) predict their own behavior, (iii) determine whether a prompt is from internal evaluation or real-world deployment, and (iv) follow instructions that depend on self-knowledge.We evaluate 16 LLMs on SAD, including both base (pretrained) and chat models.While all models perform better than chance, even the highest-scoring model (Claude 3 Opus) is far from a human baseline on certain tasks. We also observe that performance on SAD is only partially predicted by metrics of general knowledge. Chat models, which are finetuned to serve as AI assistants, outperform their corresponding base models on SAD but not on general knowledge tasks.The purpose of SAD is to facilitate scientific understanding of situational awareness in LLMs by breaking it down into quantitative abilities. Situational awareness is important because it enhances a model's capacity for autonomous planning and action. While this has potential benefits from automation, it also introduces novel risks related to AI safety and control.