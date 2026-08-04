---
title: "The Stronger the Diffusion Model, the Easier the Backdoor: Data Poisoning to Induce Copyright BreachesWithout Adjusting Finetuning Pipeline"
source: "https://proceedings.mlr.press/v235/wang24bm.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bm/wang24bm.pdf"
categories: ['adversarial-robustness-and-model-security', 'generative-models-and-variational-inference']
tags: ['backdoor-attack', 'data-poisoning', 'diffusion-models', 'copyright-infringement']
venue: "ICML 2024"
tldr: "Demonstrates that stronger diffusion models are more vulnerable to data poisoning backdoor attacks that induce copyright breaches without modifying the finetuning pipeline."
---

# The Stronger the Diffusion Model, the Easier the Backdoor: Data Poisoning to Induce Copyright BreachesWithout Adjusting Finetuning Pipeline

**Source**: [https://proceedings.mlr.press/v235/wang24bm.html](https://proceedings.mlr.press/v235/wang24bm.html)

**TLDR**: Demonstrates that stronger diffusion models are more vulnerable to data poisoning backdoor attacks that induce copyright breaches without modifying the finetuning pipeline.

## Abstract

The commercialization of text-to-image diffusion models (DMs) brings forth potential copyright concerns. Despite numerous attempts to protect DMs from copyright issues, the vulnerabilities of these solutions are underexplored. In this study, we formalized the Copyright Infringement Attack on generative AI models and proposed a backdoor attack method, SilentBadDiffusion, to induce copyright infringement without requiring access to or control over training processes. Our method strategically embeds connections between pieces of copyrighted information and text references in poisoning data while carefully dispersing that information, making the poisoning data inconspicuous when integrated into a clean dataset. Our experiments show the stealth and efficacy of the poisoning data. When given specific text prompts, DMs trained with a poisoning ratio of 0.20% can produce copyrighted images. Additionally, the results reveal that the more sophisticated the DMs are, the easier the success of the attack becomes. These findings underline potential pitfalls in the prevailing copyright protection strategies and underscore the necessity for increased scrutiny to prevent the misuse of DMs.