---
title: "Stealing part of a production language model"
source: "https://proceedings.mlr.press/v235/carlini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/carlini24a/carlini24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'llm-geometry-and-interpretability-research']
tags: ['model-stealing', 'embedding-extraction', 'black-box-attack', 'production-LLM']
venue: "ICML 2024"
tldr: "Presents the first practical model-stealing attack that extracts the embedding projection layer from black-box production language models via API queries."
---

# Stealing part of a production language model

**Source**: [https://proceedings.mlr.press/v235/carlini24a.html](https://proceedings.mlr.press/v235/carlini24a.html)

**TLDR**: Presents the first practical model-stealing attack that extracts the embedding projection layer from black-box production language models via API queries.

## Abstract

We introduce the first model-stealing attack that extracts precise, nontrivial information from black-box production language models like OpenAI’s ChatGPT or Google’s PaLM-2. Specifically, our attack recovers the embedding projection layer (up to symmetries) of a transformer model, given typical API access. For under $20 USD, our attack extracts the entire projection matrix of OpenAI’s Ada and Babbage language models. We thereby confirm, for the first time, that these black-box models have a hidden dimension of 1024 and 2048, respectively. We also recover the exact hidden dimension size of the GPT-3.5-turbo model, and estimate it would cost under \$2,000 in queries to recover the entire projection matrix. We conclude with potential defenses and mitigations, and discuss the implications of possible future work that could extend our attack.