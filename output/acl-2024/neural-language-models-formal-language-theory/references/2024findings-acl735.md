---
title: "Non-Autoregressive Machine Translation as Constrained HMM"
source: "https://aclanthology.org/2024.findings-acl.735/"
pdf_url: ""
categories: ['neural-language-models-formal-language-theory', 'state-memory-replay-sequence-modeling']
tags: ['non-autoregressive', 'machine-translation', 'hidden-markov-model', 'directed-acyclic-transformer', 'sequence-modeling']
venue: "ACL 2024"
tldr: "Reframes directed acyclic Transformer non-autoregressive translation as a constrained HMM, providing theoretical and empirical insights."
---

# Non-Autoregressive Machine Translation as Constrained HMM

**Source**: [https://aclanthology.org/2024.findings-acl.735/](https://aclanthology.org/2024.findings-acl.735/)

**TLDR**: Reframes directed acyclic Transformer non-autoregressive translation as a constrained HMM, providing theoretical and empirical insights.

## Abstract

AbstractIn non-autoregressive translation (NAT), directed acyclic Transformers (DAT) have demonstrated their ability to achieve comparable performance to the autoregressive Transformers.In this paper, we first show that DAT is essentially a fully connected left-to-right Hidden Markov Model (HMM), with the source and target sequences being observations and the token positions being latent states.Even though generative models like HMM do not suffer from label bias in traditional task settings (e.g., sequence labeling), we argue here that the left-to-right HMM in NAT may still encounter this issue due to the missing observations at the inference stage.To combat label bias, we propose two constrained HMMs: 1) Adaptive Window HMM, which explicitly balances the number of outgoing transitions at different states; 2) Bi-directional HMM, i.e., a combination of left-to-right and right-to-left HMMs, whose uni-directional components can implicitly regularize each other’s biases via shared parameters.Experimental results on WMT’14 EnDe and WMT’17 ZhEn demonstrate that our methods can achieve better or comparable performance to the original DAT using various decoding methods.We also demonstrate that our methods effectively reduce the impact of label bias.