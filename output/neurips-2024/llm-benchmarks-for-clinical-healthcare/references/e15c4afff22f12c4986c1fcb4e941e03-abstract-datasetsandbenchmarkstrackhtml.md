---
title: "EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e15c4afff22f12c4986c1fcb4e941e03-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare', 'ai-benchmarking-and-evaluation-methodology']
tags: ['ehr', 'discharge-summaries', 'llm-benchmark', 'clinical-qa', 'healthcare']
venue: "NeurIPS 2024"
tldr: "Introduces EHRNoteQA, a benchmark for evaluating LLMs on real-world clinical question answering over multi-admission discharge summaries."
---

# EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e15c4afff22f12c4986c1fcb4e941e03-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e15c4afff22f12c4986c1fcb4e941e03-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces EHRNoteQA, a benchmark for evaluating LLMs on real-world clinical question answering over multi-admission discharge summaries.

## Abstract

Discharge summaries in Electronic Health Records (EHRs) are crucial for clinical decision-making, but their length and complexity make information extraction challenging, especially when dealing with accumulated summaries across multiple patient admissions. Large Language Models (LLMs) show promise in addressing this challenge by efficiently analyzing vast and complex data. Existing benchmarks, however, fall short in properly evaluating LLMs' capabilities in this context, as they typically focus on single-note information or limited topics, failing to reflect the real-world inquiries required by clinicians. To bridge this gap, we introduce EHRNoteQA, a novel benchmark built on the MIMIC-IV EHR, comprising 962 different QA pairs each linked to distinct patients' discharge summaries. Every QA pair is initially generated using GPT-4 and then manually reviewed and refined by three clinicians to ensure clinical relevance. EHRNoteQA includes questions that require information across multiple discharge summaries and covers eight diverse topics, mirroring the complexity and diversity of real clinical inquiries. We offer EHRNoteQA in two formats: open-ended and multi-choice question answering, and propose a reliable evaluation method for each. We evaluate 27 LLMs using EHRNoteQA and examine various factors affecting the model performance (e.g., the length and number of discharge summaries). Furthermore, to validate EHRNoteQA as a reliable proxy for expert evaluations in clinical practice, we measure the correlation between the LLM performance on EHRNoteQA, and the LLM performance manually evaluated by clinicians. Results show that LLM performance on EHRNoteQA have higher correlation with clinician-evaluated performance (Spearman: 0.78, Kendall: 0.62) compared to other benchmarks, demonstrating its practical relevance in evaluating LLMs in clinical settings. EHRNoteQA will be publicly available to support further research and improve LLM evaluation in clinical practice. EHRNoteQA is publicly available under PhysioNet credential access at https://doi.org/10.13026/acga-ht95, and the code is available at https://github.com/ji-youn-kim/EHRNoteQA.