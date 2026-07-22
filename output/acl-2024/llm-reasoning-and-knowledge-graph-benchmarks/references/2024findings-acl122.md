---
title: "ChatKBQA: A Generate-then-Retrieve Framework for Knowledge Base Question Answering with Fine-tuned Large Language Models"
source: "https://aclanthology.org/2024.findings-acl.122/"
pdf_url: ""
categories: ['llm-reasoning-and-knowledge-graph-benchmarks', 'text-to-sql-parsing-and-benchmarks']
tags: ['KBQA', 'knowledge-base', 'semantic-parsing', 'generate-then-retrieve', 'fine-tuned-LLMs']
venue: "ACL 2024"
tldr: "ChatKBQA proposes a generate-then-retrieve framework using fine-tuned LLMs for efficient and accurate knowledge base question answering."
---

# ChatKBQA: A Generate-then-Retrieve Framework for Knowledge Base Question Answering with Fine-tuned Large Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.122/](https://aclanthology.org/2024.findings-acl.122/)

**TLDR**: ChatKBQA proposes a generate-then-retrieve framework using fine-tuned LLMs for efficient and accurate knowledge base question answering.

## Abstract

AbstractKnowledge Base Question Answering (KBQA) aims to answer natural language questions over large-scale knowledge bases (KBs), which can be summarized into two crucial steps: knowledge retrieval and semantic parsing. However, three core challenges remain: inefficient knowledge retrieval, mistakes of retrieval adversely impacting semantic parsing, and the complexity of previous KBQA methods. To tackle these challenges, we introduce ChatKBQA, a novel and simple generate-then-retrieve KBQA framework, which proposes first generating the logical form with fine-tuned LLMs, then retrieving and replacing entities and relations with an unsupervised retrieval method, to improve both generation and retrieval more directly. Experimental results show that ChatKBQA achieves new state-of-the-art performance on standard KBQA datasets, WebQSP, and CWQ. This work can also be regarded as a new paradigm for combining LLMs with knowledge graphs (KGs) for interpretable and knowledge-required question answering.