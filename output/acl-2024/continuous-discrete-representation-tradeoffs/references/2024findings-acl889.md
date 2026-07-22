---
title: "TLCR: Token-Level Continuous Reward for Fine-grained Reinforcement Learning from Human Feedback"
source: "https://aclanthology.org/2024.findings-acl.889/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'continuous-discrete-representation-tradeoffs']
tags: ['RLHF', 'token-level-reward', 'fine-grained-alignment']
venue: "ACL 2024"
tldr: "TLCR introduces token-level continuous rewards for reinforcement learning from human feedback to resolve sequence-level label mismatch."
---

# TLCR: Token-Level Continuous Reward for Fine-grained Reinforcement Learning from Human Feedback

**Source**: [https://aclanthology.org/2024.findings-acl.889/](https://aclanthology.org/2024.findings-acl.889/)

**TLDR**: TLCR introduces token-level continuous rewards for reinforcement learning from human feedback to resolve sequence-level label mismatch.

## Abstract

AbstractReinforcement Learning from Human Feedback (RLHF) leverages human preference data to train language models to align more closely with human essence. These human preference data, however, are labeled at the sequence level, creating a mismatch between sequence-level preference labels and tokens, which are autoregressively generated from the language model. Although several recent approaches have tried to provide token-level (i.e., dense) rewards for each individual token, these typically rely on predefined discrete reward values (e.g., positive: +1, negative: -1, neutral: 0), failing to account for varying degrees of preference inherent to each token. To address this limitation, we introduce TLCR (Token-Level Continuous Reward) for RLHF, which incorporates a discriminator trained to distinguish positive and negative tokens, and the confidence of the discriminator is used to assign continuous rewards to each token considering the context. Extensive experiments show that our proposed TLCR leads to consistent performance improvements over previous sequence-level or token-level discrete rewards on open-ended generation benchmarks.