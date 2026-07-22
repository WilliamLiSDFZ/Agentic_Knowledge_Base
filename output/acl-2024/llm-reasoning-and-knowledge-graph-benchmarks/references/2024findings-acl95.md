---
title: "Everything of Thoughts: Defying the Law of Penrose Triangle for Thought Generation"
source: "https://aclanthology.org/2024.findings-acl.95/"
pdf_url: ""
categories: ['llm-agents-reasoning-and-planning', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['thought-prompting', 'Monte-Carlo-Tree-Search', 'LLM-reasoning']
venue: "ACL 2024"
tldr: "Proposes Everything of Thoughts (XoT), a prompting paradigm that simultaneously achieves high performance, efficiency, and flexibility in LLM reasoning."
---

# Everything of Thoughts: Defying the Law of Penrose Triangle for Thought Generation

**Source**: [https://aclanthology.org/2024.findings-acl.95/](https://aclanthology.org/2024.findings-acl.95/)

**TLDR**: Proposes Everything of Thoughts (XoT), a prompting paradigm that simultaneously achieves high performance, efficiency, and flexibility in LLM reasoning.

## Abstract

AbstractThis paper introduce a novel thought prompting approach called ”Everything of Thoughts” (XoT) for Large Language Models (LLMs) to defy the law of ”Penrose triangle” of existing thought paradigms, to achieve three key perspectives in thought generation simultaneously: performance, efficiency, and flexibility. XoT leverages pretrained reinforcement learning and Monte Carlo Tree Search (MCTS) to incorporate external domain knowledge and planning capability into thoughts, thereby enhancing LLMs’ decision-making capabilities. Through the MCTS-LLM collaborative thought revision framework, XoT autonomously produces high-quality comprehensive cognitive mappings with minimal LLM interactions. Additionally, XoT empowers LLMs to utilize flexible cognitive mappings for solving problems with multiple solutions.We evaluate XoT on several challenging problem-solving tasks, including Game of 24, 8-Puzzle, and Pocket Cube. Our results demonstrate that XoT significantly outperforms existing approaches in various dimensions, showcasing its remarkable proficiency in addressing complex problems across diverse domains. The data and code are available at https://github.com/microsoft/Everything-of-Thoughts-XoT.