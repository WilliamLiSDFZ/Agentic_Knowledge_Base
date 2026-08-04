---
title: "Dual Operating Modes of In-Context Learning"
source: "https://proceedings.mlr.press/v235/lin24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24l/lin24l.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['in-context-learning', 'task-retrieval', 'task-learning']
venue: "ICML 2024"
tldr: "A theoretical analysis revealing the dual operating modes of in-context learning: task learning and task retrieval."
---

# Dual Operating Modes of In-Context Learning

**Source**: [https://proceedings.mlr.press/v235/lin24l.html](https://proceedings.mlr.press/v235/lin24l.html)

**TLDR**: A theoretical analysis revealing the dual operating modes of in-context learning: task learning and task retrieval.

## Abstract

In-context learning (ICL) exhibits dual operating modes: task learning, i.e., acquiring a new skill from in-context samples, and task retrieval, i.e., locating and activating a relevant pretrained skill. Recent theoretical work proposes various mathematical models to analyze ICL, but they cannot fully explain the duality. In this work, we analyze a generalized probabilistic model for pretraining data, obtaining a quantitative understanding of the two operating modes of ICL. Leveraging our analysis, we provide the first explanation of an unexplained phenomenon observed with real-world large language models (LLMs). Under some settings, the ICL risk initially increases and then decreases with more in-context examples. Our analysis offers a plausible explanation for this "early ascent" phenomenon: a limited number of in-context samples may lead to the retrieval of an incorrect skill, thereby increasing the risk, which will eventually diminish as task learning takes effect with more in-context samples. We also analyze ICL with biased labels, e.g., zero-shot ICL, where in-context examples are assigned random labels, and predict the bounded efficacy of such approaches. We corroborate our analysis and predictions with extensive experiments with Transformers and LLMs.