---
title: "Split-and-Denoise: Protect large language model inference with local differential privacy"
source: "https://proceedings.mlr.press/v235/mai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mai24a/mai24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'large-language-model-alignment-and-capabilities']
tags: ['local-differential-privacy', 'llm-inference', 'embedding-privacy']
venue: "ICML 2024"
tldr: "A split-and-denoise framework protecting LLM inference privacy using local differential privacy for Embedding-as-a-Service applications."
---

# Split-and-Denoise: Protect large language model inference with local differential privacy

**Source**: [https://proceedings.mlr.press/v235/mai24a.html](https://proceedings.mlr.press/v235/mai24a.html)

**TLDR**: A split-and-denoise framework protecting LLM inference privacy using local differential privacy for Embedding-as-a-Service applications.

## Abstract

Large Language Models (LLMs) excel in natural language understanding by capturing hidden semantics in vector space. This process enriches the value of text embeddings for various downstream tasks, thereby fostering the Embedding-as-a-Service (EaaS) business model. However, the risk of privacy leakage due to direct text transmission to servers remains a critical concern. To address this, we introduce Split-N-Denoise (SnD), an private inference framework that splits the model to execute the token embedding layer on the client side at minimal computational cost. This allows the client to introduce noise prior to transmitting the embeddings to the server, and subsequently receive and denoise the perturbed output embeddings for downstream tasks. Our approach is designed for the inference stage of LLMs and requires no modifications to the model parameters. Extensive experiments demonstrate SnD’s effectiveness in optimizing the privacy-utility tradeoff across various LLM architectures and diverse downstream tasks. The results reveal an improvement in performance under the same privacy budget compared to the baselines by over 10% on average, offering clients a privacy-preserving solution for local privacy protection.