---
title: "Addressing Order Sensitivity of In-Context Demonstration Examples in Causal Language Models"
source: "https://aclanthology.org/2024.findings-acl.386/"
categories: ['llm-training-alignment-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['in-context-learning', 'order-sensitivity', 'causal-language-models']
venue: "ACL 2024"
tldr: "This paper investigates why causal language models are more sensitive to the order of in-context demonstration examples and proposes mitigation strategies."
---

# Addressing Order Sensitivity of In-Context Demonstration Examples in Causal Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.386/](https://aclanthology.org/2024.findings-acl.386/)

**TLDR**: This paper investigates why causal language models are more sensitive to the order of in-context demonstration examples and proposes mitigation strategies.

## Abstract

AbstractIn-context learning has become a popular paradigm in natural language processing. However, its performance can be significantly influenced by the order of in-context demonstration examples. In this paper, we found that causal language models (CausalLMs) are more sensitive to this order compared to prefix language models (PrefixLMs). We attribute this phenomenon to the auto-regressive attention masks within CausalLMs, which restrict each token from accessing information from subsequent tokens. This results in different receptive fields for samples at different positions, thereby leading to representation disparities across positions. To tackle this challenge, we introduce an unsupervised fine-tuning method, termed the Information-Augmented and Consistency-Enhanced approach. This approach utilizes contrastive learning to align representations of in-context examples across different positions and introduces a consistency loss to ensure similar representations for inputs with different permutations. This enhances the model’s predictive consistency across permutations. Experimental results on five benchmarks suggest that our proposed method can reduce the sensitivity of CausalLMs to the order of in-context examples and exhibit robust generalizability, particularly when demonstrations are sourced from a candidate pool different from that used in the training phase, or when the number of in-context examples differs from what is used during training.