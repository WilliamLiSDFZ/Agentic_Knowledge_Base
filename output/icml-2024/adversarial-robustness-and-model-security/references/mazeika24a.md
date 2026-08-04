---
title: "HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal"
source: "https://proceedings.mlr.press/v235/mazeika24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mazeika24a/mazeika24a.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['red-teaming', 'LLM-safety', 'robustness-evaluation']
venue: "ICML 2024"
tldr: "HarmBench, a standardized evaluation framework for automated red teaming and robust refusal assessment of large language models."
---

# HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

**Source**: [https://proceedings.mlr.press/v235/mazeika24a.html](https://proceedings.mlr.press/v235/mazeika24a.html)

**TLDR**: HarmBench, a standardized evaluation framework for automated red teaming and robust refusal assessment of large language models.

## Abstract

Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify several desirable properties previously unaccounted for in red teaming evaluations and systematically design HarmBench to meet these criteria. Using HarmBench, we conduct a large-scale comparison of 18 red teaming methods and 33 target LLMs and defenses, yielding novel insights. We also introduce a highly efficient adversarial training method that greatly enhances LLM robustness across a wide range of attacks, demonstrating how HarmBench enables codevelopment of attacks and defenses. We open source HarmBench at https://github.com/centerforaisafety/HarmBench.