---
title: "Getting the most out of your tokenizer for pre-training and domain adaptation"
source: "https://proceedings.mlr.press/v235/dagan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dagan24a/dagan24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['tokenization', 'llm-pretraining', 'domain-adaptation']
venue: "ICML 2024"
tldr: "Systematically studies tokenizer design choices and their impact on LLM pretraining and domain adaptation performance."
---

# Getting the most out of your tokenizer for pre-training and domain adaptation

**Source**: [https://proceedings.mlr.press/v235/dagan24a.html](https://proceedings.mlr.press/v235/dagan24a.html)

**TLDR**: Systematically studies tokenizer design choices and their impact on LLM pretraining and domain adaptation performance.

## Abstract

Tokenization is an understudied and often neglected component of modern LLMs. Most published works use a single tokenizer for all experiments, often borrowed from another model, without performing ablations or analysis to optimize tokenization. Moreover, the tokenizer is generally kept unchanged when fine-tuning a base model. In this paper, we show that the size, pre-tokenization regular expression, and training data of a tokenizer can significantly impact the model’s generation speed, effective context size, memory usage, and downstream performance. We train specialized Byte-Pair Encoding code tokenizers, and conduct extensive ablations on the impact of tokenizer design on the performance of LLMs for code generation tasks such as HumanEval and MBPP, and provide recommendations for tokenizer hyper-parameters selection and switching the tokenizer in a pre-trained LLM. We perform our experiments on models trained from scratch and from pre-trained models, verifying their applicability to a wide range of use-cases. We find that when fine-tuning on more than 50 billion tokens, we can specialize the tokenizer of a pre-trained LLM to obtain large gains in generation speed and effective context size.