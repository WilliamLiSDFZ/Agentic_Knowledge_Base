---
title: "SpeechGuard: Exploring the Adversarial Robustness of Multi-modal Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.596/"
categories: ['llm-security-robustness-and-detection', 'multimodal-language-vision-learning-systems']
tags: ['adversarial-robustness', 'speech-language-models', 'multimodal-safety']
venue: "ACL 2024"
tldr: "An investigation of adversarial vulnerabilities in integrated speech and large language models and evaluation of their safety robustness."
---

# SpeechGuard: Exploring the Adversarial Robustness of Multi-modal Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.596/](https://aclanthology.org/2024.findings-acl.596/)

**TLDR**: An investigation of adversarial vulnerabilities in integrated speech and large language models and evaluation of their safety robustness.

## Abstract

AbstractIntegrated Speech and Large Language Models (SLMs) that can follow speech instructions and generate relevant text responses have gained popularity lately. However, the safety and robustness of these models remains largely unclear. In this work, we investigate the potential vulnerabilities of such instruction-following speech-language models to adversarial attacks and jailbreaking. Specifically, we design algorithms that can generate adversarial examples to jailbreak SLMs in both white-box and black-box attack settings without human involvement. Additionally, we propose countermeasures to thwart such jailbreaking attacks. Our models, trained on dialog data with speech instructions, achieve state-of-the-art performance on spoken question-answering task, scoring over 80% on both safety and helpfulness metrics. Despite safety guardrails, experiments on jailbreaking demonstrate the vulnerability of SLMs to adversarial perturbations and transfer attacks, with average attack success rates of 90% and 10% respectively when evaluated on a dataset of carefully designed harmful questions spanning 12 different toxic categories. However, we demonstrate that our proposed countermeasures reduce the attack success significantly.