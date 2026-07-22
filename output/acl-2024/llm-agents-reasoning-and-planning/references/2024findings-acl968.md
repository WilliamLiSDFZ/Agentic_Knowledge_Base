---
title: "FragRel: Exploiting Fragment-level Relations in the External Memory of Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.968/"
pdf_url: ""
categories: ['state-memory-replay-sequence-modeling', 'llm-agents-reasoning-and-planning']
tags: ['long-context', 'external-memory', 'fragment-relations']
venue: "ACL 2024"
tldr: "Proposes FragRel, which exploits fragment-level relations in external memory to improve LLM processing of long-context inputs."
---

# FragRel: Exploiting Fragment-level Relations in the External Memory of Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.968/](https://aclanthology.org/2024.findings-acl.968/)

**TLDR**: Proposes FragRel, which exploits fragment-level relations in external memory to improve LLM processing of long-context inputs.

## Abstract

AbstractTo process contexts with unlimited length using Large Language Models (LLMs), recent studies explore hierarchically managing the long text. Only several text fragments are taken from the external memory and passed into the temporary working memory, i.e., LLM’s context window. However, existing approaches isolatedly handle the text fragments without considering their structural connections, thereby suffering limited capability on texts with intensive inter-relations, e.g., coherent stories and code repositories. This work attempts to resolve this by exploiting the fragment-level relations in external memory. First, we formulate the fragment-level relations and present several instantiations for different text types. Next, we introduce a relation-aware fragment assessment criteria upon previous independent fragment assessment. Finally, we present the fragment-connected Hierarchical Memory based LLM. We validate the benefits of involving these relations on long story understanding, repository-level code generation, and long-term chatting.