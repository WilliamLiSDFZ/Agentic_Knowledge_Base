---
title: "GTA: A Benchmark for General Tool Agents"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8a75ee6d4b2eb0b777f549a32a5a5c28-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-agent-communication-and-cooperation']
tags: ['tool-use-benchmark', 'llm-agents', 'real-world-evaluation']
venue: "NeurIPS 2024"
tldr: "GTA introduces a benchmark for evaluating general tool-use capabilities of LLM agents in realistic scenarios."
---

# GTA: A Benchmark for General Tool Agents

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8a75ee6d4b2eb0b777f549a32a5a5c28-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8a75ee6d4b2eb0b777f549a32a5a5c28-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: GTA introduces a benchmark for evaluating general tool-use capabilities of LLM agents in realistic scenarios.

## Abstract

In developing general-purpose agents, significant focus has been placed on integrating large language models (LLMs) with various tools. This poses a challenge to the tool-use capabilities of LLMs. However, there are evident gaps between existing tool evaluations and real-world scenarios. Current evaluations often use AI-generated queries, single-step tasks, dummy tools, and text-only inputs, which fail to reveal the agents' real-world problem-solving abilities effectively. To address this, we propose GTA, a benchmark for General Tool Agents,  featuring three main aspects: (i) Real user queries: human-written queries with simple real-world objectives but implicit tool-use, requiring the LLM to reason the suitable tools and plan the solution steps. (ii) Real deployed tools: an evaluation platform equipped with tools across perception, operation, logic, and creativity categories to evaluate the agents' actual task execution performance. (iii) Real multimodal inputs: authentic image files, such as spatial scenes, web page screenshots, tables, code snippets, and printed/handwritten materials, used as the query contexts to align with real-world scenarios closely. We designed 229 real-world tasks and executable tool chains to evaluate mainstream LLMs. Our findings show that real-world user queries are challenging for existing LLMs, with GPT-4 completing less than 50\% of the tasks and most LLMs achieving below 25\%. This evaluation reveals the bottlenecks in the tool-use capabilities of current LLMs in real-world scenarios, which is beneficial for the advancement of general-purpose tool agents. Dataset and code are available at https://github.com/open-compass/GTA.