---
title: "DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a4cb1444fb05839d0113d2773da88a49-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['visual-language-multimodal-generation-reasoning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['data-analysis', 'code-generation', 'llm', 'benchmark', 'reasoning']
venue: "NeurIPS 2024"
tldr: "DACO introduces an application-driven benchmark and framework for comprehensive data analysis via LLM-based code generation."
---

# DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a4cb1444fb05839d0113d2773da88a49-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a4cb1444fb05839d0113d2773da88a49-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: DACO introduces an application-driven benchmark and framework for comprehensive data analysis via LLM-based code generation.

## Abstract

Data analysis is a crucial analytical process essential for deriving insights from real-world databases. As shown in Figure 1, the need for data analysis typically arises from specific application scenarios, and requires diverse reasoning skills including mathematical reasoning, logical reasoning, and strategic reasoning. Existing work often focus on simple factual retrieval or arithmetic resolutions and thus are insufficient for addressing complex real-world queries. This work aims to propose new resources and benchmarks on this crucial yet challenging and under-explored task. Due to the prohibitively high cost of collecting expert annotations, we use large language models (LLMs) enhanced by code generation to automatically generate high-quality data analysis, which will later be refined by human annotators. We construct the DACO dataset, containing (1) 440 databases (of tabular data) collected from real-world scenarios, (2) ~2k automatically generated query-answer pairs that can serve as weak supervision for model training, and (3) a concentrated but high-quality test set with human refined annotations that serves as our main evaluation benchmark. Experiments show that while LLMs like GPT-4 exhibit promising data analysis capabilities, they are still evaluated as less helpful than human-written analysis on 58.1% cases. Leveraging our weak supervision data, we experiment with various fine-tuning methods, including supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF). Our trained model outperforms existing baselines for table question answering, and RLHF further boosts the helpfulness of generated analysis on 58.5% cases.Data and code are released at https://github.com/shirley-wu/daco.