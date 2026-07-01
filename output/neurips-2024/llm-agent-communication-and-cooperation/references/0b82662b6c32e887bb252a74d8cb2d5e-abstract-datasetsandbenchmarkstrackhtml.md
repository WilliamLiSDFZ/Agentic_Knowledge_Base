---
title: "WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-agent-communication-and-cooperation']
tags: ['LLM-agents', 'autonomous-planning', 'benchmark']
venue: "NeurIPS 2024"
tldr: "WorkArena++ is a benchmark evaluating LLM-based agents on compositional planning and reasoning tasks grounded in common knowledge work scenarios."
---

# WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: WorkArena++ is a benchmark evaluating LLM-based agents on compositional planning and reasoning tasks grounded in common knowledge work scenarios.

## Abstract

The ability of large language models (LLMs) to mimic human-like intelligence has led to a surge in LLM-based autonomous agents. Though recent LLMs seem capable of planning and reasoning given user instructions, their effectiveness in applying these capabilities for autonomous task solving remains underexplored. This is especially true in enterprise settings, where automated agents hold the promise of a high impact. To fill this gap, we propose WorkArena++, a novel benchmark consisting of 682 tasks corresponding to realistic workflows routinely performed by knowledge workers. WorkArena++ is designed to evaluate the planning, problem-solving, logical/arithmetic reasoning, retrieval, and contextual understanding abilities of web agents. Our empirical studies across state-of-the-art LLMs and vision-language models (VLMs), as well as human workers, reveal several challenges for such models to serve as useful assistants in the workplace. In addition to the benchmark, we provide a mechanism to effortlessly generate thousands of ground-truth observation/action traces, which can be used for fine-tuning existing models. Overall, we expect this work to serve as a useful resource to help the community progress towards capable autonomous agents. The benchmark can be found at https://github.com/ServiceNow/WorkArena.