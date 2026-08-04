---
title: "One Size Fits All for Semantic Shifts: Adaptive Prompt Tuning for Continual Learning"
source: "https://proceedings.mlr.press/v235/kim24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ai/kim24ai.pdf"
categories: ['continual-learning-memory-plasticity', 'test-time-adaptation-methods-and-evaluation']
tags: ['continual-learning', 'prompt-tuning', 'semantic-shift']
venue: "ICML 2024"
tldr: "Proposes adaptive prompt tuning that handles variable-degree semantic shifts in continual learning scenarios."
---

# One Size Fits All for Semantic Shifts: Adaptive Prompt Tuning for Continual Learning

**Source**: [https://proceedings.mlr.press/v235/kim24ai.html](https://proceedings.mlr.press/v235/kim24ai.html)

**TLDR**: Proposes adaptive prompt tuning that handles variable-degree semantic shifts in continual learning scenarios.

## Abstract

In real-world continual learning (CL) scenarios, tasks often exhibit intricate and unpredictable semantic shifts, posing challenges for fixed prompt management strategies which are tailored to only handle semantic shifts of uniform degree (i.e., uniformly mild or uniformly abrupt). To address this limitation, we propose an adaptive prompting approach that effectively accommodates semantic shifts of varying degree where mild and abrupt shifts are mixed. AdaPromptCL employs the assign-and-refine semantic grouping mechanism that dynamically manages prompt groups in accordance with the semantic similarity between tasks, enhancing the quality of grouping through continuous refinement. Our experiment results demonstrate that AdaPromptCL outperforms existing prompting methods by up to 21.3%, especially in the benchmark datasets with diverse semantic shifts between tasks.