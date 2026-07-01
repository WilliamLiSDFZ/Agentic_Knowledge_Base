---
title: "CRAG - Comprehensive RAG Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1435d2d0fca85a84d83ddcb754f58c29-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['rag-evaluation-and-diagnosis-framework', 'ai-benchmarking-and-evaluation-methodology']
tags: ['retrieval-augmented-generation', 'benchmark', 'question-answering']
venue: "NeurIPS 2024"
tldr: "CRAG is a comprehensive RAG benchmark designed to capture the diverse and dynamic nature of real-world QA tasks beyond existing datasets."
---

# CRAG - Comprehensive RAG Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1435d2d0fca85a84d83ddcb754f58c29-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/1435d2d0fca85a84d83ddcb754f58c29-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: CRAG is a comprehensive RAG benchmark designed to capture the diverse and dynamic nature of real-world QA tasks beyond existing datasets.

## Abstract

Retrieval-Augmented Generation (RAG) has recently emerged as a promising solution to alleviate Large Language Model (LLM)’s deficiency in lack of knowledge. Existing RAG datasets, however, do not adequately represent the diverse and dynamic nature of real-world Question Answering (QA) tasks. To bridge this gap, we introduce the Comprehensive RAG Benchmark (CRAG), a factual question answering benchmark of 4,409 question-answer pairs and mock APIs to simulate web and Knowledge Graph (KG) search. CRAG is designed to encapsulate a diverse array of questions across five domains and eight question categories, reflecting varied entity popularity from popular to long-tail, and temporal dynamisms ranging from years to seconds. Our evaluation on this benchmark highlights the gap to fully trustworthy QA. Whereas most advanced LLMs achieve $\le 34\%$ accuracy on CRAG, adding RAG in a straightforward manner improves the accuracy only to 44%. State-of-the-art industry RAG solutions only answer 63% questions without any hallucination. CRAG also reveals much lower accuracy in answering questions regarding facts with higher dynamism, lower popularity, or higher complexity, suggesting future research directions. The CRAG benchmark laid the groundwork for a KDD Cup 2024 challenge, attracted thousands of participants and submissions. We commit to maintaining CRAG to serve research communities in advancing RAG solutions and general QA solutions. CRAG is available at https://github.com/facebookresearch/CRAG/.