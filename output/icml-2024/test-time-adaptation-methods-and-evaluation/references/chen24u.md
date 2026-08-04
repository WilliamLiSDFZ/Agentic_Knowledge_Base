---
title: "From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning"
source: "https://proceedings.mlr.press/v235/chen24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24u/chen24u.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'test-time-adaptation-methods-and-evaluation']
tags: ['sycophancy', 'LLM-alignment', 'pinpoint-tuning', 'truthfulness']
venue: "ICML 2024"
tldr: "Pinpoint tuning targets and reduces sycophantic behavior in LLMs by fine-tuning specifically on instances where models incorrectly capitulate to user challenges."
---

# From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning

**Source**: [https://proceedings.mlr.press/v235/chen24u.html](https://proceedings.mlr.press/v235/chen24u.html)

**TLDR**: Pinpoint tuning targets and reduces sycophantic behavior in LLMs by fine-tuning specifically on instances where models incorrectly capitulate to user challenges.

## Abstract

Large Language Models (LLMs) tend to prioritize adherence to user prompts over providing veracious responses, leading to the sycophancy issue. When challenged by users, LLMs tend to admit mistakes and provide inaccurate responses even if they initially provided the correct answer. Recent works propose to employ supervised fine-tuning (SFT) to mitigate the sycophancy issue, while it typically leads to the degeneration of LLMs’ general capability. To address the challenge, we propose a novel supervised pinpoint tuning (SPT), where the region-of-interest modules are tuned for a given objective. Specifically, SPT first reveals and verifies a small percentage ($<$5%) of the basic modules, which significantly affect a particular behavior of LLMs. i.e., sycophancy. Subsequently, SPT merely fine-tunes these identified modules while freezing the rest. To verify the effectiveness of the proposed SPT, we conduct comprehensive experiments, demonstrating that SPT significantly mitigates the sycophancy issue of LLMs (even better than SFT). Moreover, SPT introduces limited or even no side effects on the general capability of LLMs. Our results shed light on how to precisely, effectively, and efficiently explain and improve the targeted ability of LLMs.