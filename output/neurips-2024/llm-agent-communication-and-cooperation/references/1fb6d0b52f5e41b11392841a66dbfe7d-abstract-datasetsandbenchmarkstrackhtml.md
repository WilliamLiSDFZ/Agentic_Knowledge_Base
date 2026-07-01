---
title: "Mars: Situated Inductive Reasoning in an Open-World Environment"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1fb6d0b52f5e41b11392841a66dbfe7d-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-agent-communication-and-cooperation', 'ai-benchmarking-and-evaluation-methodology']
tags: ['inductive-reasoning', 'open-world', 'llm-agents', 'situated-learning', 'knowledge-acquisition']
venue: "NeurIPS 2024"
tldr: "Mars is a benchmark for evaluating situated inductive reasoning of LLMs in open-world environments requiring knowledge acquisition and generalization."
---

# Mars: Situated Inductive Reasoning in an Open-World Environment

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1fb6d0b52f5e41b11392841a66dbfe7d-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1fb6d0b52f5e41b11392841a66dbfe7d-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Mars is a benchmark for evaluating situated inductive reasoning of LLMs in open-world environments requiring knowledge acquisition and generalization.

## Abstract

Large Language Models (LLMs) trained on massive corpora have shown remarkable success in knowledge-intensive tasks. Yet, most of them rely on pre-stored knowledge. Inducing new general knowledge from a specific environment andperforming reasoning with the acquired knowledge—situated inductive reasoning, is crucial and challenging for machine intelligence. In this paper, we design Mars, an interactive environment devised for situated inductive reasoning. It introduces counter-commonsense game mechanisms by modifying terrain, survival setting and task dependency while adhering to certain principles. In Mars, agents need to actively interact with their surroundings, derive useful rules and perform decision-making tasks in specific contexts. We conduct experiments on various RL-based and LLM-based methods, finding that they all struggle on this challenging situated inductive reasoning benchmark. Furthermore, we explore Induction from Reflection, where we instruct agents to perform inductive reasoning from history trajectory. The superior performance underscores the importance of inductive reasoning in Mars. Through Mars, we aim to galvanize advancements in situated inductive reasoning and set the stage for developing the next generation of AI systems that can reason in an adaptive and context-sensitive way.