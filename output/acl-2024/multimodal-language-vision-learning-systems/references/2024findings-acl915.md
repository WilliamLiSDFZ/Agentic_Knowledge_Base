---
title: "CounterCurate: Enhancing Physical and Semantic Visio-Linguistic Compositional Reasoning via Counterfactual Examples"
source: "https://aclanthology.org/2024.findings-acl.915/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems']
tags: ['counterfactual-reasoning', 'visio-linguistic-compositionality', 'multimodal-models']
venue: "ACL 2024"
tldr: "Proposes CounterCurate to generate counterfactual examples improving physical and semantic compositional reasoning in multimodal models."
---

# CounterCurate: Enhancing Physical and Semantic Visio-Linguistic Compositional Reasoning via Counterfactual Examples

**Source**: [https://aclanthology.org/2024.findings-acl.915/](https://aclanthology.org/2024.findings-acl.915/)

**TLDR**: Proposes CounterCurate to generate counterfactual examples improving physical and semantic compositional reasoning in multimodal models.

## Abstract

AbstractWe propose CounterCurate, a framework to comprehensively improve the visio-linguistic compositional reasoning capability for both contrastive and generative multimodal models. In particular, we identify two critical under- explored problems: the neglect of physically grounded reasoning (counting and position understanding) and the potential of using highly capable text and image generation models for semantic counterfactual fine-tuning. Our work pioneers an approach in addressing these gaps.We first spotlight the near-chance performance of multimodal models like CLIP and LLaVA in physically grounded compositional reasoning. We then apply simple data augmentation using the grounded image generation model GLIGEN to generate fine-tuning data, resulting in significant performance improvements: +33% and +37% for CLIP and LLaVA, respectively, on our newly curated Flickr30k-Positions benchmark. Moreover, we exploit the capabilities of high-performing text generation and image generation models, specifically GPT-4V and DALLE-3, to curate challenging semantic counterfactuals, thereby further enhancing compositional reasoning capabilities on benchmarks such as SugarCrepe, where CounterCurate outperforms GPT-4V.To facilitate future research, we release ourcode, dataset, benchmark, and checkpoints at https://countercurate.github.io/