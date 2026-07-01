---
title: "HonestLLM: Toward an Honest and Helpful Large Language Model"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0d99a8c048befb6dd6e17d7684adacac-Abstract-Conference.html"
categories: ['llm-values-ethics-alignment-evaluation', 'llm-safety-robustness-and-privacy-defenses']
tags: ['llm-honesty', 'helpfulness', 'alignment', 'safety', 'truthfulness']
venue: "NeurIPS 2024"
tldr: "Proposes HonestLLM, a framework to make large language models simultaneously honest and helpful for safe real-world deployment."
---

# HonestLLM: Toward an Honest and Helpful Large Language Model

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0d99a8c048befb6dd6e17d7684adacac-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/0d99a8c048befb6dd6e17d7684adacac-Abstract-Conference.html)

**TLDR**: Proposes HonestLLM, a framework to make large language models simultaneously honest and helpful for safe real-world deployment.

## Abstract

Large Language Models (LLMs) have achieved remarkable success across various industries and applications, owing to their exceptional generative capabilities. Nevertheless, honesty and helpfulness, which ensure safe and useful real-world deployments, have been considered as the longstanding cornerstones in practice. In this paper, we first established comprehensive principles for honesty LLM and further created the HoneSet with 930 queries across six categories, which is designed to evaluate LLMs’ ability to maintain honesty. Then, we improved the honesty and helpfulness of LLMs in both training-free and fine-tuning settings. Specifically, we propose a training-free method named Curiosity-Driven Prompting, which enables LLMs to express their internal confusion and uncertainty about the given query and then optimize their responses. Moreover, we also propose a two-stage fine-tuning approach, inspired by curriculum learning, to enhance the honesty and helpfulness of LLMs. The method first teaches LLMs to distinguish between honest and dishonest, and then LLMs are trained to learn to respond more helpfully. Experimental results demonstrated that both of the two proposed methods improve the helpfulness of LLMs while making them maintain honesty. Our research has paved the way for more reliable and trustworthy LLMs in real-world applications.