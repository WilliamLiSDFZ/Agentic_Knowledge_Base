---
title: "STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'rag-evaluation-and-diagnosis-framework']
tags: ['LLM-retrieval', 'knowledge-bases', 'semi-structured-data']
venue: "NeurIPS 2024"
tldr: "STaRK benchmarks LLM-based retrieval over semi-structured knowledge bases combining unstructured text and structured relational information."
---

# STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: STaRK benchmarks LLM-based retrieval over semi-structured knowledge bases combining unstructured text and structured relational information.

## Abstract

Answering real-world complex queries, such as complex product search, often requires accurate retrieval from semi-structured knowledge bases that involve blend of unstructured (e.g., textual descriptions of products) and structured (e.g., entity relations of products) information. However, many previous works studied textual and relational retrieval tasks as separate topics. To address the gap, we develop STARK, a large-scale Semi-structure retrieval benchmark on Textual and Relational Knowledge Bases. Our benchmark covers three domains: product search, academic paper search, and queries in precision medicine. We design a novel pipeline to synthesize realistic user queries that integrate diverse relational information and complex textual properties, together with their ground-truth answers (items). We conduct rigorous human evaluation to validate the quality of our synthesized queries. We further enhance the benchmark with high-quality human-generated queries to provide an authentic reference. STARK serves as a comprehensive testbed for evaluating the performance of retrieval systems driven by large language models (LLMs). Our experiments suggest that STARK presents significant challenges to the current retrieval and LLM systems, highlighting the need for more capable semi-structured retrieval systems.