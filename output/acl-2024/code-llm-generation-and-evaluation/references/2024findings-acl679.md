---
title: "CodeAttack: Revealing Safety Generalization Challenges of Large Language Models via Code Completion"
source: "https://aclanthology.org/2024.findings-acl.679/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'code-llm-generation-and-evaluation']
tags: ['safety-generalization', 'code-completion', 'jailbreak-attack']
venue: "ACL 2024"
tldr: "CodeAttack reveals safety generalization vulnerabilities in LLMs by exploiting code completion as an attack vector."
---

# CodeAttack: Revealing Safety Generalization Challenges of Large Language Models via Code Completion

**Source**: [https://aclanthology.org/2024.findings-acl.679/](https://aclanthology.org/2024.findings-acl.679/)

**TLDR**: CodeAttack reveals safety generalization vulnerabilities in LLMs by exploiting code completion as an attack vector.

## Abstract

AbstractThe rapid advancement of Large Language Models (LLMs) has brought about remarkable generative capabilities but also raised concerns about their potential misuse. While strategies like supervised fine-tuning and reinforcement learning from human feedback have enhanced their safety, these methods primarily focus on natural languages, which may not generalize to other domains. This paper introduces CodeAttack, a framework that transforms natural language inputs into code inputs, presenting a novel environment for testing the safety generalization of LLMs. Our comprehensive studies on state-of-the-art LLMs including GPT-4, Claude-2, and Llama-2 series reveal a new and universal safety vulnerability of these models against code input: CodeAttack bypasses the safety guardrails of all models more than 80% of the time. We find that a larger distribution gap between CodeAttack and natural language leads to weaker safety generalization, such as encoding natural language input with data structures. Furthermore, we give our hypotheses about the success of CodeAttack: the misaligned bias acquired by LLMs during code training, prioritizing code completion over avoiding the potential safety risk. Finally, we analyze potential mitigation measures. These findings highlight new safety risks in the code domain and the need for more robust safety alignment algorithms to match the code capabilities of LLMs.