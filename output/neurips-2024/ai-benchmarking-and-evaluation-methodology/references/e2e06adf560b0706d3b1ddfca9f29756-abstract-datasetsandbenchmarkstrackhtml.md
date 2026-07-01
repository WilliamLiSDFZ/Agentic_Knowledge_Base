---
title: "A StrongREJECT for Empty Jailbreaks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e2e06adf560b0706d3b1ddfca9f29756-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['llm-safety-robustness-and-privacy-defenses', 'ai-benchmarking-and-evaluation-methodology']
tags: ['jailbreak-evaluation', 'LLM-safety', 'benchmark-methodology']
venue: "NeurIPS 2024"
tldr: "StrongREJECT is proposed as a more rigorous evaluation framework exposing that many reported near-100% jailbreak attack success rates are substantially exaggerated due to flawed assessment methods."
---

# A StrongREJECT for Empty Jailbreaks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e2e06adf560b0706d3b1ddfca9f29756-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/e2e06adf560b0706d3b1ddfca9f29756-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: StrongREJECT is proposed as a more rigorous evaluation framework exposing that many reported near-100% jailbreak attack success rates are substantially exaggerated due to flawed assessment methods.

## Abstract

Most jailbreak papers claim the jailbreaks they propose are highly effective, often boasting near-100% attack success rates. However, it is perhaps more common than not for jailbreak developers to substantially exaggerate the effectiveness of their jailbreaks. We suggest this problem arises because jailbreak researchers lack a standard, high-quality benchmark for evaluating jailbreak performance, leaving researchers to create their own. To create a benchmark, researchers must choose a dataset of forbidden prompts to which a victim model will respond, along with an evaluation method that scores the harmfulness of the victim model’s responses. We show that existing benchmarks suffer from significant shortcomings and introduce the StrongREJECT benchmark to address these issues. StrongREJECT's dataset contains prompts that victim models must answer with specific, harmful information, while its automated evaluator measures the extent to which a response gives useful information to forbidden prompts. In doing so, the StrongREJECT evaluator achieves state-of-the-art agreement with human judgments of jailbreak effectiveness. Notably, we find that existing evaluation methods significantly overstate jailbreak effectiveness compared to human judgments and the StrongREJECT evaluator. We describe a surprising and novel phenomenon that explains this discrepancy: jailbreaks bypassing a victim model’s safety fine-tuning tend to reduce its capabilities. Together, our findings underscore the need for researchers to use a high-quality benchmark, such as StrongREJECT, when developing new jailbreak attacks. We release the StrongREJECT code and data at https://strong-reject.readthedocs.io/.