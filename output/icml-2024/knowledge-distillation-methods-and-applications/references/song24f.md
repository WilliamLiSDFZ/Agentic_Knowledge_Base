---
title: "SLEB: Streamlining LLMs through Redundancy Verification and Elimination of Transformer Blocks"
source: "https://proceedings.mlr.press/v235/song24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24f/song24f.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['LLM-pruning', 'transformer-block-elimination', 'redundancy', 'model-compression']
venue: "ICML 2024"
tldr: "SLEB streamlines LLMs by identifying and removing redundant transformer blocks through a redundancy verification process to reduce deployment costs."
---

# SLEB: Streamlining LLMs through Redundancy Verification and Elimination of Transformer Blocks

**Source**: [https://proceedings.mlr.press/v235/song24f.html](https://proceedings.mlr.press/v235/song24f.html)

**TLDR**: SLEB streamlines LLMs by identifying and removing redundant transformer blocks through a redundancy verification process to reduce deployment costs.

## Abstract

Large language models (LLMs) have proven to be highly effective across various natural language processing tasks. However, their large number of parameters poses significant challenges for practical deployment. Pruning, a technique aimed at reducing the size and complexity of LLMs, offers a potential solution by removing redundant components from the network. Despite the promise of pruning, existing methods often struggle to achieve substantial end-to-end LLM inference speedup. In this paper, we introduce SLEB, a novel approach designed to stream- line LLMs by eliminating redundant transformer blocks. We choose the transformer block as the fundamental unit for pruning, because LLMs exhibit block-level redundancy with high similarity between the outputs of neighboring blocks. This choice allows us to effectively enhance the processing speed of LLMs. Our experimental results demonstrate that SLEB outperforms previous LLM pruning methods in accelerating LLM inference while also maintaining superior perplexity and accuracy, making SLEB as a promising technique for enhancing the efficiency of LLMs. The code is available at: https://github.com/jiwonsong-dev/SLEB.