---
title: "RulE: Knowledge Graph Reasoning with Rule Embedding"
source: "https://aclanthology.org/2024.findings-acl.256/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['knowledge-graph', 'rule-embedding', 'logical-reasoning']
venue: "ACL 2024"
tldr: "RulE is a principled framework that embeds logical rules into a unified space to enhance knowledge graph reasoning."
---

# RulE: Knowledge Graph Reasoning with Rule Embedding

**Source**: [https://aclanthology.org/2024.findings-acl.256/](https://aclanthology.org/2024.findings-acl.256/)

**TLDR**: RulE is a principled framework that embeds logical rules into a unified space to enhance knowledge graph reasoning.

## Abstract

AbstractKnowledge graph reasoning is an important problem for knowledge graphs. In this paper, we propose a novel and principled framework called RulE (stands for Rule Embedding) to effectively leverage logical rules to enhance KG reasoning. Unlike knowledge graph embedding methods, RulE learns rule embeddings from existing triplets and first-order rules by jointly representing entities, relations and logical rules in a unified embedding space. Based on the learned rule embeddings, a confidence score can be calculated for each rule, reflecting its consistency with the observed triplets. This allows us to perform logical rule inference in a soft way, thus alleviating the brittleness of logic. On the other hand, RulE injects prior logical rule information into the embedding space, enriching and regularizing the entity/relation embeddings. This makes KGE alone perform better too. RulE is conceptually simple and empirically effective. We conduct extensive experiments to verify each component of RulE.Results on multiple benchmarks reveal that our model outperforms the majority of existing embedding-based and rule-based approaches.