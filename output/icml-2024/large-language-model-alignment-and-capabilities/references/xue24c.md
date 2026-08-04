---
title: "OpenMoE: An Early Effort on Open Mixture-of-Experts Language Models"
source: "https://proceedings.mlr.press/v235/xue24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xue24c/xue24c.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['mixture-of-experts', 'open-source-LLM', 'scaling']
venue: "ICML 2024"
tldr: "Presents OpenMoE, a series of fully open-sourced decoder-only mixture-of-experts LLMs scaled up to 34B parameters trained on over 1T tokens."
---

# OpenMoE: An Early Effort on Open Mixture-of-Experts Language Models

**Source**: [https://proceedings.mlr.press/v235/xue24c.html](https://proceedings.mlr.press/v235/xue24c.html)

**TLDR**: Presents OpenMoE, a series of fully open-sourced decoder-only mixture-of-experts LLMs scaled up to 34B parameters trained on over 1T tokens.

## Abstract

To help the open-source community have a better understanding of Mixture-of-Experts (MoE) based large language models (LLMs), we train and release OpenMoE, a series of fully open-sourced and reproducible decoder-only MoE LLMs, ranging from 650M to 34B parameters and trained on up to over 1T tokens. Our investigation confirms that MoE-based LLMs can offer a more favorable cost-effectiveness trade-off than dense LLMs, highlighting the potential effectiveness for future LLM development. One more important contribution of this study is an in-depth analysis of the routing mechanisms within our OpenMoE models, leading to three significant findings: Context-Independent Specialization, Early Routing Learning, and Drop-towards-the-End. We discovered that routing decisions in MoE models are predominantly based on token IDs, with minimal context relevance. The token-to-expert assignments are determined early in the pre-training phase and remain largely unchanged. This imperfect routing can result in performance degradation, particularly in sequential tasks like multi-turn conversations, where tokens appearing later in a sequence are more likely to be dropped. Finally, we rethink our design based on the above-mentioned observations and analysis. To facilitate future MoE LLM development, we propose potential strategies for mitigating the issues we found and further improving off-the-shelf MoE LLM designs.