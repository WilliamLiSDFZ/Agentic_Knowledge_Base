---
title: "Better & Faster Large Language Models via Multi-token Prediction"
source: "https://proceedings.mlr.press/v235/gloeckle24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gloeckle24a/gloeckle24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['multi-token-prediction', 'language-model-training', 'sample-efficiency']
venue: "ICML 2024"
tldr: "Proposes training LLMs to predict multiple future tokens simultaneously, yielding improved sample efficiency and performance."
---

# Better & Faster Large Language Models via Multi-token Prediction

**Source**: [https://proceedings.mlr.press/v235/gloeckle24a.html](https://proceedings.mlr.press/v235/gloeckle24a.html)

**TLDR**: Proposes training LLMs to predict multiple future tokens simultaneously, yielding improved sample efficiency and performance.

## Abstract

Large language models such as GPT and Llama are trained with a next-token prediction loss. In this work, we suggest that training language models to predict multiple future tokens at once results in higher sample efficiency. More specifically, at each position in the training corpus, we ask the model to predict the following $n$ tokens using $n$ independent output heads, operating on top of a shared model trunk. Considering multi-token prediction as an auxiliary training task, we measure improved downstream capabilities with no overhead in training time for both code and natural language models. The method is increasingly useful for larger model sizes, and keeps its appeal when training for multiple epochs. Gains are especially pronounced on generative benchmarks like coding, where our models consistently outperform strong baselines by several percentage points. Our 13B parameter models solves 12% more problems on Human Eval and 17% more on MBPP than comparable next-token models. Experiments on small algorithmic tasks demonstrate that multi-token prediction is favorable for the development of induction heads and algorithmic reasoning capabilities. As an additional benefit, models trained with 4-token prediction are up to $3\times$ faster at inference, even with large batch sizes.