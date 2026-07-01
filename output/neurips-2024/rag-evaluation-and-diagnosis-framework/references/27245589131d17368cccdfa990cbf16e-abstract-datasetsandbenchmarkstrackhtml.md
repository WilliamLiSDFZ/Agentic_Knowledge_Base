---
title: "RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/27245589131d17368cccdfa990cbf16e-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['rag-evaluation-and-diagnosis-framework', 'ai-benchmarking-and-evaluation-methodology']
tags: ['RAG-evaluation', 'retrieval-augmented-generation', 'fine-grained-diagnosis']
venue: "NeurIPS 2024"
tldr: "RAGChecker provides a fine-grained diagnostic framework for evaluating retrieval and generation modules of RAG systems independently."
---

# RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/27245589131d17368cccdfa990cbf16e-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/27245589131d17368cccdfa990cbf16e-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: RAGChecker provides a fine-grained diagnostic framework for evaluating retrieval and generation modules of RAG systems independently.

## Abstract

Despite Retrieval-Augmented Generation (RAG) has shown promising capability in leveraging external knowledge, a comprehensive evaluation of RAG systems is still challenging due to the modular nature of RAG, evaluation of long-form responses and reliability of measurements. In this paper, we propose a fine-grained evaluation framework, RAGChecker, that incorporates a suite of diagnostic metrics for both the retrieval and generation modules. Meta evaluation verifies that RAGChecker has significantly better correlations with human judgments than other evaluation metrics. Using RAGChecker, we evaluate 8 RAG systems and conduct an in-depth analysis of their performance, revealing insightful patterns and trade-offs in the design choices of RAG architectures. The metrics of RAGChecker can guide researchers and practitioners in developing more effective RAG systems.