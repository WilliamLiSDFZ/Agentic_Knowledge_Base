---
title: "GPTSwarm: Language Agents as Optimizable Graphs"
source: "https://proceedings.mlr.press/v235/zhuge24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhuge24a/zhuge24a.pdf"
categories: ['llm-driven-automated-system-optimization', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-agents', 'graph-optimization', 'prompt-engineering', 'swarm', 'computational-graphs']
venue: "ICML 2024"
tldr: "GPTSwarm unifies LLM-based prompt engineering approaches by modeling agents as optimizable computational graphs."
---

# GPTSwarm: Language Agents as Optimizable Graphs

**Source**: [https://proceedings.mlr.press/v235/zhuge24a.html](https://proceedings.mlr.press/v235/zhuge24a.html)

**TLDR**: GPTSwarm unifies LLM-based prompt engineering approaches by modeling agents as optimizable computational graphs.

## Abstract

Various human-designed prompt engineering techniques have been proposed to improve problem solvers based on Large Language Models (LLMs), yielding many disparate code bases. We unify these approaches by describing LLM-based agents as computational graphs. The nodes implement functions to process multimodal data or query LLMs, and the edges describe the information flow between operations. Graphs can be recursively combined into larger composite graphs representing hierarchies of inter-agent collaboration (where edges connect operations of different agents). Our novel automatic graph optimizers (1) refine node-level LLM prompts (node optimization) and (2) improve agent orchestration by changing graph connectivity (edge optimization). Experiments demonstrate that our framework can be used to efficiently develop, integrate, and automatically improve various LLM agents. Our code is public.