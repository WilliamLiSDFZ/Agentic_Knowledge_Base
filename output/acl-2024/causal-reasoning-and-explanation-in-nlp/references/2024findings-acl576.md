---
title: "Understanding and Patching Compositional Reasoning in LLMs"
source: "https://aclanthology.org/2024.findings-acl.576/"
pdf_url: ""
categories: ['causal-reasoning-and-explanation-in-nlp', 'transformer-architecture-analysis-and-design']
tags: ['compositional-reasoning', 'LLM-failure', 'implicit-relations', 'patching', 'reasoning-chains']
venue: "ACL 2024"
tldr: "Identifies root causes of compositional reasoning failures in LLMs and proposes methods to patch these deficiencies through improved implicit relation generation."
---

# Understanding and Patching Compositional Reasoning in LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.576/](https://aclanthology.org/2024.findings-acl.576/)

**TLDR**: Identifies root causes of compositional reasoning failures in LLMs and proposes methods to patch these deficiencies through improved implicit relation generation.

## Abstract

AbstractLLMs have marked a revolutonary shift, yet they falter when faced with compositional reasoning tasks. Our research embarks on a quest to uncover the root causes of compositional reasoning failures of LLMs, uncovering that most of them stem from the improperly generated or leveraged implicit reasoning results. Inspired by our empirical findings, we resort to Logit Lens and an intervention experiment to dissect the inner hidden states of LLMs. This deep dive reveals that implicit reasoning results indeed surface within middle layers and play a causative role in shaping the final explicit reasoning results. Our exploration further locates multi-head self-attention (MHSA) modules within these layers, which emerge as the linchpins in accurate generation and leveraing of implicit reasoning results. Grounded on the above findings, we develop CREME, a lightweight method to patch errors in compositional reasoning via editing the located MHSA modules. Our empirical evidence stands testament to CREME’s effectiveness, paving the way for autonomously and continuously enhancing compositional reasoning capabilities in language models.