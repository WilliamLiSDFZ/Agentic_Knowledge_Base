---
title: "Reasons to Reject? Aligning Language Models with Judgments"
source: "https://aclanthology.org/2024.findings-acl.730/"
categories: ['llm-training-alignment-and-evaluation']
tags: ['rlhf', 'language-feedback', 'alignment']
venue: "ACL 2024"
tldr: "Proposes aligning language models using natural language judgments as feedback rather than scalar reward signals."
---

# Reasons to Reject? Aligning Language Models with Judgments

**Source**: [https://aclanthology.org/2024.findings-acl.730/](https://aclanthology.org/2024.findings-acl.730/)

**TLDR**: Proposes aligning language models using natural language judgments as feedback rather than scalar reward signals.

## Abstract

AbstractAs humans, we consistently interact with our peers and receive feedback in the form of natural language. This language feedback allows us to maintain appropriate behavior, and rectify potential errors. The question arises naturally: can we use language feedback to align large language models (LLMs)? In contrast to previous research that aligns LLMs with scalar rewards, we present the first systematic exploration of alignment through the lens of language feedback (i.e., judgment). We start with an in-depth investigation of potential methods that can be adapted for aligning LLMs with judgments, revealing that these methods cannot fully capitalize on judgments. To facilitate more effective utilization of judgments, we propose a novel framework, Contrastive Unlikelihood Training (CUT), that allows for fine-grained inappropriate content detection and correction based on judgments. Our results show that, with merely 1317 off-the-shelf judgment data, CUT can beat the 175B DaVinci003 and surpass the best baseline by 50.84 points on AlpacaEval using LLaMA2-13b. CUT can also align LLMs in an iterative fashion using up-to-date model-specific judgments, improving performance from 81.09 to 91.68 points on AlpacaEval using LLaMA2-chat-13b. Further analysis suggests that judgments hold greater potential in LLM alignment than rewards.