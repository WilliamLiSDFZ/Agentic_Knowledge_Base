---
title: "Making Harmful Behaviors Unlearnable for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.611/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['llm-safety', 'fine-tuning', 'unlearnable-examples', 'harmful-behavior', 'adversarial']
venue: "ACL 2024"
tldr: "Proposes a method to make harmful behaviors unlearnable for LLMs during fine-tuning to prevent misuse while preserving utility."
---

# Making Harmful Behaviors Unlearnable for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.611/](https://aclanthology.org/2024.findings-acl.611/)

**TLDR**: Proposes a method to make harmful behaviors unlearnable for LLMs during fine-tuning to prevent misuse while preserving utility.

## Abstract

AbstractLarge language models (LLMs) have shown great potential to empower various domains and are often customized by fine-tuning for the requirements of different applications. However, the powerful learning ability of LLMs not only enables them to learn new tasks but also makes them vulnerable to learning undesired behaviors, such as harmfulness and hallucination, as the fine-tuning data often implicitly or explicitly contains such content. Can we fine-tune LLMs on harmful data without learning harmful behaviors? This paper proposes a controllable training framework to make undesired behaviors unlearnable during the fine-tuning process. Specifically, we introduce security vectors to control the model’s behavior and make it consistent with the undesired behavior. Security vectors are activated during fine-tuning, the consistent behavior makes the model believe that such behavior has already been learned and there is no need for further optimization, while inconsistent data can still be learned. After fine-tuning, security vectors are deactivated to restore the LLM’s normal behavior. Our experiments show that the security vectors can prevent LLM from learning harmful and hallucination behavior while preserving the ability to learn other information.