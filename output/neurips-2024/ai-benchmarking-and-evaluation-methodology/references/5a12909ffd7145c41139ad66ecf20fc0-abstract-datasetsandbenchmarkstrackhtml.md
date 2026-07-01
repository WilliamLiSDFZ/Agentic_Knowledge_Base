---
title: "SETLEXSEM CHALLENGE: Using Set Operations to Evaluate the Lexical and Semantic Robustness of Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5a12909ffd7145c41139ad66ecf20fc0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['set-operations', 'llm-robustness', 'lexical-semantic-evaluation']
venue: "NeurIPS 2024"
tldr: "SETLEXSEM Challenge evaluates large language models' consistency on set operations under lexical and semantic variations."
---

# SETLEXSEM CHALLENGE: Using Set Operations to Evaluate the Lexical and Semantic Robustness of Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5a12909ffd7145c41139ad66ecf20fc0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5a12909ffd7145c41139ad66ecf20fc0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SETLEXSEM Challenge evaluates large language models' consistency on set operations under lexical and semantic variations.

## Abstract

Set theory is foundational to mathematics and, when sets are finite, to reasoning about the world. An intelligent system should perform set operations consistently, regardless of superficial variations in the operands. Initially designed for semantically-oriented NLP tasks, large language models (LLMs) are now being evaluated on algorithmic tasks. Because sets are comprised of arbitrary symbols (e.g. numbers, words), they provide an opportunity to test, systematically, the invariance of LLMs’ algorithmic abilities under simple lexical or semantic variations. To this end, we present the SETLEXSEM CHALLENGE, a synthetic benchmark that evaluates the performance of LLMs on set operations. SETLEXSEM assesses the robustness of LLMs’ instruction-following abilities under various conditions, focusing on the set operations and the nature and construction of the set members. Evaluating seven LLMs with SETLEXSEM, we find that they exhibit poor robust- ness to variation in both operation and operands. We show – via the framework’s systematic sampling of set members along lexical and semantic dimensions – that LLMs are not only not robust to variation along these dimensions but demonstrate unique failure modes in particular, easy-to-create semantic groupings of "deceptive" sets. We find that rigorously measuring language model robustness to variation in frequency and length is challenging and present an analysis that measures them in- dependently. The code for reproducing the results of this paper, and for generating the SETLEXSEM CHALLENGE dataset, is available https://github.com/amazon-science/SetLexSem-Challenge.