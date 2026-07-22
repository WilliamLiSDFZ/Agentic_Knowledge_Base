---
title: "Large Language Models Can Learn Representation in Natural Language"
source: "https://aclanthology.org/2024.findings-acl.542/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'concept-embedding-taxonomy-hierarchy-representation']
tags: ['natural-language-representations', 'entity-retrieval', 'tool-use']
venue: "ACL 2024"
tldr: "Demonstrates that LLMs can learn and leverage natural language representations of entities to improve performance on complex multi-entity tasks."
---

# Large Language Models Can Learn Representation in Natural Language

**Source**: [https://aclanthology.org/2024.findings-acl.542/](https://aclanthology.org/2024.findings-acl.542/)

**TLDR**: Demonstrates that LLMs can learn and leverage natural language representations of entities to improve performance on complex multi-entity tasks.

## Abstract

AbstractOne major challenge for Large Language Models (LLMs) is completing complex tasks involving multiple entities, such as tool APIs. To tackle this, one approach is to retrieve relevant entities to enhance LLMs in task completion. A crucial issue here is obtaining accurate natural language representations for each entity to aid in retriever precision. In this paper, we propose the Natural Language Representation Optimization Problem, which aims to refine entity descriptions for improved retrieval and LLM utilization. We introduce the Learning to Represent with Natural Language method, which utilizes LLMs to optimize entity representations consisting of text patterns based on environmental feedback. We iteratively prompt LLMs to enhance or adjust patterns based on entity samples and evaluate their effectiveness through environmental feedback. Our method successfully learns human-understandable representations for classification tasks (e.g., instructions and documents) and API call tasks (e.g., APIbench and Virtual Home), significantly improving GPT-4’s task performance.