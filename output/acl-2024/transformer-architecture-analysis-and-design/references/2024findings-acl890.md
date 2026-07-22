---
title: "Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization"
source: "https://aclanthology.org/2024.findings-acl.890/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['long-context', 'positional-bias', 'attention', 'LLM']
venue: "ACL 2024"
tldr: "Addresses the lost-in-the-middle problem in LLMs by calibrating positional attention bias to improve utilization of information in the middle of long contexts."
---

# Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization

**Source**: [https://aclanthology.org/2024.findings-acl.890/](https://aclanthology.org/2024.findings-acl.890/)

**TLDR**: Addresses the lost-in-the-middle problem in LLMs by calibrating positional attention bias to improve utilization of information in the middle of long contexts.

## Abstract

AbstractLarge language models (LLMs), even when specifically trained to process long input contexts, struggle to capture relevant information located in the middle of their input. This phenomenon has been known as the lost-in-the-middle problem. In this work, we make three contributions. First, we set out to understand the factors that cause this phenomenon. In doing so, we establish a connection between lost-in-the-middle to LLMs’ intrinsic attention bias: LLMs exhibit an U-shaped attention bias where the tokens at the beginning and at the end of its input receive higher attention, regardless of their relevance. Second, we mitigate this positional bias through a calibration mechanism, found-in-the-middle, that allows the model to attend to contexts faithfully according to their relevance, even though when they are in the middle. Third, we show found-in-the-middle not only achieves better performance in locating relevant information within a long context, but also eventually leads to improved retrieval-augmented generation (RAG) performance across various tasks, outperforming existing methods by up to 10 percentage point. These findings open up future directions in understanding LLM attention bias and its potential consequences.