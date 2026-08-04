---
title: "Instruction Tuning for Secure Code Generation"
source: "https://proceedings.mlr.press/v235/he24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24k/he24k.pdf"
categories: ['adversarial-robustness-and-model-security', 'large-language-model-alignment-and-capabilities']
tags: ['instruction-tuning', 'code-generation', 'security']
venue: "ICML 2024"
tldr: "Investigates instruction tuning methods to improve secure code generation in large language models."
---

# Instruction Tuning for Secure Code Generation

**Source**: [https://proceedings.mlr.press/v235/he24k.html](https://proceedings.mlr.press/v235/he24k.html)

**TLDR**: Investigates instruction tuning methods to improve secure code generation in large language models.

## Abstract

Modern language models (LMs) have gained widespread acceptance in everyday and professional contexts, particularly in programming. An essential procedure enabling this adoption is instruction tuning, which substantially enhances LMs’ practical utility by training them to follow user instructions and human preferences. However, existing instruction tuning schemes overlook a crucial aspect: the security of generated code. As a result, even the state-of-the-art instruction-tuned LMs frequently produce unsafe code, posing significant security risks. In this work, we introduce SafeCoder to address this gap. SafeCoder performs security-centric fine-tuning using a diverse and high-quality dataset that we collected using an automated pipeline. We integrate the security fine-tuning with standard instruction tuning, to facilitate a joint optimization of both security and utility. Despite its simplicity, we show that SafeCoder is effective across a variety of popular LMs and datasets. It is able to drastically improve security (by about 30%), while preserving utility.