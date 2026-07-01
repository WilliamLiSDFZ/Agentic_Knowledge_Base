---
title: "WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/9dd4533e7e4e5ed809344280609c5b05-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-agent-communication-and-cooperation']
tags: ['multimodal-agents', 'benchmark', 'murder-mystery']
venue: "NeurIPS 2024"
tldr: "WhodunitBench introduces a murder mystery game benchmark to evaluate large multimodal agents across perception, reasoning, and decision-making capabilities."
---

# WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/9dd4533e7e4e5ed809344280609c5b05-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/9dd4533e7e4e5ed809344280609c5b05-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: WhodunitBench introduces a murder mystery game benchmark to evaluate large multimodal agents across perception, reasoning, and decision-making capabilities.

## Abstract

Recently, large language models (LLMs) have achieved superior performance, empowering the development of large multimodal agents (LMAs). An LMA is anticipated to execute practical tasks requires various capabilities including multimodal perception, interaction, reasoning, and decision making. However, existing benchmarks are limited in assessing compositional skills and actions demanded by practical scenarios, where they primarily focused on single tasks and static scenarios. To bridge this gap, we introduce WhodunitBench, a benchmark rooted from murder mystery games, where players are required to utilize the aforementioned skills to achieve their objective (i.e., identifying the `murderer' or hiding themselves), providing a simulated dynamic environment for evaluating LMAs. Specifically, WhodunitBench includes two evaluation modes. The first mode, the arena-style evaluation, is constructed from 50 meticulously curated scripts featuring clear reasoning clues and distinct murderers; The second mode, the chain of evaluation, consists of over 3000 curated multiple-choice questions and open-ended questions, aiming to assess every facet of the murder mystery games for LMAs. Experiments show that although current LMAs show acceptable performance in basic perceptual tasks, they are insufficiently equipped for complex multi-agent collaboration and multi-step reasoning tasks. Furthermore, the full application of the theory of mind to complete games in a manner akin to human behavior remains a significant challenge. We hope this work can illuminate the path forward, providing a solid foundation for the future development of LMAs. Our WhodunitBench is open-source and accessible at: https://github.com/jun0wanan/WhodunitBench-MurderMysteryGames