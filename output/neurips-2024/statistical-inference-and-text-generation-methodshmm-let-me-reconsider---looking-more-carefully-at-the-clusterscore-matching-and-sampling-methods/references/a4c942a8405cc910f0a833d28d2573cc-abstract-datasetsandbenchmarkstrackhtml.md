---
title: "AMBROSIA: A Benchmark for Parsing Ambiguous Questions into Database Queries"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a4c942a8405cc910f0a833d28d2573cc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**']
tags: ['semantic-parsing', 'text-to-SQL', 'ambiguity', 'benchmark', 'natural-language-interfaces']
venue: "NeurIPS 2024"
tldr: "AMBROSIA is a benchmark for evaluating text-to-SQL parsers on ambiguous natural language questions with multiple valid interpretations."
---

# AMBROSIA: A Benchmark for Parsing Ambiguous Questions into Database Queries

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a4c942a8405cc910f0a833d28d2573cc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a4c942a8405cc910f0a833d28d2573cc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: AMBROSIA is a benchmark for evaluating text-to-SQL parsers on ambiguous natural language questions with multiple valid interpretations.

## Abstract

Practical semantic parsers are expected to understand user utterances and map them to executable programs, even when these are ambiguous. We introduce a new benchmark, AMBROSIA, which we hope will inform and inspire the development of text-to-SQL parsers capable of recognizing and interpreting ambiguous requests. Our dataset contains questions showcasing three different types of ambiguity (scope ambiguity, attachment ambiguity, and vagueness), their interpretations, and corresponding SQL queries. In each case, the ambiguity persists even when the database context is provided. This is achieved through a novel approach that involves controlled generation of databases from scratch. We benchmark various LLMs on AMBROSIA, revealing that even the most advanced models struggle to identify and interpret ambiguity in questions.