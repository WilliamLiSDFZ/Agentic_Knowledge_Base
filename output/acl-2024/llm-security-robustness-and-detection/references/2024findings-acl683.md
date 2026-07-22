---
title: "TRAP: Targeted Random Adversarial Prompt Honeypot for Black-Box Identification"
source: "https://aclanthology.org/2024.findings-acl.683/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['adversarial-prompts', 'model-identification', 'black-box-detection']
venue: "ACL 2024"
tldr: "Proposes TRAP, a honeypot-based method using targeted random adversarial prompts to identify whether a released LLM violates usage compliance rules."
---

# TRAP: Targeted Random Adversarial Prompt Honeypot for Black-Box Identification

**Source**: [https://aclanthology.org/2024.findings-acl.683/](https://aclanthology.org/2024.findings-acl.683/)

**TLDR**: Proposes TRAP, a honeypot-based method using targeted random adversarial prompts to identify whether a released LLM violates usage compliance rules.

## Abstract

AbstractLarge Language Model (LLM) services and models often come with legal rules on *who* can use them and *how* they must use them. Assessing the compliance of the released LLMs is crucial, as these rules protect the interests of the LLM contributor and prevent misuse. In this context, we describe the novel fingerprinting problem of Black-box Identity Verification (BBIV). The goal is to determine whether a third-party application uses a certain LLM through its chat function. We propose a method called Targeted Random Adversarial Prompt (TRAP) that identifies the specific LLM in use. We repurpose adversarial suffixes, originally proposed for jailbreaking, to get a pre-defined answer from the target LLM, while other models give random answers. TRAP detects the target LLMs with over 95% true positive rate at under 0.2% false positive rate even after a single interaction. TRAP remains effective even if the LLM has minor changes that do not significantly alter the original function.