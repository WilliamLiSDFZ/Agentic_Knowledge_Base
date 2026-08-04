---
title: "Fast Adversarial Attacks on Language Models In One GPU Minute"
source: "https://proceedings.mlr.press/v235/sadasivan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sadasivan24a/sadasivan24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['adversarial-attacks', 'beam-search', 'language-models', 'jailbreaking', 'prompt-injection']
venue: "ICML 2024"
tldr: "BEAST is a fast beam-search-based adversarial attack on language models that balances speed, success rate, and readability within one GPU minute."
---

# Fast Adversarial Attacks on Language Models In One GPU Minute

**Source**: [https://proceedings.mlr.press/v235/sadasivan24a.html](https://proceedings.mlr.press/v235/sadasivan24a.html)

**TLDR**: BEAST is a fast beam-search-based adversarial attack on language models that balances speed, success rate, and readability within one GPU minute.

## Abstract

In this paper, we introduce a novel class of fast, beam search-based adversarial attack (BEAST) for Language Models (LMs). BEAST employs interpretable parameters, enabling attackers to balance between attack speed, success rate, and the readability of adversarial prompts. The computational efficiency of BEAST facilitates us to investigate its applications on LMs for jailbreaking, eliciting hallucinations, and privacy attacks. Our gradient-free targeted attack can jailbreak aligned LMs with high attack success rates within one minute. For instance, BEAST can jailbreak Vicuna-7B-v1.5 under one minute with a success rate of 89% when compared to a gradient-based baseline that takes over an hour to achieve 70% success rate using a single Nvidia RTX A6000 48GB GPU. BEAST can also generate adversarial suffixes for successful jailbreaks that can transfer to unseen prompts and unseen models such as GPT-4-Turbo. Additionally, we discover a unique outcome wherein our untargeted attack induces hallucinations in LM chatbots. Through human evaluations, we find that our untargeted attack causes Vicuna-7B-v1.5 to produce $\sim$15% more incorrect outputs when compared to LM outputs in the absence of our attack. We also learn that 22% of the time, BEAST causes Vicuna to generate outputs that are not relevant to the original prompt. Further, we use BEAST to generate adversarial prompts in a few seconds that can boost the performance of existing membership inference attacks for LMs. We believe that our fast attack, BEAST, has the potential to accelerate research in LM security and privacy.