---
title: "Generation Meets Verification: Accelerating Large Language Model Inference with Smart Parallel Auto-Correct Decoding"
source: "https://aclanthology.org/2024.findings-acl.313/"
categories: ['collaborative-llm-deployment-and-inference-optimization', 'minimum-bayes-risk-decoding-efficiency']
tags: ['inference-acceleration', 'speculative-decoding', 'semi-autoregressive']
venue: "ACL 2024"
tldr: "SPACE accelerates LLM inference losslessly by combining semi-autoregressive generation with speculative auto-correct decoding."
---

# Generation Meets Verification: Accelerating Large Language Model Inference with Smart Parallel Auto-Correct Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.313/](https://aclanthology.org/2024.findings-acl.313/)

**TLDR**: SPACE accelerates LLM inference losslessly by combining semi-autoregressive generation with speculative auto-correct decoding.

## Abstract

AbstractThis research aims to accelerate the inference speed of large language models (LLMs) with billions of parameters. We propose Smart Parallel Auto-Correct dEcoding (SPACE), an approach designed for achieving lossless acceleration of LLMs. By integrating semi-autoregressive inference and speculative decoding capabilities, SPACE uniquely enables autoregressive LLMs to parallelize token generation and verification. This is realized through a specialized semi-autoregressive supervised fine-tuning process that equips existing LLMs with the ability to simultaneously predict multiple tokens. Additionally, an auto-correct decoding algorithm facilitates the simultaneous generation and verification of token sequences within a single model invocation. Through extensive experiments on a range of LLMs, SPACE has demonstrated inference speedup ranging from 2.7x-4.0x on HumanEval-X while maintaining output quality.