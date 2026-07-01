---
title: "Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d8a6eb79f8ccaacbe7198a5caf3a0323-Abstract-Conference.html"
categories: ['llm-training-and-optimization-techniques', 'llm-agent-communication-and-cooperation']
tags: ['llm-ensemble', 'heterogeneous-models', 'deep-parallel-collaboration', 'answer-fusion', 'generalization']
venue: "NeurIPS 2024"
tldr: "Proposes a deep parallel collaboration framework for ensembling heterogeneous LLMs without requiring an extra reward or fusion model."
---

# Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d8a6eb79f8ccaacbe7198a5caf3a0323-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d8a6eb79f8ccaacbe7198a5caf3a0323-Abstract-Conference.html)

**TLDR**: Proposes a deep parallel collaboration framework for ensembling heterogeneous LLMs without requiring an extra reward or fusion model.

## Abstract

Large language models (LLMs) exhibit complementary strengths in various tasks, motivating the research of LLM ensembling.However, existing work focuses on training an extra reward model or fusion model to select or combine all candidate answers, posing a great challenge to the generalization on unseen data distributions.Besides, prior methods use textual responses as communication media, ignoring the valuable information in the internal representations.In this work, we propose a training-free ensemble framework \textsc{DeePEn}, fusing the informative probability distributions yielded by different LLMs at each decoding step.Unfortunately, the vocabulary discrepancy between heterogeneous LLMs directly makes averaging the distributions unfeasible due to the token misalignment.To address this challenge, \textsc{DeePEn} maps the probability distribution of each model from its own probability space to a universal \textit{relative space} based on the relative representation theory, and performs aggregation.Next, we devise a search-based inverse transformation to transform the aggregated result back to the probability space of one of the ensembling LLMs (main model), in order to determine the next token.We conduct extensive experiments on ensembles of different number of LLMs, ensembles of LLMs with different architectures, and ensembles between the LLM and the specialist model.Experimental results show that (i) \textsc{DeePEn} achieves consistent improvements across six benchmarks covering subject examination, reasoning, and knowledge, (ii) a well-performing specialist model can benefit from a less effective LLM through distribution fusion, and (iii) \textsc{DeePEn} has complementary strengths with other ensemble methods such as voting.