---
title: "LangSuit·E: Planning, Controlling and Interacting with Large Language Models in Embodied Text Environments"
source: "https://aclanthology.org/2024.findings-acl.879/"
categories: ['llm-agents-reasoning-and-planning']
tags: ['embodied-agents', 'text-environments', 'llm-planning']
venue: "ACL 2024"
tldr: "LangSuit·E is a benchmark for evaluating LLMs as few-shot and zero-shot embodied agents in dynamic text-based interactive environments."
---

# LangSuit·E: Planning, Controlling and Interacting with Large Language Models in Embodied Text Environments

**Source**: [https://aclanthology.org/2024.findings-acl.879/](https://aclanthology.org/2024.findings-acl.879/)

**TLDR**: LangSuit·E is a benchmark for evaluating LLMs as few-shot and zero-shot embodied agents in dynamic text-based interactive environments.

## Abstract

AbstractRecent advances in Large Language Models (LLMs) have shown inspiring achievements in constructing autonomous agents that rely onlanguage descriptions as inputs. However, it remains unclear how well LLMs can function as few-shot or zero-shot embodied agents in dynamic interactive environments. To address this gap, we introduce LangSuit·E, a versatile and simulation-free testbed featuring 6 representative embodied tasks in textual embodied worlds. Compared with previous LLM-based testbeds, LangSuit·E (i) offers adaptability to diverse environments without multiple simulation engines, (ii) evaluates agents’ capacity to develop “internalized world knowledge” with embodied observations, and (iii) allows easy customization of communication and action strategies. To address the embodiment challenge, we devise a novel chain-of-thought (CoT) schema, EmMem, which summarizes embodied states w.r.t. history information. Comprehensive benchmark results illustrate challenges and insights of embodied planning. LangSuit·E represents a significant step toward building embodied generalists in the context of language models.