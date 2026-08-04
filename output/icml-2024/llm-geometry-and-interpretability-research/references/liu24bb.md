---
title: "How do Large Language Models Navigate Conflicts between Honesty and Helpfulness?"
source: "https://proceedings.mlr.press/v235/liu24bb.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bb/liu24bb.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['llm-alignment', 'honesty', 'helpfulness']
venue: "ICML 2024"
tldr: "An experimental investigation using psychological models to study how LLMs navigate trade-offs between honesty and helpfulness in everyday communication scenarios."
---

# How do Large Language Models Navigate Conflicts between Honesty and Helpfulness?

**Source**: [https://proceedings.mlr.press/v235/liu24bb.html](https://proceedings.mlr.press/v235/liu24bb.html)

**TLDR**: An experimental investigation using psychological models to study how LLMs navigate trade-offs between honesty and helpfulness in everyday communication scenarios.

## Abstract

In day-to-day communication, people often approximate the truth — for example, rounding the time or omitting details — in order to be maximally helpful to the listener. How do large language models (LLMs) handle such nuanced trade-offs? To address this question, we use psychological models and experiments designed to characterize human behavior to analyze LLMs. We test a range of LLMs and explore how optimization for human preferences or inference-time reasoning affects these trade-offs. We find that reinforcement learning from human feedback improves both honesty and helpfulness, while chain-of-thought prompting skews LLMs towards helpfulness over honesty. Finally, GPT-4 Turbo demonstrates human-like response patterns including sensitivity to the conversational framing and listener’s decision context. Our findings reveal the conversational values internalized by LLMs and suggest that even these abstract values can, to a degree, be steered by zero-shot prompting.