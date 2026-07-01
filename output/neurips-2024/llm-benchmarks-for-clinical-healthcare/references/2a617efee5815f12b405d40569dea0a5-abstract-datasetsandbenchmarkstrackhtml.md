---
title: "Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2a617efee5815f12b405d40569dea0a5-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-benchmarks-for-clinical-healthcare', 'ai-benchmarking-and-evaluation-methodology']
tags: ['LLM-bias', 'pre-training-data', 'healthcare-benchmarking']
venue: "NeurIPS 2024"
tldr: "Cross-Care is the first benchmark framework assessing how pre-training data composition drives language model biases in healthcare applications."
---

# Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2a617efee5815f12b405d40569dea0a5-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2a617efee5815f12b405d40569dea0a5-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Cross-Care is the first benchmark framework assessing how pre-training data composition drives language model biases in healthcare applications.

## Abstract

Large language models (LLMs) are increasingly essential in processing natural languages, yet their application is frequently compromised by biases and inaccuracies originating in their training data.In this study, we introduce \textbf{Cross-Care}, the first benchmark framework dedicated to assessing biases and real world knowledge in LLMs, specifically focusing on the representation of disease prevalence across diverse demographic groups.We systematically evaluate how demographic biases embedded in pre-training corpora like $ThePile$ influence the outputs of LLMs.We expose and quantify discrepancies by juxtaposing these biases against actual disease prevalences in various U.S. demographic groups.Our results highlight substantial misalignment between LLM representation of disease prevalence and real disease prevalence rates across demographic subgroups, indicating a pronounced risk of bias propagation and a lack of real-world grounding for medical applications of LLMs.Furthermore, we observe that various alignment methods minimally resolve inconsistencies in the models' representation of disease prevalence across different languages.For further exploration and analysis, we make all data and a data visualization tool available at: \url{www.crosscare.net}.