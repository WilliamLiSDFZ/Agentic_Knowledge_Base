---
title: "MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9f80af32390984cb709cdeb014d0df41-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare']
tags: ['clinical-journey', 'llm-evaluation', 'medical-benchmarking']
venue: "NeurIPS 2024"
tldr: "MedJourney is a benchmark for evaluating LLMs on patient clinical journey tasks in the medical domain."
---

# MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9f80af32390984cb709cdeb014d0df41-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9f80af32390984cb709cdeb014d0df41-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MedJourney is a benchmark for evaluating LLMs on patient clinical journey tasks in the medical domain.

## Abstract

Large language models (LLMs) have demonstrated remarkable capabilities in language understanding and generation, leading to their widespread adoption across various fields. Among these, the medical field is particularly well-suited for LLM applications, as many medical tasks can be enhanced by LLMs. Despite the existence of benchmarks for evaluating LLMs in medical question-answering and exams, there remains a notable gap in assessing LLMs' performance in supporting patients throughout their entire hospital visit journey in real-world clinical practice. In this paper, we address this gap by dividing a typical patient's clinical journey into four stages: planning, access, delivery and ongoing care. For each stage, we introduce multiple tasks and corresponding datasets, resulting in a comprehensive benchmark comprising 12 datasets, of which five are newly introduced, and seven are constructed from existing datasets. This proposed benchmark facilitates a thorough evaluation of LLMs' effectiveness across the entire patient journey, providing insights into their practical application in clinical settings. Additionally, we evaluate three categories of LLMs against this benchmark: 1) proprietary LLM services such as GPT-4; 2) public LLMs like QWen; and 3) specialized medical LLMs, like HuatuoGPT2. Through this extensive evaluation, we aim to provide a better understanding of LLMs' performance in the medical domain, ultimately contributing to their more effective deployment in healthcare settings.