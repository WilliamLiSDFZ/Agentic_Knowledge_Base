---
title: "ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/54a7139c548c88e288aa0fcd2bcbeceb-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['zero-shot-coordination', 'multi-agent', 'cooperative-ai', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Presents ZSC-Eval, an evaluation toolkit and benchmark for measuring zero-shot coordination ability of agents with unseen partners in cooperative multi-agent settings."
---

# ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/54a7139c548c88e288aa0fcd2bcbeceb-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/54a7139c548c88e288aa0fcd2bcbeceb-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents ZSC-Eval, an evaluation toolkit and benchmark for measuring zero-shot coordination ability of agents with unseen partners in cooperative multi-agent settings.

## Abstract

Zero-shot coordination (ZSC) is a new cooperative multi-agent reinforcement learning (MARL) challenge that aims to train an ego agent to work with diverse, unseen partners during deployment. The significant difference between the deployment-time partners' distribution and the training partners' distribution determined by the training algorithm makes ZSC a unique out-of-distribution (OOD) generalization challenge. The potential distribution gap between evaluation and deployment-time partners leads to inadequate evaluation, which is exacerbated by the lack of appropriate evaluation metrics. In this paper, we present ZSC-Eval, the first evaluation toolkit and benchmark for ZSC algorithms.  ZSC-Eval consists of: 1) Generation of evaluation partner candidates through behavior-preferring rewards to approximate deployment-time partners' distribution; 2) Selection of evaluation partners by Best-Response Diversity (BR-Div); 3) Measurement of generalization performance with various evaluation partners via the Best-Response Proximity (BR-Prox) metric. We use ZSC-Eval to benchmark ZSC algorithms in Overcooked and Google Research Football environments and get novel empirical findings.  We also conduct a human experiment of current ZSC algorithms to verify the ZSC-Eval's consistency with human evaluation. ZSC-Eval is now available at https://github.com/sjtu-marl/ZSC-Eval.