---
title: "R2E: Turning any Github Repository into a Programming Agent Environment"
source: "https://proceedings.mlr.press/v235/jain24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jain24c/jain24c.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['LLM-agents', 'coding', 'evaluation-benchmark', 'GitHub', 'programming-environments']
venue: "ICML 2024"
tldr: "R2E automatically converts GitHub repositories into interactive environments to evaluate LLM-based coding agents on real-world programming tasks."
---

# R2E: Turning any Github Repository into a Programming Agent Environment

**Source**: [https://proceedings.mlr.press/v235/jain24c.html](https://proceedings.mlr.press/v235/jain24c.html)

**TLDR**: R2E automatically converts GitHub repositories into interactive environments to evaluate LLM-based coding agents on real-world programming tasks.

## Abstract

While Large Language Models’ (LLMs) coding capabilities have advanced rapidly, corresponding evaluation benchmarks on real-world programming setups are yet to catch up. Building a scalable and interactive testbed for evaluating general-purpose AI coding agents for real-world code has been challenging, particularly due to a lack of high-quality test suites available. In this paper, we present Repository to Environment (R2E), a framework that can turn any GitHub repository into a test environment to evaluate the performance of code-generating systems, both static and interactive. R2E is powered by a synergistic combination of program analysis and LLMs to construct equivalence test harnesses for any GitHub function. We instantiate our framework to build the first large-scale benchmark, R2E-Eval1, for building realistic environments for AI coding assistants. Our results demonstrate that even when SOTA models cannot generate correct solutions with advanced prompting techniques, they can effectively use environment feedback highlighting the need to move from static functional coding to interactive programming paradigm. We hope that our framework (and the instantiated benchmark) can motivate research directions by providing web-scale open-ended coding environments. R2E code is available at https://r2e.dev/