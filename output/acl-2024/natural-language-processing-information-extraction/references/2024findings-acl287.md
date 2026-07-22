---
title: "Locating and Extracting Relational Concepts in Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.287/"
categories: ['language-model-representations-and-embedding-spaces', 'natural-language-processing-information-extraction']
tags: ['relational-concepts', 'knowledge-extraction', 'language-models']
venue: "ACL 2024"
tldr: "Investigates how relational concepts are stored and can be located and extracted from large language model representations."
---

# Locating and Extracting Relational Concepts in Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.287/](https://aclanthology.org/2024.findings-acl.287/)

**TLDR**: Investigates how relational concepts are stored and can be located and extracted from large language model representations.

## Abstract

AbstractRelational concepts are indeed foundational to the structure of knowledge representation, as they facilitate the association between various entity concepts, allowing us to express and comprehend complex world knowledge.By expressing relational concepts in natural language prompts, people can effortlessly interact with large language models (LLMs) and recall desired factual knowledge. However, the process of knowledge recall lacks interpretability, and representations of relational concepts within LLMs remain unknown to us. In this paper, we identify hidden states that can express entity and relational concepts through causal mediation analysis in fact recall processes. Our finding reveals that at the last token position of the input prompt, there are hidden states that solely express the causal effects of relational concepts. Based on this finding, we assume that these hidden states can be treated as relational representations and we can successfully extract them from LLMs. The experimental results demonstrate high credibility of the relational representations: they can be flexibly transplanted into other fact recall processes, and can also be used as robust entity connectors. Moreover, we also show that the relational representations exhibit significant potential for controllable fact recall through relation rewriting.