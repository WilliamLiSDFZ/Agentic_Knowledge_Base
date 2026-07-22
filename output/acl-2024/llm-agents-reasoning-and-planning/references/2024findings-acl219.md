---
title: "A + B: A General Generator-Reader Framework for Optimizing LLMs to Unleash Synergy Potential"
source: "https://aclanthology.org/2024.findings-acl.219/"
categories: ['llm-hallucination-detection-and-mitigation', 'llm-agents-reasoning-and-planning']
tags: ['retrieval-augmented-generation', 'generate-then-read', 'knowledge-grounding']
venue: "ACL 2024"
tldr: "Proposes a general generator-reader framework that optimizes the synergy between LLM generation and reading for knowledge-intensive tasks."
---

# A + B: A General Generator-Reader Framework for Optimizing LLMs to Unleash Synergy Potential

**Source**: [https://aclanthology.org/2024.findings-acl.219/](https://aclanthology.org/2024.findings-acl.219/)

**TLDR**: Proposes a general generator-reader framework that optimizes the synergy between LLM generation and reading for knowledge-intensive tasks.

## Abstract

AbstractRetrieval-Augmented Generation (RAG) is an effective solution to supplement necessary knowledge to large language models (LLMs). Targeting its bottleneck of retriever performance, “generate-then-read” pipeline is proposed to replace the retrieval stage with generation from the LLM itself. Although promising, this research direction is underexplored and still cannot work in the scenario when source knowledge is given. In this paper, we formalize a general “A + B” framework with varying combinations of foundation models and types for systematic investigation. We explore the efficacy of the base and chat versions of LLMs and found their different functionalities suitable for generator A and reader B, respectively. Their combinations consistently outperform single models, especially in complex scenarios. Furthermore, we extend the application of the “A + B” framework to scenarios involving source documents through continuous learning, enabling the direct integration of external knowledge into LLMs. This approach not only facilitates effective acquisition of new knowledge but also addresses the challenges of safety and helpfulness post-adaptation. The paper underscores the versatility of the “A + B” framework, demonstrating its potential to enhance the practical application of LLMs across various domains.