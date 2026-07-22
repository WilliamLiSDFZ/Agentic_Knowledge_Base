---
title: "Strong hallucinations from negation and how to fix them"
source: "https://aclanthology.org/2024.findings-acl.752/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'neural-language-models-formal-language-theory']
tags: ['hallucination', 'negation', 'logical-consistency']
venue: "ACL 2024"
tldr: "Language models produce strong hallucinations from negation due to computational constraints, and targeted fixes can substantially reduce this failure mode."
---

# Strong hallucinations from negation and how to fix them

**Source**: [https://aclanthology.org/2024.findings-acl.752/](https://aclanthology.org/2024.findings-acl.752/)

**TLDR**: Language models produce strong hallucinations from negation due to computational constraints, and targeted fixes can substantially reduce this failure mode.

## Abstract

AbstractDespite great performance on many tasks, language models (LMs) still struggle with reasoning, sometimes providing responses that cannot possibly be true because they stem from logical incoherence. We call such responses strong hallucinations and prove that they follow from an LM’s computation of its internal representations for logical operators and outputs from those representations. Focusing on negation, we provide a novel solution in which negation is treated not as another element of a latent representation, but as an operation over an LM’s latent representations that constrains how they may evolve. We show that our approach improves model performance in cloze prompting and natural language inference tasks with negation without requiring training on sparse negative data.