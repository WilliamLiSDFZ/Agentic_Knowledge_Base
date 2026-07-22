---
title: "ViCor: Bridging Visual Understanding and Commonsense Reasoning with Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.640/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'llm-agents-reasoning-and-planning']
tags: ['visual-commonsense-reasoning', 'VLM', 'LLM', 'synergy', 'multimodal']
venue: "ACL 2024"
tldr: "ViCor bridges vision-language models and LLMs to tackle visual commonsense reasoning by exploiting their complementary strengths."
---

# ViCor: Bridging Visual Understanding and Commonsense Reasoning with Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.640/](https://aclanthology.org/2024.findings-acl.640/)

**TLDR**: ViCor bridges vision-language models and LLMs to tackle visual commonsense reasoning by exploiting their complementary strengths.

## Abstract

AbstractIn our work, we explore the synergistic capabilities of pre-trained vision-and-language models (VLMs) and large language models (LLMs) on visual commonsense reasoning (VCR) problems. We find that VLMs and LLMs-based decision pipelines are good at different kinds of VCR problems. Pre-trained VLMs exhibit strong performance for problems involving understanding the literal visual content, which we noted as visual commonsense understanding (VCU). For problems where the goal is to infer conclusions beyond image content, which we noted as visual commonsense inference (VCI), VLMs face difficulties, while LLMs, given sufficient visual evidence, can use commonsense to infer the answer well. We empirically validate this by letting LLMs classify VCR problems into these two categories and show the significant difference between VLM and LLM with image caption decision pipelines on two subproblems. Moreover, we identify a challenge with VLMs’ passive perception, which may miss crucial context information, leading to incorrect reasoning by LLMs. Based on these, we suggest a collaborative approach, named ViCor, where pre-trained LLMs serve as problem classifiers to analyze the problem category, then either use VLMs to answer the question directly or actively instruct VLMs to concentrate on and gather relevant visual elements to support potential commonsense inferences. We evaluate our framework on two VCR benchmark datasets and outperform all other methods without in-domain fine-tuning.