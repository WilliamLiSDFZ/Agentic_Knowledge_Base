---
title: "CToolEval: A Chinese Benchmark for LLM-Powered Agent Evaluation in Real-World API Interactions"
source: "https://aclanthology.org/2024.findings-acl.928/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'lexical-semantic-change-detection-methods']
tags: ['llm-agents', 'api-interaction', 'chinese-benchmark']
venue: "ACL 2024"
tldr: "CToolEval is a Chinese benchmark evaluating LLMs as agents in real-world API interaction scenarios relevant to Chinese societal applications."
---

# CToolEval: A Chinese Benchmark for LLM-Powered Agent Evaluation in Real-World API Interactions

**Source**: [https://aclanthology.org/2024.findings-acl.928/](https://aclanthology.org/2024.findings-acl.928/)

**TLDR**: CToolEval is a Chinese benchmark evaluating LLMs as agents in real-world API interaction scenarios relevant to Chinese societal applications.

## Abstract

AbstractAssessing the capabilities of large language models (LLMs) as agents in decision making and operational tasks is crucial for the development of LLM-as-agent service. We propose CToolEval, a benchmark designed to evaluate LLMs in the context of Chinese societal applications, featuring 398 APIs across 27 widely-used Apps (e.g., Apps for shopping, map, music, travel, etc.) that cover 14 domains. We further present an evaluation framework that simulates real-life scenarios, to facilitate the assessment of tool invocation ability of LLMs for tool learning and task completion ability for user interation. Our extensive experiments with CToolEval evaluate 11 LLMs, revealing that while GPT-3.5-turbo excels in tool invocation, Chinese LLMs usually struggle with issues like hallucination and a lack of comprehensive tool understanding. Our findings highlight the need for further refinement in decision-making capabilities of LLMs, offering insights into bridging the gap between current functionalities and agent-level performance. To promote further research for LLMs to fully act as reliable agents in complex, real-world situations, we release our data and codes at https://github.com/tjunlp-lab/CToolEval.