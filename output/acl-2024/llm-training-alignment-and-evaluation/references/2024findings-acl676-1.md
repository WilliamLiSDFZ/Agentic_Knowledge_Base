---
title: "Hybrid Alignment Training for Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.676/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['alignment-training', 'instruction-following', 'human-preference', 'hybrid', 'LLMs']
venue: "ACL 2024"
tldr: "Hybrid Alignment Training combines instruction-following and human-preference alignment objectives into a unified training framework for LLMs."
---

# Hybrid Alignment Training for Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.676/](https://aclanthology.org/2024.findings-acl.676/)

**TLDR**: Hybrid Alignment Training combines instruction-following and human-preference alignment objectives into a unified training framework for LLMs.

## Abstract

AbstractAlignment training is crucial for enabling large language models (LLMs) to cater to human intentions and preferences. It is typically performed based on two stages with different objectives: instruction-following alignment and human-preference alignment. However, aligning LLMs with these objectives in sequence suffers from an inherent problem: the objectives may conflict, and the LLMs cannot guarantee to simultaneously align with the instructions and human preferences well. To response to these, in this work, we propose a Hybrid Alignment Training (Hbat) approach, based on alternating alignment and modified elastic weight consolidation methods. The basic idea is to alternate between different objectives during alignment training, so that better collaboration can be achieved between the two alignment tasks. We experiment with Hbat on summarization and dialogue tasks. Experimental results show that the proposed Hbat can significantly outperform all baselines. Notably, Hbat yields consistent performance gains over the traditional two-stage alignment training when using both proximal policy optimization and direct preference optimization.