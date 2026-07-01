---
title: "Self-Guiding Exploration for Combinatorial Problems"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/eb9120be0dcaac0aec66d2e75deb69dd-Abstract-Conference.html"
categories: ['neural-combinatorial-optimization-and-learning']
tags: ['llm-reasoning', 'combinatorial-problems', 'self-guided-exploration']
venue: "NeurIPS 2024"
tldr: "Proposes a self-guiding exploration strategy leveraging LLMs to solve combinatorial reasoning problems via structured prompting."
---

# Self-Guiding Exploration for Combinatorial Problems

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/eb9120be0dcaac0aec66d2e75deb69dd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/eb9120be0dcaac0aec66d2e75deb69dd-Abstract-Conference.html)

**TLDR**: Proposes a self-guiding exploration strategy leveraging LLMs to solve combinatorial reasoning problems via structured prompting.

## Abstract

Large Language Models (LLMs) have become pivotal in addressing reasoning tasks across diverse domains, including arithmetic, commonsense, and symbolic reasoning. They utilize prompting techniques such as Exploration-of-Thought, Decomposition, and Refinement to effectively navigate and solve intricate tasks. Despite these advancements, the application of LLMs to Combinatorial Problems (CPs), known for their NP-hardness and critical roles in logistics and resource management remains underexplored. To address this gap, we introduce a novel prompting strategy: Self-Guiding Exploration (SGE), designed to enhance the performance of solving CPs. SGE operates autonomously, generating multiple thought trajectories for each CP task. It then breaks these trajectories down into actionable subtasks, executes them sequentially, and refines the results to ensure optimal outcomes. We present our research as the first to apply LLMs to a broad range of CPs and demonstrate that SGE outperforms existing prompting strategies by over 27.84% in CP optimization performance. Additionally, SGE achieves a 2.46% higher accuracy over the best existing results in other reasoning tasks (arithmetic, commonsense, and symbolic).