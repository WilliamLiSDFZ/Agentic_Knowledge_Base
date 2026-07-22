---
title: "Raccoon: Prompt Extraction Benchmark of LLM-Integrated Applications"
source: "https://aclanthology.org/2024.findings-acl.791/"
pdf_url: ""
categories: ['llm-security-robustness-and-detection', 'transformer-architecture-analysis-and-design']
tags: ['prompt-extraction', 'benchmark', 'LLM-security']
venue: "ACL 2024"
tldr: "Raccoon is a benchmark for evaluating prompt extraction attack vulnerabilities in LLM-integrated applications."
---

# Raccoon: Prompt Extraction Benchmark of LLM-Integrated Applications

**Source**: [https://aclanthology.org/2024.findings-acl.791/](https://aclanthology.org/2024.findings-acl.791/)

**TLDR**: Raccoon is a benchmark for evaluating prompt extraction attack vulnerabilities in LLM-integrated applications.

## Abstract

AbstractWith the proliferation of LLM-integrated applications such as GPT-s, millions are deployed, offering valuable services through proprietary instruction prompts. These systems, however, are prone to prompt extraction attacks through meticulously designed queries. To help mitigate this problem, we introduce the Raccoon benchmark which comprehensively evaluates a model’s susceptibility to prompt extraction attacks. Our novel evaluation method assesses models under both defenseless and defended scenarios, employing a dual approach to evaluate the effectiveness of existing defenses and the resilience of the models. The benchmark encompasses 14 categories of prompt extraction attacks, with additional compounded attacks that closely mimic the strategies of potential attackers, alongside a diverse collection of defense templates. This array is, to our knowledge, the most extensive compilation of prompt theft attacks and defense mechanisms to date. Our findings highlight universal susceptibility to prompt theft in the absence of defenses, with OpenAI models demonstrating notable resilience when protected. This paper aims to establish a more systematic benchmark for assessing LLM robustness against prompt extraction attacks, offering insights into their causes and potential countermeasures.