---
title: "Position: Towards Implicit Prompt For Text-To-Image Models"
source: "https://proceedings.mlr.press/v235/yang24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24o/yang24o.pdf"
categories: ['position-papers-on-ml-research-directions', 'adversarial-robustness-and-model-security']
tags: ['implicit-prompts', 'text-to-image', 'safety']
venue: "ICML 2024"
tldr: "A position paper advocating for evaluation of text-to-image models against implicit prompts that bypass explicit safety filters."
---

# Position: Towards Implicit Prompt For Text-To-Image Models

**Source**: [https://proceedings.mlr.press/v235/yang24o.html](https://proceedings.mlr.press/v235/yang24o.html)

**TLDR**: A position paper advocating for evaluation of text-to-image models against implicit prompts that bypass explicit safety filters.

## Abstract

Recent text-to-image (T2I) models have had great success, and many benchmarks have been proposed to evaluate their performance and safety. However, they only consider explicit prompts while neglecting implicit prompts (hint at a target without explicitly mentioning it). These prompts may get rid of safety constraints and pose potential threats to the applications of these models. This position paper highlights the current state of T2I models toward implicit prompts. We present a benchmark named ImplicitBench and conduct an investigation on the performance and impacts of implicit prompts with popular T2I models. Specifically, we design and collect more than 2,000 implicit prompts of three aspects: General Symbols, Celebrity Privacy, and Not-Safe-For-Work (NSFW) Issues, and evaluate six well-known T2I models’ capabilities under these implicit prompts. Experiment results show that (1) T2I models are able to accurately create various target symbols indicated by implicit prompts; (2) Implicit prompts bring potential risks of privacy leakage for T2I models. (3) Constraints of NSFW in most of the evaluated T2I models can be bypassed with implicit prompts. We call for increased attention to the potential and risks of implicit prompts in the T2I community and further investigation into the capabilities and impacts of implicit prompts, advocating for a balanced approach that harnesses their benefits while mitigating their risks.