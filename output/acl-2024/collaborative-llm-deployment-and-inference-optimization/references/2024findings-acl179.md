---
title: "Speculative Decoding via Early-exiting for Faster LLM Inference with Thompson Sampling Control Mechanism"
source: "https://aclanthology.org/2024.findings-acl.179/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization']
tags: ['speculative-decoding', 'early-exiting', 'Thompson-sampling']
venue: "ACL 2024"
tldr: "Proposes early-exiting speculative decoding with a Thompson sampling control mechanism to accelerate LLM inference."
---

# Speculative Decoding via Early-exiting for Faster LLM Inference with Thompson Sampling Control Mechanism

**Source**: [https://aclanthology.org/2024.findings-acl.179/](https://aclanthology.org/2024.findings-acl.179/)

**TLDR**: Proposes early-exiting speculative decoding with a Thompson sampling control mechanism to accelerate LLM inference.

## Abstract

AbstractThe recent advancements in large language models (LLMs) have been extraordinary, yet the escalating inference costs associated with them present challenges in real-world applications. To address these challenges, we propose a novel approach called Early-exiting Speculative Decoding (EESD) with lossless acceleration. Specifically, EESD utilizes a segment of the LLM to generate draft tokens, incorporating Early-exiting structures after the first N layers. To enhance the quality of draft tokens, a self-distillation method is integrated. This early-exiting design not only reduces deployment and training costs but also significantly accelerates the token generation speed. Moreover, we introduce a novel sampling mechanism that leverages Thompson Sampling to regulate the generation processes, automatically determining the quantity of draft tokens in each round. The original LLM is then employed to validate these draft tokens through a single forward pass, and thus guarantees that the final output text maintains a distribution consistent with vanilla auto-regressive decoding. The experimental results on both 13B and 70B models demonstrate that our approach decodes tokens at a markedly accelerated rate compared to prior methods, showing the effectiveness of our approach.