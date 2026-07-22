---
title: "StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.664/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['tool-learning', 'benchmark-stability', 'LLM-evaluation']
venue: "ACL 2024"
tldr: "Presents StableToolBench, a stable large-scale benchmark for evaluating LLMs' ability to use external tools reliably across diverse real-world tasks."
---

# StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.664/](https://aclanthology.org/2024.findings-acl.664/)

**TLDR**: Presents StableToolBench, a stable large-scale benchmark for evaluating LLMs' ability to use external tools reliably across diverse real-world tasks.

## Abstract

AbstractLarge Language Models (LLMs) have witnessed remarkable advancements in recent years, prompting the exploration of tool learning, which integrates LLMs with external tools to address diverse real-world challenges. Assessing the capability of LLMs to utilise tools necessitates large-scale and stable benchmarks. However, previous works relied on either hand-crafted online tools with limited scale, or large-scale real online APIs suffering from instability of API status. To address this problem, we introduce StableToolBench, a benchmark evolving from ToolBench, proposing a virtual API server and stable evaluation system. The virtual API server contains a caching system and API simulators which are complementary to alleviate the change in API status. Meanwhile, the stable evaluation system designs solvable pass and win rates using GPT-4 as the automatic evaluator to eliminate the randomness during evaluation. Experimental results demonstrate the stability of StableToolBench, and further discuss the effectiveness of API simulators, the caching system, and the evaluator system.