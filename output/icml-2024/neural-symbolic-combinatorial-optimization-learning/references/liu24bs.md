---
title: "Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model"
source: "https://proceedings.mlr.press/v235/liu24bs.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bs/liu24bs.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'llm-driven-automated-system-optimization']
tags: ['heuristic-design', 'large-language-models', 'evolutionary-algorithms', 'automatic-algorithm-design', 'combinatorial-optimization']
venue: "ICML 2024"
tldr: "Evolution of Heuristics (EoH) uses large language models within an evolutionary paradigm to automatically design efficient heuristics for complex optimization problems."
---

# Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model

**Source**: [https://proceedings.mlr.press/v235/liu24bs.html](https://proceedings.mlr.press/v235/liu24bs.html)

**TLDR**: Evolution of Heuristics (EoH) uses large language models within an evolutionary paradigm to automatically design efficient heuristics for complex optimization problems.

## Abstract

Heuristics are widely used for dealing with complex search and optimization problems. However, manual design of heuristics can be often very labour extensive and requires rich working experience and knowledge. This paper proposes Evolution of Heuristic (EoH), a novel evolutionary paradigm that leverages both Large Language Models (LLMs) and Evolutionary Computation (EC) methods for Automatic Heuristic Design (AHD). EoH represents the ideas of heuristics in natural language, termed thoughts. They are then translated into executable codes by LLMs. The evolution of both thoughts and codes in an evolutionary search framework makes it very effective and efficient for generating high-performance heuristics. Experiments on three widely studied combinatorial optimization benchmark problems demonstrate that EoH outperforms commonly used handcrafted heuristics and other recent AHD methods including FunSearch. Particularly, the heuristic produced by EoH with a low computational budget (in terms of the number of queries to LLMs) significantly outperforms widely-used human hand-crafted baseline algorithms for the online bin packing problem.