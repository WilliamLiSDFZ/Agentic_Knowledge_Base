---
title: "Dwell in the Beginning: How Language Models Embed Long Documents for Dense Retrieval"
source: "https://aclanthology.org/2024.acl-short.35/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'transformer-architecture-analysis-and-design']
tags: ['positional-bias', 'dense-retrieval', 'document-encoding']
venue: "ACL 2024"
tldr: "Transformer-based models for dense retrieval exhibit positional biases, over-representing information from the beginning of long documents."
---

# Dwell in the Beginning: How Language Models Embed Long Documents for Dense Retrieval

**Source**: [https://aclanthology.org/2024.acl-short.35/](https://aclanthology.org/2024.acl-short.35/)

**TLDR**: Transformer-based models for dense retrieval exhibit positional biases, over-representing information from the beginning of long documents.

## Abstract

AbstractThis study investigates the existence of positional biases in Transformer-based language models for text representation learning, particularly in the context of web document retrieval. We build on previous research that demonstrated loss of information in the middle of input sequences for causal language models, extending it to the domain of embedding learning. We examine positional biases at multiple stages of the training pipeline for an encoder-decoder neural retrieval model, namely language model pre-training, contrastive pre-training, and contrastive fine-tuning. Experiments with the MS-MARCO document collection reveal that after contrastive pre-training the model already generates embeddings that better capture the beginning of the input content, with fine-tuning further aggravating this effect.