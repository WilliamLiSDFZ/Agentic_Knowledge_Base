---
title: "Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation"
source: "https://proceedings.mlr.press/v235/halawi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/halawi24a/halawi24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-safety', 'finetuning', 'covert-attack', 'malicious-adaptation', 'safety-alignment']
venue: "ICML 2024"
tldr: "Introduces covert malicious finetuning as a stealthy method to undermine LLM safety through black-box finetuning interfaces."
---

# Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation

**Source**: [https://proceedings.mlr.press/v235/halawi24a.html](https://proceedings.mlr.press/v235/halawi24a.html)

**TLDR**: Introduces covert malicious finetuning as a stealthy method to undermine LLM safety through black-box finetuning interfaces.

## Abstract

Black-box finetuning is an emerging interface for adapting state-of-the-art language models to user needs. However, such access may also let malicious actors undermine model safety. To demonstrate the challenge of defending finetuning interfaces, we introduce covert malicious finetuning, a method to compromise model safety via finetuning while evading detection. Our method constructs a malicious dataset where every individual datapoint appears innocuous, but finetuning on the dataset teaches the model to respond to encoded harmful requests with encoded harmful responses. Applied to GPT-4, our method produces a finetuned model that acts on harmful instructions 99% of the time and avoids detection by defense mechanisms such as dataset inspection, safety evaluations, and input/output classifiers. Our findings question whether black-box finetuning access can be secured against sophisticated adversaries.