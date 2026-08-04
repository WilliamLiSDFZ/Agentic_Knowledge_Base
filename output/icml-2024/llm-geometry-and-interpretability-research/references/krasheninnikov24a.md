---
title: "Implicit meta-learning may lead language models to trust more reliable sources"
source: "https://proceedings.mlr.press/v235/krasheninnikov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/krasheninnikov24a/krasheninnikov24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['meta-learning', 'fine-tuning', 'source-reliability', 'implicit-learning']
venue: "ICML 2024"
tldr: "LLMs can implicitly learn to weight document reliability during fine-tuning, modulating updates based on synthetic usefulness indicators."
---

# Implicit meta-learning may lead language models to trust more reliable sources

**Source**: [https://proceedings.mlr.press/v235/krasheninnikov24a.html](https://proceedings.mlr.press/v235/krasheninnikov24a.html)

**TLDR**: LLMs can implicitly learn to weight document reliability during fine-tuning, modulating updates based on synthetic usefulness indicators.

## Abstract

We demonstrate that large language models (LLMs) may learn indicators of document usefulness and modulate their updates accordingly. We introduce random strings ("tags") as indicators of usefulness in a synthetic fine-tuning dataset. Fine-tuning on this dataset leads to implicit meta-learning (IML): in further fine-tuning, the model updates to make more use of text that is tagged as useful. We perform a thorough empirical investigation of this phenomenon, finding (among other things) that (i) it occurs in both pretrained LLMs and those trained from scratch, as well as on a vision task, and (ii) larger models and smaller batch sizes tend to give more IML. We also use probing to examine how IML changes the way models store knowledge in their parameters. Finally, we reflect on what our results might imply about the capabilities, risks, and controllability of future AI systems.