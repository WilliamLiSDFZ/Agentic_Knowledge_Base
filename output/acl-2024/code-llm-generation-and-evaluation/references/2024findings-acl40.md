---
title: "CodeM: Less Data Yields More Versatility via Ability Matrix"
source: "https://aclanthology.org/2024.findings-acl.40/"
categories: ['code-llm-generation-and-evaluation', 'llm-training-alignment-and-evaluation']
tags: ['code-llm', 'instruction-tuning', 'data-efficiency']
venue: "ACL 2024"
tldr: "Introduces an ability matrix framework enabling code LLMs to achieve versatile performance with significantly less training data."
---

# CodeM: Less Data Yields More Versatility via Ability Matrix

**Source**: [https://aclanthology.org/2024.findings-acl.40/](https://aclanthology.org/2024.findings-acl.40/)

**TLDR**: Introduces an ability matrix framework enabling code LLMs to achieve versatile performance with significantly less training data.

## Abstract

AbstractIn the era of code large language models (code LLMs), data engineering plays a pivotal role during the instruction fine-tuning phase. To train a versatile model, previous efforts devote tremendous efforts into crafting instruction data covering all the downstream scenarios. Nonetheless, this will incur significant expenses in constructing data and training model. Therefore, this paper introduces CodeM, a novel data construction strategy, which can efficiently train a versatile model using less data via our newly proposed ability matrix. CodeM uses ability matrix to decouple code LLMs’ abilities into two dimensions, constructing a lightweight training corpus that only covers a subset of target scenarios. Extensive experiments on HumanEvalPack and MultiPL-E imply that code LLMs can combine the single-dimensional abilities to master composed abilities, validating the effectiveness of CodeM.