---
title: "On the Vulnerability of Safety Alignment in Open-Access LLMs"
source: "https://aclanthology.org/2024.findings-acl.549/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'llm-training-alignment-and-evaluation']
tags: ['safety-alignment', 'jailbreak-attacks', 'open-access-llms']
venue: "ACL 2024"
tldr: "Examines vulnerabilities in safety-aligned open-access LLMs and analyzes how fine-tuning-based attacks can bypass ethical alignment constraints."
---

# On the Vulnerability of Safety Alignment in Open-Access LLMs

**Source**: [https://aclanthology.org/2024.findings-acl.549/](https://aclanthology.org/2024.findings-acl.549/)

**TLDR**: Examines vulnerabilities in safety-aligned open-access LLMs and analyzes how fine-tuning-based attacks can bypass ethical alignment constraints.

## Abstract

AbstractLarge language models (LLMs) possess immense capabilities but are susceptible to malicious exploitation. To mitigate the risk, safety alignment is employed to align LLMs with ethical standards. However, safety-aligned LLMs may remain vulnerable to carefully crafted jailbreak attacks, but these attacks often face high rejection rates and limited harmfulness. In this paper, we expose the vulnerabilities of safety alignment in open-access LLMs, which can significantly enhance the success rate and harmfulness of jailbreak attacks. Through reverse alignment, achieved by accessing model parameters, we show the feasibility of efficiently fine-tuning LLMs to undermine their inherent safeguards. We investigate two types of reverse alignment techniques: reverse supervised fine-tuning (RSFT) and reverse preference optimization (RPO). RSFT operates by supervising the fine-tuning of LLMs to reverse their inherent values. We also explore how to prepare data needed for RSFT. RPO optimizes LLMs to enhance their preference for harmful content, reversing the models’ safety alignment. Our extensive experiments reveal that open-access high-performance LLMs can be adeptly reverse-aligned to output harmful content, even in the absence of manually curated malicious datasets. Our research acts as a whistleblower for the community, emphasizing the need to pay more attention to safety of open-accessing LLMs. It also underscores the limitations of current safety alignment approaches and calls for research on robust safety alignment methods to counteract malicious fine-tuning attacks.