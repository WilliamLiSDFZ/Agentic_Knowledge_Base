---
title: "Fantastic Semantics and Where to Find Them: Investigating Which Layers of Generative LLMs Reflect Lexical Semantics"
source: "https://aclanthology.org/2024.findings-acl.866/"
categories: ['language-model-representations-and-embedding-spaces', 'transformer-architecture-analysis-and-design']
tags: ['lexical-semantics', 'generative-llm', 'layer-analysis']
venue: "ACL 2024"
tldr: "Investigates which layers of generative LLMs best reflect lexical semantics, finding that middle layers carry the most semantic information."
---

# Fantastic Semantics and Where to Find Them: Investigating Which Layers of Generative LLMs Reflect Lexical Semantics

**Source**: [https://aclanthology.org/2024.findings-acl.866/](https://aclanthology.org/2024.findings-acl.866/)

**TLDR**: Investigates which layers of generative LLMs best reflect lexical semantics, finding that middle layers carry the most semantic information.

## Abstract

AbstractLarge language models have achieved remarkable success in general language understanding tasks. However, as a family of generative methods with the objective of next token prediction, the semantic evolution with the depth of these models are not fully explored, unlike their predecessors, such as BERT-like architectures. In this paper, we specifically investigate the bottom-up evolution of lexical semantics for a popular LLM, namely Llama2, by probing its hidden states at the end of each layer using a contextualized word identification task. Our experiments show that the representations in lower layers encode lexical semantics, while the higher layers, with weaker semantic induction, are responsible for prediction. This is in contrast to models with discriminative objectives, such as mask language modeling, where the higher layers obtain better lexical semantics. The conclusion is further supported by the monotonic increase in performance via the hidden states for the last meaningless symbols, such as punctuation, in the prompting strategy. Our codes are available at https://github.com/RyanLiut/LLM_LexSem.