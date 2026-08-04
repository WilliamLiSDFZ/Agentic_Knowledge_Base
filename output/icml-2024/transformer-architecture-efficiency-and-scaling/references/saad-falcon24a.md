---
title: "Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT"
source: "https://proceedings.mlr.press/v235/saad-falcon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/saad-falcon24a/saad-falcon24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'transformer-architecture-efficiency-and-scaling']
tags: ['long-context', 'retrieval', 'benchmarking', 'BERT', 'document-retrieval']
venue: "ICML 2024"
tldr: "A new benchmark (LoCo) and long-context retrieval model (M2-BERT) are introduced to address failures of retrieval pipelines on long documents."
---

# Benchmarking and Building Long-Context Retrieval Models with LoCo and M2-BERT

**Source**: [https://proceedings.mlr.press/v235/saad-falcon24a.html](https://proceedings.mlr.press/v235/saad-falcon24a.html)

**TLDR**: A new benchmark (LoCo) and long-context retrieval model (M2-BERT) are introduced to address failures of retrieval pipelines on long documents.

## Abstract

Retrieval pipelines are an integral component of many machine learning systems. However, they perform poorly in domains where documents are long (e.g., 10K tokens or more) and where identifying the relevant document requires synthesizing information across the entire text. Developing long-context retrieval encoders suitable for these domains raises three challenges: (1) how to evaluate long-context retrieval performance, (2) how to pretrain a base language model to represent both short contexts (corresponding to queries) and long contexts (corresponding to documents), and (3) how to finetune this model for retrieval under the batch size limitations imposed by GPU memory constraints. To address these challenges, we first introduce LoCoV1, a 12 task benchmark constructed to measure long-context retrieval where chunking is not possible or not effective. We next present the M2-BERT retrieval encoder, an 80M parameter state-space encoder model built from the Monarch Mixer architecture, capable of scaling to documents up to 32K tokens long. We describe a pretraining data mixture which allows this encoder to process both short and long context sequences, and a finetuning approach that adapts this base model to retrieval with only single-sample batches. Finally, we validate the M2-BERT retrieval encoder on LoCoV1, finding that it outperforms competitive Transformer-based models by at least 22.2 points, despite containing 90× fewer parameters.