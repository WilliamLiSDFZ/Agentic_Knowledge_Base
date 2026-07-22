---
title: "TAXI: Evaluating Categorical Knowledge Editing for Language Models"
source: "https://aclanthology.org/2024.findings-acl.906/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'llm-training-alignment-and-evaluation']
tags: ['knowledge-editing', 'categorical-reasoning', 'LLM-evaluation', 'consistency', 'benchmark']
venue: "ACL 2024"
tldr: "TAXI is a benchmark evaluating whether knowledge editing in LLMs preserves categorical consistency across related facts."
---

# TAXI: Evaluating Categorical Knowledge Editing for Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.906/](https://aclanthology.org/2024.findings-acl.906/)

**TLDR**: TAXI is a benchmark evaluating whether knowledge editing in LLMs preserves categorical consistency across related facts.

## Abstract

AbstractHumans rarely learn one fact in isolation. Instead, learning a new fact induces knowledge of other facts about the world. For example, in learning a korat is a type of cat, you also infer it is a mammal and has claws, ensuring your model of the world is consistent. Knowledge editing aims to inject new facts into language models to improve their factuality, but current benchmarks fail to evaluate consistency, which is critical to ensure efficient, accurate, and generalizable edits. We manually create TAXI, a new benchmark dataset specifically created to evaluate consistency in categorical knowledge edits. TAXI contains 11,120 multiple-choice queries for 976 edits spanning 41 categories (e.g., Dogs), 164 subjects (e.g., Labrador), and 183 properties (e.g., is a mammal). We then use TAXI to evaluate popular editors’ categorical consistency, measuring how often editing a subject’s category appropriately edits its properties. We find that 1) the editors achieve marginal, yet non-random consistency, 2) their consistency far underperforms human baselines, and 3) consistency is more achievable when editing atypical subjects.