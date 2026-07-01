---
title: "SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ac840df270ac537dd74530a15c332684-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['spreadsheet-manipulation', 'LLM-benchmark', 'real-world-evaluation', 'table-reasoning', 'code-generation']
venue: "NeurIPS 2024"
tldr: "SpreadsheetBench is a challenging real-world benchmark for evaluating LLMs on spreadsheet manipulation tasks."
---

# SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ac840df270ac537dd74530a15c332684-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ac840df270ac537dd74530a15c332684-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: SpreadsheetBench is a challenging real-world benchmark for evaluating LLMs on spreadsheet manipulation tasks.

## Abstract

We introduce SpreadsheetBench, a challenging spreadsheet manipulation benchmark exclusively derived from real-world scenarios, designed to immerse current large language models (LLMs) in the actual workflow of spreadsheet users. Unlike existing benchmarks that rely on synthesized queries and simplified spreadsheet files, SpreadsheetBench is built from 912 real questions gathered from online Excel forums, which reflect the intricate needs of users. The associated spreadsheets from the forums contain a variety of tabular data such as multiple tables, non-standard relational tables, and abundant non-textual elements. Furthermore, we propose a more reliable evaluation metric akin to online judge platforms, where multiple spreadsheet files are created as test cases for each instruction, ensuring the evaluation of robust solutions capable of handling spreadsheets with varying values.Our comprehensive evaluation of various LLMs under both single-round and multi-round inference settings reveals a substantial gap between the state-of-the-art (SOTA) models and human performance, highlighting the benchmark's difficulty.