---
title: "Comments as Natural Logic Pivots: Improve Code Generation via Comment Perspective"
source: "https://aclanthology.org/2024.findings-acl.420/"
pdf_url: ""
categories: ['code-llm-generation-and-evaluation', 'llm-agents-reasoning-and-planning']
tags: ['code-generation', 'chain-of-thought', 'comment-guided']
venue: "ACL 2024"
tldr: "Using code comments as logical pivots improves LLM code generation by bridging natural language problem descriptions and code through intermediate reasoning steps."
---

# Comments as Natural Logic Pivots: Improve Code Generation via Comment Perspective

**Source**: [https://aclanthology.org/2024.findings-acl.420/](https://aclanthology.org/2024.findings-acl.420/)

**TLDR**: Using code comments as logical pivots improves LLM code generation by bridging natural language problem descriptions and code through intermediate reasoning steps.

## Abstract

AbstractCode generation aims to understand the problem description and generate corresponding code snippets, where existing works generally decompose such complex tasks into intermediate steps by prompting strategies, such as Chain-of-Thought and its variants. While these studies have achieved some success, their effectiveness is highly dependent on the capabilities of advanced Large Language Models (LLMs) such as GPT-4, particularly in terms of API calls, which significantly limits their practical applicability. Consequently, how to enhance the code generation capabilities of small and medium-scale code LLMs without significantly increasing training costs is an appealing challenge. In this paper, we suggest that code comments are the natural logic pivot between natural language and code language and propose using comments to boost the code generation ability of code LLMs. Concretely, we propose MANGO (comMents As Natural loGic pivOts), including a comment contrastive training strategy and a corresponding logical comment decoding strategy. Experiments are performed on HumanEval and MBPP, utilizing StarCoder and WizardCoder as backbone models, and encompassing model parameter sizes between 3B and 7B. The results indicate that MANGO significantly improves the code pass rate based on the strong baselines. Meanwhile, the robustness of the logical comment decoding strategy is notably higher than the Chain-of-thoughts prompting.