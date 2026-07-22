---
title: "Can Large Language Models Follow Concept Annotation Guidelines? A Case Study on Scientific and Financial Domains"
source: "https://aclanthology.org/2024.findings-acl.478/"
categories: ['natural-language-processing-information-extraction', 'llm-training-alignment-and-evaluation']
tags: ['annotation-guidelines', 'in-context-learning', 'concept-definitions']
venue: "ACL 2024"
tldr: "Examines LLMs' ability to follow concept annotation guidelines via in-context demonstrations in scientific and financial domains."
---

# Can Large Language Models Follow Concept Annotation Guidelines? A Case Study on Scientific and Financial Domains

**Source**: [https://aclanthology.org/2024.findings-acl.478/](https://aclanthology.org/2024.findings-acl.478/)

**TLDR**: Examines LLMs' ability to follow concept annotation guidelines via in-context demonstrations in scientific and financial domains.

## Abstract

AbstractAlthough large language models (LLMs) exhibit remarkable capacity to leverage in-context demonstrations, it is still unclear to what extent they can learn new facts or concept definitions via prompts. To address this question, we examine the capacity of instruction-tuned LLMs to follow in-context concept annotation guidelines for zero-shot sentence labeling tasks. We design guidelines that present different types of factual and counterfactual concept definitions, which are used as prompts for zero-shot sentence classification tasks. Our results show that although concept definitions consistently help in task performance, only the larger models (with 70B parameters or more) have limited ability to work under counterfactual contexts. Importantly, only proprietary models such as GPT-3.5 can recognize nonsensical guidelines, which we hypothesize is due to more sophisticated alignment methods. Finally, we find that Falcon-180B-chat is outperformed by Llama-2-70B-chat is most cases, which indicates that increasing model scale does not guarantee better adherence to guidelines. Altogether, our simple evaluation method reveals significant gaps in concept understanding between the most capable open-source language models and the leading proprietary APIs.