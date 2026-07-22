---
title: "A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.443/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-hallucination-detection-and-mitigation']
tags: ['jailbreak', 'safety', 'adversarial-attacks']
venue: "ACL 2024"
tldr: "A comprehensive study benchmarks jailbreak attack and defense strategies for large language models."
---

# A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.443/](https://aclanthology.org/2024.findings-acl.443/)

**TLDR**: A comprehensive study benchmarks jailbreak attack and defense strategies for large language models.

## Abstract

AbstractLarge Language Models (LLMs) have increasingly become central to generating content with potential societal impacts. Notably, these models have demonstrated capabilities for generating content that could be deemed harmful. To mitigate these risks, researchers have adopted safety training techniques to align model outputs with societal values to curb the generation of malicious content. However, the phenomenon of “jailbreaking” — where carefully crafted prompts elicit harmful responses from models — persists as a significant challenge. This research conducts a comprehensive analysis of existing studies on jailbreaking LLMs and their defense techniques. We meticulously investigate nine attack techniques and seven defense techniques applied across three distinct language models: Vicuna, LLama, and GPT-3.5 Turbo. We aim to evaluate the effectiveness of these attack and defense techniques. Our findings reveal that existing white-box attacks underperform compared to universal techniques and that including special tokens in the input significantly affects the likelihood of successful attacks. This research highlights the need to concentrate on the security facets of LLMs. Additionally, we contribute to the field by releasing our datasets and testing framework, aiming to foster further research into LLM security. We believe these contributions will facilitate the exploration of security measures within this domain.