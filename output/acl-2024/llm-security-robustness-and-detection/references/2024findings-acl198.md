---
title: "Red Teaming Visual Language Models"
source: "https://aclanthology.org/2024.findings-acl.198/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection']
tags: ['red-teaming', 'vision-language-models', 'safety', 'adversarial']
venue: "ACL 2024"
tldr: "This work investigates red teaming of vision-language models to identify how multimodal inputs can induce harmful or inaccurate outputs."
---

# Red Teaming Visual Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.198/](https://aclanthology.org/2024.findings-acl.198/)

**TLDR**: This work investigates red teaming of vision-language models to identify how multimodal inputs can induce harmful or inaccurate outputs.

## Abstract

AbstractVLMs (Vision-Language Models) extend the capabilities of LLMs (Large Language Models) to accept multimodal inputs. Since it has been verified that LLMs can be induced to generate harmful or inaccurate content through specific test cases (termed as Red Teaming), how VLMs perform in similar scenarios, especially with their combination of textual and visual inputs, remains a question. To explore this problem, we present a novel red teaming dataset RTVLM, which encompasses 12 subtasks (e.g., image misleading, multi-modal jailbreaking, face fairness, etc) under 4 primary aspects (faithfulness, privacy, safety, fairness). Our RTVLM is the first red teaming dataset to benchmark current VLMs in terms of these 4 different aspects. Detailed analysis shows that 10 prominent open-sourced VLMs struggle with the red teaming in different degrees and have up to 31% performance gap with GPT-4V. Additionally, we simply apply red teaming alignment to LLaVA-v1.5 with Supervised Fine-tuning (SFT) using RTVLM, and this bolsters the models’ performance with 10% in RTVLM test set, 13% in MM-hallu, and without noticeable decline in MM-Bench, overpassing other LLaVA-based models in similar size with regular alignment data. This reveals that current open-sourced VLMs still lack red teaming alignment. Our code and datasets will be open-sourced.