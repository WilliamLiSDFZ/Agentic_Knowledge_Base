---
title: "On the Role of Long-tail Knowledge in Retrieval Augmented Large Language Models"
source: "https://aclanthology.org/2024.acl-short.12/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['retrieval-augmented-generation', 'long-tail-knowledge', 'LLM-performance']
venue: "ACL 2024"
tldr: "Investigates the role of long-tail knowledge in RAG systems and shows indiscriminate retrieval can hurt performance on common queries."
---

# On the Role of Long-tail Knowledge in Retrieval Augmented Large Language Models

**Source**: [https://aclanthology.org/2024.acl-short.12/](https://aclanthology.org/2024.acl-short.12/)

**TLDR**: Investigates the role of long-tail knowledge in RAG systems and shows indiscriminate retrieval can hurt performance on common queries.

## Abstract

AbstractRetrieval augmented generation (RAG) exhibits outstanding performance in promoting the knowledge capabilities of large language models (LLMs) with retrieved documents related to user queries. However, RAG only focuses on improving the response quality of LLMs via enhancing queries indiscriminately with retrieved information, paying little attention to what type of knowledge LLMs really need to answer original queries more accurately. In this paper, we suggest that long-tail knowledge is crucial for RAG as LLMs have already remembered common world knowledge during large-scale pre-training. Based on our observation, we propose a simple but effective long-tail knowledge detection method for LLMs. Specifically, the novel Generative Expected Calibration Error (GECE) metric is derived to measure the “long-tailness” of knowledge based on both statistics and semantics. Hence, we retrieve relevant documents and infuse them into the model for patching knowledge loopholes only when the input query relates to long-tail knowledge. Experiments show that, compared to existing RAG pipelines, our method achieves over 4x speedup in average inference time and consistent performance improvement in downstream tasks.