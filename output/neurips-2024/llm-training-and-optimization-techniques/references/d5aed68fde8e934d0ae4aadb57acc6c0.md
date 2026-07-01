---
title: "PaDeLLM-NER: Parallel Decoding in Large Language Models for Named Entity Recognition"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d5aed68fde8e934d0ae4aadb57acc6c0-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['named-entity-recognition', 'parallel-decoding', 'latency-reduction']
venue: "NeurIPS 2024"
tldr: "A parallel decoding approach for LLM-based NER that reduces generation latency by simultaneously predicting entity labels instead of autoregressively."
---

# PaDeLLM-NER: Parallel Decoding in Large Language Models for Named Entity Recognition

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d5aed68fde8e934d0ae4aadb57acc6c0-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d5aed68fde8e934d0ae4aadb57acc6c0-Abstract-Conference.html)

**TLDR**: A parallel decoding approach for LLM-based NER that reduces generation latency by simultaneously predicting entity labels instead of autoregressively.

## Abstract

In this study, we aim to reduce generation latency for Named Entity Recognition (NER) with Large Language Models (LLMs). The main cause of high latency in LLMs is the sequential decoding process, which autoregressively generates all labels and mentions for NER, significantly increase the sequence length. To this end, we introduce Parallel Decoding in LLM for NE} (PaDeLLM-NER), a approach that integrates seamlessly into existing generative model frameworks without necessitating additional modules or architectural modifications. PaDeLLM-NER allows for the simultaneous decoding of all mentions, thereby reducing generation latency. Experiments reveal that PaDeLLM-NER significantly increases inference speed that is 1.76 to 10.22 times faster than the autoregressive approach for both English and Chinese. Simultaneously it maintains the quality of predictions as evidenced by the performance that is on par with the state-of-the-art across various datasets. All resources are available at https://github.com/GeorgeLuImmortal/PaDeLLM_NER.