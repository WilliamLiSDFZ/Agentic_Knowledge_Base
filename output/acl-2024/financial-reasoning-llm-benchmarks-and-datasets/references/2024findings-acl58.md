---
title: "EconNLI: Evaluating Large Language Models on Economics Reasoning"
source: "https://aclanthology.org/2024.findings-acl.58/"
pdf_url: ""
categories: ['financial-reasoning-llm-benchmarks-and-datasets', 'llm-training-alignment-and-evaluation']
tags: ['economics-reasoning', 'LLM-evaluation', 'financial-NLP', 'benchmark']
venue: "ACL 2024"
tldr: "Introduces EconNLI, a benchmark for evaluating LLMs' ability to understand economic knowledge and reason about outcomes of economic events."
---

# EconNLI: Evaluating Large Language Models on Economics Reasoning

**Source**: [https://aclanthology.org/2024.findings-acl.58/](https://aclanthology.org/2024.findings-acl.58/)

**TLDR**: Introduces EconNLI, a benchmark for evaluating LLMs' ability to understand economic knowledge and reason about outcomes of economic events.

## Abstract

AbstractLarge Language Models (LLMs) are widely used for writing economic analysis reports or providing financial advice, but their ability to understand economic knowledge and reason about potential results of specific economic events lacks systematic evaluation. To address this gap, we propose a new dataset, natural language inference on economic events (EconNLI), to evaluate LLMs’ knowledge and reasoning abilities in the economic domain. We evaluate LLMs on (1) their ability to correctly classify whether a premise event will cause a hypothesis event and (2) their ability to generate reasonable events resulting from a given premise. Our experiments reveal that LLMs are not sophisticated in economic reasoning and may generate wrong or hallucinated answers. Our study raises awareness of the limitations of using LLMs for critical decision-making involving economic reasoning and analysis. The dataset and codes are available at https://github.com/Irenehere/EconNLI.