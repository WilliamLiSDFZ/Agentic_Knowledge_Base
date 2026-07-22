---
title: "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models"
source: "https://aclanthology.org/2024.acl-long.70/"
pdf_url: ""
categories: ['collaborative-llm-deployment-and-inference-optimization', 'transformer-architecture-analysis-and-design']
tags: ['mixture-of-experts', 'expert-specialization', 'model-scaling']
venue: "ACL 2024"
tldr: "Introduces DeepSeekMoE, a novel MoE architecture achieving finer expert specialization through segment-level expert decomposition and shared expert isolation."
---

# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

**Source**: [https://aclanthology.org/2024.acl-long.70/](https://aclanthology.org/2024.acl-long.70/)

**TLDR**: Introduces DeepSeekMoE, a novel MoE architecture achieving finer expert specialization through segment-level expert decomposition and shared expert isolation.

## Abstract

AbstractIn the era of large language models, Mixture-of-Experts (MoE) is a promising architecture for managing computational costs when scaling up model parameters. However, conventional MoE architectures like GShard, which activate the top-K out of N experts, face challenges in ensuring expert specialization, i.e. each expert acquires non-overlapping and focused knowledge. In response, we propose the DeepSeekMoE architecture towards ultimate expert specialization. It involves two principal strategies: (1) finely segmenting the experts into mN ones and activating mK from them, allowing for a more flexible combination of activated experts; (2) isolating Ks experts as shared ones, aiming at capturing common knowledge and mitigating redundancy in routed experts. Starting from a modest scale with 2B parameters, we demonstrate that DeepSeekMoE 2B achieves comparable performance with GShard 2.9B, which has 1.5 × expert parameters and computation. In addition, DeepSeekMoE 2B nearly approaches the performance of its dense counterpart with the same number of total parameters, which sets the upper bound of MoE models. Subsequently, we scale up DeepSeekMoE to 16B parameters and show that it achieves comparable performance with DeepSeek 7B and LLaMA2 7B, with only about 40% of computations.