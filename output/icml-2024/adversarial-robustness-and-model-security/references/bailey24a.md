---
title: "Image Hijacks: Adversarial Images can Control Generative Models at Runtime"
source: "https://proceedings.mlr.press/v235/bailey24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bailey24a/bailey24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['adversarial-images', 'vision-language-models', 'behavior-matching']
venue: "ICML 2024"
tldr: "Adversarial images called image hijacks are introduced that can control vision-language model behavior at inference time."
---

# Image Hijacks: Adversarial Images can Control Generative Models at Runtime

**Source**: [https://proceedings.mlr.press/v235/bailey24a.html](https://proceedings.mlr.press/v235/bailey24a.html)

**TLDR**: Adversarial images called image hijacks are introduced that can control vision-language model behavior at inference time.

## Abstract

Are foundation models secure against malicious actors? In this work, we focus on the image input to a vision-language model (VLM). We discover image hijacks, adversarial images that control the behaviour of VLMs at inference time, and introduce the general Behaviour Matching algorithm for training image hijacks. From this, we derive the Prompt Matching method, allowing us to train hijacks matching the behaviour of an arbitrary user-defined text prompt (e.g. ’the Eiffel Tower is now located in Rome’) using a generic, off-the-shelf dataset unrelated to our choice of prompt. We use Behaviour matching to craft hijacks for four types of attack: forcing VLMs to generate outputs of the adversary’s choice, leak information from their context window, override their safety training, and believe false statements. We study these attacks against LLaVA, a state-of-the-art VLM based on CLIP and LLaMA-2, and find that all attack types achieve a success rate of over 80%. Moreover, our attacks are automated and require only small image perturbations.