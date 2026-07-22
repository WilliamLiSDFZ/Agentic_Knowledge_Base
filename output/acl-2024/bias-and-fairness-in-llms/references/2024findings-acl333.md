---
title: "Unveiling Selection Biases: Exploring Order and Token Sensitivity in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.333/"
categories: ['bias-and-fairness-in-llms', 'llm-training-alignment-and-evaluation']
tags: ['selection-bias', 'option-order', 'token-sensitivity']
venue: "ACL 2024"
tldr: "An investigation into order and token selection biases in LLMs when tasked with choosing optimal options from sequences."
---

# Unveiling Selection Biases: Exploring Order and Token Sensitivity in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.333/](https://aclanthology.org/2024.findings-acl.333/)

**TLDR**: An investigation into order and token selection biases in LLMs when tasked with choosing optimal options from sequences.

## Abstract

AbstractIn this paper, we investigate the phenomena of “selection biases” in Large Language Models (LLMs), focusing on problems where models are tasked with choosing the optimal option from an ordered sequence. We delve into biases related to option order and token usage, which significantly impact LLMs’ decision-making processes. We also quantify the impact of these biases through an extensive empirical analysis across multiple models and tasks. Furthermore, we propose mitigation strategies to enhance model performance. Our key contributions are threefold: 1) Precisely quantifying the influence of option order and token on LLMs, 2) Developing strategies to mitigate the impact of token and order sensitivity to enhance robustness, and 3) Offering a detailed analysis of sensitivity across models and tasks, which informs the creation of more stable and reliable LLM applications for selection problems.