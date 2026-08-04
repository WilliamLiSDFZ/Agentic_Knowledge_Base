---
title: "Data Engineering for Scaling Language Models to 128K Context"
source: "https://proceedings.mlr.press/v235/fu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24d/fu24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['long-context', 'continual-pretraining', 'data-engineering']
venue: "ICML 2024"
tldr: "Data engineering strategies for continual pretraining are studied to scale language model context lengths up to 128K tokens."
---

# Data Engineering for Scaling Language Models to 128K Context

**Source**: [https://proceedings.mlr.press/v235/fu24d.html](https://proceedings.mlr.press/v235/fu24d.html)

**TLDR**: Data engineering strategies for continual pretraining are studied to scale language model context lengths up to 128K tokens.

## Abstract

We study continual pretraining recipe for scaling language models’ context lengths to 128K, with a focus on data engineering. We hypothesize that long context modeling, in particular the ability to utilize information at arbitrary input locations, is a capability that is mostly already acquired through large-scale pretraining, and that this capability can be readily extended to contexts substantially longer than seen during training (e.g., 4K to 128K) through lightweight continual pretraining on appropriate data mixture. We investigate the quantity and quality of the data for continual pretraining: (1) for quantity, we show that 500 million to 5 billion tokens are enough to enable the model to retrieve information anywhere within the 128K context; (2) for quality, our results equally emphasize domain balance and length upsampling. Concretely, naïvely upsampling longer data on certain domains like books, a common practice of existing work, gives suboptimal performance; a balanced domain mixture is equally important. We demonstrate that continual pretraining of the full model on 1B-5B tokens of such data is an effective and affordable strategy for scaling the context length of language models to 128K. Our recipe outperforms strong open-source long-context models and closes the gap to frontier models like GPT-4 128K.