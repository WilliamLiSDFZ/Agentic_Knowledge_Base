---
title: "SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses']
tags: ['llm-safety', 'benchmark', 'prompt-robustness']
venue: "NeurIPS 2024"
tldr: "Presents SG-Bench, a benchmark evaluating LLM safety generalization across diverse tasks and prompt types covering both discriminative and generative paradigms."
---

# SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/de7b99107c53e60257c727dc73daf1d1-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents SG-Bench, a benchmark evaluating LLM safety generalization across diverse tasks and prompt types covering both discriminative and generative paradigms.

## Abstract

Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety. Our assessment of 3 advanced proprietary LLMs and 10 open-source LLMs with the benchmark reveals that most LLMs perform worse on discriminative tasks than generative ones, and are highly susceptible to prompts, indicating poor generalization in safety alignment. We also explain these findings quantitatively and qualitatively to provide insights for future research.