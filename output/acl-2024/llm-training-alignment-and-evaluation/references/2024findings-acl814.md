---
title: "ROSE Doesn’t Do That: Boosting the Safety of Instruction-Tuned Large Language Models with Reverse Prompt Contrastive Decoding"
source: "https://aclanthology.org/2024.findings-acl.814/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['LLM-safety', 'instruction-tuning', 'contrastive-decoding', 'reverse-prompt', 'alignment']
venue: "ACL 2024"
tldr: "Proposes reverse prompt contrastive decoding to boost safety of instruction-tuned LLMs without requiring additional training data."
---

# ROSE Doesn’t Do That: Boosting the Safety of Instruction-Tuned Large Language Models with Reverse Prompt Contrastive Decoding

**Source**: [https://aclanthology.org/2024.findings-acl.814/](https://aclanthology.org/2024.findings-acl.814/)

**TLDR**: Proposes reverse prompt contrastive decoding to boost safety of instruction-tuned LLMs without requiring additional training data.

## Abstract

AbstractWith the development of instruction-tuned large language models (LLMs), improving the safety of LLMs has become more critical. However, the current approaches for aligning the LLMs output with expected safety usually require substantial training efforts, e.g., high-quality safety data and expensive computational resources, which are costly and inefficient. To this end, we present reverse prompt contrastive decoding (ROSE), a simple-yet-effective method to directly boost the safety of existing instruction-tuned LLMs without any additional training. The principle of ROSE is to improve the probability of desired safe output via suppressing the undesired output induced by the carefully-designed reverse prompts. Experiments on 6 safety and 2 general-purpose tasks show that, our ROSE not only brings consistent and significant safety improvements (up to +13.8% safety score) upon 5 types of instruction-tuned LLMs, but also benefits the general-purpose ability of LLMs. In-depth analyses explore the underlying mechanism of ROSE, and reveal when and where to use it.