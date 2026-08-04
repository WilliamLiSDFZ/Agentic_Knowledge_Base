---
title: "TravelPlanner: A Benchmark for Real-World Planning with Language Agents"
source: "https://proceedings.mlr.press/v235/xie24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xie24j/xie24j.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['LLM-planning', 'benchmark', 'language-agents']
venue: "ICML 2024"
tldr: "TravelPlanner is a benchmark evaluating real-world multi-constraint planning abilities of language agents through travel itinerary generation."
---

# TravelPlanner: A Benchmark for Real-World Planning with Language Agents

**Source**: [https://proceedings.mlr.press/v235/xie24j.html](https://proceedings.mlr.press/v235/xie24j.html)

**TLDR**: TravelPlanner is a benchmark evaluating real-world multi-constraint planning abilities of language agents through travel itinerary generation.

## Abstract

Planning has been part of the core pursuit for artificial intelligence since its conception, but earlier AI agents mostly focused on constrained settings because many of the cognitive substrates necessary for human-level planning have been lacking. Recently, language agents powered by large language models (LLMs) have shown interesting capabilities such as tool use and reasoning. Are these language agents capable of planning in more complex settings that are out of the reach of prior AI agents? To advance this investigation, we propose TravelPlanner, a new planning benchmark that focuses on travel planning, a common real-world planning scenario. It provides a rich sandbox environment, various tools for accessing nearly four million data records, and 1,225 meticulously curated planning intents and reference plans. Comprehensive evaluations show that the current language agents are not yet capable of handling such complex planning tasks—even GPT-4 only achieves a success rate of 0.6%. Language agents struggle to stay on task, use the right tools to collect information, or keep track of multiple constraints. However, we note that the mere possibility for language agents to tackle such a complex problem is in itself non-trivial progress. TravelPlanner provides a challenging yet meaningful testbed for future language agents.