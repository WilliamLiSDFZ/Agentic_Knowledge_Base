---
title: "Chain-of-Verification Reduces Hallucination in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.212/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-agents-reasoning-and-planning']
tags: ['hallucination', 'chain-of-verification', 'LLM', 'factual-accuracy', 'self-correction']
venue: "ACL 2024"
tldr: "Proposes Chain-of-Verification, a method where LLMs verify their own responses step-by-step to reduce factual hallucinations."
---

# Chain-of-Verification Reduces Hallucination in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.212/](https://aclanthology.org/2024.findings-acl.212/)

**TLDR**: Proposes Chain-of-Verification, a method where LLMs verify their own responses step-by-step to reduce factual hallucinations.

## Abstract

AbstractGeneration of plausible yet incorrect factual information, termed hallucination, is an unsolved issue in large language models. We study the ability of language models to deliberate on the responses they give in order to correct their mistakes. We develop the Chain-of-Verification (CoVe) method whereby the model first (i) drafts an initial response; then (ii) plans verification questions to fact-check its draft; (iii) answers those questions independently so the answers are not biased by other responses; and (iv) generates its final verified response. In experiments, we show CoVe decreases hallucinations across a variety of tasks, from list-based questions from Wikidata, closed book MultiSpanQA and longform text generation.