---
title: "Generalization-Enhanced Code Vulnerability Detection via Multi-Task Instruction Fine-Tuning"
source: "https://aclanthology.org/2024.findings-acl.625/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-security-robustness-and-detection']
tags: ['vulnerability-detection', 'multi-task-fine-tuning', 'code-security']
venue: "ACL 2024"
tldr: "Improves code vulnerability detection generalization through multi-task instruction fine-tuning of code pre-trained models."
---

# Generalization-Enhanced Code Vulnerability Detection via Multi-Task Instruction Fine-Tuning

**Source**: [https://aclanthology.org/2024.findings-acl.625/](https://aclanthology.org/2024.findings-acl.625/)

**TLDR**: Improves code vulnerability detection generalization through multi-task instruction fine-tuning of code pre-trained models.

## Abstract

AbstractCode Pre-trained Models (CodePTMs) based vulnerability detection have achieved promising results over recent years. However, these models struggle to generalize as they typically learn superficial mapping from source code to labels instead of understanding the root causes of code vulnerabilities, resulting in poor performance in real-world scenarios beyond the training instances. To tackle this challenge, we introduce VulLLM, a novel framework that integrates multi-task learning with Large Language Models (LLMs) to effectively mine deep-seated vulnerability features. Specifically, we construct two auxiliary tasks beyond the vulnerability detection task. First, we utilize the vulnerability patches to construct a vulnerability localization task. Second, based on the vulnerability features extracted from patches, we leverage GPT-4 to construct a vulnerability interpretation task. VulLLM innovatively augments vulnerability classification by leveraging generative LLMs to understand complex vulnerability patterns, thus compelling the model to capture the root causes of vulnerabilities rather than overfitting to spurious features of a single task. The experiments conducted on six large datasets demonstrate that VulLLM surpasses seven state-of-the-art models in terms of effectiveness, generalization, and robustness.