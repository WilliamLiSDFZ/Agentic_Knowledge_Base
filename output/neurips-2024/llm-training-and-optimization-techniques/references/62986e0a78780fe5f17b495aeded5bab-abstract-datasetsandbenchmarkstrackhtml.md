---
title: "Instruction Tuning Large Language Models to Understand Electronic Health Records"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/62986e0a78780fe5f17b495aeded5bab-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare', 'llm-training-and-optimization-techniques']
tags: ['electronic-health-records', 'instruction-tuning', 'clinical-llm']
venue: "NeurIPS 2024"
tldr: "An instruction-tuning framework for LLMs on EHR data to build a conversational AI assistant capable of clinical question answering."
---

# Instruction Tuning Large Language Models to Understand Electronic Health Records

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/62986e0a78780fe5f17b495aeded5bab-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/62986e0a78780fe5f17b495aeded5bab-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: An instruction-tuning framework for LLMs on EHR data to build a conversational AI assistant capable of clinical question answering.

## Abstract

Large language models (LLMs) have shown impressive capabilities in solving a wide range of tasks based on human instructions. However, developing a conversational AI assistant for electronic health record (EHR) data remains challenging due to (1) the lack of large-scale instruction-following datasets and (2) the limitations of existing model architectures in handling complex and heterogeneous EHR data.In this paper, we introduce MIMIC-Instr, a dataset comprising over 400K open-ended instruction-following examples derived from the MIMIC-IV EHR database. This dataset covers various topics and is suitable for instruction-tuning general-purpose LLMs for diverse clinical use cases. Additionally, we propose Llemr, a general framework that enables LLMs to process and interpret EHRs with complex data structures. Llemr demonstrates competitive performance in answering a wide range of patient-related questions based on EHR data.Furthermore, our evaluations on clinical predictive modeling benchmarks reveal that the fine-tuned  Llemr achieves performance comparable to state-of-the-art (SOTA) baselines using curated features. The dataset and code are available at \url{https://github.com/zzachw/llemr}.