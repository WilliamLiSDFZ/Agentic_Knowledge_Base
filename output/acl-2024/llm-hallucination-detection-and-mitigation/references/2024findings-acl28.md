---
title: "Towards Verifiable Generation: A Benchmark for Knowledge-aware Language Model Attribution"
source: "https://aclanthology.org/2024.findings-acl.28/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['hallucination', 'attribution', 'structured-knowledge']
venue: "ACL 2024"
tldr: "Defines a benchmark and evaluation metrics for attributing LLM outputs to structured knowledge to support verifiable generation."
---

# Towards Verifiable Generation: A Benchmark for Knowledge-aware Language Model Attribution

**Source**: [https://aclanthology.org/2024.findings-acl.28/](https://aclanthology.org/2024.findings-acl.28/)

**TLDR**: Defines a benchmark and evaluation metrics for attributing LLM outputs to structured knowledge to support verifiable generation.

## Abstract

AbstractAlthough achieving great success, Large Language Models (LLMs) usually suffer from unreliable hallucinations. Although language attribution can be a potential solution, there are no suitable benchmarks and evaluation metrics to attribute LLMs to structured knowledge. In this paper, we define a new task of Knowledge-aware Language Model Attribution (KaLMA) that improves upon three core concerns with conventional attributed LMs. First, we extend attribution source from unstructured texts to Knowledge Graph (KG), whose rich structures benefit both the attribution performance and working scenarios. Second, we propose a new “Conscious Incompetence” setting considering the incomplete knowledge repository, where the model identifies the need for supporting knowledge beyond the provided KG. Third, we propose a comprehensive automatic evaluation metric encompassing text quality, citation quality, and text citation alignment. To implement the above innovations, we build a dataset in biography domain BioKaLMA via evolutionary question generation strategy, to control the question complexity and necessary knowledge to the answer. For evaluation, we develop a baseline solution and demonstrate the room for improvement in LLMs’ citation generation, emphasizing the importance of incorporating the “Conscious Incompetence” setting, and the critical role of retrieval accuracy.