---
title: "MedCalc-Bench: Evaluating Large Language Models for Medical Calculations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare']
tags: ['llm-evaluation', 'medical-calculations', 'clinical-benchmarks']
venue: "NeurIPS 2024"
tldr: "MedCalc-Bench introduces a benchmark for evaluating LLMs on quantitative medical calculations used in clinical practice."
---

# MedCalc-Bench: Evaluating Large Language Models for Medical Calculations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MedCalc-Bench introduces a benchmark for evaluating LLMs on quantitative medical calculations used in clinical practice.

## Abstract

Current benchmarks for evaluating large language models (LLMs) in medicine are primarily focused on question-answering involving domain knowledge and descriptive reasoning. While such qualitative capabilities are vital to medical diagnosis, in real-world scenarios, doctors frequently use clinical calculators that follow quantitative equations and rule-based reasoning paradigms for evidence-based decision support. To this end, we propose MedCalc-Bench, a first-of-its-kind dataset focused on evaluating the medical calculation capability of LLMs. MedCalc-Bench contains an evaluation set of over 1000 manually reviewed instances from 55 different medical calculation tasks. Each instance in MedCalc-Bench consists of a patient note, a question requesting to compute a specific medical value, a ground truth answer, and a step-by-step explanation showing how the answer is obtained. While our evaluation results show the potential of LLMs in this area, none of them are effective enough for clinical settings. Common issues include extracting the incorrect entities, not using the correct equation or rules for a calculation task, or incorrectly performing the arithmetic for the computation. We hope our study highlights the quantitative knowledge and reasoning gaps in LLMs within medical settings, encouraging future improvements of LLMs for various clinical calculation tasks. MedCalc-Bench is publicly available at: https://github.com/ncbi-nlp/MedCalc-Bench.