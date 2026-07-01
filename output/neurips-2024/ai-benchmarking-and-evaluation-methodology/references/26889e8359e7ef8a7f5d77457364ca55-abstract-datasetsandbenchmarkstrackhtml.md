---
title: "BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/26889e8359e7ef8a7f5d77457364ca55-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'machine-learning-theory-and-evaluation-methods']
tags: ['benchmark-evaluation', 'best-practices', 'AI-assessment']
venue: "NeurIPS 2024"
tldr: "BetterBench systematically assesses AI benchmarks, identifies common issues, and proposes best practices for rigorous model evaluation."
---

# BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/26889e8359e7ef8a7f5d77457364ca55-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/26889e8359e7ef8a7f5d77457364ca55-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: BetterBench systematically assesses AI benchmarks, identifies common issues, and proposes best practices for rigorous model evaluation.

## Abstract

AI models are increasingly prevalent in high-stakes environments, necessitating thorough assessment of their capabilities and risks. Benchmarks are popular for measuring these attributes and for comparing model performance, tracking progress, and identifying weaknesses in foundation and non-foundation models. They can inform model selection for downstream tasks and influence policy initiatives. However, not all benchmarks are the same: their quality depends on their design and usability. In this paper, we develop an assessment framework considering 40 best practices across a benchmark's life cycle and evaluate 25 AI benchmarks against it. We find that there exist large quality differences and that commonly used benchmarks suffer from significant issues. We further find that most benchmarks do not report statistical significance of their results nor can results be easily replicated. To support benchmark developers in aligning with best practices, we provide a checklist for minimum quality assurance based on our assessment. We also develop a living repository of benchmark assessments to support benchmark comparability.