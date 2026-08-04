---
title: "Characterizing Large Language Model Geometry Helps Solve Toxicity Detection and Generation"
source: "https://proceedings.mlr.press/v235/balestriero24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/balestriero24a/balestriero24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'anomaly-and-out-of-distribution-detection']
tags: ['LLM-geometry', 'intrinsic-dimension', 'toxicity-detection']
venue: "ICML 2024"
tldr: "Geometric analysis of LLM internal representations in closed form is used to improve toxicity detection and generation tasks."
---

# Characterizing Large Language Model Geometry Helps Solve Toxicity Detection and Generation

**Source**: [https://proceedings.mlr.press/v235/balestriero24a.html](https://proceedings.mlr.press/v235/balestriero24a.html)

**TLDR**: Geometric analysis of LLM internal representations in closed form is used to improve toxicity detection and generation tasks.

## Abstract

Large Language Models (LLMs) drive current AI breakthroughs despite very little being known about their internal representations. In this work, we propose to shed the light on LLMs inner mechanisms through the lens of geometry. In particular, we develop in closed form $(i)$ the intrinsic dimension in which the Multi-Head Attention embeddings are constrained to exist and $(ii)$ the partition and per-region affine mappings of the feedforward (MLP) network of LLMs’ layers. Our theoretical findings further enable the design of novel principled solutions applicable to state-of-the-art LLMs. First, we show that, through our geometric understanding, we can bypass LLMs’ RLHF protection by controlling the embedding’s intrinsic dimension through informed prompt manipulation. Second, we derive interpretable geometrical features that can be extracted from any (pre-trained) LLM, providing a rich abstract representation of their inputs. We observe that these features are sufficient to help solve toxicity detection, and even allow the identification of various types of toxicity. Our results demonstrate how, even in large-scale regimes, exact theoretical results can answer practical questions in LLMs. Code: https://github.com/RandallBalestriero/SplineLLM