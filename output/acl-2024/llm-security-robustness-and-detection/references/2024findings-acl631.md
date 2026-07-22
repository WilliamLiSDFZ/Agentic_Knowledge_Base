---
title: "DORY: Deliberative Prompt Recovery for LLM"
source: "https://aclanthology.org/2024.findings-acl.631/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'privacy-risks-in-language-model-embeddings']
tags: ['prompt-recovery', 'llm-privacy', 'deliberative-inference']
venue: "ACL 2024"
tldr: "Proposes DORY, a deliberative prompt recovery method for LLMs that works under inference-only API constraints to address privacy concerns."
---

# DORY: Deliberative Prompt Recovery for LLM

**Source**: [https://aclanthology.org/2024.findings-acl.631/](https://aclanthology.org/2024.findings-acl.631/)

**TLDR**: Proposes DORY, a deliberative prompt recovery method for LLMs that works under inference-only API constraints to address privacy concerns.

## Abstract

AbstractPrompt recovery in large language models (LLMs) is crucial for understanding how LLMs work and addressing concerns regarding privacy, copyright, etc. The trend towards inference-only APIs complicates this task by restricting access to essential outputs for recovery. To tackle this challenge, we extract prompt-related information from limited outputs and identify a strong(negative) correlation between output probability-based uncertainty and the success of prompt recovery.This finding led to the development of Deliberative PrOmpt RecoverY (DORY), our novel approach that leverages uncertainty to recover prompts accurately. DORY involves reconstructing drafts from outputs, refining these with hints, and filtering out noise based on uncertainty. Our evaluation shows that DORY outperforms existing baselines across diverse LLMs and prompt benchmarks, improving performance by approximately 10.82% and establishing a new state-of-the-art record in prompt recovery tasks. Significantly, DORY operates using a single LLM without any external resources or model, offering a cost-effective, user-friendly prompt recovery solution.