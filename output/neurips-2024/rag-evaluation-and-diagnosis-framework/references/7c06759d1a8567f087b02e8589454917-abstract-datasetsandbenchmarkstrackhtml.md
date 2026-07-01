---
title: "UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7c06759d1a8567f087b02e8589454917-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['rag-evaluation-and-diagnosis-framework', 'scientific-document-retrieval-and-citation']
tags: ['retrieval-augmented-generation', 'document-analysis', 'benchmark']
venue: "NeurIPS 2024"
tldr: "A benchmark suite evaluating RAG systems on real-world document analysis tasks including academic literature and financial question answering."
---

# UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7c06759d1a8567f087b02e8589454917-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7c06759d1a8567f087b02e8589454917-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark suite evaluating RAG systems on real-world document analysis tasks including academic literature and financial question answering.

## Abstract

The use of Retrieval-Augmented Generation (RAG) has improved Large Language Models (LLMs) in collaborating with external data, yet significant challenges exist in real-world scenarios. In areas such as academic literature and finance question answering, data are often found in raw text and tables in HTML or PDF formats, which can be lengthy and highly unstructured. In this paper, we introduce a benchmark suite, namely Unstructured Document Analysis (UDA), that involves 2,965 real-world documents and 29,590 expert-annotated Q&A pairs. We revisit popular LLM- and RAG-based solutions for document analysis and evaluate the design choices and answer qualities across multiple document domains and diverse query types. Our evaluation yields interesting findings and highlights the importance of data parsing and retrieval.  We hope our benchmark can shed light and better serve real-world document analysis applications. The benchmark suite and code can be found at https://github.com/qinchuanhui/UDA-Benchmark